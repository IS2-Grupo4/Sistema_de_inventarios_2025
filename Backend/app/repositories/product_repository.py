from sqlalchemy.orm import Session
from Backend.app.domain.models.product import Producto

class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def add(self, producto: Producto):
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def get_all(self):
        return self.db.query(Producto).all()

    def get_by_id(self, producto_id: int):
        return self.db.query(Producto).filter(Producto.id == producto_id).first()

    def delete(self, producto_id: int):
        producto = self.get_by_id(producto_id)
        if producto:
            self.db.delete(producto)
            self.db.commit()
        return producto