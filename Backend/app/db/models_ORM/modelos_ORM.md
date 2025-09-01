# Qué es un ORM?

ORM = Object-Relational Mapping

Es una capa que traduce objetos de Python a tablas en la base de datos y viceversa.

# En otras palabras:

   - Vos trabajás con objetos de Python (Producto, Usuario, etc.).
   - El ORM se encarga de convertir esos objetos en registros de la base de datos (filas y columnas) cuando guardás.
   - Y cuando consultás la base de datos, te devuelve objetos de Python, no tuplas o diccionarios crudos.

**Recordar que la base de datos utiliza lenguaje SQL, no entiende lenguaje python. El ORM es el traductor entre el lenguaje y la base de datos.** 

Esto nos ahorra el tener que saber utilizar dos lenguajes distintos, y si no estamos duchos con SQL no es problema.

**Cada entidad definida en el dominio suele tener su propio modelo ORM**