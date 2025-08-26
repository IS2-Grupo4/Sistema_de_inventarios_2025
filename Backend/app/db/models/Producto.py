class ProductoORM:
    def __init__(self, producto_id: int, nombre: str, descripcion: str, precio: float, stock: int):
        self.producto_id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"<ProductoORM {self.nombre} (${self.precio}) Stock: {self.stock}>"

    def actualizar_stock(self, cantidad: int):
        """Modifica el stock sumando o restando según la cantidad."""
        self.stock += cantidad