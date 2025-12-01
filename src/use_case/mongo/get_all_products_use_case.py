from src.model.mongo.repository.interfaces.product_repository_interface import ProductRepositoryInterface

from src.main.http_types.http_response import HttpResponse

from .interfaces.get_all_products_use_case_interface import GetAllProductsUseCaseInterface

class GetAllProductsMongoUseCase(GetAllProductsUseCaseInterface):

    def __init__(self, repository: ProductRepositoryInterface):
        
        self.__repository = repository


    def handle(self) -> HttpResponse:

        products = self.__get_products_from_database()  

        products_with_no_image = self.__taking_off_image_from_products(products)  

        response = self.__formatted_response(products_with_no_image)

        return response


    def __get_products_from_database(self):
        
            products = self.__repository.get_all_products()

            return products
    

    def __taking_off_image_from_products(self, products: list) -> list:

        for product in products:

            del product["_id"]

            code = list(product.keys())[0]

            for item in product[code]:

                del item["image"]
                
        return products
    

    def __formatted_response(self, products: list) -> HttpResponse:

        return HttpResponse(
            status_code=200,
            body=products
        )
