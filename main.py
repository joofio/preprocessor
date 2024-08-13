import requests
import medspacy
from medspacy.ner import TargetRule
from bs4 import BeautifulSoup

def setup_medspacy():
    nlp = medspacy.load()

    target_rules = [
        TargetRule("Biktarvy", "DRUG"),
        TargetRule("bictegravir", "INGREDIENT"),
        TargetRule("Emtricitabine", "INGREDIENT"),
        TargetRule("Tenofovir alafenamide", "INGREDIENT"),
        TargetRule("Rifampicin", "INGREDIENT"),
        TargetRule("St. John’s wort", "DRUG"),
        TargetRule("Hypericum perforatum", "INGREDIENT"),
        TargetRule("Pregnancy", "CONDITION"),
        TargetRule("Breast-feeding", "CONDITION"),
        TargetRule("HIV", "CONDITION"),
    ]

    nlp.get_pipe("medspacy_target_matcher").add(target_rules)
    return nlp

def preprocess(htmlDOM: BeautifulSoup, nlp):
    textNodes = htmlDOM.findAll(text=True)

    for textNode in textNodes:
        text = textNode + ""
        doc = nlp(text)
        if not doc.ents:
            print("No entities found")
            continue
        else:
            parent = textNode.parent
            for ent in doc.ents:
                if parent.has_attr('class'):
                    parent['class'] = parent['class'] + [ent.label_]
                else:
                    parent['class'] = [ent.label_]
    
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
