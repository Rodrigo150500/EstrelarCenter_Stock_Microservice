from abc import ABC, abstractmethod

from src.main.http_types.http_response import HttpResponse


class GetProductsBySearchMongoUseCaseInterface(ABC):

    @abstractmethod
    def handle(self) -> HttpResponse:
        pass