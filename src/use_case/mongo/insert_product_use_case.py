from bson import Binary

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface
from .interfaces.insert_product_use_case import InserProductMongoUseCaseInterface
from src.model.mongo.repository.interfaces.insert_product_interface import InsertProductInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.validators.insert_product_validator_request import insert_product_validator_request

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from src.errors.types.http_conflict import HttpConflict
from src.errors.types.http_not_found import HttpNotFound

from datetime import datetime

class InsertProductMongoUseCase(InserProductMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface):
        
        self.__repository = repository
    

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        insert_product_validator_request(body)

        self.__verify_if_product_exists(body)

        image = self.__export_image_to_binary(body["image"])

        body_formatted_request = self.__format_body(body, image)
    
        response = self.__insert_in_database(body_formatted_request) #Response available from database

        formatted_response = self.__format_response(body_formatted_request)

        return formatted_response 

    
    def __verify_if_product_exists(self, body: dict) -> None:

        try:

            self.__repository.get_product_by_code(body["code"])
        
        except HttpNotFound:

            return
        
        raise HttpConflict("Error: Product already exists")
    

    def __export_image_to_binary(self, image: str) -> Binary | str:

        if (isinstance(image, str) and "erro.jpg" not in image):

            if image.startswith("data:image"):

                image = image.split(",", 1)[1]  # remove o "data:image/png;base64,"

            image_exported = export_image_string64_to_binary(image)
    
        return image_exported
    
    
    def __format_body(self, body: dict, image: Binary) -> dict:

        body = {
            "code": body["code"],
            "variants": [{
                "description": body["description"],
                "stock": body["stock"],
                "image": image,
                "brand": body["brand"],
                "reference": body["reference"],
                "location": body["location"],
                "measure": body["measure"],
                "keepBuying": body["keepBuying"],
                "last_change": datetime.now(),
                "quantity_change": body["quantity_change"]
                }
            ]
        }

        return body


    def __insert_in_database(self, body:dict) -> InsertProductInterface:

        response = self.__repository.insert_product(body)
        
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