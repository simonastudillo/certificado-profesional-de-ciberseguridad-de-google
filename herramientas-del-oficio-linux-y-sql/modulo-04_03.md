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

---

## Filtrados con AND, OR y NOT
- Las vulnerabilidades, por ejemplo, ​pueden depender de más de un factor.
- ​Por ejemplo, una ​vulnerabilidad de Seguridad puede estar relacionada con ​máquinas que utilizan un cliente de correo electrónico ​específico en un sistema operativo específico.
- ​Por lo tanto, para encontrar las posibles vulnerabilidades, ​necesitamos encontrar máquinas que utilicen ​tanto el cliente de correo electrónico como el sistema operativo.
- ​Para hacer una consulta con ​varias condiciones que deben cumplirse, ​utilizamos el operador AND entre dos condiciones distintas.
- ​AND es un operador que especifica que ​ambas condiciones deben cumplirse simultáneamente.
- ​Volviendo a nuestra analogía con ​las frutas y verduras, es lo mismo que pedirle a alguien que seleccione manzanas de ​la caja grande donde las manzanas son grandes y frescas.
- ​Esto significa que nuestros resultados no incluirán manzanas pequeñas, ​incluso si están frescas, ​ni manzanas podridas, incluso si son grandes.
- ​Solo incluirán manzanas grandes y frescas.
- ​Las manzanas deben cumplir ambas condiciones.
- ​Volviendo a nuestra base de datos, ​la tabla de máquinas muestra ​todos los sistemas operativos y clientes de correo electrónico.
- ​Queremos una lista de máquinas que ejecutan el sistema operativo ​1 y una lista de máquinas que utilizan el cliente de correo electrónico 1.
- ​En primer lugar, vamos a empezar por ​crear las primeras líneas de la consulta y ​decirle a SQL que SELECT * FROM de la tabla de máquinas.
- ​Luego, agregaremos la cláusula WHERE.
- ​Primero, indicamos ​la primera condición que debe cumplir, ​que la columna del sistema operativo tenga un valor de '0S 1'.
- ​Luego, usamos AND para unir esto a otra condición. 
- Y por último, introducimos la otra condición, ​en este caso, que ​la columna del cliente de correo electrónico debería ​tener un valor de «Cliente de correo electrónico 1"
- ​Vamos a ejecutar esto para obtener los resultados de la consulta.
- ¡Todos los resultados coinciden con nuestras dos condiciones!
- ​Sigamos y exploremos más formas de combinar ​diferentes condiciones trabajando con el operador OR.
- ​El operador OR es un operador que ​especifica que se puede cumplir cualquiera de las condiciones.
- ​En un diagrama de Venn, ​digamos que cada círculo representa una condición.
- ​Cuando se unen con OR, ​SQL seleccionará todas las filas que ​cumplan una de las condiciones.
- ​Y también está bien si cumple ambas condiciones.
- ​Ejecutemos otra consulta y usemos el operador OR.
- ​Supongamos que queremos que el ​filtro identifique las máquinas que tienen ​OS 1 u OS 3 porque ambos tipos necesitan un parche.
- ​Después de WHERE, nuestra primera condición indica que queremos ​filtrar, de modo que la consulta seleccione máquinas con 'OS 1'.
- ​Usamos el operador OR porque también queremos ​encontrar registros que coincidan con otra condición.
- ​Esta condición adicional se coloca después de O e ​indica que también se deben seleccionar máquinas que ejecuten «OS 3».
- Al ejecutar ​la consulta, ​nuestros resultados ahora incluyen registros que tienen un valor de ​OS 1 o OS 3 en la columna del sistema operativo.
- ​El último operador que analizaremos ​es el operador NOT.
- ​NOT niega una condición.
- ​En un diagrama, ​podemos mostrar esto seleccionando ​todas las entradas que no coincidan con nuestra condición.
- ​La condición está representada por el círculo.
- La parte rellenada fuera ​del círculo representa lo que se devuelve.
- ​Se trata de todos los datos que no coinciden con la condición.
- Por ejemplo, al elegir fruta, ​puedes buscar cualquier fruta que no sea una manzana.
- ​Eso es mucho ​más eficiente que decirle a tu amigo que quieres ​un plátano, una naranja o una lima, etc.
- ​Supongamos que desea actualizar ​todos los dispositivos de ​su empresa, excepto los que utilizan OS 3.
- ​Llevando esto a SQL, ​podemos escribir esta consulta.
- ​Colocamos NOT después de ​WHERE y antes del estado del filtro.
- ​Ejecución de estas consultas nos da la lista ​de todas las máquinas que no están ejecutando OS 3, y ​ahora sabemos qué máquinas actualizar.

---

## Más sobre filtros con AND, OR y NOT
- Operadores lógicos
   - AND, OR, y NOT le permiten filtrar sus consultas para devolver la información específica que le ayudará en su trabajo como analista de seguridad.
   - Todos ellos se consideran operadores lógicos.

- AND
   - En primer lugar, AND se utiliza para filtrar a partir de dos condiciones.
   - AND especifica que ambas condiciones deben cumplirse simultáneamente.
   - Por ejemplo, un problema de ciberseguridad podría afectar sólo a aquellas cuentas de clientes que cumplan tanto la condición de ser gestionadas por un representante de soporte con un ID de 5 como la de estar ubicadas en EE.UU..
   - Para encontrar los nombres y correos electrónicos de esos clientes concretos, debe colocar las dos condiciones a ambos lados del operador AND en la cláusula WHERE:
   ```sql
   SELECT firstname, lastname, email, country, supportrepid
   FROM customers
   WHERE supportrepid = 5 AND country = 'USA';
   ```

- OR
   - El operador OR también conecta dos condiciones, pero OR especifica que puede cumplirse cualquiera de ellas.
   - Devuelve resultados en los que se cumple la primera condición, la segunda o ambas.
   - Por ejemplo, si es responsable de encontrar a todos los Clientes que se encuentran en EE.UU. o Canadá para poder comunicarles información sobre una actualización de seguridad, puede utilizar el operador OR para encontrar todos los registros necesarios.
   - Aunque ambas condiciones se basen en la misma columna, deberá escribir las dos condiciones completas.
   - Por ejemplo, la consulta del ejemplo contiene el filtro WHERE country = 'Canada' OR country = 'USA'. 
   - La siguiente consulta muestra cómo colocar las dos condiciones a ambos lados del operador OR en la cláusula WHERE:
   ```sql
   SELECT firstname, lastname, email, country, supportrepid
   FROM customers
   WHERE country = 'USA' OR country = 'Canada';
   ```

- NOT
   - A diferencia de los dos operadores anteriores, el operador NOT sólo funciona con una única condición, y no con varias.
   - El operador NOT niega una condición.
   - Esto significa que SQL devuelve todos los registros que no coinciden con la condición especificada en la consulta.
   - Por ejemplo, si un Problema de ciberseguridad no afecta a los clientes de EE.UU. pero podría afectar a los de otros países, puede devolver todos los clientes que no estén en EE.UU..
   - Esto sería más eficaz que crear condiciones individuales para todos los demás países.
   - Para utilizar el operador NOT para esta tarea, escriba la siguiente consulta y coloque NOT directamente después de WHERE:
   ```sql
   SELECT firstname, lastname, email, country, supportrepid
   FROM customers
   WHERE NOT country = 'USA';
   ```
   - Otra forma de encontrar valores que no sean iguales a un determinado valor es utilizando el operador <> o el operador !=.
   - Por ejemplo, WHERE country <> 'USA' y WHERE country != 'USA' son los mismos filtros que WHERE NOT country = 'USA'. 

- Combinación de operadores lógicos
   - Los operadores lógicos pueden combinarse en filtros.
   - Por ejemplo, si sabe que EE.UU. y Canadá no están afectados por un problema de ciberseguridad, puede combinar los operadores para devolver los clientes de todos los países además de estos dos.
   - En la siguiente consulta, NOT se coloca antes de la primera condición, se une a una segunda condición con AND, y luego NOT también se coloca antes de esa segunda condición.
   - Puede ejecutarla para explorar lo que devuelve:
   ```sql
   SELECT firstname, lastname, email, country
   FROM customers
   WHERE NOT country = 'Canada' AND NOT country = 'USA';
   ```

---

## Actividad: Filtrado con AND, OR y NOT
- Introducción
   - En este laboratorio, utilizará los operadores AND, OR y NOT en SQL para filtrar información.
   - Utilizará SQL para obtener información específica sobre los empleados, sus máquinas y los departamentos a los que pertenecen.
   - Utilizará el shell MariaDB para ejecutar consultas SQL.

- Lo que hará
   - Filtrar los intentos de inicio de sesión que se produjeron fuera de horario
   - Filtrar los intentos de inicio de sesión en fechas específicas
   - Filtrar los intentos de inicio de sesión desde ubicaciones específicas
   - Filtrar información sobre empleados de departamentos específicos
   - Filtrar información sobre empleados que no pertenezcan a un departamento específico

- Resumen de la actividad
   - Como analista de seguridad, es probable que debas analizar datos.
   - A menudo, encontrar los datos específicos que necesitas depende de más de un factor.
   - Para recuperar información específica de la base de datos, puedes filtrar según múltiples condiciones.
   - También puedes filtrar según lo que no coincide con una condición en particular.
   - En este lab, crearás filtros más complejos con los operadores AND, OR y NOT para consultas en SQL.
   - Prepárate para ejecutar algunas consultas complejas en SQL.

- Situación
   - En este caso, debes obtener de la base de datos información específica sobre los empleados, sus máquinas y los departamentos a los que pertenecen.
   - Tu equipo necesita los datos para investigar posibles problemas de seguridad y actualizar las computadoras.
   - Tu objetivo es filtrar la información necesaria a partir de la base de datos.
   - Estos son los pasos que seguirás en esta tarea:
      1. Recuperarás todos los intentos de acceso fallidos después del horario de atención.
      2. Recuperarás todos los intentos de acceso que ocurrieron en fechas específicas.
      3. Recuperarás accesos que no se hayan originado en México.
      4. Recuperarás información sobre ciertos empleados del departamento de Marketing.
      5. Recuperarás información sobre empleados del departamento de Finanzas o Ventas.
      6. Obtendrás información sobre empleados que no pertenecen al departamento de Tecnología de la Información.

- Comienza el lab

1. Recupera intentos de acceso fallidos después del horario de atención
- Usa el operador AND para recuperar todos los intentos de acceso fallidos ocurridos después del horario de atención.
- How many failed login attempts occurred after 18:00?
   - [x] 19
   - [ ] 20
   - [ ] 44
   - [ ] 39

2. Recupera intentos de acceso en fechas específicas
- Usa el operador OR para recuperar los intentos de acceso fallidos durante esos días específicos
- How many login attempts were made on these two days?
   - [x] 75
   - [ ] 89
   - [ ] 67
   - [ ] 44

3. Recupera intentos de acceso realizados fuera de México
- Ejecuta la siguiente consulta en SQL para recuperar información sobre los intentos de acceso que no se originaron en México
- How many login attempts were made outside of Mexico?
   - [ ] 73
   - [ ] 194
   - [ ] 122
   - [x] 144

4. Recupera información de los empleados de Marketing
- Escribe una consulta en SQL para recuperar esta información de la tabla employees. Selecciona todas las columnas y, luego, incluye filtros en las columnas department y office para mostrar solo los registros necesarios.
- What is the username of the first employee in the Marketing department in the East building?
   - [x] elarson
   - [ ] jclark
   - [ ] alevitsk
   - [ ] fbautist

5. Recupera información de los empleados de Finanzas o Ventas
- Escribe una consulta en SQL para recuperar los registros de los empleados del departamento 'Finance' o 'Sales'.
- What is the username of the first employee in the Sales department returned by the query?
   - [ ] bisles
   - [ ] tbarnes
   - [x] lrodriqu
   - [ ] sgilmore

6. Recupera información de los empleados que no pertenecen al departamento de TI
- Escribe una consulta en SQL para recuperar los registros de los empleados que no pertenecen al departamento 'Information Technology'.
- How many employees are not in the Information Technology department?
   - [ ] 122
   - [ ] 188
   - [x] 161
   - [ ] 170


- Listado de queries utilizadas en el lab
```sql
-- PART 1
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00' AND success = 0;

SELECT count(*) quantity
FROM log_in_attempts
WHERE login_time > '18:00:00' AND success = 0;

-- PART 2
SELECT * 
FROM log_in_attempts 
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';

SELECT count(*) quantity
FROM log_in_attempts 
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';

-- PART 3
SELECT * 
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';

SELECT * 
FROM log_in_attempts
WHERE country NOT LIKE 'MEX%';

SELECT count(*) quantity
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';

-- PART 4
SELECT *
FROM employees
WHERE department = 'Marketing'
AND office LIKE 'East%';

-- PART 5
SELECT *
FROM employees
WHERE department = 'Finance'
OR department = 'Sales';

-- PART 6

SELECT *
FROM employees
WHERE department != 'Information Technology';

SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

---

## Ejemplo opcional: Filtrado con AND, OR y NOT
- Mismo laboratorio que el anterior.

---

## Ejemplo: Filtro con AND, OR y NOT
- Resumen de actividades
   - Como analista de seguridad, es probable que necesites analizar datos.
   - Y a menudo encontrar los datos específicos que necesitas depende de más de un factor.
   - Para recuperar información específica de la base de datos, puedes filtrar por múltiples condiciones.
   - También puede filtrar lo que no coincide con una condición determinada.
   - En esta actividad de laboratorio, utilizará los operadores AND, OR y NOT para crear filtros más complejos para consultas SQL.
   - Este ejemplo es un recorrido de la actividad previa de Qwiklab, incluyendo instrucciones detalladas y soluciones.
   - Puede utilizar este ejemplo si no pudo completar el laboratorio o si necesita orientación adicional para realizar las tareas del laboratorio.
   - También puede consultar este ejemplo para prepararse para el cuestionario calificado de este módulo.

- Listado de queries de ejemplo para el lab
```sql
SELECT *
FROM log_in_attempts
WHERE login_time > 'X' AND success = Y;

SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;

SELECT * 
FROM log_in_attempts 
WHERE login_date = 'X' OR login_date = 'Y';

SELECT * 
FROM log_in_attempts 
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';

SELECT * 
FROM log_in_attempts
WHERE X country LIKE 'Y';

SELECT * 
FROM log_in_attempts 
WHERE NOT country LIKE 'MEX%';

SELECT * 
FROM employees;

SELECT * 
FROM employees 
WHERE department = 'Marketing' AND office LIKE 'East%';

SELECT * 
FROM employees 
WHERE department = 'Finance' OR department = 'Sales';

SELECT * 
FROM employees 
WHERE NOT department = 'Information Technology';
```

- Conclusión
   - Ahora tiene experiencia práctica en el uso de SQL para
      - ejecutar consultas SQL para recuperar información de una base de datos y
      - aplicar los operadores AND, OR y NOT para filtrar consultas SQL.

---

## Actividad de Portfolio: Aplicar filtros a las consultas SQL
- Resumen de la actividad
   - En esta actividad, crearás un nuevo documento de portafolio para demostrar tu experiencia usando SQL.
   - Puedes agregar este documento a tu portafolio de ciberseguridad, el cual puedes compartir con posibles empleadores o reclutadores.
   - Para crear tu documento de portafolio, revisarás un escenario y seguirás una serie de pasos.
   - Este escenario está relacionado con el laboratorio que acabas de completar sobre el uso de los operadores AND, OR y NOT en SQL para filtrar información.
   - Explicarás las consultas que realizaste en ese laboratorio, y esto te ayudará a prepararte para futuras entrevistas de trabajo y otros pasos del proceso de contratación.

- Escenario
   - Usted es un profesional de seguridad en una gran organización.
   - Parte de su trabajo es investigar problemas de seguridad para ayudar a mantener el sistema seguro.
   - Recientemente descubrió algunos problemas potenciales de seguridad que involucran intentos de inicio de sesión y máquinas de empleados.
   - Su tarea es examinar los datos de la organización en sus tablas employees y log_in_attempts.
   - Deberá utilizar filtros SQL para recuperar registros de diferentes conjuntos de datos e investigar los posibles problemas de seguridad.
   - Este escenario incluye las mismas consultas que las del laboratorio Filtro con AND, OR y NOT .
   - Puede volver a visitar el laboratorio para obtener capturas de pantalla e incluirlas en su documento de portafolio.
   - Si lo desea, también puede completar esta actividad sin volver a visitar el laboratorio escribiendo sus consultas en la plantilla.

- Instrucciones paso a paso

1. Acceder a la plantilla
- [Plantilla: Aplicar filtros a consultas SQL](./resources/Apply filters to SQL queries.docx)

2. Acceder al material de apoyo
- El documento Instrucciones para incluir consultas SQL proporciona instrucciones y prácticas recomendadas para incluir ejemplos de consultas SQL en su actividad de portafolio
   - [Instrucciones para incluir consultas SQL](./resources/Instructions for including SQL queries.docx)
- El documento Formatos de tablas describe cómo se organizan las tablas utilizadas para esta actividad de portafolio:
   - [Formatos de tablas](./resources/Table formats.docx)

3. Recuperar después de horas de intentos fallidos de inicio de sesión
- Recientemente ha descubierto un posible incidente de seguridad ocurrido fuera del horario laboral.
- Para investigarlo, necesita consultar la tabla log_in_attempts y revisar la actividad de inicio de sesión fuera del horario laboral.
- Utilice filtros en SQL para crear una consulta que identifique todos los intentos de inicio de sesión fallidos que se produjeron después de las 18:00.
- (La hora del intento de inicio de sesión se encuentra en la columna login_time. La columna success contiene un valor de 0 cuando un intento de inicio de sesión falló; puede utilizar un valor de 0 o FALSE en su consulta para identificar los intentos de inicio de sesión fallidos)

4. Recuperar los intentos de inicio de sesión en fechas concretas
- Un evento sospechoso ocurrió el 2022-05-09.
- Para investigar este evento, desea revisar todos los intentos de inicio de sesión que se produjeron ese día y el día anterior.
- Utilice filtros en SQL para crear una consulta que identifique todos los intentos de inicio de sesión que se produjeron el 2022-05-09 o el 2022-05-08.
- (La fecha del intento de inicio de sesión se encuentra en la columna login_date).
- (La fecha del intento de inicio de sesión se encuentra en la columna login_date )

5. Recuperar intentos de inicio de sesión fuera de México
- Ha habido actividad sospechosa con intentos de inicio de sesión, pero el equipo ha determinado que esta actividad no se originó en México.
- Ahora, necesita investigar los intentos de inicio de sesión que ocurrieron fuera de México.
- Utilice filtros en SQL para crear una consulta que identifique todos los intentos de inicio de sesión que se produjeron fuera de México.
- (Cuando se refiere a México, la columna de país contiene valores tanto de MEX como de MEXICO, y necesita usar la palabra clave LIKE con % para asegurarse de que su consulta refleje esto)

6. Recuperar empleados en Marketing
- Su equipo desea realizar actualizaciones de seguridad en máquinas específicas de empleados en el departamento de Marketing.
- Usted es responsable de obtener información sobre estos equipos de empleados y necesitará consultar la tabla de empleados.
- Utilice filtros en SQL para crear una consulta que identifique a todos los empleados del departamento de Marketing de todas las oficinas del edificio Este.
- (El departamento del empleado se encuentra en la columna departamento, que contiene valores que incluyen Marketing. La oficina se encuentra en la columna oficina. Algunos ejemplos de valores en esta columna son Este-170, Este-320 y Norte-434. Tendrá que utilizar la palabra clave LIKE con % para filtrar el edificio Este)

7. Recuperar empleados en Finanzas o Ventas
- Su equipo necesita ahora realizar una actualización de seguridad diferente en las máquinas para los empleados de los departamentos de Ventas y Finanzas.
- Utilice filtros en SQL para crear una consulta que identifique a todos los empleados de los departamentos de Ventas o Finanzas.
- (El departamento del empleado se encuentra en la columna departamento, que contiene valores que incluyen Ventas y Finanzas)

8. Recuperar a todos los empleados que no estén en IT
- Su equipo necesita realizar una actualización más en las máquinas de los empleados.
- Los empleados que pertenecen al departamento de tecnología de la información ya han recibido esta actualización, pero los empleados de todos los demás departamentos la necesitan.
- Utilice filtros en SQL para crear una consulta que identifique a todos los empleados que no pertenezcan al departamento de informática.
- (El departamento del empleado se encuentra en la columna departamento, que contiene valores que incluyen Tecnología de la información)

9. Finalice su documento
- Para finalizar el documento y dejar claro su propósito a los posibles empleadores, asegúrate de completar las secciones Descripción del proyecto y Resumen de la plantilla Aplicar filtros a consultas SQL.
- En la sección Descripción del proyecto, ofrece una visión general del escenario y de lo que consigues mediante SQL. Escribe de dos a cuatro frases.
- En la sección Resumen, proporcione un breve resumen de las tareas anteriores y conéctelas con el escenario. Escribe aproximadamente de dos a cuatro frases.

- Qué incluir en tu respuesta
   - Capturas de pantalla de las consultas o versiones mecanografiadas de las mismas
   - Explicaciones de las consultas
   - Una descripción del proyecto al principio
   - Un resumen al final
   - Detalles sobre el uso de LIKE para buscar un patrón
   - Detalles sobre el filtrado de fechas y horas
   - Detalles sobre el uso de AND y OR para filtrar según varias condiciones
   - Detalles sobre el uso de NOT en los filtros

- Apply filters to SQL queries

1. Project description
Recientemente, se descubrió un posible incidente de seguridad relacionado con intentos de inicio de sesión y máquinas de empleados. Para investigar este incidente, se revisa registros específicos en las tablas log_in_attempts y employees utilizando consultas SQL. El objetivo es filtrar información relevante para identificar patrones sospechosos y garantizar la seguridad de los sistemas.

2. Retrieve after hours failed login attempts
Revisé la tabla log_in_attempts para identificar todos los intentos de inicio de sesión fallidos que ocurrieron después de las 18:00 (hora en que termina el horario laboral). Se utilizó la siguiente consulta SQL `SELECT * FROM log_in_attempts WHERE login_time > '18:00:00' AND success = 0;` para filtrar los registros. Esta consulta devuelve todos los intentos fallidos de inicio de sesión que se produjeron fuera del horario laboral, lo que permite investigar posibles incidentes de seguridad. En total se encontraron 19 intentos de inicio de sesión fallidos después de las 18:00.

3. Retrieve login attempts on specific date
Para investigar un evento sospechoso ocurrido el 2022-05-09, se revisaron todos los intentos de inicio de sesión que se produjeron ese día y el día anterior. Se utilizó la siguiente consulta SQL `SELECT * FROM log_in_attempts WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';` para filtrar los registros. Esta consulta devuelve todos los intentos de inicio de sesión realizados en esas fechas específicas, lo que permite analizar la actividad durante ese período. En total se encontraron 75 intentos de inicio de sesión en esos dos días.

4. Retrieve login attempts outside of Mexico
Para investigar la actividad sospechosa que no se originó en México, se revisaron todos los intentos de inicio de sesión que ocurrieron fuera de México. Se utilizó la siguiente consulta SQL `SELECT * FROM log_in_attempts WHERE NOT country LIKE 'MEX%';` para filtrar los registros. Se utiliza "MEX" ya que existen registros con el valor "MEX" y otros con el valor de "MEXICO". Esta consulta devuelve todos los intentos de inicio de sesión realizados fuera de México, lo que permite identificar posibles amenazas externas. En total se encontraron 144 intentos de inicio de sesión fuera de México.

5. Retrieve employees in Marketing
Para obtener información sobre los empleados del departamento de Marketing en el edificio Este, se revisó la tabla employees. Se utilizó la siguiente consulta SQL `SELECT * FROM employees WHERE department = 'Marketing' AND office LIKE 'East%';` para filtrar los registros. Esta consulta devuelve todos los empleados que pertenecen al departamento de Marketing y trabajan en el edificio Este, lo que permite identificar a los empleados relevantes para las actualizaciones de seguridad.

6. Retrieve employees in Finance or Sales
Para obtener información sobre los empleados de los departamentos de Finanzas o Ventas, se revisó la tabla employees. Se utilizó la siguiente consulta SQL `SELECT * FROM employees WHERE department = 'Finance' OR department = 'Sales';` para filtrar los registros. Esta consulta devuelve todos los empleados que pertenecen a cualquiera de los dos departamentos, lo que permite identificar a los empleados relevantes para las actualizaciones de seguridad.

7. Retrieve all employees not in IT
Para obtener información sobre todos los empleados que no pertenecen al departamento de Tecnología de la Información, se revisó la tabla employees. Se utilizó la siguiente consulta SQL `SELECT * FROM employees WHERE NOT department = 'Information Technology';` para filtrar los registros. Esta consulta devuelve todos los empleados que no pertenecen al departamento de TI, lo que permite identificar a los empleados que necesitan recibir actualizaciones de seguridad. En total se encontraron 161 empleados que no pertenecen al departamento de TI.

8. Summary
En esta actividad, se utilizaron consultas SQL para filtrar información específica de las tablas log_in_attempts y employees. Se aplicaron operadores lógicos como AND, OR y NOT para recuperar registros relevantes relacionados con intentos de inicio de sesión y empleados de diferentes departamentos. Estas consultas permitieron identificar patrones sospechosos, analizar la actividad fuera del horario laboral, y garantizar que los empleados recibieran las actualizaciones de seguridad necesarias.

---

## Ejemplo de actividad de Portfolio: Aplicar filtros a las consultas SQL
- [Ejemplo de actividad de Portfolio: Aplicar filtros a las consultas SQL](./resources/Apply-filters-to-SQL-queries-exemplar.docx)
- El ejemplar utiliza detalles del escenario dado e incluye lo siguiente:
   - Capturas de pantalla de las consultas o versiones mecanografiadas de las consultas
   - Explicaciones de las consultas
   - Una descripción del Proyecto al principio
   - Un resumen al final
   - Detalles sobre el uso de LIKE para buscar un patrón
   - Detalles sobre el filtrado de fechas y horas
   - Detalles sobre el uso de AND y OR para filtrar según múltiples condiciones
   - Detalles sobre el uso de NOT en filtros