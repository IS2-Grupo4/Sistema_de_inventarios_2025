from pydantic import BaseModel, ConfigDict
from typing import List

class ProductoCreate(BaseModel):
    nombre: str
    sku: str
    stock: int = 0
    stock_minimo: int = 0
    descripcion: str | None = None   #Atributo opcional, por defecto esta vacio

class ProductoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # permite mapear desde ORM (Lo que permite transformar de modelo ORM o modelo dominio a un JSON, que es lo que tiene que devolver un ENDPOINT)
    id: int
    nombre: str
    sku: str
    stock: int
    stock_minimo: int
    descripcion: str | None

class PaginacionProductos(BaseModel):
    page: int
    limit: int
    total_items: int
    total_pages: int
    items: List[ProductoResponse]