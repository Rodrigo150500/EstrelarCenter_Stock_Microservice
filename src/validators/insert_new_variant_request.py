from cerberus import Validator

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def insert_new_variant_request(params: dict, body: dict) -> None:
    
    params_validate = Validator({
        "code": {"type": "string", "required": True, "empty": False},
    })

    body_validate = Validator({         
        "description": {"type": "string", "required": True, "empty": False},
        "brand": {"type": "string", "required": False},
        "reference": {"type": "string", "required": False},
        "location": {"type": "list", "required": False},
        "image": {"type": "string", "required": True},
        "measure": {"type": "string", "required": True, "allowed": ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]},
        "quantity_change":{"type": "integer", "required": True, "dependencies": "stock"},
        "stock": {"type": "integer", "required": True, "min": 0, "empty": False,"dependencies": "quantity_change"},
        "keepBuying": {"type": "boolean", "required": True},
        "warehouse": {
            "type": "dict",
            "required": False,
            "schema":{
            "quantity_change": {"type": "integer", "required": True, 'empty': False,    "dependencies": "^warehouse"},
            "stock": {"type": "integer", "required": True, "min": 0, "dependencies": "^warehouse"},
            "measure": {"type": "string", "required": True, "allowed": ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"], "dependencies": "^warehouse"},
            "location": {"type": "list", "required": False, "dependencies": "^warehouse"}
            }
        }
    })
    
    response_body = body_validate.validate(body)
    response_params = params_validate.validate(params)

    if response_body is False:
        error = body_validate.errors

        raise HttpUnprocessableEntity(
        message=error
        )
    
    if response_params is False:
        error = params_validate.errors

        raise HttpUnprocessableEntity(
        message=error
        )