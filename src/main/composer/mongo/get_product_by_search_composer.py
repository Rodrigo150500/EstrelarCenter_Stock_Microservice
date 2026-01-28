from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_product_by_search_use_case import GetProductsBySearchMongoUseCase

def get_product_by_search_composer():

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = GetProductsBySearchMongoUseCase(repository)

    return use_case
