from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase
from src.domain.entity.product_entity import ProductEntity

def insert_product_composer():

    product_entity = ProductEntity()
    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = InsertProductMongoUseCase(repository, product_entity)

    return use_case
