import os

import base64

from bson import Binary

PORT = os.getenv("PORT")

def export_image_string64_to_binary(image: str):

    error_image = f"https://localhost:{PORT}/static/stock/src/assets/erro.jpg" 

    try:

        if (isinstance(image, str)):
            
            image_bytes = base64.b64decode(image)

            image_binary = Binary(image_bytes)

            return image_binary

        return error_image

    except:
        
        return error_image
        