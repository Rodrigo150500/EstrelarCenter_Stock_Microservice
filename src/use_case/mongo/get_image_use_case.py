import base64

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.get_product_image_validator_request import get_image_product_validator_request

from .interfaces.get_image_use_case_interface import GetImageMongoUseCaseInterface

from src.errors.types.http_not_found import HttpNotFound

from bson.binary import Binary

class GetImageMongoUseCase(GetImageMongoUseCaseInterface):


    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository


    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        get_image_product_validator_request(params)

        image = self.__get_product_from_database(params=params)

        image_string = self.__transform_image_binary_to_string_base_64(image)

        response = self.__format_response(image_string)

        return response


    def __get_product_from_database(self, params: dict) -> dict:

        code = params["code"]
        object_id = params["_id"]

        image = self.__repository.get_variant_image_by_code(code, object_id)

        if not image: raise HttpNotFound("Error: Product not registred")

        return image
    
    
    def __transform_image_binary_to_string_base_64(self, image: Binary) -> dict:


        error_image = "/static/erro.jpg"


        if image and isinstance(image, (bytes, bytearray)):

            base64_str = base64.b64encode(image).decode("utf-8")

            image_string = f"data:image/png;base64,{base64_str}"

        else:

            image_string = error_image

        return image_string


    def __format_response(self, image) -> HttpResponse:

        return HttpResponse(
              body={
                    "data":{
                        "operation":"Get",
                        "count": 1,
                        "attributes": image
                    }
                }, status_code=200
        )