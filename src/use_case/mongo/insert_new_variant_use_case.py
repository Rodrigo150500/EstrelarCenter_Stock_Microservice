from src.model.mongo.repository.product_repository import ProductRepositoryMongoInterface
from src.domain.entity.interfaces.product_entity_interface import ProductEntityInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService

from src.validators.insert_new_variant_request import insert_new_variant_request

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from .interfaces.insert_new_variant_use_case_interface import InsertNewVariantMongoUseCaseInterface


from bson import Binary

class InsertNewVariantMongoUseCase(InsertNewVariantMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface, entity: ProductEntityInterface):
        
        self.__repository = repository
        self.__entity = entity

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        params = http_request.params
        body = http_request.body
        host = http_request.header

        self.__verify_if_product_exists(params)

        product_validated = self.__entity.create(body, True)
        
        image = self.__export_image_to_binary(body["image"], host)

        product_to_save = self.__format_body(product_validated, image)

        self.__insert_in_database(params, product_to_save)

        formatted_response = self.__format_response(product_to_save)

        return formatted_response
    

    def __verify_if_product_exists(self, params: dict) -> None:

        code = params["code"]

        try:

            response = self.__repository.check_if_product_exists(code)

            if response == False: raise HttpNotFound("Erro: Product not found")

            return
        
        except HttpNotFound:
            raise

        except HttpUnavailableService:
            raise


    def __export_image_to_binary(self, image: str, host: str) -> dict:
        
        if (isinstance(image, str) and "erro.jpg" not in image):

            if image.startswith("data:image"):

                image = image.split(",", 1)[1]  # remove o "data:image/png;base64,"

            image_exported = export_image_string64_to_binary(image, host)
    
        return image_exported


    def __format_body(self, body: dict, image: Binary):
        
        body["image"] = image

        return body
    

    def __insert_in_database(self, params: dict, body: dict) -> None:

        code = params["code"]

        try:
        
            self.__repository.insert_new_variant(code, body)

            return

        except HttpUnavailableService:
            raise
        

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