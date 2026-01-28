from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.remove_item_use_case import RemoveItemMongoUseCase

def remove_item_composer():

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = RemoveItemMongoUseCase(repository)

    return use_case
