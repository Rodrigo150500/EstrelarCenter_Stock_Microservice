from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface

from src.validators.remove_item_validator_request import remove_item_validator_request

from .interfaces.remove_item_use_case_interface import RemoveItemMongoUseCaseInterface

class RemoveItemMongoUseCase(RemoveItemMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository


    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        remove_item_validator_request(params)

        self.__verify_if_exists(params)

        self.__remove_in_database(params)

        formatted_response = self.__formatted_response(params)

        return formatted_response
    
    
    def __verify_if_exists(self, params: dict) -> None:
        
        code = params["code"]

        object_id = params["_id"]

        response = self.__repository.check_if_variant_exists(code, object_id)

        if response == False: raise HttpNotFound('Product not found')


    def __remove_in_database(self, params: dict) -> None:

        code = params["code"]
        object_id = params["_id"]

        self.__repository.remove_variant_by_object_id(code, object_id)


    def __formatted_response(self, params: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "operation": "Update",
                    "count": 1,
                    "attributes": params
                }
            },status_code=200
        )
