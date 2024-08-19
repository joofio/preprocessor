import json
import requests
import medspacy
from bs4 import BeautifulSoup
from spacy.tokens import Span

from rules import pregnancy, hiv, diabetes, side_effects

def setup_medspacy():
    """Set up the medSpaCy pipeline"""
    nlp = medspacy.load()

    Span.set_extension('code', default=None, force=True)
    Span.set_extension('system', default='SNOMED-CT', force=True)

    nlp.get_pipe('medspacy_target_matcher').add(pregnancy.pregnancy_rules)
    nlp.get_pipe('medspacy_target_matcher').add(hiv.hiv_rules)
    nlp.get_pipe('medspacy_target_matcher').add(diabetes.diabetes_rules)
    nlp.get_pipe('medspacy_target_matcher').add(side_effects.side_effect_rules)

    return nlp

def preprocess(html_dom: BeautifulSoup, nlp):
    """Preprocess the HTML DOM"""
    text_nodes = html_dom.findAll(text=True)

    for text_node in text_nodes:
        text = text_node + ""
        doc = nlp(text)
        if doc.ents:
            parent = text_node.parent
            for ent in doc.ents:
                if ent._.code:
                    class_code = ent._.code
                else:
                    class_code = ent.text
                if parent.has_attr('class'):
                    if class_code not in parent['class']:
                        parent['class'] = parent['class'] + [class_code]
                else:
                    parent['class'] = [class_code]
    return html_dom

def change_epi_status(epi):
    """Change the status of the EPI to Preprocessed"""	
    if epi['entry'][0]['resource']['category'][0]['coding'][0]['code'] != 'P':
        epi['entry'][0]['resource']['category'][0]['coding'][0]['code'] = 'P'
        epi['entry'][0]['resource']['category'][0]['coding'][0]['display'] = 'Preprocessed'

def main():
    """Main function"""	
    response = requests.get('https://gravitate-health.lst.tfo.upm.es/epi/api/fhir/Bundle/bundlepackageleaflet-en-94a96e39cfdcd8b378d12dd4063065f9', timeout=15)
    preprocessor = setup_medspacy()
    epi = response.json()
    change_epi_status(epi)

    sections = epi['entry'][0]['resource']['section'][0]['section']

    for section in sections:
        html_dom = BeautifulSoup(section['text']['div'], 'html.parser')

        html_dom = preprocess(html_dom, preprocessor)
        str_dom = str(html_dom)
        section['text']['div'] = str_dom

    epi['entry'][0]['resource']['section'][0]['section'] = sections

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(epi, f)


if __name__ == "__main__":
    main()
