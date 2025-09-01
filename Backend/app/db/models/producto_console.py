from typing import List
from app.domain.product import Producto

productos: List[Producto] = []


def crearProducto():
    producto_id = len(productos) + 1
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))
    newProducto = Producto(id= producto_id,
                            nombre =nombre,
                             descripcion = descripcion,
                              precio= precio,
                              stock= stock
                              ) 
    newProducto.validar()
    productos.append(newProducto)
    print(f"Producto '{newProducto.nombre}' creado con éxito.\n")


def listarProducto():
    if not productos:
        print("La lista de productos esta vacía\n")
        return
    print("\n=== LISTA DE PRODUCTOS ===")
    for p in productos:
            print(p)

def borrarProducto():
    if not productos:
        print("No hay productos para borrar\n")
        return
    listarProducto()
    try:
        producto_id = int(input("Ingrese el ID del producto a borrar: "))
        for p in productos:
            if p.producto_id == producto_id:
                productos.remove(p)
                print(f"Producto '{p.nombre}' eliminado\n")
                return        
        print("No existe un producto con ese ID\n")    
    except ValueError:
        print("Ingrese un numero\n")

while True:
     try:  
         print("0_Salir")
         print("1_Crear produtos")
         print("2_Listar produtos")
         print("3_Borar productos\n")
         opcion=int(input("Elige una opcion: ")) 
         if opcion==0:
              break
         elif opcion==1:
            while True:
                crearProducto()
                salir=input("Para dejar de crear productos presione x :").lower()
                if salir=="x":
                     break
         elif opcion==2:
              listarProducto()
         elif opcion==3:
             borrarProducto()
     except ValueError:
        print("Ingrese un número válido.\n")     
