from datetime import datetime

from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes

def setup_use_case_data():

    product = {
            "code": "10",
            "variants": [{
                "_id": ObjectId(),
                "description": "Product A",
                "stock": 25,
                "image": imagem_bytes,
                "brand": "kit-kat",
                "reference": "kat 500",
                "location": "CX25",
                "measure": "Caixa",
                "keepBuying": True,
                "last_change": datetime.now(),
                "quantity_change": 5
                },{
                    "_id": ObjectId(),
                    "description": "Product B",
                    "stock": 50,
                    "image": imagem_bytes,
                    "brand": "Bis",
                    "reference": "Bis 150",
                    "location": "C15",
                    "measure": "Unidade",
                    "keepBuying": False,
                    "last_change": datetime.now(),
                    "quantity_change": -10
                }
            ]
        }
    
    data = {
        "product": product
    }

    return data

def delete_product_use_case_sucessfully_data(code: str):

    expected_response = {
        "data":{
            "operation":"delete",
            "count": 1,
            "attributes": {
                "code": code
            }
        }
    }

    data = {
        "expected_response": expected_response
    }

    return data