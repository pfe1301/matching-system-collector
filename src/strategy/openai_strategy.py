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

    def get_data(self, input_text: str, *args, **kwargs):
        """
            Implement `get_data` function responsible for data collection
            Parameters:
                input_text (string): the prompt to send to the API

            Returns:
                data (string): the text response of the api
        """
        super().get_data(input_text, *args, **kwargs)
        try:
            return self.make_request(prompt=input_text)
        except:
            # Sleep for one minute before making next call
            # TODO: Retry until max_retries reached ?
            time.sleep(6000)
            return self.make_request(prompt=input_text)

    def make_request(self, prompt: str) -> str:
        """
            Make actual request to the API
            Parameters:
                promopt (string): the prompt to send to the API

            Returns:
                data (string): the text response of the api

            Eventual features:
                make request with custom configuration
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
