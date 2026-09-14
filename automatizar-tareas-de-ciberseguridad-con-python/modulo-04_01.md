# Python para la automatización

## Bienvenido al módulo 4
- ​En esta sección, ​vamos a explorar cómo un analista de seguridad como ​usted pone Python en práctica.
- ​Como analista de seguridad, ​es probable que trabaje con registros de seguridad que capturan ​información sobre diversas actividades del sistema.
- ​Estos registros son a menudo muy ​grandes y difíciles de interpretar rápidamente.
- ​Pero Python puede automatizar ​fácilmente estas tareas y hacer las cosas mucho más eficientes.
- ​Así que primero, nos centraremos ​en la apertura y lectura de archivos en Python.
- ​Esto incluye los archivos de registro.
- ​Luego exploraremos el análisis sintáctico de archivos.
- ​Esto significa que será capaz de trabajar con archivos de forma que ​le proporcionen la información ​relacionada con la seguridad que está buscando.
- ​Por último, parte de escribir código es depurar código.
- ​Es importante ser capaz de interpretar ​los mensajes de error para que su código funcione.
- ​Cubriremos tipos comunes de ​errores de Python y formas de resolverlos.
- ​En general, después de completar esta sección, ​tendrá una mejor comprensión de Python y ​cómo como analista de seguridad puede utilizarlo.

---

## Automatice las tareas de ciberseguridad con Python
- ​La Automatización es una preocupación clave en la profesión de Seguridad.
- ​Por ejemplo, sería difícil ​supervisar cada intento individual de acceder al sistema.
- ​Por este motivo, es útil automatizar ​los controles de Seguridad establecidos para mantener a ​los actores malintencionados fuera del sistema.
- ​También es útil para automatizar ​la detección de actividades inusuales.
- ​Python es excelente para la automatización.
- ​Exploremos tres ejemplos específicos de esto.
- ​En primer lugar, imagine que es un analista de Seguridad de ​una empresa de atención médica que almacena los ​registros confidenciales de los pacientes en un servidor de bases de datos.
- ​Su empresa desea implementar ​controles adicionales para proteger esta información.
- ​Para mejorar la seguridad de los registros, ​decide implementar una política de tiempo de espera que bloquea a ​un usuario si ha pasado ​más de tres minutos iniciando sesión en la base de datos.
- ​Esto se debe a que ​es posible que si un usuario dedica demasiado tiempo, ​sea que esté adivinando la contraseña.
- ​Para ello, puede utilizar ​Python para identificar cuándo un usuario ha introducido ​un nombre de usuario y empezar a registrar ​el tiempo que transcurre hasta que este usuario introduzca la contraseña correcta.
- ​Ahora, veamos un ejemplo diferente.
- ​Esta vez, imagina que eres ​un analista de Seguridad que trabaja en un bufete de abogados.
- ​Recientemente se han producido ​algunos ataques de Seguridad en curso en los que los ​actores de amenazas piratean ​las cuentas de los empleados e ​intentan robar la información de los clientes.
- ​Luego amenazan con usar esto con fines malintencionados.
- ​Por eso, el equipo de seguridad está trabajando para atacar ​todas las vulnerabilidades de seguridad que permiten ​a estos atacantes entrar en las bases de datos de la empresa.
- ​Usted es responsable personalmente de ​rastrear todos los inicios de sesión de los usuarios ​comprobando su marca de tiempo de inicio de sesión, dirección IP y ubicación de inicio de sesión.
- ​Por ejemplo, si un usuario ​inicia sesión durante las primeras horas de la mañana, ​debe estar marcado.
- ​Además, si inician sesión desde ​una ubicación que no es una ​de las dos zonas de trabajo establecidas, ​debes marcar su cuenta.
- ​Por último, si un usuario ​inicia sesión simultáneamente desde dos direcciones IP diferentes, ​debes marcar su cuenta.
- ​Python puede ayudarlo a realizar un seguimiento y ​analizar toda esta información de inicio de sesión diferente.
- ​Consideremos un último ejemplo.
- ​Imagine que es un analista de Seguridad ​que trabaja en una organización grande.
- ​Recientemente, esta organización ​ha aumentado las medidas de Seguridad ​para garantizar que todas las aplicaciones orientadas al cliente ​estén mejor protegidas.
- ​Como hay una contraseña para acceder a estas aplicaciones, ​quieren monitorear ​todos los intentos de inicio de sesión con contraseña para detectar actividades sospechosas.
- ​Una señal de actividad sospechosa es tener ​varios intentos fallidos de inicio ​de sesión en poco tiempo.
- ​Debe marcar a los usuarios si han tenido ​más de tres errores de inicio de sesión en los últimos 30 minutos.
- ​Una forma de hacerlo en Python es analizar ​un archivo de registro txt estático con ​todos los intentos de inicio de sesión de los usuarios en cada máquina.
- ​Python podría estructurar la información de este archivo, ​incluidos el nombre de usuario, la dirección IP, la ​marca de tiempo y el estado de inicio de sesión.
- ​Luego, podría usar condicionales para ​determinar si es necesario marcar a un usuario.
- ​Estos son solo algunos ejemplos de cómo ​un analista de Seguridad podría ​aplicar Python en su trabajo diario.