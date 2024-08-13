import requests
import medspacy
from bs4 import BeautifulSoup

response = requests.get('https://gravitate-health.lst.tfo.upm.es/epi/api/fhir/Bundle/bundlepackageleaflet-en-94a96e39cfdcd8b378d12dd4063065f9')

epi = response.json()

sections = epi['entry'][0]['resource']['section'][0]['section']

for section in sections:
    print(section['title'])
    print(section['text']['div'])

    htmlDOM = BeautifulSoup(section['text']['div'], 'html.parser')

    textNodes = htmlDOM.findAll(text=True)

    for textNode in textNodes:
        print(textNode)
        print('---')

