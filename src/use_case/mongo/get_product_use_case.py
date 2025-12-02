import os

import base64

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.get_product_validator_request import get_product_validator_request

from src.errors.types.http_not_found import HttpNotFound

PORT = os.getenv("PORT")

class GetProductMongoUseCase:

    def __init__(self, repository: ProductRepositoryInterface ) -> None:
        
        self.__repository = repository
    

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        get_product_validator_request(params)

        product = self.__get_product_from_database(params)

        formatted_product = self.__format_product(params, product)
        
        formatted_response = self.__format_response(formatted_product)

        return formatted_response
    

    def __get_product_from_database(self, params: dict) -> dict:

        code = params["code"]

        product = self.__repository.get_product_by_code(code)

        if not product: raise HttpNotFound("Error: Product not registred")

        return product


    def __format_product(self,params: dict, product: dict) -> list:

        code = params["code"]

        products = product[code]

        products_list = []

        for item in products:

            item["image"] = self.__transform_image_binary_to_string_base_64(item["image"])

            products_list.append(item)

        return products_list


    def __transform_image_binary_to_string_base_64(self, product_image: bytes ) -> str:

        error_image = f"https://localhost:{PORT}/static/stock/src/assets/erro.jpg"

        if not product_image:

            return error_image

        if product_image and isinstance(product_image, (bytes, bytearray)):

            base64_str = base64.b64encode(product_image).decode("utf-8")

            return f"data:image/png;base64,{base64_str}"
        
        else:

            return error_image

            
    def __format_response(self, products: list) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation": "get",
                    "count": len(products),
                    "attributes": products
                }
            }, status_code=200
        )