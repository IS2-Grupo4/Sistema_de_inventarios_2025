from sqlalchemy.orm import Session
from app.db.models_ORM.product_orm import ProductoORM
from app.mappers.mapper_product import orm_a_dominio, dominio_a_orm
from app.domain.product import Producto
from app.db.squemas.products_squemas import PaginacionProductos

class ProductoRepository:
    def __init__(self, session: Session):
        self.session = session

    def obtener_por_id(self, producto_id: int) -> Producto | None:

        orm_obj = self.session.get(ProductoORM, producto_id)
        return orm_a_dominio(orm_obj) if orm_obj else None



    def listar(self, page=1, limit=10) -> PaginacionProductos:

        query = self.session.query(ProductoORM).order_by(ProductoORM.id)   

        """
        Destripando la linea de cod:

            self.session.query(ProductoORM):

            Crea un objeto Query que representa SELECT * FROM productos, pero todavía no pega a la BD.
            Esto te permite encadenar filtros, orden, etc., antes de ejecutar.

            Hasta que no utilices un metodo terminal la query no se va a ejecutar. (all(), first(), one(), count(), etc)

            order_by(ProductoORM.id):
            
            Para paginación estable, siempre se agrega un order_by (ej. por id). Sin orden, el motor puede devolver filas
            en un orden no determinístico y te puede “bailar” la paginación.

        """

        total_items = query.count()   # Primera Query
        total_pages = (total_items + limit - 1) // limit  # redondeo hacia arriba

        productos_orm = query.offset((page - 1) * limit).limit(limit).all()     #Segunda Query

        productos = [orm_a_dominio(p) for p in productos_orm]   #La query devolvio una lista de objetos ProductoORM, aca se transforman a modelos de dominio.

        return {
            "page": page,
            "limit": limit,
            "total_items": total_items,
            "total_pages": total_pages,
            "items": productos
        }

        




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