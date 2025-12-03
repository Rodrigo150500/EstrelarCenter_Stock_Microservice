from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

def insert_product_sucessfully():

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


    body = {
            'code': "16",
            'description': "Product A" ,
            'measure': "Unidade",
            'stock': 25,
            'brand': "Kit-Kat",
            'last_change': "+5 03/12/25 12:35:33"  ,
            'image': imagem_bytes,
            'location': "P9",
            'reference': "KIT104",
    }

    body["image"] = export_image_string64_to_binary(body['image'])

    expected_body = {
        "data":{
            "operation": "Insert",
            "count": 1,
            "attributes": body
        }
    }
    
    data = {
        "body": body,
        "expected_body": expected_body
    }

    return data


def insert_product_that_already_exists():

    body = {
            'code': "16",
            'description': "Product A" ,
            'measure': "Unidade",
            'stock': 25,
            'brand': "Kit-Kat",
            'last_change': "+5 03/12/25 12:35:33"  ,
            'image': "imagem_bytes",
            'location': "P9",
            'reference': "KIT104",
    }

   
    data = {
        "body": body,
    }

    return data


