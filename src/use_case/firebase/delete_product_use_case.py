from src.model.firebase.repository.interface.product_repository_interface import ProductRepositoryFirebaseInterface

from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

from src.validators.delete_product_validator_request import delete_product_validator_request

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_internal_server_error import HttpInternalServerError

from .interfaces.delete_product_use_case_interface import DeleteProductUseCaseInterface

class DeleteProductFirebaseUseCase(DeleteProductUseCaseInterface):

    def __init__(self, repository: ProductRepositoryFirebaseInterface):
        
        self.__repository = repository
        

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        delete_product_validator_request(params)

        self.__verify_if_exists_in_database(params)

        self.__delete_product_in_database(params)

        formatted_response = self.__format_response(params)

        return formatted_response


    def __verify_if_exists_in_database(self, params: dict) -> None:

        try:
            code = params["code"]

            product = self.__repository.get_product_by_code(code)

            if (not product):

                raise HttpNotFound("Product not found")
        
        except HttpNotFound:

            raise
        
        except Exception as exception:

            print(f"Error:[DeleteProductFirebaseUseCase][__verify_if_exists_in_database]: {str(exception)}")
            
            raise HttpUnavailableService("Error: Banco de dados indisponível")
    

    def __delete_product_in_database(self, params):

        try:

            code = params["code"]

            self.__repository.delete_product_by_code(code)

        except Exception as exception:
            
            print(f"Error:[DeleteProductFirebaseUseCase][__delete_product_in_database]: {str(exception)}")
            
            raise HttpUnavailableService("Erro ao deletar no banco de dados")

        
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
        
     
