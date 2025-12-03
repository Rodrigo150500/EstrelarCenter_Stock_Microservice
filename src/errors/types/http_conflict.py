class HttpConflict(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)

        self.message = message
        self.status_code = 409
        self.name = "HttpConflict"