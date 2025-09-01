# ¿Que es el "dominio"?

El "dominio" de una entidad, en criollo, son todas las reglas de negocio y datos que definen QUÉ ES esta entidad en nuestro sistema y QUÉ PUEDE HACER. Es lo primero que se modela en un proyecto grande.

# Todo se construye SOBRE el dominio
- La base de datos persiste el dominio
- La API expone el dominio
- Los servicios usan el dominio

# ¿Para qué sirve separar el "dominio"?
Para que todas estas reglas de negocio estén en un solo lugar claro, no mezcladas con la base de datos o la web. Si después cambian las reglas, sólo se modificá este archivo.

# Exento de tecnologias especificas
El dominio esta definido con lenguaje de programacion puro, indepdientemente de cual sea (Python, Java, C, etc) exentó de cualquier tipo de dependencia, frameword, DDBB.

# Las validaciones de los atributos se hacen en el dominio.

Ventajas de esto:
- Una sola vez: Las reglas se escriben una sola vez
- Obligatorio: Nadie puede crear un Producto inválido
- Consistente: Todos usan las mismas reglas
- Testeable: Podés testear las reglas sin API/DB