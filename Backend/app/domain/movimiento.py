from dataclasses import dataclass
from datetime import datetime

@dataclass
class Movimiento:
    id: int | None
    producto_id: int
    deposito_origen_id: int
    deposito_destino_id: int
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: str   # puede ser "ENTRADA", "SALIDA", "TRANSFERENCIA"


