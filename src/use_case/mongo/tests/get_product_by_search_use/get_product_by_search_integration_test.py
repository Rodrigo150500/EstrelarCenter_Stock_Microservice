import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_product_by_search_use_case import GetProductsBySearchMongoUseCase

from get_product_by_search_integration_data import setup_use_case_data,get_product_sucessfully_data, adding_last_id_should_return_second_part_data, product_not_found_should_return_error_data

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFound

mongo_db_connection.connect()

@pytest.fixture
def setup_use_case():

    data = setup_use_case_data()

    try:
        
        connection = mongo_db_connection.get_db_connection()
        repository = ProductRepositoryMongo(connection)
        use_case = GetProductsBySearchMongoUseCase(repository)

        repository.insert_product(data["product"])

        variants = repository.get_product_by_code(data["product"]["code"])["variants"]

        object_id_list = []

        for product in variants:
            object_id_list.append(str(product["_id"]))

        yield use_case, object_id_list

    finally:
        
        repository.delete_product_by_code(data["product"]["code"])


def test_get_product_sucessfully(setup_use_case):

    use_case, object_id_list = setup_use_case

    data = get_product_sucessfully_data(object_id_list)

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == data["expected_response"]


def test_adding_last_id_should_return_second_part(setup_use_case):

    use_case, object_id_list = setup_use_case

    data = adding_last_id_should_return_second_part_data(object_id_list)

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)
    
    assert response.body == data["expected_response"]


def test_product_not_in_db_should_return_not_found(setup_use_case):

    use_case, _ = setup_use_case

    data = product_not_found_should_return_error_data()

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)