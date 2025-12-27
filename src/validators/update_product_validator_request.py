from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from cerberus import Validator


def update_product_validator_request(body: dict, params: dict):

  params_validate = Validator({
    "code": {"type": "string", "required": True, "empty": False},
    "index": {"type": "string", "required": True, "minlength": 1}
  })

  body_validate = Validator({         
    "code":{'type': 'string', 'required': True, "empty": False},
    "description": {"type": "string", "required": False},
    "stock": {"type": "integer", "required": False},
    "image": {"type": "string", "required": False},
    "brand": {"type": "string", "required": False},
    "reference": {"type": "string", "required": False},
    "location": {"type": "string", "required": False},
    "measure": {"type": "string", "required": False},
    "keepBuying": {"type": "boolean", "required": False},
    "quantity_change":{"type": "integer", "required": False}     
  })

  response_body = body_validate.validate(body)
  response_params = params_validate.validate(params)

  if response_body is False:
    error = body_validate.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    raise HttpUnprocessableEntity(
      message=formatted_error_message
    )
  
  if response_params is False:
    error = params_validate.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    raise HttpUnprocessableEntity(
      message=formatted_error_message
    )
  


