from sqlalchemy.orm import  Mapped, mapped_column
from app.database import Base
from sqlalchemy import Text, Integer, String

class ProductoORM(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    sku: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    stock_minimo: Mapped[int] = mapped_column(Integer, default=0)
    descripcion: Mapped[str] = mapped_column(Text, nullable=True)