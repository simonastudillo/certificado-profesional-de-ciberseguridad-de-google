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
- Desplazamiento por la página
- Botón Finalizar Laboratorio

---

## Actividad: Realizar una consulta SQL
- Introducción
   - En este laboratorio, aprenderá a recuperar información de una base de datos utilizando SQL.
   - Utilizará el shell de MariaDB para ejecutar sus consultas SQL.
- Lo que hará
   - Devolver información sobre los dispositivos de los empleados
   - Examinar los intentos de inicio de sesión
   - Ordenar los datos devueltos por una consulta
- Resumen de la actividad
   - Anteriormente, aprendiste a usar consultas en SQL básicas para recuperar información de una base de datos.
   - También aprendiste a usar la palabra clave ORDER BY para ordenar los datos devueltos de manera ascendente o descendente.
   - En este lab, usarás SELECT y FROM en SQL para que se devuelva la información que necesites de una base de datos.
   - También usarás la palabra clave ORDER BY para ordenar la información que devuelve una consulta en función de una columna específica.
   - Es importante que sepas cómo consultar información de una base de datos, ya que es una tarea común que podrías realizar como analista de seguridad.
   - Debes saber cómo obtener la información que necesitas para mejorar la seguridad general y de los datos.
- Situación
   - En este caso, debes determinar cuáles dispositivos de los empleados deben actualizarse.
   - También debes investigar la actividad de acceso de los usuarios para explorar si se produjo alguna actividad inusual.
   - La información que necesitas se encuentra en las tablas machines y login_attempts de la base de datos organization.
   - La tabla machines se enfoca en el hardware y contiene las siguientes columnas:
      - device_id
      - operating_system
      - email_client
      - OS_patch_date
      - employee_id
   - La tabla log_in_attempts se enfoca en la actividad del usuario y contiene estas columnas:
      - event_id
      - username
      - login_date
      - login_time
      - country
      - ip_address
      - correcto
   - Estos son los pasos que seguirás:
      1. Obtendrás información sobre cuáles dispositivos de los empleados deben actualizarse.
      2. Examinarás los intentos de acceso en busca de actividad inusual.
      3. Usarás la palabra clave ORDER BY para ordenar los datos que devuelven tus consultas en SQL.

- Comienza el lab

1. Recupera datos de los dispositivos de los empleados
- Ejecuta la siguiente consulta para seleccionar toda la información de dispositivos de la tabla machines:
```sql
SELECT *
FROM machines;
```
- Ejecuta la siguiente consulta para seleccionar solo las columnas device_id y email_client de la tabla machines.
- What email client is returned in the third row?
   - [ ] Email Client 4
   - [ ] Email Client 3
   - [ ] Email Client 1
   - [x] Email Client 2
- Ejecuta la consulta para que devuelva solo las columnas device_id, operating_system y OS_patch_date de la tabla machines.
- What is the patch date of the first entry?
   - [ ] 2021-03-01
   - [ ] 2021-12-01
   - [ ] 2021-06-01
   - [x] 2021-09-01
> ¿Por qué es útil esta información? Como analista, encontrar entradas antiguas de OS_patch_date es la forma de identificar máquinas “vulnerables” que los hackers podrían explotar. Esas máquinas son las que querrías segmentar para una actualización.

2. Investiga la actividad de acceso
- Escribe una consulta en SQL para seleccionar las columnas event_id y country de la tabla log_in_attempts
- Were any login attempts made from Australia?
   - [ ] Yes
   - [x] No
> ¿Por qué sería útil saber esto? Si tu empresa solo opera en Norteamérica, un acceso desde Australia es una “señal de alerta” que indica un posible robo de credenciales.
- Escribe una consulta en SQL que seleccione las columnas username, login_date y login_time de la tabla log_in_attempts.
- What username is returned in the fifth row?
   - [ ] apatel
   - [x] jrafael
   - [ ] mrah
   - [ ] dkot
> ¿Por qué estoy viendo los horarios de acceso? Los hackers suelen usar credenciales robadas para acceder a las 3:00 a.m. porque suponen que el empleado está dormido y no notará una alerta de “Nuevo acceso”. Como analista, debes buscar anomalías. Si un trabajador de oficina diurno de repente tiene un acceso exitoso a la medianoche, es una "señal de alerta" de que la cuenta podría estar comprometida o de que un usuario interno está accediendo a datos a los que no debería.
- Escribe una consulta en SQL que seleccione todas las columnas de la tabla log_in_attempts. Para ello, usa un solo símbolo después de la palabra clave SELECT.

3. Ordena los datos de intentos de acceso
- Ejecuta la siguiente consulta, que ordena los datos log_in_attempts por login_date
- What are the username and login date of the first record returned?
   - [x] ivelasco on 2022-05-08
   - [ ] daquino on 2022-05-08
   - [ ] sbaelish on 2022-05-10
   - [ ] mabadi on 2022-05-10
- Modifica la consulta del paso anterior: agrega la hora de acceso a la cláusula ORDER BY.
- What are the username and login time of the first record returned by the above query?
   - [x] bsand at 00:19:11
   - [ ] wjaffrey at 00:15:55
   - [ ] pwashing at 00:36:12
   - [ ] gesparza at 00:40:00

- Listado de queries utilizadas en el lab
```sql
-- PART 1
SELECT *
FROM machines;

SELECT device_id, email_client
FROM machines;

SELECT device_id, email_client
FROM machines
LIMIT 1 OFFSET 2;

SELECT device_id, operating_system, OS_patch_date
FROM machines;

SELECT device_id, operating_system, OS_patch_date
FROM machines
LIMIT 1;

-- PART 2
SELECT event_id, country
FROM log_in_attempts;

SELECT event_id, country
FROM log_in_attempts
ORDER BY country;

SELECT username, login_date, login_time
FROM log_in_attempts;

SELECT username, login_date, login_time
FROM log_in_attempts
LIMIT 1 OFFSET 4;

SELECT *
FROM log_in_attempts;

-- PART 3
SELECT *
FROM log_in_attempts
ORDER BY login_date;

SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;
```

---

## Ejemplo: Realizar una consulta SQL

- Resumen de la actividad
   - Anteriormente, aprendiste a utilizar consultas SQL básicas para recuperar información de una base de datos.
   - También aprendió a utilizar la palabra clave ORDER BY para ordenar los datos devueltos en forma ascendente o descendente.
   - En esta actividad de laboratorio, utilizará SELECT y FROM en SQL para devolver la información que necesita de una base de datos.
   - También utilizará la palabra clave ORDER BY para secuenciar la información devuelta por una consulta en función de una columna especificada.
   - Es importante saber cómo consultar información de una base de datos porque ésta es una tarea común que puedes encontrar como analista de seguridad.
   - Debes saber cómo obtener la información que necesitas para mejorar la seguridad y mantener los datos a salvo.
   - Con esto en mente, es hora de explorar el escenario.
   - Los términos fila y registro se utilizan indistintamente en esta actividad de laboratorio.

- Listado de queries de ejemplo para el lab
```sql
SELECT *
FROM machines;

SELECT device_id, email_client
FROM machines;

SELECT device_id, operating_system, OS_patch_date
FROM machines;

SELECT event_id, country
FROM log_in_attempts;

SELECT username, login_date, login_time
FROM log_in_attempts;

SELECT *
FROM log_in_attempts;

SELECT *
FROM log_in_attempts
ORDER BY login_date;

SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;
```

- Conclusión
   - Ha completado esta actividad y ahora tiene experiencia práctica en la ejecución de consultas SQL básicas para
      - seleccionar columnas específicas de una tabla,
      - seleccionar todas las columnas de una tabla utilizando un asterisco (*), y
      - ordenar los resultados de la consulta utilizando la palabra clave ORDER BY.

---

## Ejemplo opcional: Realizar una consulta SQL
- Mismo laboratorio que el anterior.

---

## Filtros básicos en consultas SQL
- Una de las funciones más potentes de SQL es su capacidad para filtrar.
- Filtrar es seleccionar datos que cumplan una determinada condición.
- ​Piense en el filtrado como una forma de elegir sólo los datos que deseamos.
- ​Digamos que queremos seleccionar manzanas de un carro de fruta.
- El filtrado nos permite especificar qué tipo de manzanas queremos elegir.
- ​Cuando vamos a comprar manzanas, podríamos decir explícitamente: "Elija sólo manzanas que sean frescas".
- ​Esto elimina de la selección las manzanas que no son frescas.
- ​Como analista de seguridad, podría filtrar una tabla de intentos de registro para encontrar todos los intentos ​de un país específico.
- ​Podría hacerlo aplicando un filtro en la columna de país.
- Por ejemplo, podría filtrar para que sólo devolviera los registros que contuvieran Canadá.
- ​Antes de empezar, debemos centrarnos en una parte importante de la sintaxis de SQL.
- ​Aprendamos qué son los operadores. 
   - ​Un operador es un símbolo o palabra clave que representa una operación.
   - Un ejemplo de operador sería el operador igual a.
   - ​Por ejemplo, si quisiéramos encontrar todos los registros que ​tienen 'USA' en la columna de país, utilizaríamos country = ''USA'
   - ​Para filtrar una consulta en SQL, simplemente añadimos una línea adicional a la sentencia SELECT y FROM ​que utilizamos antes.
- ​Esta línea adicional utilizará una cláusula WHERE.
- ​En SQL, WHERE indica la condición para un filtro.
- ​Después de la palabra clave WHERE, se enumera la condición específica mediante operadores.
- ​Así que si quisiéramos encontrar todos los intentos de inicio de sesión realizados en Estados Unidos, ​crearíamos este filtro.
- ​En esta condición concreta, estamos indicando que se devuelvan todos los registros que ​tengan un valor en la columna de país que sea igual a 'USA' ​Intentemos juntarlo todo en SQL.
- ​Vamos a empezar seleccionando todas las columnas de la tabla ​log_in_attempts.
- Y, a continuación, añadiremos el filtro WHERE.
- ​¡Ahora, ejecutemos esta consulta! Debido a nuestro filtro, sólo se devuelven las filas ​en las que el país del intento de registro fue 'USA'
- ​En el ejemplo anterior, la condición para nuestro filtro se basaba simplemente en devolver ​registros que fueran iguales a un valor determinado.
- ​También podemos hacer que nuestras condiciones sean más complejas buscando ​un patrón en lugar de una palabra exacta.
- ​Por ejemplo, en la tabla de empleados, tenemos una columna para oficina.
- Podríamos buscar registros en esta columna que coincidan con un patrón determinado.
- ​Quizás querríamos todas las oficinas del edificio Este.
- ​Para buscar un patrón, utilizamos el signo de porcentaje para que actúe como comodín para ​caracteres no especificados. 
- Si ejecutamos un filtro para 'Este%', esto nos devolvería todos los registros que empiecen por Este -- ​por ejemplo, las oficinas Este-120, Este-290 y Este-435. 
- Al buscar patrones con el signo de porcentaje, ​no podemos utilizar el operador igual.
- ​En su lugar, utilizamos otro operador, LIKE. 
- LIKE es un operador que se utiliza con WHERE para buscar un patrón en una columna.
- ​Como LIKE es un operador similar al signo igual, ​lo utilizamos en lugar del signo igual.
- ​Así, cuando nuestro objetivo es devolver todos los valores de la columna office que empiecen por la palabra ​East, LIKE aparecería en una cláusula WHERE.
- ​Volvamos al ejemplo en el que queríamos filtrar por ​intentos de registro realizados en Estados Unidos.
- Imagínese que nos damos cuenta de que nuestra base de datos contiene incoherencias con la forma en que se representa ​Estados Unidos.
- ​Algunas entradas utilizan US mientras que otras utilizan USA.
- ​Vamos a meternos en SQL y aplicar este nuevo tipo de filtro con LIKE.
- ​Vamos a empezar con las mismas dos primeras líneas de ​código porque queremos seleccionar todas las columnas de la tabla de intentos de registro.
- ​Y vamos a añadir un filtro con LIKE para que se devuelvan los registros si ​contienen un valor en la columna de país que empiece por los caracteres US.
- ​Esto incluye tanto US como USA.
- ​Ejecutemos esta consulta para comprobar si cambia la salida.
- Esto devuelve todas ​las entradas en las que la ubicación del usuario estaba en Estados Unidos.

---

## La cláusula WHERE y los operadores básicos
- Cómo ayuda el filtrado
   - Como analista de Seguridad, a menudo será responsable de trabajar con registros de Seguridad muy grandes y complicados.
   - Para encontrar la información que necesita, a menudo tendrá que utilizar SQL para filtrar los registros.
   - En un contexto de Ciberseguridad, podría utilizar filtros para encontrar los intentos de inicio de sesión de un usuario específico o todos los intentos de inicio de sesión realizados en el momento de un Problema de Seguridad.
   - Como otro ejemplo, podría filtrar para encontrar los dispositivos que están ejecutando una versión específica de una aplicación.
- WHERE
   - Para crear un filtro en SQL, debe utilizar la palabra clave WHERE.
   - WHERE indica la condición para un filtro.
   - Si necesitara enviar correos electrónicos a empleados con un título de Personal de TI, podría utilizar una consulta como la del siguiente ejemplo.
   - En lugar de devolver todos los registros de la tabla employees, esta cláusula WHERE indica a SQL que devuelva sólo aquellos que contengan 'IT Staff' en la columna title.
   - Utiliza el operador de signo igual (=) para establecer esta condición.
```sql
SELECT firstname, lastname, title, email
FROM employees
WHERE title = 'IT Staff';
```

- Filtrado por patrones
   - También puede filtrar basándose en un patrón.
   - Por ejemplo, puede identificar las entradas que empiezan o terminan con un carácter o caracteres determinados.
   - Filtrar por un patrón requiere incorporar dos elementos más a su cláusula WHERE:
      - un comodín
      - el operador LIKE
   - Comodines
      - Un comodín es un carácter especial que puede ser sustituido por cualquier otro carácter.
      - Dos de los comodines más útiles son el signo de porcentaje (%) y el guión bajo (_):
         - El signo de porcentaje sustituye a cualquier otro carácter.
         - El símbolo de subrayado sólo sustituye a otro carácter.
      - Estos comodines pueden colocarse después de una Cadena, antes de una Cadena, o en ambas ubicaciones dependiendo del Patrón por el que esté filtrando.
      - La siguiente tabla incluye estos comodines aplicados a la Cadena 'a' y ejemplos de lo que devolvería cada patrón.

| Patrón | Resultados que podría devolver |
| ---- | ---- |
| 'a%' | apple123, art, a |
| 'a_' | as, an, a7 |
| 'a__' | ant, add, a1c |
| '%a' | pizza, Z6ra, a |
| '_a' | ma, 1a, Ha |
| '%a%' | Again, back, a |
| '_a_' | Car, ban, ea7 |

- LIKE
   - Para aplicar comodines al filtro, debe utilizar el operador LIKE en lugar del signo igual (=).
   - LIKE se utiliza con WHERE para buscar un patrón en una columna.
   - Por ejemplo, si desea enviar un correo electrónico a los empleados cuyo título sea 'IT Staff' o 'IT Manager', puede utilizar el operador LIKE combinado con el comodín %:
   ```sql
   SELECT lastname, firstname, title, email
   FROM employees
   WHERE title LIKE 'IT%';
   ```
   - Esta consulta devuelve todos los registros con valores en la columna title que empiecen por el patrón 'IT'.
   - Esto significa que se devuelven tanto 'IT Staff' como 'IT Manager'.
   - Como otro ejemplo, si desea buscar en la tabla de facturas para encontrar todos los clientes ubicados en estados con una abreviatura de 'NY', 'NV', 'NS' o 'NT', puede utilizar el patrón 'N_' en la columna state:
   ```sql
   SELECT firstname,lastname, state, country
   FROM customers
   WHERE state LIKE 'N_';
   ```
   - Esto devuelve todos los registros con abreviaturas de estados que siguen este patrón.

---

## Actividad: Filtrar una consulta SQL
- Introducción
   - En este laboratorio, aplicará filtros básicos a las consultas SQL para recuperar información de una base de datos.
   - Utilizará SQL para obtener información específica sobre los empleados, sus máquinas y los departamentos a los que pertenecen.
   - Utilizará el shell MariaDB para ejecutar consultas SQL.

- Lo que hará
   - Devolver información sobre las máquinas y sus sistemas operativos
   - Filtrar por máquinas con un sistema operativo específico
   - Filtrar por empleados en departamentos específicos
   - Filtrar por empleados que utilizan máquinas específicas

- Resumen de la actividad
   - Como analista de seguridad, saber cómo hacer mejores consultas para recuperar datos específicos puede ayudarte a encontrar con mayor eficiencia la información relacionada con la seguridad que necesitas.
   - En este lab, aplicarás filtros básicos a consultas en SQL para recuperar información de la base de datos MariaDB.
   - MariaDB es una popular base de datos relacional de código abierto compatible con MySQL.
   - Esta actividad representa una gran oportunidad para aplicar lo que aprendiste y agregar filtros en consultas en SQL.
   - Los términos fila y registro se usan indistintamente en este lab.
- Situación
   - En este caso, debes obtener información específica sobre los empleados, sus máquinas y los departamentos a los que pertenecen.
   - Tu equipo necesita estos datos para realizar varias tareas, como ejecutar actualizaciones, publicar un aviso de privacidad en ciertos departamentos y enviarle una alerta a un empleado sobre un problema en una máquina.
   - Tu objetivo es encontrar la información solicitada haciendo consultas en una base de datos.
   - Agregarás filtros en tus consultas para encontrar la información con más rapidez.
   - Estos son los pasos que seguirás:
      1. Obtendrás una lista de todas las máquinas de la organización y sus sistemas operativos.
      2. Obtendrás una lista de todas las máquinas que tengan el sistema operativo OS/2.
      3. Obtendrás una lista de todos los empleados de los departamentos de Finanzas y Ventas.
      4. Obtendrás información sobre las máquinas.

- Comienza el lab

1. Obtén una lista de todas las máquinas de la organización
- Ejecuta una consulta en SQL para obtener solo las columnas device_id y operating_system de la tabla machines.
- ¿Cuántas filas se devolvieron de la tabla de máquinas? (Puedes ver la cantidad de filas en la parte inferior del resultado).
   - [ ] 300
   - [ ] 100
   - [ ] 250
   - [x] 200

2. Obtén una lista de todas las máquinas con 'OS 2'
- Selecciona todos los registros de la tabla machines que tengan un valor de 'OS 2' en la columna operating_system.
- ¿Cuántas máquinas en la base de datos usan el sistema operativo OS 2?
   - [ ] 88
   - [ ] 44
   - [ ] 200
   - [x] 80

3. Obtén una lista de los empleados de departamentos específicos
- Filtra las filas obtenidas a partir de la columna department en la tabla employees para incluir únicamente los empleados del departamento 'Finance' (Finanzas). 
- ¿Cuál es el employee_id de la primera fila que se devuelve?
   - [ ] 1049
   - [ ] 1001
   - [x] 1003
   - [ ] 1119
- Modifica la consulta anterior para obtener la información de los empleados del departamento de 'Sales' (Ventas).
- ¿Cuántos empleados trabajan en el departamento de Sales?
   - [x] 33
   - [ ] 10
   - [ ] 17
   - [ ] 42

4. Identifica las máquinas de los empleados
- Escribe una consulta para identificar qué empleado usa la oficina 'South-109'. (Los datos se deben devolver a partir de la columna office de la tabla employees).
- ¿Cuál de los siguientes empleados usa la computadora que tiene el problema?
   - [ ] jhill
   - [x] jlansky
   - [ ] tsnow
   - [ ] nmitchell
- Modifica la consulta que usaste en el paso anterior para obtener información sobre todos los empleados del edificio 'South'. Usa el operador LIKE con % en esta consulta.
- ¿A qué departamento pertenece el primer empleado que aparece en el edificio South?
   - [ ] Sales
   - [ ] Information Technology
   - [x] Finance
   - [ ] Marketing

- Listado de queries utilizadas en el lab
```sql
-- PART 1
SELECT device_id, operating_system
FROM machines;

-- PART 2
SELECT device_id, operating_system
FROM machines
WHERE operating_system = 'OS 2';

-- PART 3
SELECT *
FROM employees
WHERE department = 'Finance';

SELECT *
FROM employees
WHERE department = 'Finance'
LIMIT 1;

SELECT *
FROM employees
WHERE department = 'Sales';

-- PART 4
SELECT *
FROM employees
WHERE office = 'South-109';

SELECT *
FROM employees
WHERE office LIKE 'South%';

SELECT *
FROM employees
WHERE office LIKE 'South%'
LIMIT 1;
``` 

---

## Ejemplo: Filtrar una consulta SQL
- Resumen de actividades
   - Como analista de seguridad, saber cómo hacer mejores consultas para recuperar piezas específicas de datos puede ayudarle a encontrar la información relacionada con la seguridad que necesita de manera más eficiente.
   - En esta actividad de laboratorio, aplicará filtros básicos a consultas SQL para recuperar información de una base de datos MariaDB.
   - MariaDB es una popular base de datos relacional de código abierto compatible con MySQL.
   - Esta actividad te brinda una gran oportunidad para aplicar lo que has aprendido y agregar filtros a las consultas SQL.

- Listado de queries de ejemplo para el lab
```sql
DESCRIBE machines; 
DESCRIBE employees;

SELECT device_id, operating_system 
FROM machines;

SELECT device_id, operating_system 
FROM machines 
WHERE operating_system = 'OS 2';

SELECT * 
FROM employees 
WHERE department = 'Finance';

SELECT * 
FROM employees
WHERE department = 'Sales';

SELECT *
FROM employees
WHERE office = 'South-109';

SELECT *
FROM employees
WHERE office LIKE 'South%';
```

- Conclusión
   - Ahora tiene experiencia práctica en el uso de SQL para
      - Aplicar la cláusula WHERE para filtrar lo que devuelve una consulta SQL y
      - Utilizar el operador LIKE para filtrar patrones.