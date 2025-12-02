import base64

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.get_product_image_validator_request import get_image_product_validator_request

from .interfaces.get_image_use_case_interface import GetImageMongoUseCaseInterface

from src.errors.types.http_not_found import HttpNotFound

class GetImageMongoUseCase(GetImageMongoUseCaseInterface):


    def __init__(self, repository: ProductRepositoryInterface):
        
        self.__repository = repository


    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        get_image_product_validator_request(params)

        product = self.__get_product_from_database(params=params)

        image = self.__transform_image_binary_to_string_base_64(product, params)

        response = self.__format_response(image)

        return response


    def __get_product_from_database(self, params: dict) -> dict:

        code = params["code"]

        product = self.__repository.get_product_by_code(code)

        if not product: raise HttpNotFound("Error: Product not registred")

        return product
    
    
    def __transform_image_binary_to_string_base_64(self, product: dict, params: dict) -> dict:

        code = params["code"]

        item = params["item"]

        error_image = "/static/erro.jpg"

        image_mongo = product[code][item]["image"]

        if image_mongo and isinstance(image_mongo, (bytes, bytearray)):
            base64_str = base64.b64encode(image_mongo).decode("utf-8")

            product[code][item]["image"] = f"data:image/png;base64,{base64_str}"
        else:
            product[code][item]["image"] = error_image

        return product[code][item]["image"]


    def __format_response(self, image) -> HttpResponse:

        return HttpResponse(
              body={
                    "data":{
                        "operation":"get",
                        "count": 1,
                        "attributes": image
                    }
                }, status_code=200
        )