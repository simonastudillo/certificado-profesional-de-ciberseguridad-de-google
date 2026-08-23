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