from app.domain.movimiento import Movimiento
from app.db.modelsORM.movimientoORM import MovimientoORM


def movimiento_to_orm(movimiento: Movimiento) -> MovimientoORM:
    """
    Convierte un objeto de dominio Movimiento a un objeto ORM MovimientoORM.
    """
    return MovimientoORM(
        id=movimiento.id,
        producto_id=movimiento.producto_id,
        deposito_origen_id=movimiento.deposito_origen_id,
        deposito_destino_id=movimiento.deposito_destino_id,
        usuario_id=movimiento.usuario_id,
        cantidad=movimiento.cantidad,
        fecha=movimiento.fecha,
        tipo=movimiento.tipo,
    )

#movimiento_to_orm: se usa cuando querés guardar en la DB un Movimiento creado en tu lógica de negocio.

def orm_to_movimiento(orm_obj: MovimientoORM) -> Movimiento:
    """
    Convierte un objeto ORM MovimientoORM a un objeto de dominio Movimiento.
    """
    return Movimiento(
        id=orm_obj.id,
        producto_id=orm_obj.producto_id,
        deposito_origen_id=orm_obj.deposito_origen_id,
        deposito_destino_id=orm_obj.deposito_destino_id,
        usuario_id=orm_obj.usuario_id,
        cantidad=orm_obj.cantidad,
        fecha=orm_obj.fecha,
        tipo=orm_obj.tipo,
    )
#orm_to_movimiento: se usa cuando traés datos desde la DB (con SQLAlchemy) y querés transformarlos a tu modelo de dominio para trabajar en el core.
