from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryInterface
from .interfaces.insert_product_use_case import InserProductMongoUseCaseInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.insert_product_validator_request import insert_product_validator_request

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from src.errors.types.http_conflict import HttpConflict


class InsertProductMongoUseCase(InserProductMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryInterface):
        
        self.__repository = repository
    

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        insert_product_validator_request(body)

        self.__verify_if_product_exists(body)

        body_formatted_request = self.__format_image(body)
    
        self.__insert_in_database(body_formatted_request)

        formatted_response = self.__format_response(body_formatted_request)

        return formatted_response 

    
    def __verify_if_product_exists(self, body: dict) -> None:

        product = self.__repository.get_product_by_code(body["code"])

        if product: raise HttpConflict("Error: Product already exists")

    def __format_image(self, body: dict) -> list:

        image = body["image"]

        if (isinstance(image, str) and "erro.jpg" not in image):

            if image.startswith("data:image"):

                image = image.split(",", 1)[1]  # remove o "data:image/png;base64,"

            body["image"] = export_image_string64_to_binary(image)
    
        return body
    

    def __insert_in_database(self, body:dict) -> dict:

        code = body["code"]
        
        response = self.__repository.insert_product_item(code, body)
        
        return response
    
    
    def __format_response(self, body: dict) -> HttpResponse:

        return HttpResponse(
            body={
                "data":{
                    "operation": "Insert",
                    "count": 1,
                    "attributes": body
                }
            }, status_code= 201
        )