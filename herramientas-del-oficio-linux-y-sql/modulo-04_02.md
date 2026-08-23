# Consultas SQL

## Consultas básicas
- ​Vamos a determinar ​qué computadora se ha asignado a un determinado empleado.
- ​Digamos que tenemos acceso a la tabla de empleados.
- ​La tabla de empleados tiene cinco columnas.
- ​Dos de ellas, employee_id y device_id, ​contienen la información que necesitamos.
- ​Escribiremos una consulta a esta tabla que ​devuelva sólo esas dos columnas de la tabla.
- ​Las dos palabras clave SQL que necesitamos para ​las consultas SQL básicas son SELECT y FROM.
- ​SELECT indica qué columnas devolver.
- ​FROM indica qué tabla consultar.
- ​El uso de estas palabras clave en SQL es muy similar ​a cómo utilizaríamos estas palabras en el lenguaje cotidiano.
- Por ejemplo, podemos pedirle a un amigo que seleccione ​manzanas y plátanos de ​la caja grande cuando vayamos a comprar fruta.
- ​Esto ya es muy similar a SQL.
- ​Así que vamos a utilizar SELECT y FROM en SQL para ​obtener la información que necesitamos sobre ​los empleados y las computadoras que utilizan. 
- ​Empezamos escribiendo la sentencia SQL (SELECT employee_id, device_id)
- ​Después de FROM, hemos identificado ​que la información se ​obtendrá de la tabla de empleados (FROM employees).
- ​Y después de SELECT, employee_id y device_id ​indican las dos columnas que ​queremos obtener de esta tabla.
- ​Note cómo una coma separa ​las dos columnas que queremos devolver.
- ​También merece la pena mencionar aquí un par de ​aspectos clave relacionados con la sintaxis de SQL.
- ​La sintaxis se refiere a las reglas que determinan ​qué está correctamente estructurado en un lenguaje de computación.
- ​En SQL, las palabras clave no distinguen entre mayúsculas y minúsculas, por lo que ​también podría escribir select y from en minúsculas, ​pero las estamos colocando en mayúsculas porque ​hace que la consulta sea más fácil de entender.
- ​Otro aspecto de esta sintaxis ​es que los puntos y coma se ​colocan al final de la sentencia.
- ​Y ahora, ejecutaremos la consulta pulsando Intro.
- ​El resultado nos da la información que ​necesitamos para emparejar a los empleados con sus computadoras.
- ​Supongamos que desea saber ​de qué departamento es el empleado que utiliza ​la computadora, o su ​nombre de usuario, o la oficina en la que trabaja.
- ​Para ello, podemos utilizar SQL para hacer ​otra sentencia que imprima ​todas las columnas de la tabla.
- ​Podemos hacerlo colocando un asterisco después de SELECT (SELECT * FROM employees).
- ​Esto se conoce comúnmente como select all.
- ​Ahora, ejecutemos esta consulta a la tabla de empleados en SQL.