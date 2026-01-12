import pytest

from unittest.mock import Mock

from src.use_case.mongo.get_product_by_search_use_case import GetAllProductsMongoUseCase

from .data.get_all_products_use_case_data import get_all_products_sucessfully_data


@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = GetAllProductsMongoUseCase(repository)

    return use_case, repository


def test_get_all_products_sucessfully(setup_use_case):

    data = get_all_products_sucessfully_data()

    use_case, repository = setup_use_case

    repository.get_all_products.return_value = data["get_all_products"]

    response = use_case.handle()

    assert response.body == data["expected_body"]
    assert response.status_code == 200

    repository.get_all_products.assert_called_once()