import re

from bson.objectid import ObjectId

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface

from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound

from .interfaces.get_products_by_search_use_case_interface import GetProductsBySearchMongoUseCaseInterface

from src.validators.get_product_by_search_validator_request import get_product_by_search_validator_request

class GetProductsBySearchMongoUseCase(GetProductsBySearchMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository


    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        get_product_by_search_validator_request(params)

        products_to_search = self.__preparing_search_schema(params)

        products = self.__search_in_database(products_to_search)

        formatted_response = self.__format_response(products)

        return formatted_response
    

    def __preparing_search_schema(self, params: dict) -> list:

        search = params["search"]
        fields = params["fields"]
        last_id = params["last_id"]

        pipeline = []

        #Transforming each variant in document
        pipeline.append({"$unwind":"$variants"})
        
        safe = re.escape(search)
        
        or_conditions = []


        if "description" in fields:
            
            or_conditions.append({
                "variants.description": {"$regex": safe, "$options": "i"}
            })
        
        if "brand" in fields:

            or_conditions.append({
                "variants.brand":{"$regex": safe, "$options": "i"}
            })
        
        if "reference" in fields:

            or_conditions.append({
                "variants.reference": {"$regex": safe, "$options": "i"}
            })
        
        if or_conditions:
            pipeline.append({
                "$match":{"$or": or_conditions}
            })
        
        if last_id:
            pipeline.append({
                "$match":{
                    "variants._id": {"$gt":ObjectId(last_id)}
                }
            })

        #Sort + limit
        pipeline.append({
            "$sort":{"variants._id":1}
        })

        pipeline.append({
            "$limit": 10
        })

        pipeline.append({
            "$replaceRoot":{"newRoot":"$variants"}
        })

        return pipeline
                

    def __search_in_database(self, pipeline: list) -> list:

        try:

            products = self.__repository.search_by_text(pipeline)

            return products
        
        except HttpNotFound: 
            raise

        except Exception:
            raise 
    

    def __format_response(self, product: list) -> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "operation": "Get",
                    "count": len(product),
                    "attributes": product
                }
            }, status_code= 200
        )