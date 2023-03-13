import re
from strategy import (
    CollectionStrategy,
    WriteSonicStrategy,
    OpenaiStrategy,
    DBPediaStrategy,
    UnknownStrategyException
)


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
    elif (strategy == 'dbpedia'):
        return DBPediaStrategy()
    else:
        raise UnknownStrategyException(f"Uknown strategy {strategy}")
