import os

from src.errors.types.http_unavailable_service_error import HttpUnavailableServiceError

from pymongo.results import DeleteResult, UpdateResult

from .interfaces.product_repository_interface import ProductRepositoryInterface

COLLECTION_NAME = os.getenv("COLLECTION_NAME_MONGO_DB_PRODUCTS")

class ProductRepositoryMongo(ProductRepositoryInterface):

    def __init__(self, connection):
        
        self.__collection = connection.get_collection(COLLECTION_NAME)


    def get_product_by_code(self, code: str) -> dict:
        
        try:

            product_filter = {
                code:{"$exists": True}
            }

            #Se não houver encontrado retorno é none
            product =  self.__collection.find_one(product_filter)
            
            return product

        except Exception as exception:

            print(f"Error:[product_repository_mongo][get_product_by_code]: {str(exception)}")

            raise HttpUnavailableServiceError("Banco de dados indisponível")


    def remove_item(self, code: str, item: int) -> UpdateResult:

        try:

            product_filter = {code: {"$exists": True}}

            # remove pelo índice
            self.__collection.update_one(
                product_filter,
                {"$unset": {f"{code}.{item}": item}}
            )
            
            # 2. depois remove os "null" do array
            response = self.__collection.update_one(
                product_filter,
                {"$pull": {code: None}}
            )

            return response
        
        except Exception as exception:

            print(f"Error:[product_repository_mongo][remove_item]: {str(exception)}")

            raise HttpUnavailableServiceError("Banco de dados indisponível")


    def delete_product_by_code(self, code: str) -> DeleteResult:

        try:

            product_filter = {
                code:{"$exists": True}
            }

            response = self.__collection.delete_one(product_filter)

            return response
        
        except Exception as exception:

            print(f"Error:[product_repository_mongo][delete_product_by_code]: {str(exception)}")

            raise HttpUnavailableServiceError("Banco de dados indisponível")

    

    def insert_product_item(self, code: str, fields: dict) -> UpdateResult:

        try:

            product_filter = {code: {"$exists": True}}

            update_query = {
                "$push": {
                    code: fields
                }
            }

            response = self.__collection.update_one(
                product_filter,
                update_query,
                upsert=True
            )

            return response
        
        except Exception as exception:

            print(f"Error:[product_repository_mongo][insert_product_item]: {str(exception)}")

            raise HttpUnavailableServiceError("Banco de dados indisponível")


    def update_product_item(self, code: str, item: int, fields: dict) -> UpdateResult:

        try:
            product_filter = {f"{code}.{item}": {"$exists": True}}

            update_query = {
                "$set": {
                    f"{code}.{item}": fields
                }
            }

            response = self.__collection.update_one(product_filter, update_query)

            return response
    
        except Exception as exception:

            print(f"Error:[product_repository_mongo][update_product_item]: {str(exception)}")

            raise HttpUnavailableServiceError("Banco de dados indisponível")



    def get_all_products(self) -> list:

        try:
        
            products = self.__collection.find({})
            
            products = [document for document in products]

            return products

        except Exception as exception:

            print(f"Error:[product_repository_mongo][get_all_products]: {str(exception)}")

            raise HttpUnavailableServiceError("Banco de dados indisponível")
