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

---

## Actividad: Aplicar más filtros en SQL
- Introducción
   En este laboratorio, aplicará más filtros a las consultas SQL para recuperar información de una base de datos.
   - Utilizará operadores comunes en SQL para filtrar por fechas y horas específicas.
   - Utilizará el shell de MariaDB para ejecutar sus consultas SQL.

- Lo que hará
   - Filtrar los intentos de inicio de sesión realizados después de una fecha determinada
   - Filtrar los intentos de inicio de sesión realizados en un cierto Rango de fechas
   - Filtrar los intentos de inicio de sesión realizados a una hora determinada
   - Filtrar los intentos de inicio de sesión por ID

- Resumen de la actividad
   - Como analista de seguridad, a menudo deberás consultar números y fechas.
   - Por ejemplo, es posible que debas filtrar fechas de parches para descubrir qué máquinas necesitan una actualización.
   - También podrías filtrar intentos de acceso que se hayan realizado durante cierto período para investigar un incidente de seguridad.
   - Los operadores comunes para trabajar con datos numéricos o datos de fechas y horarios te ayudarán a filtrar datos con precisión.
   - Estos son algunos de los operadores que usarás:
      - = (igual a)
      - > (mayor que)
      - < (menor que)
      - <> (distinto de)
      - >= (mayor que o igual a)
      - <= (menor que o igual a)
   - En este lab, aplicarás estos operadores para filtrar de forma precisa números y fechas específicas.

- Situación
   - En esta situación, estás investigando un incidente de seguridad reciente.
   - Debes recopilar información sobre intentos de acceso en ciertas fechas y horarios.
   - De esa forma, podrás resolver un incidente de seguridad.
   - Estos son los pasos que seguirás:
      1. Recuperarás eventos de acceso realizados después de una fecha determinada.
      2. Restringirás el enfoque de la búsqueda para que filtre accesos en un período.
      3. Investigarás los accesos que se realizaron en determinados horarios.
      4. Filtrarás intentos de acceso en función del ID de los eventos.

- Comienza el lab

1. Recupera intentos de acceso realizados después de una fecha determinada
- Completa la consulta en SQL para recuperar datos de intentos de acceso realizados después del '2022-05-09'.
- ¿Cuántos intentos de acceso se realizaron después del 2022-05-09?
   - [ ] 111
   - [x] 125
   - [ ] 185
   - [ ] 134
- Completa la consulta en SQL para recuperar datos de intentos de acceso realizados a partir del '2022-05-09'.
- ¿Cuántos intentos de acceso se realizaron a partir del 2022-05-09?
   - [ ] 190
   - [ ] 186
   - [x] 165
   - [ ] 143

2. Recupera los accesos correspondientes a un período
- Ejecuta la consulta para recuperar los registros de acceso realizados después del 11 de mayo de 2022. Usa los operadores BETWEEN y AND para obtener resultados entre el '2022-05-09' y el '2022-05-11'.
- ¿Cuántos intentos de acceso se realizaron entre el 2022-05-09 y el 2022-05-11?
   - [ ] 157
   - [ ] 134
   - [ ] 160
   - [x] 123

3. Investiga los accesos realizados en determinados horarios
- Escribe una consulta en SQL para recuperar datos de intentos de acceso realizados antes de las '07:00:00'.
- ¿Cuál es el nombre de usuario en el quinto registro que se devuelve a partir de esta consulta?
   - [ ] acook
   - [ ] bisles
   - [ ] jrafael
   - [x] eraab
- Modifica la consulta para obtener resultados entre las '06:00:00' y las '07:00:00'.
- ¿A qué hora se realizó el primer intento de acceso entre las 06:00:00 y las 07:00:00?
   - [ ] 06:03:41
   - [x] 06:01:31
   - [ ] 06:15:41
   - [ ] 06:04:34

4. Investiga los accesos según el ID de los eventos
- Escribe una consulta para obtener los intentos de acceso con un event_id mayor que o igual a 100.
- ¿Cuál es la fecha de acceso del tercer resultado que devuelve tu consulta?
   - [x] 2022-05-09
   - [ ] 2022-05-10
   - [ ] 2022-05-11
   - [ ] 2022-05-08
- Modifica la consulta para obtener resultados de intentos de acceso con un event_id entre 100 y 150.
- ¿Cuál es el nombre de usuario del séptimo resultado que devuelve tu consulta?
   - [ ] bisles
   - [ ] gesparza
   - [ ] mabadi
   - [x] tmitchel

- Listado de queries utilizadas en el lab
```sql
-- PART 1
SELECT * 
FROM log_in_attempts 
WHERE login_date > '2022-05-09';

SELECT COUNT(*) quantity
FROM log_in_attempts
WHERE login_date > '2022-05-09';

SELECT * 
FROM log_in_attempts 
WHERE login_date >= '2022-05-09';

SELECT COUNT(*) quantity
FROM log_in_attempts
WHERE login_date >= '2022-05-09';

-- PART 2
SELECT * 
FROM log_in_attempts 
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';

SELECT COUNT(*) quantity
FROM log_in_attempts 
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';

-- PART 3
SELECT *
FROM log_in_attempts
WHERE login_time < '07:00:00';

SELECT *
FROM log_in_attempts
WHERE login_time < '07:00:00'
LIMIT 1 OFFSET 4;

SELECT *
FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00';

SELECT *
FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00'
ORDER BY login_time ASC;

-- PART 4
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100;

SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100
LIMIT 1 OFFSET 2;

SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150;

SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150
LIMIT 1 OFFSET 6;
```

---

## Ejemplo opcional: Aplicar más filtros en SQL
- Mismo laboratorio que el anterior.

---

## Ejemplo: Aplicar más filtros en SQL
- Resumen de la actividad
   - Este ejemplo proporciona un recorrido detallado y soluciones para la actividad de laboratorio "Aplicar más filtros en SQL".
   - Como analista de seguridad, a menudo necesitará refinar la recuperación de datos mediante el filtrado basado en fechas, horas y rangos específicos.
   - Este ejemplo lo guiará a través del uso de operadores SQL como >, >=, <, <=, BETWEEN y el filtrado por ID específicos.

- Listado de queries de ejemplo para el lab
```sql
SELECT *
FROM log_in_attempts
WHERE login_date > 'YYYY-MM-DD';

SELECT *
FROM log_in_attempts
WHERE login_date > '2023-01-15';

SELECT *
FROM log_in_attempts
WHERE login_date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD';

SELECT *
FROM log_in_attempts
WHERE login_date BETWEEN '2023-02-01' AND '2023-02-07';

SELECT *
FROM log_in_attempts
WHERE login_time = 'HH:MM:SS';

SELECT *
FROM log_in_attempts
WHERE login_time = '09:30:00';

SELECT *
FROM log_in_attempts
WHERE login_id = ID_Value;

SELECT *
FROM log_in_attempts
WHERE login_id = 503;
```

- Conclusión
   - Ahora ha practicado la aplicación de filtros más específicos en SQL utilizando operadores de comparación (>, >=, <, <=, =) y el operador BETWEEN para recuperar datos basados en fechas, horas e identificadores únicos.
   - Estas habilidades son esenciales para llevar a cabo investigaciones exhaustivas y extraer información específica de registros de seguridad y bases de datos.
   - Se está volviendo más experto en el uso de SQL para analizar y comprender los datos relacionados con la seguridad.