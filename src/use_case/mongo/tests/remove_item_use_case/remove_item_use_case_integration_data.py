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


def remove_variant_succesfully_data(object_id_1: str):

    params = {
        "code": "10",
        "_id": str(object_id_1)
    }


    data = {
        "params": params
    }

    return data