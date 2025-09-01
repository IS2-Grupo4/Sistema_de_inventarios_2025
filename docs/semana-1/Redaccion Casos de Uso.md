# Casos de uso

## CU 000 - Registrarse


## CU 001 - Iniciar sesion

**Actor:** Administrador/Operador

**Objetivo:** Permitir al usuario autenticarse en el sistema y acceder según sus permisos

### Flujo principal                                                                   
1. El usuario ingresa usuario y contraseña                          
2. El sistema valida las credenciales                               
3. El le asigna un rol y carga las funcionalidades permitidas       
4. El usuario accede al sistema

## CU 002 - Crear deposito

**Actor:** Administrador

**Objetivo:** Permitir que el usuario agregue un nuevo depósito al sistema

### Flujo principal
1. El usuario selecciona la opción “Crear depósito” en la interfaz.
2. El sistema solicita los datos necesarios:
   - Nombre del depósito
   - Ubicación
   - Capacidad (opcional)
3. El usuario ingresa los datos y confirma.
4. El sistema valida que no exista un depósito con el mismo nombre.
5. El sistema crea el deposito
5. El sistema confirma al usuario que el depósito fue creado exitosamente.

## CU 003 - Eliminar deposito

**Actor:** Administrador

**Objetivo:** Permitir que el usuario elimine un depósito existente del sistema

### Flujo principal
1. El usuario selecciona la opción “Eliminar depósito”.
2. El sistema muestra la lista de depósitos disponibles.  
3. El usuario selecciona el depósito que desea eliminar.  
4. El sistema solicita confirmación de la eliminación.  
5. El usuario confirma la acción.
6. El sistema elimina el deposito     
7. El sistema confirma al usuario que el depósito fue eliminado exitosamente.

## CU 004 - Editar deposito

**Actor**: Administrador

**Objetivo**: Permitir que el usuario modifique un depósito existente del sistema

### Flujo principal
1. El usuario selecciona la opción “Editar depósito”.
2. El sistema muestra la lista de depósitos disponibles.  
3. El usuario selecciona el depósito que desea modificar.  
4. El sistema muestra los datos actuales del depósito.  
5. El usuario modifica los campos necesarios (nombre, ubicación, capacidad, etc.)  
6. El sistema valida que los nuevos datos sean correctos y no generen duplicados.
7. El sistema actualiza el deposito  
8. El sistema confirma al usuario que el depósito fue actualizado exitosamente.

## CU 005 - Crear producto

**Actor:**: Administrador

**Objetivo:** Permitir que el usuario registre un nuevo producto en el sistema.  

### Flujo principal:
1. El usuario selecciona la opción “Crear producto”.  
2. El sistema muestra un formulario para ingresar los datos del producto (nombre, código, descripción, precio, etc.).  
3. El usuario completa los campos requeridos.  
4. El usuario confirma la creación.  
5. El sistema valida los datos ingresados.  
6. El sistema confirma al usuario que el producto fue creado exitosamente.

## CU 006 - Eliminar producto

**Actor:** Administrador

**Objetivo:** Permitir que el usuario elimine un producto existente del sistema.  
 
### Flujo principal:
1. El usuario selecciona la opción “Eliminar producto”.  
2. El sistema muestra la lista de productos disponibles.  
3. El usuario selecciona el producto que desea eliminar.  
4. El sistema solicita confirmación.  
5. El usuario confirma la eliminación.  
6. El sistema valida que el producto no tenga movimientos de stock pendientes.  
7. El sistema confirma al usuario que el producto fue eliminado exitosamente.

## CU 007 - Editar producto

**Actor:** Administrador

**Objetivo:** Permitir que el usuario modifique los datos de un producto existente.  

### Flujo principal:
1. El usuario selecciona la opción “Editar producto”.  
2. El sistema muestra la lista de productos disponibles.  
3. El usuario selecciona el producto que desea modificar.  
4. El sistema muestra los datos actuales del producto.  
5. El usuario modifica los campos necesarios (nombre, precio, descripción, etc.).  
6. El usuario confirma los cambios.  
7. El sistema valida que los nuevos datos sean correctos.  
8. El sistema confirma al usuario que el producto fue actualizado exitosamente.

## CU 008 - Consultar stock

**Actor:** Administrador/operador

**Objetivo:** Permitir que el usuario consulte el nivel de stock de los productos en uno o varios depósitos.  

### Flujo principal:
1. El usuario selecciona la opción “Consultar stock”.  
2. El sistema muestra opciones de búsqueda y filtros (por producto, por depósito, por categoría, etc.).  
3. El usuario ingresa los criterios de búsqueda o selecciona las opciones deseadas.  
4. El sistema procesa la consulta.  
5. El sistema muestra los resultados de stock (cantidad disponible, ubicación del depósito, fecha de última actualización, etc.). 

## CU 009 - Registrar entrada

**Actor:** Operador

**Objetivo:** Permitir que el usuario registre la entrada de productos a un depósito.  

### Flujo principal:
1. El usuario selecciona la opción “Registrar entrada de stock”.  
2. El sistema solicita los datos necesarios:  
   - Producto  
   - Cantidad a ingresar  
   - Depósito de destino  
   - Fecha de entrada (opcional, por defecto la actual)  
3. El usuario ingresa los datos y confirma la operación.  
4. El sistema valida que los datos sean correctos y que el depósito exista.  
5. El sistema registra la entrada de stock.  
6. El sistema confirma al usuario que la entrada fue registrada exitosamente.

## CU 010 - Registrar salida

**Actor:** Operador

**Objetivo:** Permitir que el usuario registre la salida de productos desde un depósito.

### Flujo principal
1. El usuario selecciona la opción “Registrar salida de stock”.  
2. El sistema solicita los datos necesarios:  
   - Producto  
   - Cantidad a retirar  
   - Depósito de origen  
   - Fecha de salida (opcional, por defecto la actual)  
3. El usuario ingresa los datos y confirma la operación.  
4. El sistema valida que los datos sean correctos y que haya stock suficiente en el depósito de origen.  
5. El sistema registra la salida de stock.  
6. El sistema confirma al usuario que la salida fue registrada exitosamente.

## CU 011 - Generar alerta por stock bajo

**Actor:** Operador - (Interaccion automatica del Sistema)

**Objetivo:** Notificar al usuario cuando el stock de un producto en un depósito cae por debajo del nivel mínimo definido.  

### Flujo principal
1. El sistema monitorea los niveles de stock de manera automática.  
2. El sistema detecta que un producto en un depósito ha bajado del stock mínimo.  
3. El sistema genera una alerta.  
4. El sistema notifica al usuario responsable a través de la interfaz o vía correo (dependiendo de la configuración).  
5. El usuario recibe la alerta y toma la acción correspondiente (reposición de stock, ajuste, etc.).

## CU 012 - Registrar ingreso de usuario

**Actor:** Administrador/Operador - (Interaccion automatica del Sistema)

**Objetivo:** Registrar cada ingreso al sistema de los usuarios, ya sea un nuevo registro o un inicio de sesión

Flujo principal
1. El usuario ingresa al sistema (ya sea registrándose o haciendo login).    
2. El sistema registra automáticamente el acceso del usuario, incluyendo fecha y hora.  