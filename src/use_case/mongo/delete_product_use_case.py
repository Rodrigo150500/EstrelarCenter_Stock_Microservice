from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryInterface
from .interfaces.delete_product_use_case_interface import DeleteProductUseCaseInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.delete_product_validator_request import delete_product_validator_request

from src.errors.types.http_not_found import HttpNotFound

class DeleteProductMongoUseCase(DeleteProductUseCaseInterface):

    def __init__(self, repository: ProductRepositoryInterface):
        
        self.__repository = repository


    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        delete_product_validator_request(params)

        self.__verify_if_exists_in_database(params)

        self.__delete_product_in_database(params)

        formatted_response = self.__format_response(params)
        
        return formatted_response
    

    def __verify_if_exists_in_database(self, params: dict) -> None:

        code = params["code"]

        product = self.__repository.get_product_by_code(code)

        if not product: raise HttpNotFound("Error: Product not found")


    def __delete_product_in_database(self, params: dict) -> None:

        code = params["code"]

        self.__repository.delete_product_by_code(code)

    
    def __format_response(self, params: dict) -> HttpResponse:

        return HttpResponse(
                body={
                    "data":{
                        "operation":"delete",
                        "count": 1,
                        "attributes": params
                    }
                }, status_code=200
        )
            