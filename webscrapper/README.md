# Web Scraper: Remates Judiciales Costa Rica

## <ins>Propósito</ins>

El propósito de este web scraper/bot es proveer los remates judiciales diarios de la página del boletín judicial del Poder Judicial de Costa Rica. En este momento el bot convierte de manera rápida y eficiente los remates disponibles y crea un archivo fechado con los remates correspondientes de ese día. 

## <ins>Caso de uso</ins>

La idea es eventualmente crear un RESTful API que utiliza esta información para devolver un JSON con los remates. Usando el API se pueden crear aplicaciones y sitios web que usen el JSON devuelto para generar contenido.

## <ins>Siguientes pasos</ins>

Las siguientes dos metas a corto/mediano plazo son:

1) Crear un Single Page App (SPA) en React en donde se puedan filtrar y ver los diferentes activos por rematar en una manera elegante y simple para el usuario. El plan es crear una lista de cartas o recuadros que al darle click sobre ellos, abran un Modal con la información relevante de cada remate y de ser necesario un link a una vista detallada del remate. Esta página contaría con una opción de búsqueda y filtro para lograr que el usuario encuentre los remates que se ajusten a sus preferencias. Por ejemplo: tipo de remate (vehículo, tipo de vehículo, fabricante de vehículo, propiedad, precio de remate, precio de remate, ubicación de la subasta, etc.)  
2) Crear un RESTful API que devuelva la información en formato JSON para ser consumido no sólo por la SPA descrita en el punto anterior sino hacerlo público bajo la especificación de OpenAPI (OAS)

Metas a largo plazo:

1) Agregar pruebas
2) Hacer una versión para JS 
3) Analizar el rendimiento para optar por la mejor versión
4) Publicar para el consumo público
5) Hostear la aplicación: puedo empezar publicando con Heroku u otras opciones por investigar. Hacer un deployment en Azure para aprender y si tiene sentido pagar por dejarlo ahí entonces hacerlo.

## <ins>Mejoras</ins>
### Refactors
1) Limpiar el código y hacerlo más modular, es decir crear abstracciones para poder reutilizar las funciones principales para futuros proyectos. Por ejemplo: crear una función con un parámetro definido como el URL que se quiere visitar y se encargue de crear el driver y devuelva el HTML que se quiere parsear. De tal manera, otra función con un parámetro de WebElement puede parsear el argumento que se le pase y esta devuelva la información parseada. Otra función definiría aspectos como el formato y otra función se puede encargar de crear los archivos fechados en diferentes formatos o sólo en algunos formatos específicos.
2) Agregar documentación antes de cada línea/bloque de código lo que tenga más sentido
3) Estructurar el proyecto en varias carpetas de tal manera que se vea más ordenado
