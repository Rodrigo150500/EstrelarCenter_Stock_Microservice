from src.model.mongo.repository.product_repository import ProductRepositoryMongoInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound

from src.validators.insert_new_variant_request import insert_new_variant_request

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from .interfaces.insert_new_variant_use_case_interface import InsertNewVariantMongoUseCaseInterface

from datetime import datetime

from bson.objectid import ObjectId

class InsertNewVariantMongoUseCase(InsertNewVariantMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        params = http_request.params
        body = http_request.body

        insert_new_variant_request(params, body)
        
        self.__verify_if_product_exists(params)

        body_image_formatted = self.__export_image_in_binary(body)

        body_last_change_formatted = self.__add_metadata_fields(body_image_formatted)

        self.__insert_in_database(params, body_last_change_formatted)

        formatted_response = self.__format_response(body_image_formatted)

        return formatted_response
    

    def __verify_if_product_exists(self, params: dict) -> None:

        code = params["code"]

        response = self.__repository.check_if_product_exists(code)

        if response == False: raise HttpNotFound("Erro: Product not found")

        return
    

    def __export_image_in_binary(self, body: dict) -> dict:
        
        image_string = body["image"]

        image = export_image_string64_to_binary(image_string)

        body["image"] = image

        return body        


    def __add_metadata_fields(self, body: dict) -> dict:

        body["last_change"] = datetime.now()
        body["_id"] = ObjectId()

        return body


    def __insert_in_database(self, params: dict, body: dict) -> None:

        code = params["code"]
        
        self.__repository.insert_new_variant(code, body)

        return
    

    def __format_response(self, body: dict) -> HttpResponse:

        del body["image"]
        body["_id"] = str(body["_id"])

        return HttpResponse(
            body={
                "data":{
                    "operation": "Insert",
                    "count": 1,
                    "attributes": body
                }
            }, status_code=201
        )