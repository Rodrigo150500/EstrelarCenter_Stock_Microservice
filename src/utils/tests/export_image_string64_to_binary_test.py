import os
from bson import Binary

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from .data.export_image_string64_to_binary_data import export_image_sucessfully, export_image_with_error

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

host = f"{HOST}:{PORT}"

def test_export_image_sucessfully():

    data = export_image_sucessfully()

    response = export_image_string64_to_binary(data["image"], host)

    assert response == Binary(data["expected_response"])


def test_export_image_with_error():

    data = export_image_with_error()

    response = export_image_string64_to_binary(data["image"], host)

    assert response == data["expected_response"]