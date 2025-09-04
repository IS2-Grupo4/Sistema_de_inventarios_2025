from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String, DateTime
from datetime import datetime
from app.database import Base

class MovimientoORM(Base):
    __tablename__ = "movimientos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    deposito_origen_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"), nullable=True)
    deposito_destino_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"), nullable=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relaciones (los ORM relacionados deben existir: ProductoORM, DepositoORM, UsuarioORM)
    producto = relationship("ProductoORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM", foreign_keys=[deposito_origen_id], back_populates="movimientos_origen")
    deposito_destino = relationship("DepositoORM", foreign_keys=[deposito_destino_id], back_populates="movimientos_destino")
    usuario = relationship("UsuarioORM", back_populates="movimientos")

