# Más filtros SQL

## Filtrar fechas y números
- ​En primer lugar, analicemos los tres tipos de datos comunes que encontrará en las bases de datos: ​cadenas, numéricos y de fecha y hora.
- ​Datos de cadena son datos que consisten en una secuencia ordenada de caracteres.
- Estos caracteres pueden ser números, letras o símbolos.
- ​Por ejemplo, encontrará cadenas de datos en los nombres de usuario, ​como un nombre de usuario: analyst10.
- Datos ​numéricos son datos que constan de números, ​como el recuento de intentos de inicio de sesión.
- ​A diferencia de las cadenas, las operaciones matemáticas se pueden usar en datos numéricos, ​como la multiplicación o la suma.
- ​Datos de fecha y hora se refieren a los datos que representan una fecha u hora.
- ​Anteriormente, aplicábamos filtros mediante cadenas de datos, pero ​ahora vamos a trabajar con datos numéricos y de fecha y hora.
- ​Como analista de Seguridad, con frecuencia necesitará consultar números y fechas.
- Por ejemplo, podríamos filtrar las fechas de los parches para encontrar las máquinas que necesitan una actualización, ​o podríamos filtrar los intentos de inicio de sesión para mostrar solo ​los realizados en un período de tiempo determinado.
- ​Aprendimos sobre los operadores en el último vídeo y ​los volveremos a usar para números y fechas.
- ​Los operadores comunes para trabajar con ​tipos de datos numéricos o de fecha y hora incluyen: igual, mayor que, menor que, ​no igual a, mayor o igual a y menor que o igual a.
- ​Supongamos que quieres buscar los intentos de inicio de sesión realizados después de las 18:00 horas.
- ​Debido a que esto ha pasado el horario laboral normal, ​debes buscar patrones sospechosos.
- Puede identificar estos intentos utilizando el operador mayor que en el filtro.
- ​Empezaremos a escribir nuestra consulta en SQL.
- Empezamos indicando que queremos seleccionar todas las columnas de la tabla ​log_in_attempts.
- Luego agregaremos nuestro filtro con WHERE.
- ​Nuestra condición indica que el valor de la columna de hora debe ser mayor o, en el caso de ​fechas y horas, posterior a «18:00», que es la forma en que se escriben las 6 p. m. en SQL.
- ​Ejecutemos esto y examinemos el resultado.
- Ahora tenemos una lista de los intentos de inicio de sesión realizados después de las 6 p. m.
- ​También podemos filtrar por números y fechas usando el operador BETWEEN.
- ​BETWEEN es un operador que filtra números o fechas dentro de un rango.
- ​Un ejemplo de esto sería buscar ​todos los parches instalados dentro de un rango determinado.
- ​¡Hagámoslo! Busquemos todos los parches instalados entre el 1 de marzo de ​2021 y el 1 de septiembre de 2021.
- ​En nuestra consulta, empezamos por seleccionar todos los registros FROM de la tabla de máquinas.
- ​Y añadimos el operador BETWEEN en la sentencia WHERE.
- ​Analicemos la declaración.
- ​Primero, después de WHERE, indicamos qué columna filtrar, ​en nuestro caso, OS_Patch_Date.
- ​Luego viene nuestro operador BETWEEN.
- ​Luego agregamos el principio de nuestro rango, escribimos AND y ​terminamos agregando el final de nuestro rango y un punto y coma.
- ​Ahora, ejecutemos esto y exploremos el resultado.
- ​¡Y ahora tenemos una lista de todas las máquinas parcheadas entre esas dos fechas!
- Es importante tener en cuenta que cuando filtramos por cadenas ​, fechas y horas, utilizamos comillas para especificar lo que buscamos.
- ​Sin embargo, para los números, no utilizamos comillas.

---

## Operadores para filtrar fechas y números
- Números, fechas y horas en ciberseguridad
   - Los analistas de seguridad no sólo trabajan con datos de cadena, o datos formados por una secuencia ordenada de caracteres.
   - También trabajan frecuentemente con datos numéricos, o datos formados por números.
   - Algunos ejemplos de datos numéricos que puede encontrar en su trabajo como analista de seguridad incluyen:
      - el número de intentos de inicio de sesión
      - el recuento de un tipo específico de entrada de registro
      - el volumen de datos que se envían desde una fuente
      - el volumen de datos que se envían a un destino
      - el volumen de datos que se envían a un destino
   - También se encontrará con Datos de fecha y hora, o datos que representan una fecha y/o una hora.
   - Como primer ejemplo, los registros generalmente pondrán una marca de tiempo en cada registro.
   - Otros datos de fecha y hora pueden ser:
      - fechas de inicio de sesión
      - horas de inicio de sesión
      - fechas de los parches
      - la duración de una conexión

- Operadores de comparación
   - En SQL, el filtrado de datos numéricos y de fecha y hora suele implicar operadores.
   - Puede utilizar los siguientes operadores en sus filtros para asegurarse de que devuelve sólo las filas que necesita:

| operador | utilice |
| --- | --- |
| < | menor que |
| > | mayor que |
| = | igual a |
| <= | menor o igual que |
| >= | mayor que o igual a |
| <> | no igual a |
| != | no igual a |

- Incorporación de operadores a los filtros
   - Estos operadores de comparación se utilizan en la cláusula WHERE al final de una consulta.
   - La siguiente consulta utiliza el operador > para filtrar la columna birthdate.
   - Puede ejecutar esta consulta para explorar su resultado:
   ```sql
   SELECT firstname, lastname, birthdate
   FROM employees
   WHERE birthdate > '1970-01-01';
   ```
   - Esta consulta devuelve los nombres y apellidos de los empleados nacidos después de, pero no en, '1970-01-01' (o el 1 de enero de 1970).
   - Si en su lugar utilizara el operador >=, los resultados también incluirían resultados exactamente en '1970-01-01'.
   - En otras palabras, el operador > es exclusivo y el operador >= es inclusivo.
   - Un operador exclusivo es un operador que no incluye el valor de comparación.
   - Un operador inclusivo es un operador que incluye el valor de comparación.

- BETWEEN
   - Otro operador utilizado tanto para datos numéricos como para datos de fecha y hora es el operador BETWEEN.
   - BETWEEN filtra por números o fechas dentro de un rango.
   - El operador BETWEEN es inclusivo.
   - Esto significa que los registros con un hiredate del 1 de enero de 2002 o del 1 de enero de 2003 se incluyen en los resultados de la consulta anterior.
   - Por ejemplo, si desea encontrar los nombres y apellidos de todos los empleados contratados entre el 1 de enero de 2002 y el 1 de enero de 2003, puede utilizar el operador BETWEEN de la siguiente manera:
   ```sql
   SELECT firstname, lastname, hiredate
   FROM employees
   WHERE hiredate BETWEEN '2002-01-01' AND '2003-01-01';
   ```