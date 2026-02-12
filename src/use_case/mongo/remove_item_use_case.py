from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService

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

        formatted_response = self.__format_response()

        return formatted_response
    
    
    def __verify_if_exists(self, params: dict) -> None:
        
        code = params["code"]

        object_id = params["_id"]

        try:

            response = self.__repository.check_if_variant_exists(code, object_id)

            if response == False: raise HttpNotFound('Product not found')
        
        except HttpNotFound:
            raise

        except HttpUnavailableService:
            raise


    def __remove_in_database(self, params: dict) -> None:

        code = params["code"]
        object_id = params["_id"]

        try:

            self.__repository.remove_variant_by_object_id(code, object_id)

        except HttpUnavailableService:
            raise


    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=204
        )
