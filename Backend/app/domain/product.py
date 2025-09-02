class Producto:
    def __init__(self, id: int, nombre: str, sku: str, stock: int, 
                 stock_minimo: int, descripcion: str):
        self.id = id
        self.nombre = nombre
        self.sku = sku
        self.stock = stock
        self.stock_minimo = stock_minimo
        self.descripcion = descripcion
    
    def validar(self, productos_existentes: list = None):
        """
        Valida que el producto cumpla con las reglas básicas
        y que no se duplique nombre ni SKU.
        """
        # Validaciones básicas
        if not self.nombre or len(self.nombre.strip()) == 0:
            raise ValueError("El producto debe tener un nombre")
        
        if not self.sku or len(self.sku.strip()) < 3:
            raise ValueError("El SKU debe tener al menos 3 caracteres")
        
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        if self.stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo")
        
        if self.stock < self.stock_minimo :
            raise ValueError("El stock es menor al stock minimo")

        # Validaciones de duplicados
        if productos_existentes:
            for p in productos_existentes:
                if p.nombre.lower() == self.nombre.lower():
                    raise ValueError(f"Ya existe un producto con el nombre '{self.nombre}'")
                if p.sku.lower() == self.sku.lower():
                    raise ValueError(f"Ya existe un producto con el SKU '{self.sku}'")
    
    def actualizar_stock(self, nueva_cantidad: int):
        """Actualiza la cantidad de stock"""
        if nueva_cantidad < 0:
            raise ValueError("El stock no puede ser negativo")
        self.stock = nueva_cantidad
    
    def tiene_stock_suficiente(self, cantidad_requerida: int) -> bool:
        """Verifica si hay stock suficiente para una operación"""
        return self.stock >= cantidad_requerida
    
    def esta_en_stock_critico(self) -> bool:
        """Verifica si el stock está por debajo del mínimo"""
        return self.stock < self.stock_minimo
    
    def generar_alerta_stock(self) -> str:
        """Genera mensaje de alerta si el stock es crítico"""
        if self.esta_en_stock_critico():
            return f"ALERTA: Producto {self.nombre} (SKU: {self.sku}) " \
                   f"tiene stock crítico: {self.stock} unidades. " \
                   f"Mínimo requerido: {self.stock_minimo} unidades."
        return ""
