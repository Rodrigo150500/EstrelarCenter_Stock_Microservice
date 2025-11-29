class HttpNotFound(Exception):

    def __init__(self, message: str) -> None:
        
        self.message = message
        self.status_code = 404
        self.name = "NotFound"