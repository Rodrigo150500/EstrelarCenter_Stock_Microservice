from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.use_case.mongo.interfaces.update_product_use_case_interface import UpdateProductMongoUseCaseInterface
from src.model.mongo.repository.product_repository import ProductRepositoryMongoInterface

from src.validators.update_product_validator_request import update_product_validator_request

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_internal_server_error import HttpInternalServerError

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary


class UpdateProductMongoUseCase(UpdateProductMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository

    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        params = http_request.params
        body = http_request.body

        update_product_validator_request(body, params)

        self.__verify_if_exists_in_database(params)
    
        product_with_image_string = self.__transform_image_to_binary(body)

        product_formatted_to_update = self.__format_product_to_update(product_with_image_string)

        self.__update_product(product_formatted_to_update, params)
        
        response = self.__formatted_response()

        return response


    def __verify_if_exists_in_database(self, params: dict) -> None:

        code = params["code"]

        try:

            self.__repository.get_product_by_code(code) #TODO Trocar por um modelo que verifica se o produto existe e se o _id da variante também exista
            
            return 

        except HttpNotFound:
            raise

        except HttpUnavailableService:
            raise

        except Exception as exception:

            print(f"Error: [UpdateProductMongoUseCase][GetProductFromDatabase]: {str(exception  )}")

            raise HttpInternalServerError("Error: Erro interno no servidor")
        

    def __format_product_to_update(self, body: dict) -> dict:

        body_formatted = {}

        for key, value in body.items():

            body_formatted[f"variants.$.{key}"] = value
        
        return body_formatted


    def __transform_image_to_binary(self, body: dict) -> dict:

        if "image" in body:

            image_string = body["image"]

            image_binary = export_image_string64_to_binary(image_string)

            body["image"] = image_binary

        return body

    
    def __update_product(self, product: dict, params: dict) -> None:

        try:

            code = params["code"]
            object_id = params["_id"]

            self.__repository.update_product_variant_by_object_id(code, object_id, product)

        except HttpUnavailableService:
            raise 

        except Exception as exception:

            print(f"Error: [UpdateProductMongoUseCase][UpdateProduct]: {str(exception)}")

            raise HttpInternalServerError("Error: Erro interno no servidor")
        

    def __formatted_response(self) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation": "Update",
                    "count": 1
                }
            }
        )
