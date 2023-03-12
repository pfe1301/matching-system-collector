from .collection_strategy import CollectionStrategy
import requests
import json
import dotenv
import os
from requests import Response

dotenv.load_dotenv()

endpoint = "https://api.writesonic.com/v2/business/content/chatsonic"
api_key = os.getenv('CHAT_SONIC_API_KEY')

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": api_key,

}


class WriteSonicStrategy(CollectionStrategy):

    def get_data(self, input_text, *args, google=True, memory=False, **kwargs, ):
        """
            Implement `get_data` function responsible for data collection
            Parameters:
                input_text (string): the prompt to send to the API

            Returns:
                data (string): the text response of the api
        """
        super().get_data(input_text, *args, **kwargs)
        print(input_text)
        payload = {
            "enable_google_results": google,
            "enable_memory": memory,
            "input_text": input_text
        }
        response: Response = requests.post(
            endpoint, json=payload, headers=headers)
        response_data = json.loads(response.text)
        print(response_data)
        # try:
        #     return response_data['message']
        # except:
        return ""
