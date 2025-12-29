import os

from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_not_found import HttpNotFound

from pymongo.results import DeleteResult, UpdateResult

from .interfaces.product_repository_interface import ProductRepositoryMongoInterface
from .interfaces.insert_product_interface import InsertProductInterface

from bson.objectid import ObjectId

COLLECTION_NAME = os.getenv("COLLECTION_NAME_MONGO_DB_PRODUCTS")

class ProductRepositoryMongo(ProductRepositoryMongoInterface):

    def __init__(self, connection):
        
        self.__collection = connection.get_collection(COLLECTION_NAME)


    def get_product_by_code(self, code: str) -> dict:
        
        try:

            response = self.__collection.find_one(
                {"code": code}
            )

            if not response: raise HttpNotFound("Error: Product not found")

            return response
        
        except HttpNotFound:
            
            raise
            
        except Exception as exception:

            print(f"Error:[ProductRepositoryMongo][GetProductByCode]: {str(exception)}")

            raise HttpUnavailableService("Error: Database Unvailable")


    def remove_variant_by_object_id(self, code: str, object_id: str) -> UpdateResult:
        
        try:

            response = self.__collection.update_one(
                {"code": code},
                {"$pull": {"variants":{"_id": ObjectId(object_id)}}}
            )

            return response
        
        except Exception as exception:

            print(f"Error: [ProductRepositoryMongo][RemoveVariantByObjectId]: {str(exception)}")

            raise HttpUnavailableService("Error: Database unavailable")


    def delete_product_by_code(self, code: str) -> DeleteResult:

        try:

            response = self.__collection.delete_one(
                {"code": code}
            )

            return response
        
        except Exception as exception:

            print(f"Error: [ProductRepositoryMongo][RemoveVariantByObjectId]: {str(exception)}")

            raise HttpUnavailableService("Error: Database unavailable")
    

    def insert_product(self, fields: dict) -> InsertProductInterface:

        try:

            response = self.__collection.insert_one(fields)

            return response
        
        except Exception as exception:

            print(f"Error: [ProductRepositoryMongo][InsertProductVariant]: {str(exception)}")

            raise HttpUnavailableService("Error: Database unavailable")


    def insert_new_variant(self, code: str, fields: dict) -> UpdateResult:

        try:

            response = self.__collection.update_one(
                {"code": code},
                {"$push": {"variants": fields}}
            )

            return response
        
        except Exception as exception:

            print(f"Error:[ProductRepositoryMongo][InsertNewVariant]:{str(exception)}")

            raise HttpUnavailableService("Error: Database unvailable")


    def update_product_variant_by_object_id(self, code: str, object_id: str, fields: dict) -> UpdateResult:

        try:

            response = self.__collection.update_one(
                {"code": code, "variants._id": ObjectId(object_id)},
                {"$set": fields}
            )

            return response

        
        except Exception as exception:

            print(f"Error:[ProductRepositoryMongo][UpdateProductVariant]: {str(exception)}")

            raise HttpUnavailableService("Error: Database unvailable")



    def get_all_products(self) -> list:

        try:

            response = self.__collection.find({})

            return list(response)
        
        except Exception as exception:

            print(f"Error: [ProductRepositoryMongo][RemoveVariantByObjectId]: {str(exception)}")

            raise HttpUnavailableService("Error: Database unavailable")