import requests

class SnomedCodeLookup:
    """Class to look up SNOMED codes"""

    def get_concept_from_code(self, code):
        """Get the concept from the concept ID"""
        response = requests.get(f'https://termbrowser.nhs.uk/sct-browser-api/snomed/uk-edition/v20240731/concepts/{code}', timeout=15)
        response.raise_for_status()
        term = response.json()

        return term['descriptions'][0]['term']
