from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.delete_product_use_case import DeleteProductMongoUseCase

def delete_product_composer():
    
    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = DeleteProductMongoUseCase(repository)

    return use_case
