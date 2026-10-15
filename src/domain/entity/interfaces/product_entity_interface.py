from abc import ABC, abstractmethod

class ProductEntityInterface(ABC):

    @abstractmethod
    def create(data):
        pass


    @abstractmethod
    def update(new_data: dict):
        pass