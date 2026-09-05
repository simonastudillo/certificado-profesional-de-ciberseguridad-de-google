# Visión general de los registros

## Bienvenido al Módulo 4
- ​Libros de Historia. Recibos. Diarios. ​¿Qué tienen en común todas estas cosas?
- ​Registran acontecimientos.
- Ya sean acontecimientos históricos, transacciones financieras, ​o entradas de diarios privados, ​los registros conservan los detalles de los acontecimientos.
- ​Y tener acceso a estos detalles puede ayudarnos de muchas maneras.
- ​Previamente, exploramos los diferentes tipos de procesos y ​procedimientos implicados durante cada fase del ciclo de vida de la Respuesta ante incidentes.
- ​En esta sección, nos centraremos en uno de los componentes clave de la investigación de incidentes, ​los logs y las alertas.
- ​En Seguridad, los logs registran los detalles de los eventos y ​estos detalles se utilizan para apoyar las investigaciones.
- ​Primero, aprenderá todo sobre los logs, qué son y cómo se crean.
- ​También aprenderá a leer y analizar los logs.
- ​Después, revisaremos los sistemas de detección de intrusiones.
- ​Exploraremos cómo interpretar las firmas.
- ​Tendrá la oportunidad de aplicar lo que ha aprendido mediante actividades prácticas ​utilizando una herramienta llamada Suricata.
- ​Por último, buscará en herramientas SIEM como Splunk y ​Chronicle para localizar eventos de interés y acceder a los datos de registro.
- ​Los eventos son una valiosa fuente de datos.
- ​Ayudan a crear un contexto en torno a una alerta, por lo que ​podrá interpretar las acciones que tuvieron lugar en un sistema.
- ​Saber leer, analizar y conectar diferentes eventos le ayudará ​a identificar comportamientos maliciosos y a proteger los sistemas de los ataques.

---

## La importancia de los registros
- ​Los dispositivos producían datos en forma de eventos.
- ​Como recordatorio, los eventos son sucesos observables que ocurren en un ​sistema o dispositivo de red. ​Estos datos proporcionan visibilidad de un entorno.
- ​Los registros son una de las formas clave en las que los profesionales de Seguridad detectan ​actividades inusuales o maliciosas.
- ​Un registro es un registro de los eventos que se producen en los sistemas de una organización.
- ​La actividad del sistema se registra en lo que se conoce como un archivo de registro o, por lo ​general, denominado registros.
- ​Casi todos los dispositivos o sistemas pueden generar registros.
- ​Los registros contienen varias entradas que detallan información sobre un evento o ​suceso específico.
- ​Los registros son útiles para los analistas de Seguridad durante la investigación de incidentes, ​ya que registran los detalles de qué, dónde y cuándo ocurrió un evento en la red.
- ​Esto incluye detalles como la fecha, la hora, la ubicación, la acción realizada y ​los nombres de los usuarios o sistemas que realizaron la acción.
- ​Estos detalles ofrecen una valiosa información estadística, no solo para la ​solución de problemas relacionados con el rendimiento del sistema, ​sino, lo que es más importante, para la supervisión de Seguridad.
- Los ​registros permiten a los analistas crear una historia y un ​cronograma en torno a varios eventos para comprender qué sucedió exactamente.
- ​Esto se hace mediante el análisis de registros.
- El ​análisis de registros es el proceso de examinar los registros para identificar eventos de interés.
- ​Dado que hay diferentes fuentes disponibles para obtener registros, se ​puede generar un enorme volumen de datos de registro.
- ​Es útil ser selectivo en lo que registramos, de modo que podamos registrarlo de manera eficiente.
- ​Por ejemplo, las aplicaciones web generan un gran volumen de mensajes de registro, pero ​no todos estos datos pueden ser relevantes para una investigación.
- ​De hecho, puede que incluso ralentice las cosas.
- ​Excluir datos específicos del registro ​ayuda a reducir el tiempo dedicado a buscar en los datos de registro.
- ​Tal vez recuerdes nuestra conversación sobre la tecnología SIEM.
- ​Las herramientas SIEM proporcionan a los profesionales de Seguridad una visión general ​de alto nivel de lo que ocurre en una red.
- ​Para ello, las herramientas SIEM recopilan primero datos de varias fuentes de datos.
- ​Luego, los datos se agregan o se centralizan en un solo lugar.
- ​Por último, los diversos formatos de registro se normalizan o ​se convierten en un único formato preferido.
- ​Las herramientas SIEM ayudan a procesar grandes volúmenes de registros de múltiples fuentes de datos en tiempo real.
- ​Esto permite a los analistas de Seguridad buscar rápidamente los datos de registro y ​realizar análisis de registros para respaldar sus investigaciones.
- ​Entonces, ¿cómo se recopilan los registros?
- ​El software conocido como reenviadores de registros recopila registros de varias fuentes y los ​reenvía automáticamente a un repositorio de registros centralizado para su almacenamiento.
- ​Dado que diferentes tipos de dispositivos y sistemas pueden crear registros, ​hay diferentes fuentes de datos de registro en un entorno.
- ​Estos incluyen los registros de red, que generan dispositivos como proxies, ​enrutadores, conmutadores y firewalls, y ​los registros del sistema, que generan los sistemas operativos.
- ​También hay registros de aplicaciones, que son registros relacionados con aplicaciones de software, ​registros de seguridad, que son generados por herramientas de seguridad como IDS o IPS, ​y, por último, registros de autenticación, que registran los intentos de inicio de sesión.
- ​Este es un ejemplo de un registro de red de un router.
```log
[ALLOW: google.com] Source: 192.167.1.1 Friday, 10 June 2022 12:10:45
```
- ​Aquí hay un par de entradas de registro, pero nos centraremos en la primera línea.
- ​Aquí podemos observar una serie de campos.
- ​En primer lugar, hay una acción que especifica ALLOW.
- Esto significa que la ​configuración del firewall del router permitía el acceso desde una dirección IP específica a google.com.
- ​A continuación, hay un campo que especifica la fuente, que muestra una dirección IP.
- ​Hasta ahora, la información de esta entrada de registro nos indica que se ​permite el tráfico de red a google.com desde esta dirección IP de origen.
- ​El último campo especifica la marca de tiempo, ​que es uno de los campos más esenciales de un registro.
- ​Podemos identificar la fecha y la hora exactas de una acción que se ha producido.
- ​Esto es útil para ​correlacionar varios eventos y desarrollar una cronología del incidente.