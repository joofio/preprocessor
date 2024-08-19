import json
import requests
import medspacy
from bs4 import BeautifulSoup
from spacy.tokens import Span
from pydantic import BaseModel

import rules.pregnancy as pregnancy
import rules.hiv as hiv
import rules.diabetes as diabetes
import rules.side_effects as side_effects

class DOMResponse(BaseModel):
    htmlString: str

def setup_medspacy():
    nlp = medspacy.load()

    Span.set_extension("code", default=None, force=True)
    Span.set_extension("system", default="SNOMED-CT", force=True)
    
    nlp.get_pipe("medspacy_target_matcher").add(pregnancy.pregnancy_rules)
    nlp.get_pipe("medspacy_target_matcher").add(hiv.hiv_rules)
    nlp.get_pipe("medspacy_target_matcher").add(diabetes.diabetes_rules)
    nlp.get_pipe("medspacy_target_matcher").add(side_effects.side_effect_rules)

    return nlp

def preprocess(htmlDOM: BeautifulSoup, nlp):
    textNodes = htmlDOM.findAll(text=True)

    for textNode in textNodes:
        text = textNode + ""
        doc = nlp(text)
        if doc.ents:
            parent = textNode.parent
            for ent in doc.ents:
                if ent._.code:
                    classCode = ent._.code
                else:
                    classCode = ent.text
                if parent.has_attr('class'):
                    if classCode not in parent['class']:
                        parent['class'] = parent['class'] + [classCode]
                else:
                    parent['class'] = [classCode]
    
    return htmlDOM

def change_epi_status(epi):
    if epi['entry'][0]['resource']['category'][0]['coding'][0]['code'] != "P":
        epi['entry'][0]['resource']['category'][0]['coding'][0]['code'] = 'P'
        epi['entry'][0]['resource']['category'][0]['coding'][0]['display'] = 'Preprocessed'

def main():
    response = requests.get('https://gravitate-health.lst.tfo.upm.es/epi/api/fhir/Bundle/bundlepackageleaflet-en-94a96e39cfdcd8b378d12dd4063065f9')
    preprocessor = setup_medspacy()
    epi = response.json()
    change_epi_status(epi)

    sections = epi['entry'][0]['resource']['section'][0]['section']

    for section in sections:
        htmlDOM = BeautifulSoup(section['text']['div'], 'html.parser')

        htmlDOM = preprocess(htmlDOM, preprocessor)
        strDOM = str(htmlDOM)
        section['text']['div'] = strDOM

    epi['entry'][0]['resource']['section'][0]['section'] = sections

    with open('output.json', 'w') as f:
        json.dump(epi, f)


if __name__ == "__main__":
    main()