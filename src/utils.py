import re
from strategy import (
    CollectionStrategy,
    WriteSonicStrategy,
    OpenaiStrategy,
    UnknownStrategyException
)


def construct_prompt(entity: str, type_: str, lang: str = 'en') -> str:
    """
        A utility function responsible for prompt construction
        Parameters:
            entity (string): The entity to construct the prompt for
            type_ (string): The type of the entity (job or skill)
            lang (string): The language in which the prompt is constructed
        Returns:
            prompt (string): The prompt to send to the API
    """
    prompt = ""
    if lang == 'en':
        if type_ == 'job':
            prompt = f"Give a detailed description about this job {entity}, skills, tools,missions and tasks and pretty much every thing about it"
        else:
            # skill
            prompt = f"Give a detailed description about this skill {entity}, jobs that could be used in and pretty much every thing about it"

    # TODO: Add Fr language

    return prompt

# TODO: Implement preprocessing with more features


def preprocess_entity(entity: str) -> str:
    """
        A utility function that performs basic text preprocessing before sending to the API
        Parameters:
            entity (string): The entity to preprocess
        Returns:
            cleaned_entity (string): The preprocessed entity
    """
    entity = re.sub("\n", "", entity)
    return entity


def build_strategy(strategy: str) -> CollectionStrategy:
    """
        A factory method that creates the strategy
        Parameters:
            strategy (string): A hint describing which strategy to create
        Returns:
            strategy_object (CollectionStrategy): Collection strategy object
    """
    if (strategy == 'openai'):
        return OpenaiStrategy()
    elif (strategy == 'writesonic'):
        return WriteSonicStrategy()
    else:
        raise UnknownStrategyException(f"Uknown strategy {strategy}")
