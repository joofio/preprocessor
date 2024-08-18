import requests
import medspacy
from medspacy.ner import TargetRule
from bs4 import BeautifulSoup
from spacy.tokens import Span
# import diabetes
import pregnancy
import hiv

def setup_medspacy():
    nlp = medspacy.load()

    Span.set_extension("code", default=None, force=True)
    Span.set_extension("system", default="SNOMED-CT", force=True)
    
    # nlp.get_pipe("medspacy_target_matcher").add(diabetes.diabetes_rules)
    nlp.get_pipe("medspacy_target_matcher").add(pregnancy.pregnancy_rules)
    nlp.get_pipe("medspacy_target_matcher").add(hiv.hiv_rules)

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
    
    print(htmlDOM.prettify())

response = requests.get('https://gravitate-health.lst.tfo.upm.es/epi/api/fhir/Bundle/bundlepackageleaflet-en-94a96e39cfdcd8b378d12dd4063065f9')

epi = response.json()

sections = epi['entry'][0]['resource']['section'][0]['section']

preprocessor = setup_medspacy()

for section in sections:
    print(section['title'])
    print(section['text']['div'])

    htmlDOM = BeautifulSoup(section['text']['div'], 'html.parser')

    preprocess(htmlDOM, preprocessor)
