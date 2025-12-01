from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.delete_product_use_case import DeleteProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from .data.delete_product_use_case_integration_data import delete_product_use_case_sucessfully_data

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


@pytest.fixture
def setup_use_case():

    mongo_db_connection.connect()
    
    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case  = DeleteProductMongoUseCase(repository)

    return use_case


@pytest.mark.skip()
def test_delete_product_use_case_sucessfully(setup_use_case):

    data = delete_product_use_case_sucessfully_data()

    use_case = setup_use_case

    http_request = HttpRequest(params={"code": "16"})

    response = use_case.handle(http_request)

    assert response.status_code == 200
    assert response.body == data["expected_response"]


@pytest.mark.skip()
def test_delete_product_not_found(setup_use_case):

    use_case = setup_use_case

    http_request = HttpRequest(params={"code": "AAAA"})

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)


@pytest.mark.skip()
def test_delete_product_invalid_params(setup_use_case):
    
    use_case = setup_use_case

    http_request = HttpRequest(params={"code": 123})

    with pytest.raises(HttpUnprocessableEntity):

        use_case.handle(http_request)
