import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_image_use_case import GetImageMongoUseCase

from .data.get_image_use_case_integration_data import get_image_sucessfully, get_image_not_found

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_use_case():

    mongo_db_connection.connect()

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = GetImageMongoUseCase(repository)

    return use_case


@pytest.mark.skip()
def test_get_image_sucessfully(setup_use_case):

    data = get_image_sucessfully()

    use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert response.body is not None
    assert response.status_code == 200


@pytest.mark.skip()
def test_get_image_not_found(setup_use_case):

    data = get_image_not_found()

    use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])


    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)   

    