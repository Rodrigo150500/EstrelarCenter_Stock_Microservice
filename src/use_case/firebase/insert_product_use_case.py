from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

from src.model.firebase.repository.interface.product_repository_interface import ProductRepositoryFirebaseInterface
from .interfaces.insert_product_use_case_interface import InsertProductUseCaseInterface

from src.validators.insert_product_validator_request import insert_product_validator_request

from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


class InsertProductFirebaseUseCase(InsertProductUseCaseInterface):

    def __init__(self, repository: ProductRepositoryFirebaseInterface):
        
        self.__repository = repository

    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        insert_product_validator_request(body)

        body_formatted = self.__body_format(body)

        self.__insert_in_database(body, body_formatted)

        formatted_response = self.__format_response(body_formatted)

        return formatted_response
    

    def __body_format(self, body: dict) -> dict:

        try:

            body_formatted = {
                "Descrição": body["description"],
                "Marca": body["brand"],
                "Quantidade": body["stock"],
                "Referência": body["reference"]
            }

            return body_formatted

        except Exception as exception:

            print(f"Error:[InsertProductFirebaeUseCase][__body_format]: {str(exception)}")

            raise HttpUnprocessableEntity("Error: Formato do body invalido")


    def __insert_in_database(self, body: dict, body_formatted: dict) -> None:

            code = body["code"]

            self.__repository.insert_or_update_product(code, body_formatted)
    

    def __format_response(self, body: dict) -> HttpResponse:

      return HttpResponse(
            body={
                "data":{
                    "operation": "update",
                    "count": 1,
                    "attributes": body
                }
            }, status_code=201
        )