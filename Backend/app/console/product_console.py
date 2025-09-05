import sys                                                                                                              
from pathlib import Path

# Ruta absoluta del archivo actual
current_file = Path(__file__).resolve()

# Buscar la carpeta "Backend" hacia arriba
backend_path = None
for parent in current_file.parents:
    if parent.name == "Backend":
        backend_path = parent
        break

if backend_path and str(backend_path) not in sys.path:
    sys.path.append(str(backend_path))



from typing import List

from app.domain.product import Producto
from app.repositories.product_repository import ProductoRepository
from app.db.database import SessionLocal


repo_producto = ProductoRepository(SessionLocal())

def menu():

    print("1. Crear producto")
    print("2. Obtener producto por ID")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Actualizar producto")
    print("0. Salir")

    opcion=int(input("Elige una opcion: "))

    return opcion

def crearProducto():
    nombre = input("Nombre del producto: ")
    sku=input("SKU: ")
    descripcion = input("Descripción: ")
    stock = int(input("Stock inicial: "))
    stock_minimo = int(input("Stock minimo: "))

    newProducto = Producto(
                            id=None,
                            nombre=nombre,
                            sku=sku,
                            descripcion = descripcion,
                            stock= stock,
                            stock_minimo=stock_minimo
                              ) 
    
    return repo_producto.agregar(newProducto)



def obtener_producto_por_id(id):
    producto = repo_producto.obtener_por_id(id)
    
    return producto



def listarProductos():
    
    productos=repo_producto.listar()


    if productos:
        productos["items"] = [p.__dict__ for p in productos["items"]]
        print(productos)
    
    print("No hay elementos cargados")


def borrarProducto(id):
        return repo_producto.eliminar(id)

def actualizar_producto(id):
    
    return repo_producto.editar(id)


def main():

    while True:
         
            
            opcion = menu()
            
            if opcion==0:
                break

            if opcion==1:
                try:
                    producto = crearProducto()
                    print(producto)
                except Exception as Err:
                    print(Err)
        

            if opcion==2:
                
                try:
                    id = int(input("Ingresa el ID del producto: "))
                    producto = obtener_producto_por_id(id)
                except ValueError:
                    print("Tenes que ingresar un numero")


                if producto:
                    print(producto)
                print("No se encontro un producto con ese ID")
            

            if opcion == 3:
                listarProductos()

                try:
                    id = int(input("Ingresa el ID del producto: "))
                    producto = borrarProducto(id)
                    if producto:
                        print("Producto eliminado exitosamente")
                except ValueError:
                    print("Tenes que ingresar un numero")

            if opcion == 4:
                listarProductos()

            if opcion == 5:

                try:
                    listarProductos()
                    id = int(input("Ingresa el ID del producto: "))
                    print("Ingresa los nuevos atributos: ")
                    n_nombre = input("Nombre del producto: ")
                    n_sku=input("SKU: ")
                    n_descripcion = input("Descripción: ")
                    n_stock = int(input("Stock inicial: "))
                    n_stock_minimo = int(input("Stock minimo: "))

                    n_producto = Producto(id, n_nombre, n_sku, n_stock, n_stock_minimo, n_descripcion)

                    producto_update = actualizar_producto(n_producto)
                    print(producto_update)
                except Exception as Err:
                    print(Err)


        

if __name__ == "__main__":
    main()