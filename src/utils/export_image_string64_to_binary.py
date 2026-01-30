import os

import base64

from bson import Binary

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

def export_image_string64_to_binary(image: str) -> Binary | str:

    error_image = f"https://{HOST}:{PORT}/static/erro.jpg" 

    try:

        if (isinstance(image, str)):
            
            image_bytes = base64.b64decode(image)

            image_binary = Binary(image_bytes)

            return image_binary

        return error_image

    except:
        
        return error_image
        