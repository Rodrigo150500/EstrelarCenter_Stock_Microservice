from bson.objectid import ObjectId

def get_image_sucessfully_data():

    imagem_bytes = bytes([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
    0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
    0xDE, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,
    0x54, 0x08, 0xD7, 0x63, 0x60, 0x00, 0x00, 0x00,
    0x02, 0x00, 0x01, 0xE2, 0x26, 0x05, 0x9B, 0x00,
    0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,
    0x42, 0x60, 0x82
  ])

    params = {
        "code": '16',
        "item": 0
    }

    get_product_by_code = {
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        "16":[{
            "code": "16",
            "description": "IMA BORBOLETA C/04",
            "brand": "MAX PING",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": imagem_bytes
        },{
            "code": "16",
            "description": "IMA BORBOLETA C/04 A1",
            "brand": "Ima brand",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": imagem_bytes
        }]
    }

    data = {
        "params": params,
        "get_product_by_code": get_product_by_code,
    }

    return data


def get_image_return_product_not_found_data():

    params = {
        "code": '16',
        "item": 0
    }

    data = {
        "params": params
    }

    return data