from abc import ABC, abstractmethod


class CollectionStrategy(ABC):

    @abstractmethod
    def get_data(self, input_text, *args, **kwargs):
        pass
