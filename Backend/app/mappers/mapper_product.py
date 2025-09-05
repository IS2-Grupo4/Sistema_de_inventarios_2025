from app.domain.product import Producto as ProductoDominio
from app.db.models_ORM.product_orm import ProductoORM

def orm_a_dominio(orm: ProductoORM) -> ProductoDominio:
    return ProductoDominio(
        id=orm.id,
        nombre=orm.nombre,
        sku=orm.sku,
        stock=orm.stock,
        stock_minimo=orm.stock_minimo,
        descripcion=orm.descripcion,
    )

def dominio_a_orm(dominio: ProductoDominio) -> ProductoORM:
    return ProductoORM(
        id=None,
        nombre=dominio.nombre,
        sku=dominio.sku,
        stock=dominio.stock,
        stock_minimo=dominio.stock_minimo,
        descripcion=dominio.descripcion,
    )