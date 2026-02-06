from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface
from .interfaces.delete_product_use_case_interface import DeleteProductUseCaseInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.delete_product_validator_request import delete_product_validator_request

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService

class DeleteProductMongoUseCase(DeleteProductUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository

        
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        delete_product_validator_request(params)

        self.__verify_if_exists_in_database(params)

        self.__delete_product_in_database(params)

        formatted_response = self.__format_response()
        
        return formatted_response
    

    def __verify_if_exists_in_database(self, params: dict) -> None:

        try:
            code = params["code"]

            response = self.__repository.check_if_product_exists(code)

            if response == False: raise HttpNotFound("Error: Product not found")
            
        except HttpUnavailableService:
            raise

    def __delete_product_in_database(self, params: dict) -> None:

        try:

            code = params["code"]

            self.__repository.delete_product_by_code(code)

        except HttpUnavailableService:
            raise
    
    def __format_response(self) -> HttpResponse:

        return HttpResponse(
                status_code=204
        )
            