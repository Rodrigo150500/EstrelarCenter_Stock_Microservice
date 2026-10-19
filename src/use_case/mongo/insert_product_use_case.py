from bson import Binary

from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryMongoInterface
from .interfaces.insert_product_use_case import InserProductMongoUseCaseInterface
from src.model.mongo.repository.interfaces.insert_product_interface import InsertProductInterface
from src.domain.entity.interfaces.product_entity_interface import ProductEntityInterface

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from src.errors.types.http_conflict import HttpConflict
from src.errors.types.http_unavailable_service import HttpUnavailableService

from bson.objectid import ObjectId


class InsertProductMongoUseCase(InserProductMongoUseCaseInterface):

    def __init__(self, repository: ProductRepositoryMongoInterface, product_entity: ProductEntityInterface):
        
        self.__repository = repository
        self.__product_entity = product_entity
    

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body
        host = http_request.header
    
        self.__verify_if_product_exists(body)

        product_to_save = self.__product_entity.create(body)

        image = self.__export_image_to_binary(body["image"], host)
        
        body_formatted_to_save = self.__format_body(product_to_save, image)
    
        self.__insert_in_database(body_formatted_to_save)

        formatted_response = self.__format_response(body_formatted_to_save)

        return formatted_response 

    
    def __verify_if_product_exists(self, body: dict) -> None:

        try:

            response = self.__repository.check_if_product_exists(body["code"])

            if response == True: raise HttpConflict("Error: Product already exists")

            return       

        except HttpConflict:
            raise

        except HttpUnavailableService:
            raise


    def __export_image_to_binary(self, image: str, host: str) -> Binary | str:

        if (isinstance(image, str) and "erro.jpg" not in image):

            if image.startswith("data:image"):

                image = image.split(",", 1)[1]  # remove o "data:image/png;base64,"

            image_exported = export_image_string64_to_binary(image, host)
    
        return image_exported
    
    
    def __format_body(self, body: dict, image: Binary) -> dict:

        body = {
            "_id": ObjectId(),
            "code": body["code"],
            "variants":[{
                **body,
                "image": image
            }]
        }

        del body["variants"][0]["code"]
        
        return body


    def __insert_in_database(self, body:dict) -> InsertProductInterface:

        try:

            response = self.__repository.insert_product(body)
            
            return response

        except HttpUnavailableService:
            raise
    
    
    def __format_response(self, body: dict) -> HttpResponse:


        body["_id"] = str(body["_id"])
        
        body["variants"][0]["_id"] = str(body["variants"][0]["_id"])

        del body["variants"][0]["image"]

        return HttpResponse(
            body={
                "data":{
                    "operation": "Insert",
                    "count": 1,
                    "attributes": body["variants"][0]
                }
            }, status_code= 201
        )