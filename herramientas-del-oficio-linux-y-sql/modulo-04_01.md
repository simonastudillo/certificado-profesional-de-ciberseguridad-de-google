# Introducción a SQL y a las bases de datos

## Bienvenido al Módulo 4
- Exploraremos SQL y cómo le permite ​analizar datos de una forma ​necesaria para su función como analista de seguridad. 
- ​Vamos a empezar aprendiendo sobre ​las bases de datos relacionales y cómo están estructuradas.
- ​A partir de ahí, vamos a introducir ​las consultas SQL y cómo utilizarlas ​para acceder a los datos de las bases de datos.
- ​A continuación, pasaremos a los filtros SQL, ​que nos ayudan a refinar nuestras consultas ​para obtener la información exacta que necesitamos.
- ​Por último, exploraremos las uniones SQL, ​que permiten combinar tablas entre sí.

---

## Introducción a las bases de datos
- Cuando trabajamos con grandes cantidades de datos, necesitamos saber cómo almacenarlos, para que ​estén organizados y sean rápidos de acceder y procesar.
- ​La solución a esto pasa por las bases de datos
- Podemos definir una base de datos como una colección organizada de información o datos.
- ​Las bases de datos se comparan a menudo con las hojas de cálculo.
- ​Aunque estos programas son formas cómodas de almacenar datos, las hojas de cálculo ​suelen estar diseñadas para que un solo usuario o un equipo pequeño almacene menos datos.
- ​En cambio, a las bases de datos pueden acceder varias personas simultáneamente y ​pueden almacenar cantidades ingentes de datos.
- ​Las bases de datos también pueden realizar tareas complejas mientras se accede a los datos.
- ​Como analista de seguridad, ​a menudo necesitará acceder a bases de datos que contengan información útil.
- ​Por ejemplo, podría tratarse de bases de datos que contengan información sobre intentos de inicio de sesión, ​software y actualizaciones, o máquinas y sus propietarios.
- ​Ahora que sabemos lo importantes que son las bases de datos para nosotros, ​vamos a hablar de cómo se organizan y cómo podemos interactuar con ellas.
- ​El uso de bases de datos nos permite almacenar grandes cantidades de datos a la vez que los mantenemos rápidos y ​fáciles de acceder.
- ​Hay muchas formas diferentes en las que podemos estructurar una base de datos, pero en este curso, ​trabajaremos con bases de datos relacionales.
- ​Una base de datos relacional es una base de datos estructurada que contiene tablas que ​están relacionadas entre sí.
- ​Empezaremos examinando una tabla individual en ​una base de datos más grande de información organizativa.
- ​Cada tabla contiene campos de información.
- ​Por ejemplo, en esta tabla sobre empleados, ​éstos incluirían campos como employee_id, device_id y username.
- ​Éstas son las columnas de las tablas.
- ​Además, las tablas contienen filas también llamadas registros.
- ​Las filas se rellenan con datos específicos relacionados con las columnas de la tabla.
- ​Por ejemplo, nuestra primera fila es un registro de un empleado cuyo id es 1.000 y ​que trabaja en el departamento de marketing.
- ​Las bases de datos relacionales suelen tener varias tablas.
- ​Considere un ejemplo en el que tenemos dos tablas de una base de datos más grande, una con ​empleados de la empresa y otra con máquinas dadas a esos empleados.
- ​Podemos conectar dos tablas si comparten una columna común.
- ​En este ejemplo, ​establecimos una relación entre ellas con una columna común employee_id.
- Las columnas que relacionan dos tablas entre sí se denominan claves.
- ​Existen dos tipos de claves.
- ​La primera se denomina clave primaria.
- ​La clave primaria se refiere a una columna en la que cada fila tiene una entrada única.
- ​La clave primaria no debe tener valores duplicados, ni valores nulos o ​vacíos.
- ​La clave primaria nos permite identificar de forma única cada fila de nuestra tabla.
- Para la tabla de empleados, employee_id es una clave primaria.
- ​Cada employee_id es único y no hay employee_ids que estén duplicados o ​vacíos.
- ​El segundo tipo de clave es una clave foránea.
- ​La clave foránea es una columna de una tabla que es clave primaria en otra tabla.
- ​Las claves foráneas, a diferencia de las claves primarias, pueden tener valores vacíos y duplicados.
- ​La clave foránea nos permite conectar dos tablas entre sí.
- ​En nuestro ejemplo, podemos fijarnos en la columna employee_id de la tabla machines.
- ​Previamente la identificamos como clave primaria en la tabla de empleados, por lo que ​podemos utilizarla para conectar cada máquina con su empleado correspondiente.
- ​También es importante saber que una tabla sólo puede tener una clave primaria, pero ​múltiples claves foráneas.

---

## Consulta de bases de datos con SQL
- ​SQL, o como también se pronuncia, S-Q-L, son las siglas en inglés de Lenguaje de Consulta Estructurado.
- ​SQL es un lenguaje de programación utilizado para crear, interactuar y ​solicitar información a una base de datos.
- ​Una consulta es una solicitud de datos de una tabla de una base de datos o de una combinación de tablas.
- ​Casi todas las bases de datos relacionales se basan en alguna versión de SQL para consultar datos.
- ​Las distintas versiones de SQL sólo presentan ligeras diferencias en su estructura, ​como dónde colocar las comillas.
- ​Sea cual sea la variedad de SQL que utilice, ​descubrirá que es una herramienta muy importante en su trabajo como analista de seguridad.
- ​​Un registro es un registro de los eventos que se producen en los sistemas de una organización.
- ​Como analista de Seguridad, es posible que se le encargue revisar registros por varias razones.
- ​Por ejemplo, algunos registros podrían contener detalles sobre las máquinas utilizadas en una empresa, ​y como analista, ​necesitaría encontrar aquellas máquinas que no estuvieran configuradas correctamente.
- ​Otros registros podrían describir a los visitantes de su sitio web o aplicación web y ​las tareas que realizan.
- ​En ese caso, ​podría estar buscando patrones inusuales que puedan apuntar a una actividad maliciosa.
- ​Los registros de seguridad suelen ser muy grandes y difíciles de procesar.
- ​Hay millones de puntos de datos y ​lleva mucho tiempo encontrar lo que necesita.
- ​¡Pero aquí es donde entra SQL! Puede buscar entre millones de puntos de datos para ​extraer las filas de datos relevantes mediante una consulta que se ejecuta en cuestión de segundos.
- ​SQL también es un lenguaje muy común utilizado para el análisis básico de datos, ​otro conjunto de habilidades que le diferenciarán como analista de seguridad.
- ​Como analista de seguridad, puede utilizar el filtrado de SQL para encontrar datos que respalden ​decisiones relacionadas con la seguridad y analizar cuándo las cosas pueden ir mal.
- Por ejemplo, ​puede identificar qué máquinas no han recibido el último parche.
- ​Esto es importante porque los parches son actualizaciones que ayudan a protegerse contra los ataques.
- ​Como otro ejemplo, puede utilizar SQL para determinar el mejor momento ​para actualizar una máquina en función de cuándo se utiliza menos.

---

## Filtrado SQL frente a filtrado Linux
- Acceso a SQL
   - Existen muchas interfaces para acceder a SQL y muchas versiones diferentes de SQL.
   - Una forma de acceder a SQL es a través de la línea de comandos de Linux.
   - Para acceder a SQL desde Linux, tienes que escribir un comando para la versión de SQL que quieras utilizar.
   - Por ejemplo, si quieres acceder a SQLite, puedes introducir el comando sqlite3 en la línea de comandos.
   - Después de esto, cualquier comando escrito en la línea de comandos será dirigido a SQL en lugar de a los comandos de Linux.

- Diferencias entre el filtrado de Linux y SQL
   - Aunque tanto Linux como SQL permiten filtrar los datos, existen algunas diferencias que afectan a la elección de uno u otro.
   - Propósito
      - Linux filtra datos en el contexto de archivos y directorios en un sistema de archivos.
      - Se utiliza para tareas como la búsqueda de archivos específicos, la manipulación de permisos de archivo o la gestión de procesos.
      - SQL se utiliza para filtrar datos dentro de un sistema de gestión de bases de datos.
      - Sirve para consultar y manipular datos almacenados en tablas y recuperar información específica en función de criterios definidos.
   - Sintaxis
      - Linux utiliza varios comandos y opciones de línea de comandos específicos para cada herramienta de filtrado.
      - La sintaxis varía en función de la herramienta y su finalidad.
      - Algunos ejemplos de comandos Linux son find, sed, cut, e grep.
      - SQL utiliza el Lenguaje de Consulta Estructurada (SQL), un lenguaje estandarizado con palabras clave y cláusulas específicas para filtrar datos en distintas bases de datos SQL.
      - Algunos ejemplos de palabras clave y cláusulas SQL son WHERE, SELECT, JOIN.
   - Estructura
      - SQL ofrece mucha más estructura que Linux, que es más libre y no tan ordenado.
      - Por ejemplo, si quisieras acceder a un registro de los intentos de inicio de sesión de los empleados, SQL tendría cada registro separado en columnas.
      - Linux imprimiría los datos como una línea de texto sin esta organización.
      - Como resultado, la selección de una columna específica para analizar sería más fácil y más eficiente en SQL.
      - En términos de estructura, SQL proporciona resultados más legibles y que pueden ajustarse más rápidamente que cuando se utiliza Linux.
   - Unir tablas
      - Algunas decisiones relacionadas con la seguridad requieren información procedente de distintas tablas.
      - SQL permite al analista unir varias tablas cuando devuelve datos.
      - Linux no tiene esa misma funcionalidad; no permite que los datos se conecten a otra información del ordenador.
      - Esto es más restrictivo para un analista que revisa los registros de seguridad.
   - Mejores usos
      - Como analista de seguridad, es importante entender cuando puedes usar cada herramienta.
      - Aunque SQL tiene una estructura más organizada y permite unir tablas, esto no significa que no haya situaciones que requieran filtrar datos en Linux.
      - Muchos de los datos utilizados en ciberseguridad se almacenarán en un formato de base de datos que funcione con SQL.
      - Sin embargo, otros registros pueden estar en un formato que no es compatible con SQL.
      - Por ejemplo, si los datos se almacenan en un archivo de texto, no se puede buscar en ellos con SQL. En esos casos, es útil saber cómo filtrar en Linux.