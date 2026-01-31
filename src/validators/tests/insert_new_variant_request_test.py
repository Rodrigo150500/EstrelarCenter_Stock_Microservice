import pytest

from src.validators.insert_new_variant_request import insert_new_variant_request

from src.utils.image_type import image_string

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def test_remove_item_validator_succesfully():

    params = {
        "code": "10"
    }

    body = {         
        "description": "Product Test",
        "stock": 20,
        "image": image_string,
        "brand": "kit-kat",
        "reference": "kat15",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True,
        "quantity_change": 5
    }

    insert_new_variant_request(params, body)


def test_with_wrong_type_params():

    params = {
        "code": ["10"] #must be string
    }

    body = {         
        "description": "Product Test",
        "stock": 20,
        "image": image_string,
        "brand": "kit-kat",
        "reference": "kat15",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True,
        "quantity_change": 5
    }

    with pytest.raises(HttpUnprocessableEntity):
        insert_new_variant_request(params, body)

def test_missing_required_fields():

    params = {
        "code": "10" 
    }

    body = {         
        "description": "", #Must not be empty
        "stock": 20,
        "image": image_string,
        "brand": "kit-kat",
        "reference": "kat15",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True,
        "quantity_change": 5
    }

    with pytest.raises(HttpUnprocessableEntity):
        insert_new_variant_request(params, body)
