import json
import requests
import medspacy
from bs4 import BeautifulSoup
from spacy.tokens import Span

from rules import pregnancy, hiv, diabetes, side_effects
from snomed_code_lookup import SnomedCodeLookup

def setup_medspacy():
    """Set up the medSpaCy pipeline"""
    nlp = medspacy.load()

    Span.set_extension('code', default=None, force=True)
    Span.set_extension('system', default='SNOMED_CT', force=True)

    nlp.get_pipe('medspacy_target_matcher').add(pregnancy.pregnancy_rules)
    nlp.get_pipe('medspacy_target_matcher').add(hiv.hiv_rules)
    nlp.get_pipe('medspacy_target_matcher').add(diabetes.diabetes_rules)
    nlp.get_pipe('medspacy_target_matcher').add(side_effects.side_effect_rules)

    return nlp

def preprocess(html_dom: BeautifulSoup, nlp, codes_found):
    """Preprocess the HTML DOM"""
    text_nodes = html_dom.findAll(text=True)

    for text_node in text_nodes:
        text = text_node + ""
        doc = nlp(text)
        if doc.ents:
            parent = text_node.parent
            for ent in doc.ents:
                class_code = ent._.code
                if parent.has_attr('class'):
                    if class_code not in parent['class']:
                        parent['class'] = parent['class'] + [class_code]
                else:
                    parent['class'] = [class_code]
                if codes_found.get(class_code) is None:
                    snomed = SnomedCodeLookup()
                    if ent._.system == 'RxNorm':
                        concept = ent.text
                    else:
                        concept = snomed.get_concept_from_code(class_code)
                    codes_found[class_code] = { 'concept': concept, 'system': ent._.system }
    return html_dom

def change_epi_status(epi):
    """Change the status of the EPI to Preprocessed"""	
    if epi['entry'][0]['resource']['category'][0]['coding'][0]['code'] != 'P':
        epi['entry'][0]['resource']['category'][0]['coding'][0]['code'] = 'P'
        epi['entry'][0]['resource']['category'][0]['coding'][0]['display'] = 'Preprocessed'

def from_codes_to_extensions(code, value):
    """Convert codes found to extensions"""	

    if value['system'] == 'RxNorm':
        system_url = 'http://www.nlm.nih.gov/research/umls/rxnorm'
    else:
        system_url = 'http://snomed.info/sct'

    return {
        "url": "http://hl7.eu/fhir/ig/gravitate-health/StructureDefinition/HtmlElementLink",
        "extension": [
            {
                "url": "elementClass",
                "valueString": code
            },
            {
                "url": "concept",
                "valueCodeableReference": {
                    "concept": {
                        "coding": [
                            {
                                "system": system_url,
                                "code": code,
                                "display": value['concept']
                            }
                        ]
                    }
                }
            }
        ]
    }

def main():
    """Main function"""	
    response = requests.get('https://gravitate-health.lst.tfo.upm.es/epi/api/fhir/Bundle/bundlepackageleaflet-en-94a96e39cfdcd8b378d12dd4063065f9', timeout=15)
    preprocessor = setup_medspacy()
    epi = response.json()
    codes_found = {}

    change_epi_status(epi)

    sections = epi['entry'][0]['resource']['section'][0]['section']

    for section in sections:
        html_dom = BeautifulSoup(section['text']['div'], 'html.parser')

        html_dom = preprocess(html_dom, preprocessor, codes_found)
        str_dom = str(html_dom)
        section['text']['div'] = str_dom

    epi['entry'][0]['resource']['section'][0]['section'] = sections

    extensions = []

    if epi['entry'][0]['resource'].get('extension') is not None:
        extensions = epi['entry'][0]['resource']['extension']

    for key, value in codes_found.items():
        extension_object = from_codes_to_extensions(key, value)
        extensions.append(extension_object)

    epi['entry'][0]['resource']['extension'] = extensions

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(epi, f)


if __name__ == "__main__":
    main()
