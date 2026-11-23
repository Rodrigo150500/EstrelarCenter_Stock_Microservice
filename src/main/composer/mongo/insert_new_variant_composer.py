from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.insert_new_variant_use_case import InsertNewVariantMongoUseCase
from src.domain.entity.product_entity import ProductEntity

def insert_new_variant_composer():

    product_entity = ProductEntity()
    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = InsertNewVariantMongoUseCase(repository, product_entity)

    return use_case
