from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MovimientoCreate(BaseModel):
    producto_id: int
    deposito_origen_id: int | None = None
    deposito_destino_id: int | None = None
    usuario_id: int
    cantidad: int
    tipo: str

class MovimientoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    producto_id: int
    deposito_origen_id: int | None
    deposito_destino_id: int | None
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: str
