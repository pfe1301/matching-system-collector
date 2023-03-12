import re
from strategy import (
    CollectionStrategy,
    WriteSonicStrategy,
    OpenaiStrategy,
    UnknownStrategyException
)


def construct_prompt(entity, type_, lang='en'):
    prompt = ""
    if lang == 'en':
        if type_ == 'job':
            prompt = f"Give a detailed description about this job {entity}, skills, tools,missions and tasks and pretty much every thing about it"
        else:
            # skill
            prompt = f"Give a detailed description about this skill {entity}, jobs that could be used in and pretty much every thing about it"

    # TODO: Add Fr language

    return prompt

# TODO: Implement preprocessing


def preprocess_entity(entity):
    entity = re.sub("\n", "", entity)
    return entity


def build_strategy(strategy: str) -> CollectionStrategy:
    if (strategy == 'openai'):
        return OpenaiStrategy()
    elif (strategy == 'writesonic'):
        return WriteSonicStrategy()
    else:
        raise UnknownStrategyException(f"Uknown strategy {strategy}")
