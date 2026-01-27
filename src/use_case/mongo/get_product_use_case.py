import os

import base64

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.get_product_validator_request import get_product_validator_request

from src.errors.types.http_not_found import HttpNotFound

from .interfaces.get_product_use_case_interface import GetProductMongoUseCaseInterface

from src.utils.export_image_binary_to_string64 import export_image_binary_to_string64

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

class GetProductMongoUseCase(GetProductMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface ) -> None:
        
        self.__repository = repository
    

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        params = http_request.params

        get_product_validator_request(params)

        product = self.__get_product_from_database(params)

        formatted_product = self.__format_image_to_string64(product)
        
        formatted_response = self.__format_response(formatted_product)

        return formatted_response
    

    def __get_product_from_database(self, params: dict) -> dict:

        try:

            code = params["code"]

            product = self.__repository.get_product_by_code(code)

        except HttpNotFound:

            raise

        return product


    def __format_image_to_string64(self, product: dict) -> list:

        products = product["variants"]

        products_list = []

        for item in products:

            try:

                item["image"] = export_image_binary_to_string64(item["image"])
            
            except:

                item["image"] = f'{HOST}:{PORT}/static/erro.jpg'

            products_list.append(item)

        return products_list

            
    def __format_response(self, products: list) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation": "Get",
                    "count": len(products),
                    "attributes": products
                }
            }, status_code=200
        )