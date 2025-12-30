import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_all_products_use_case import GetAllProductsMongoUseCase


@pytest.fixture
def setup_use_case():

    mongo_db_connection.connect()

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = GetAllProductsMongoUseCase(repository)
    
    return use_case

@pytest.mark.skip()
def test_get_all_products_sucessfully(setup_use_case):

    use_case = setup_use_case

    response = use_case.handle()

    assert response.status_code == 200
    assert len(response.body) > 0