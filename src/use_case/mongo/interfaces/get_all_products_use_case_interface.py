from abc import ABC, abstractmethod

from src.main.http_types.http_response import HttpResponse


class GetAllProductsMongoUseCaseInterface(ABC):

    @abstractmethod
    def handle(self) -> HttpResponse:
        pass