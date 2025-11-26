from abc import ABC, abstractmethod
from pymongo.results import UpdateResult, DeleteResult


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def get_product_by_code(self, code: str) -> dict:
        pass
    

    @abstractmethod
    def remove_item(self, code: str, item: int) -> UpdateResult:
        pass
    
    
    @abstractmethod
    def delete_product_by_code(self, code: str) -> DeleteResult:
        pass
    

    @abstractmethod
    def insert_product_item(self, code: str, fields: dict) -> UpdateResult:
        pass


    @abstractmethod
    def update_product_item(self, code: str, item: int, fields: dict) -> UpdateResult:
        pass

    @abstractmethod
    def get_all_products(self) -> list:
        pass