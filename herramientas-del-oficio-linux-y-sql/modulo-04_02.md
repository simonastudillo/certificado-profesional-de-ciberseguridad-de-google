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