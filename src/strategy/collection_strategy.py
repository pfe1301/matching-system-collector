from abc import ABC, abstractmethod


class CollectionStrategy(ABC):
    """
        An abstract class tha defines a common interface on how to collect data
    """

    @abstractmethod
    def get_data(self, entity:str, *args, **kwargs):
        pass
