from dotenv import load_dotenv
load_dotenv("dev.env")

from src.utils.export_image_binary_to_string64 import export_image_binary_to_string64

from .data.export_image_binary_to_string64_data import export_image_to_string_sucessfully, export_image_with_error

def test_export_image_to_string_sucessfully():

    data = export_image_to_string_sucessfully()

    response = export_image_binary_to_string64(data["image"])

    assert response == data["expected_response"]
    assert isinstance(response, str)


def test_export_image_with_error():

    data = export_image_with_error()

    response = export_image_binary_to_string64(data["image"])

    assert response == data["expected_response"]
    assert isinstance(response, str)