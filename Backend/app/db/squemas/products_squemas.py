from pydantic import BaseModel

class Product(BaseModel):
    nombre : str
    sku : str
    descripcion : str | None = None
    stock : int
    stock_minimo : int

