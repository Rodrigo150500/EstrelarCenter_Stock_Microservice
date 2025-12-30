import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_product_use_case import GetProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from .data.get_product_use_case_integration_data import get_product_sucessfully, get_product_not_found

from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_use_case():

    mongo_db_connection.connect()

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = GetProductMongoUseCase(repository)

    return use_case


@pytest.mark.skip()
def test_get_product_sucessfully(setup_use_case):

    data = get_product_sucessfully()

    use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    print(response.body)


@pytest.mark.skip()
def test_get_product_not_found(setup_use_case):

    data = get_product_not_found()

    use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)

