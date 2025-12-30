from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from cerberus import Validator

def get_image_product_validator_request(params: dict):

  params_validator = Validator({  
        "code":{"type": "string", "required":True},
        "item":{"type": "integer", "required": True}
            })

  response = params_validator(params)

  if response is False:

    error = params_validator.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    print(f"Error:[GetImageProductValidatorRequest][Params]: {formatted_error_message}")

    raise HttpUnprocessableEntity(
      message=params_validator.errors,
      expected_data={
        "code":"123"
      }
    )
  