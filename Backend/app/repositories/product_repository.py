from sqlalchemy.orm import Session
from app.db.models_ORM.product_orm import ProductoORM
from app.mappers.mapper_product import orm_a_dominio, dominio_a_orm
from app.domain.product import Producto

class ProductoRepository:
    def __init__(self, session: Session):
        self.session = session

    def obtener_por_id(self, producto_id: int) -> Producto | None:

        orm_obj = self.session.get(ProductoORM, producto_id)
        return orm_a_dominio(orm_obj) if orm_obj else None

    def listar(self) -> list[Producto]:
        return [orm_a_dominio(p) for p in self.session.query(ProductoORM).all()]

    def agregar(self, producto: Producto) -> Producto:
        orm_obj = dominio_a_orm(producto)
        self.session.add(orm_obj)
        self.session.commit()
        self.session.refresh(orm_obj)
        return orm_a_dominio(orm_obj)
    
    def editar(self, producto: Producto):
        orm_obj = self.session.get(ProductoORM, producto.id)

        if not orm_obj:
            raise ValueError(f"Producto con ID {producto.id} no encontrado")
        
        orm_obj.nombre = producto.nombre
        orm_obj.sku = producto.sku
        orm_obj.stock = producto.stock
        orm_obj.stock_minimo = producto.stock_minimo
        orm_obj.descripcion = producto.descripcion

        self.session.commit()
        self.session.refresh(orm_obj)

        return orm_a_dominio(orm_obj)
    
    def eliminar(self, producto_id:int):
        orm_obj = self.session.get(ProductoORM, producto_id)

        if not orm_obj:
            raise ValueError(f"Producto con ID {producto_id} no encontrado")
        
        self.session.delete(orm_obj)
        self.session.commit()