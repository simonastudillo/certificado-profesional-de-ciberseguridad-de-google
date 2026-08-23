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

---

## Consulta de una base de datos
- Por qué usamos una base de datos ya hecha: Crear tu propia base de datos desde cero es muy parecido a construir un coche en lugar de aprender a conducirlo.
- Es un proceso difícil porque hay que establecer manualmente todas las reglas para almacenar la información, evitar que se pierda y asegurarse de que el ordenador pueda encontrar datos específicos rápidamente.
- En lugar de pasar semanas construyendo ese complicado "motor", utilizamos la base de datos Chinook para que puedas ir directamente a la parte importante: aprender a hacer preguntas y obtener respuestas a partir de los datos.

- Consulta SQL básica
   - Hay dos palabras clave esenciales en cualquier consulta SQL: SELECT y FROM.
   - Utilizará estas palabras clave cada vez que desee consultar una base de datos SQL.
   - Utilizarlas juntas ayuda a SQL a identificar qué datos necesita de una base de datos y la tabla de la que los está devolviendo.
   - La base de datos Chinook incluye datos que podrían ser creados en una compañía de medios digitales.
   - Un analista de seguridad empleado por esta compañía podría necesitar consultar estos datos.
   - Por ejemplo, la base de datos contiene once tablas, incluyendo una tabla employees, una tabla customers, y una tabla invoices.
   - Estas tablas incluyen datos como nombres y direcciones.
   - Como ejemplo, puede ejecutar esta consulta para obtener datos de la tabla customers de la base de datos Chinook:
```sql
SELECT customerid, city, country
FROM customers;
```

- SELECT
   - La palabra clave SELECT indica qué columnas devolver.
   - Por ejemplo, puede devolver la columna customerid de la base de datos Chinook con:
      - SELECT customerid
   - También puede seleccionar varias columnas separándolas con una coma.
   - Por ejemplo, si desea obtener las columnas customerid y city, escriba SELECT customerid, city.
   - Si desea obtener todas las columnas de una tabla, puede acompañar la palabra clave SELECT de un asterisco (*).
   - La primera línea de la consulta será SELECT *.
   - Aunque las tablas que se consultan en este curso son relativamente pequeñas, el uso de SELECT * puede no ser aconsejable cuando se trabaja con bases de datos y tablas de gran tamaño; en esos casos, la salida final puede ser difícil de entender y puede ser lenta de ejecutar.

- FROM
   - La palabra clave SELECT siempre va acompañada de la palabra clave FROM.
   - FROM indica qué tabla consultar.
   - Para utilizar la palabra clave FROM, debe escribirla después de la palabra clave SELECT, a menudo en una nueva línea, y seguirla con el nombre de la tabla que está consultando.
   - Si quieres devolver todas las columnas de la tabla customers, puedes escribir:
   - SELECT * FROM customers;
   - Si desea finalizar la consulta aquí, ponga un punto y coma (;) al final para indicar a SQL que se trata de la consulta completa.
   - Los saltos de línea no son necesarios en las consultas SQL, pero a menudo se utilizan para que la consulta sea más fácil de entender.
   - Si lo prefiere, también puede escribir la consulta anterior en una sola línea.

- ORDER BY
   - Las tablas de bases de datos suelen ser muy complicadas, y aquí es donde resultan útiles otras palabras clave de SQL.
   - ORDER BY es una palabra clave importante para organizar los datos que se extraen de una tabla.
   - ORDER BY ordena los registros devueltos por una consulta en función de una o varias columnas especificadas.
   - Puede ser en orden ascendente o descendente.
   - La palabra clave ORDER BY ordena los registros basándose en la columna especificada después de esta palabra clave.
   - Por defecto, la secuencia será ascendente. Esto significa que si elige una columna que contenga datos numéricos, ordenará la salida de menor a mayor.
   - Por ejemplo, si se ordena en customerid, los números de identificación se ordenan de menor a mayor.
   - si la columna contiene caracteres alfabéticos, como en el ejemplo con la columna city, ordena los registros desde el principio del alfabeto hasta el final.
- Ordenación ascendente
   - Para utilizar la palabra clave ORDER BY, escríbala al final de la consulta y especifique una columna en la que basar la ordenación.
   - En este ejemplo, SQL devolverá las columnas customerid, city y country de la tabla customers, y los registros se ordenarán por la columna city:
```sql
SELECT customerid, city, country
FROM customers
ORDER BY city;
```
- Ordenación descendente
   - También puede utilizar ORDER BY con la palabra clave DESC para ordenar en orden descendente.
   - La palabra clave DESC es la abreviatura de "descendente" y le indica a SQL que ordene los números de mayor a menor, o alfabéticamente de la Z a la A.
   - Esto se puede hacer siguiendo ORDER BY con la palabra clave DESC.
   - Por ejemplo, puede ejecutar esta consulta para examinar cómo difieren los resultados cuando se aplica DESC:
```sql
SELECT customerid, city, country
FROM customers
ORDER BY city DESC;
```
- Ordenación basada en varias columnas
   - También puede elegir varias columnas para ordenar.
   - Por ejemplo, puede elegir primero la columna country y después la columna city.
   - SQL entonces ordena la salida por country, y para las filas con el mismo country, las ordena basándose en city.
   - Puede ejecutar esto para explorar cómo SQL muestra esto:
```sql
SELECT customerid, city, country
FROM customers
ORDER BY country, city;
```

---

## Recursos para completar los laboratorios SQL
- Este curso incluye actividades prácticas de laboratorio en las que tendrá la oportunidad de practicar el uso de consultas SQL en el terminal
- Lanzamiento de Qwiklabs
- Botón Comenzar Laboratorio
- Cuadro de diálogo de Control del laboratorio
- El temporizador
- Botón de Abrir Consola Linux
- Comprobar el progreso
- Uso de los comandos copiar/pegar
- Bloque de código
- Desplazamiento por
- Botón Finalizar Laboratorio