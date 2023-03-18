from strategy.utils import construct_prompt
from .collection_strategy import CollectionStrategy
import openai
import time
import os

# This might not be useful, since env variable should be loaded before
import dotenv
dotenv.load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenaiStrategy(CollectionStrategy):
    """
        OpenaiStrategy defines the strategy of interaction with open ai api to collect data
    """

    # TODO: Pass extra arguments to the init method
    # So that the decorated api call can be customized more
    def __init__(self) -> None:
        super().__init__()

    def get_data(self, entity: str, *args, **kwargs):
        """
            Implement `get_data` function responsible for data collection
            Parameters:
                input_text (string): the prompt to send to the API

            Returns:
                data (string): the text response of the api
        """
        super().get_data(entity, *args, **kwargs)
        prompt = construct_prompt(
            entity=entity,
            type_=kwargs.get('type', 'job'),
            lang=kwargs.get('lang', 'en')
        )
        return self.make_request(prompt=prompt)

    def make_request(self, prompt: str, TRY_AGAIN=2) -> str:
        """
            Make actual request to the API
            Parameters:
                promopt (string): the prompt to send to the API

            Returns:
                data (string): the text response of the api

            Eventual features:
                make request with custom configuration
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=1000,
                n=1,
                stop=None,
                temperature=0.5,
            )
            return response.choices[0].text.strip()
        except:
            if TRY_AGAIN == 0:
                raise Exception("API request failed")
            else:
                print(TRY_AGAIN, "tries left")
                TRY_AGAIN -= 1
                time.sleep(6)
                print("Trying again")
                return self.make_request(prompt=prompt, TRY_AGAIN=TRY_AGAIN)
