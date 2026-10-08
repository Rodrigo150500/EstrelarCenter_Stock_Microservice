import pytest

from src.domain.entity.product_entity import ProductEntity

from src.utils.image_type import image_string

def test_create_product_entity_successfully():

    data = {
        "code": "10",
        "description": "Chocolate Ouro Branco 45g",
        "image": image_string,
        "measure": "Unidade",
        "quantity_change": 5,
        "stock": 5,
        "keepBuying": True,
        "warehouse":{
            "quantity_change": 5,
            "stock": 5,
            "measure": "Unidade"
        }
    }

    product_entity = ProductEntity.create(data)
