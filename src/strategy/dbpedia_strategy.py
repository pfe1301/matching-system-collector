from .collection_strategy import CollectionStrategy
import requests
from requests import Response
from SPARQLWrapper import SPARQLWrapper, JSON
import urllib.parse

resource_lookup_endpoint = "https://lookup.dbpedia.org/api/search"
headers = {"Accept": "application/json"}

sparql_endpoint = "https://dbpedia.org/sparql"


class DBPediaStrategy(CollectionStrategy):

    def get_data(self, entity, *args, **kwargs):
        """
            Implement `get_data` function responsible for data collection
            Parameters:
                entity (string): the entity to search for
                input_text (string): the prompt to send to the API

            Returns:
                data (string): the text response of the api
        """
        super().get_data(entity, *args, **kwargs)

        uri = self.get_uri(entity)
        if uri:
            return self.get_description(uri, language=kwargs.get('lang', 'en'))
        else:
            return ''

    def get_uri(self, entity):

        print(f'Getting uri for {entity}...')

        params = {
            "maxResults": 1,
            "format": "JSON",
            "query": entity,
        }

        response: Response = requests.get(
            resource_lookup_endpoint, headers=headers, params=params)

        if response.status_code != 200:
            return ''
        else:
            results = response.json()["docs"]
            if results:
                uri = results[0]["resource"][0]
                return uri
            else:
                print(f'Failed to retrieve uri from dbpedia for {entity}')
                return ''

    def get_description(self, uri, language="en"):

        print(f'Getting description for {uri}...')

        query = f"""
                    SELECT ?description
                    WHERE {{
                        <{uri}> dbo:abstract ?description .
                        FILTER (lang(?description) = "{language}")
                    }}
                """

        sparql = SPARQLWrapper(sparql_endpoint)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        if results["results"]["bindings"]:
            description = results["results"]["bindings"][0]["description"]["value"]
            return description
        else:
            print(f'Failed to retrieve description from dbpedia for {uri}')
            return ''
