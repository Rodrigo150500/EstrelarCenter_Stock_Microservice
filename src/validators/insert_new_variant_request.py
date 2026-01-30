from cerberus import Validator

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def insert_new_variant_request(params: dict, body: dict) -> None:
    
    params_validate = Validator({
        "code": {"type": "string", "required": True, "empty": False},
    })

    body_validate = Validator({         
            "description": {"type": "string", "required": True, "empty": False},
            "stock": {"type": "integer", "required": True, "empty": False},
            "image": {"type": "string", "required": True, "empty": False},
            "brand": {"type": "string", "required": False},
            "reference": {"type": "string", "required": False},
            "location": {"type": "string", "required": False},
            "measure": {"type": "string", "required": True, "empty": False},
            "keepBuying": {"type": "boolean", "required": True, "empty": False},
            "quantity_change":{"type": "integer", "required": True, "empty": False}
    })
    
    response_body = body_validate.validate(body)
    response_params = params_validate.validate(params)

    if response_body is False:
        error = body_validate.errors
        error_key_message = list(error.keys())[0]
        error_message = error[error_key_message]

        formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

        print(f"Error:[InsertNewVariantRequest][Body]: {formatted_error_message}")

        raise HttpUnprocessableEntity(
        message=formatted_error_message
        )
    
    if response_params is False:
        error = params_validate.errors
        error_key_message = list(error.keys())[0]
        error_message = error[error_key_message]

        formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

        print(f"Error:[InsertNewVariantRequest][Params]: {formatted_error_message}")

        raise HttpUnprocessableEntity(
        message=formatted_error_message
        )