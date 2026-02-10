import os

PORT = os.getenv("PORT")

import base64

def export_image_binary_to_string64(image: bytes) -> str:

    try:
        
        error_image = f"https://localhost:{PORT}/static/erro.jpg"

        if not image:

            return error_image

        if image and isinstance(image, (bytes, bytearray)):

            base64_str = base64.b64encode(image).decode("utf-8")

            return f"data:image/png;base64,{base64_str}"
        
        else:

            return error_image
    
    except:

        return error_image
