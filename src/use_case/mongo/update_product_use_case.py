from datetime import datetime

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.use_case.mongo.interfaces.update_product_use_case_interface import UpdateProductMongoUseCaseInterface
from src.model.mongo.repository.product_repository import ProductRepositoryMongoInterface
from src.domain.entity.interfaces.product_entity_interface import ProductEntityInterface
from bson import Binary

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary


class UpdateProductMongoUseCase(UpdateProductMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface, product_entity: ProductEntityInterface):
        
        self.__repository = repository
        self.__product_entity = product_entity
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        params = http_request.params
        body = http_request.body
        host = http_request.header
      
        self.__verify_if_exists_in_database(params)

        old_data = self.__get_product_from_database(params)
    
        image = self.__transform_image_to_binary(body, host)

        product_validated = self.__product_entity.update(body)

        product_to_save = self.__get_changed_fields_only(old_data, product_validated, image)

        

        product_to_save = self.__format_product_to_update(product_last_change_updated)

        self.__update_product(product_to_save, params)
        
        response = self.__formatted_response(body, params)

        return response


    def __verify_if_exists_in_database(self, params: dict) -> None:

        code = params["code"]
        object_id = params["_id"]

        try:

            response = self.__repository.check_if_variant_exists(code, object_id) 

            if response == False: raise HttpNotFound("Error: product not found") 

            return
        
        except HttpNotFound:
            raise

        except HttpUnavailableService:
            raise  

    def __get_product_from_database(self, params: dict) -> dict:

        code = params["code"]
        _id = params["_id"]

        product = self.__repository.get_variant_by_code_and_id(code, _id)

        return product


 

    def __format_product_to_update(self, body: dict) -> dict:

        body_formatted = {}

        for key, value in body.items():

            body_formatted[f"variants.$.{key}"] = value
        
        return body_formatted


    def __transform_image_to_binary(self, body: dict, host: str) -> Binary | str:

        if "image" in body:

            image_string = body["image"]

            image_binary = export_image_string64_to_binary(image_string, host)

        return image_binary


    def __get_changed_fields_only(self, old_data: dict, new_data: dict, image: str | Binary):

        new_data["image"] = image

        



    
    def __update_product(self, product: dict, params: dict) -> None:

        try:

            code = params["code"]
            object_id = params["_id"]

            self.__repository.update_product_variant_by_object_id(code, object_id, product)

        except HttpUnavailableService:
            raise 
                

    def __formatted_response(self, body: dict, params: dict) -> HttpResponse:

        if "image" in body:
            del body["image"]

        body["_id"] = params["_id"]

        return HttpResponse(
            body={
                "data":{
                    "operation": "Update",
                    "count": 1,
                    "attributes": body
                }
            },
            status_code=200
        )
