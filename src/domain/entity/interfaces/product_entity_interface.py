from abc import ABC, abstractmethod

class ProductEntityInterface(ABC):

    @abstractmethod
    def create(data: dict, isVariant: bool):
        pass


    @abstractmethod
    def update(new_data: dict, old_data: dict):
        pass