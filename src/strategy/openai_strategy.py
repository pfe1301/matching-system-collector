from .collection_strategy import CollectionStrategy
import openai
import time
import os

# This might not be useful, since env variable should be loaded before
import dotenv
dotenv.load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenaiStrategy(CollectionStrategy):

    # TODO: Pass extra arguments to the init method
    # So that the decorated api call can be customized more
    def __init__(self) -> None:
        super().__init__()

    def get_data(self, input_text, *args, **kwargs):
        super().get_data(input_text, *args, **kwargs)
        try:
            return self.make_request(prompt=input_text)
        except:
            # Sleep for one minute before making next call
            time.sleep(6000)
            return self.make_request(prompt=input_text)

    def make_request(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
