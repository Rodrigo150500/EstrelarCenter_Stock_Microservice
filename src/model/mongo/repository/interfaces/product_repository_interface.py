from abc import ABC, abstractmethod

from src.model.mongo.repository.interfaces.insert_product_interface import InsertProductInterface
from pymongo.results import DeleteResult, UpdateResult

from bson.binary import Binary


class ProductRepositoryMongoInterface(ABC):

    @abstractmethod
    def get_product_by_code(self, code: str) -> dict:
        pass
     

    @abstractmethod
    def remove_variant_by_object_id(self, code: str, object_id: str) -> UpdateResult:
        pass


    @abstractmethod
    def delete_product_by_code(self, code: str) -> DeleteResult:
        pass
    

    @abstractmethod
    def insert_product(self, fields: dict) -> InsertProductInterface:
        pass


    @abstractmethod
    def insert_new_variant(self, code: str, fields: dict) -> UpdateResult:
        pass


    @abstractmethod
    def update_product_variant_by_object_id(self, code: str, object_id: str, fields: dict) -> UpdateResult:
        pass


    @abstractmethod
    def get_all_products(self) -> list:
        pass


    @abstractmethod
    def check_if_variant_exists(self, code: str, object_id: str) -> bool:
        pass


    @abstractmethod
    def check_if_product_exists(self, code: str) -> bool:
        pass


    @abstractmethod
    def get_variant_image_by_code(self, code: str, object_id: str) -> Binary:
        pass

    
    @abstractmethod
    def search_by_text(self, pipeline: list) -> list:
        pass