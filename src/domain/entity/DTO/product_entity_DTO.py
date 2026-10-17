from typing import TypedDict, NotRequired


class ProductCreateDTO(TypedDict):

    code: str
    description: str
    brand: NotRequired["str"]
    reference: NotRequired["str"]
    location: NotRequired[list["str"]]
    image: str
    measure: str
    quantity_change: int
    stock: int
    keepBuying: bool
    warehouse: NotRequired[WarehouseDTO]


class WarehouseDTO(TypedDict):

    quantity_change: int
    stock: int
    measure: str


class ProductCreateDTOProductResponse(TypedDict):

    _id: str
    brand: str
    description: str
    image: str
    keepBuying: bool
    last_change: str
    location: list["str"]
    measure: str
    quantity_change: int
    reference: str
    stock: int

class ProductCreateDTOWarehouseResponse(TypedDict):

    