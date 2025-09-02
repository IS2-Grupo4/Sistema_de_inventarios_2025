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


def listarProductos():
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
    listarProductos()
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

def actualizar_producto():
    if not productos:
        print("No hay productos para actualizar.\n")
        return
    
    listarProductos()
    try:
        producto_id = int(input("Ingrese el ID del producto a actualizar: "))
        for p in productos:
            if p.id == producto_id:
                print(f"\nEditando '{p.nombre}' (deja vacío para mantener el valor actual)\n")

                nuevo_nombre = input(f"Nombre [{p.nombre}]: ").strip()
                nuevo_sku = input(f"SKU [{p.sku}]: ").strip()
                nueva_descripcion = input(f"Descripción [{p.descripcion}]: ").strip()
                
                try:
                    nuevo_stock = input(f"Stock [{p.stock}]: ").strip()
                    nuevo_stock = int(nuevo_stock) if nuevo_stock else p.stock
                except ValueError:
                    print("Stock inválido. Manteniendo valor anterior.")
                    nuevo_stock = p.stock

                try:
                    nuevo_stock_min = input(f"Stock mínimo [{p.stock_minimo}]: ").strip()
                    nuevo_stock_min = int(nuevo_stock_min) if nuevo_stock_min else p.stock_minimo
                except ValueError:
                    print("Stock mínimo inválido. Manteniendo valor anterior.")
                    nuevo_stock_min = p.stock_minimo

                # Actualizar atributos
                p.nombre = nuevo_nombre or p.nombre
                p.sku = nuevo_sku or p.sku
                p.descripcion = nueva_descripcion or p.descripcion
                p.stock = nuevo_stock
                p.stock_minimo = nuevo_stock_min

                print(f"Producto '{p.nombre}' actualizado con éxito.\n")
                return
        
        print("No existe un producto con ese ID.\n")
    except ValueError:
        print("Ingrese un número válido.\n")


while True:
     try:  
         print("0_Salir")
         print("1_Crear produtos")
         print("2_Listar produtos")
         print("3_Borrar productos\n")
         print("4. Actualizar productos\n")
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
              listarProductos()
         elif opcion==3:
             borrarProducto()
         elif opcion == 4:
                actualizar_producto()
     except ValueError:
        print("Ingrese un número válido.\n")     
