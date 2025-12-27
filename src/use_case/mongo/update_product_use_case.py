from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.model.mongo.repository.product_repository import ProductRepositoryMongoInterface

from src.validators.update_product_validator_request import update_product_validator_request

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_internal_server_error import HttpInternalServerError

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from bson import Binary

class UpdateProductMongoUseCase:

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository.

    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        params = http_request.params
        body = http_request.body

        update_product_validator_request(body, params)

        self.__verify_if_exists_in_database(params)

        product_formatted_to_update = self.__format_product_update(body)

        
        
        response = self.__formatted_response(product_with_image_string)

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
        

    def __format_product_update(self, body: dict) -> dict:

        body_formatted = {}

        for key, value in body.items():

            body_formatted[f"variants.$.{key}"] = value
        
        return body_formatted


    def __export_image_to_binary(self, image: str) -> Binary:

        binary_image = export_image_string64_to_binary(image)

        return image

    
    def __export_images_to_string(self, products: dict) -> dict:
                       
        for variant in products["variants"]:

            image_binary = variant["image"]

            image_string = export_image_binary_to_string64(image_binary)

            variant["image"] = image_string

        return products
        

    def __formatted_response(self, product: dict) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation": "Update",
                    "count": len(product[])
                }
            }
        )
