from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from cerberus import Validator

def get_product_validator_request(params: dict):
  
  body_validator = Validator({  
        "code":{"type": "string", "required":True, "minlength": 1}
            })

  response = body_validator(params)
  
  if response is False:

    error = body_validator.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    print(f"Error:[GetProductValidatorRequest][Params]: {formatted_error_message}")

    raise HttpUnprocessableEntity(
      message=body_validator.errors
    )
  