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

---

## Mejores prácticas para la recogida y gestión de registros
- Comprender las mejores prácticas relacionadas con la recopilación y gestión de registros le ayudará a mejorar las búsquedas de registros y a respaldar mejor sus esfuerzos para identificar y resolver los incidentes de Seguridad.

- Registros
   - Las fuentes de datos, como los dispositivos, generan datos en forma de eventos.
   - Un log es un registro de los eventos que se producen en los sistemas de una organización.
   - Los registros contienen entradas de registro y cada una de ellas detalla la información correspondiente a un único evento ocurrido en un dispositivo o sistema.
   - Originalmente, los registros tenían como único propósito la solución de problemas tecnológicos comunes.
   - Por ejemplo, los registros de errores proporcionan información sobre por qué se produjo un error inesperado y ayudan a identificar la causa raíz del error para poder solucionarlo.
   - Hoy en día, prácticamente todos los dispositivos informáticos producen algún tipo de registro que proporciona valiosas estadísticas más allá de la solución de problemas.
   - Los Equipos de Seguridad acceden a los registros desde receptores de registros como las herramientas SIEM que consolidan los registros para proporcionar un repositorio central de datos de registro.
   - Los profesionales de la Seguridad utilizan los registros para realizar análisis de registros, que es el proceso de examinar los registros para identificar los eventos de Interés.
   - Los registros ayudan a descubrir los detalles que rodean a las 5 W de la investigación de incidentes: quién provocó el incidente, qué ocurrió, cuándo tuvo lugar el incidente, dónde tuvo lugar el incidente y por qué ocurrió el incidente.

- Tipos de registros
   - Dependiendo de la fuente de Datos, se pueden producir diferentes tipos de registros.
   - He aquí una Lista de algunos tipos de registro comunes que las organizaciones deberían registrar:
      - Red: Los registros de red son generados por dispositivos de red como firewalls, routers o switches.
      - Sistema: Los registros del sistema son generados por sistemas operativos como ChromeOS™, Windows, Linux o macOS®.
      - Aplicación: Los registros de aplicación son generados por aplicaciones de software y contienen información relativa a los eventos que se producen dentro de la aplicación, como una aplicación de smartphone.
      - Seguridad: Los registros de Seguridad son generados por varios dispositivos o sistemas como software antivirus y sistemas de detección de intrusiones. Los registros de Seguridad contienen información relacionada con la seguridad, como el borrado de archivos.
      - Autenticación: Los registros de autenticación se generan cada vez que se produce una autenticación, como un intento de inicio de sesión con éxito en una computadora.

- Detalles de los registros
   - Por lo general, los registros contienen la fecha, la hora, la ubicación, la acción y el autor de la misma.
   - He aquí un ejemplo de registro de autenticación: `Login Event [05:45:15] User1 Authenticated successfully`
   - Los registros contienen información y pueden ajustarse para que contengan aún más información.
   - Verbose registro registra información adicional y detallada más allá del registro por defecto.
   - He aquí un ejemplo del mismo lognterior pero registrado como verboso.
      - `Login Event [2022/11/16 05:45:15.892673] auth_performer.cc:470 User1 Authenticated successfully from device1 (192.168.1.2)`

- Gestión de registros
   - Dado que todos los dispositivos producen registros, puede resultar abrumador para las organizaciones hacer un seguimiento de todos los registros que se generan.
   - Para obtener el máximo valor de sus registros, debe elegir exactamente qué registrar, cómo acceder a ellos fácilmente y mantenerlos seguros mediante la gestión de registros.
   - La Gestión de registros es el proceso de recopilación, almacenamiento, análisis y eliminación de los datos de registro.

- Qué registrar
   - El aspecto más importante de la Gestión de registros es elegir qué registrar.
   - Las organizaciones son diferentes y sus requisitos de registro también pueden variar.
   - Es importante considerar qué fuentes de registro tienen más probabilidades de contener la información más útil en función de su Evento de Interés.
   - Esto podría consistir en configurar las fuentes de registro para reducir la cantidad de datos que registran, por ejemplo excluyendo la verbosidad excesiva.
   - Algunos datos, como los números de teléfono, las direcciones de correo electrónico y los nombres, entre otros, constituyen información de identificación personal (PII), que requiere un tratamiento especial y que en algunas jurisdicciones podría no ser posible registrar.

- El problema del overlogging
   - Desde el punto de vista de la Seguridad, puede resultar tentador registrarlo todo.
   - Este es el error más común que cometen las organizaciones.
   - Sólo porque se pueda registrar, no significa que sea necesario registrarlo.
   - Almacenar cantidades excesivas de registros puede tener muchas desventajas con algunas herramientas SIEM.
   - Por ejemplo, el overlogging puede aumentar los costes de almacenamiento y mantenimiento.
   - Además, el overlogging puede aumentar la carga de los sistemas, lo que puede causar problemas de rendimiento y afectar a la usabilidad, dificultando la búsqueda e identificación de eventos importantes.

- Retención de registros
   - Las organizaciones pueden operar en sectores con requisitos normativos.
   - Por ejemplo, algunas Regulaciones requieren que las organizaciones retengan los registros durante periodos de tiempo determinados y las organizaciones pueden implementar prácticas de retención de registros en su política de gestión de registros.
   - Las organizaciones que operan en las siguientes industrias podrían necesitar modificar su política de gestión de registros para cumplir con los requisitos normativos:
      - Industrias del sector público, como la Ley Federal de Modernización de la Seguridad de la Información (FISMA)
      - Industrias sanitarias, como la Ley de Transferencia y Responsabilidad de los Seguros Médicos de 1996 (HIPAA)
      - Industrias de servicios financieros, como el Estándar de seguridad de los datos para la industria de tarjetas de pago (PCI DSS), la Ley Gramm-Leach-Bliley (GLBA) y la Ley Sarbanes-Oxley de 2002 (SOX)

- Protección de registros
   - Junto con la gestión y la conservación, la protección de los registros es vital para mantener su integridad.
   - No es raro que los actores maliciosos modifiquen los registros en un intento de engañar a los Equipos de Seguridad e incluso de ocultar su actividad.
   - Almacenar los registros en un servidor de registros centralizado es una forma de mantener la integridad de los registros.
   - Cuando se generan registros, se envían a un servidor dedicado en lugar de almacenarse en una máquina local.
   - Esto hace que sea más difícil para los atacantes acceder a los registros porque existe una barrera entre el atacante y la ubicación del registro.

---

## Ponga a prueba sus conocimientos: Visión general de los registros

1. ¿Cuál es el objetivo principal de los registros durante la investigación de incidentes?
- [x] Proporcionar un registro de los detalles del Evento
- [ ] Gestionar los volúmenes de alerta
- [ ] Mejorar la experiencia del usuario
- [ ] Identificar y diagnosticar problemas del sistema
> El objetivo principal de los registros durante la investigación de incidentes es proporcionar un registro de los detalles del Evento. Saber qué ocurrió en los sistemas, redes y dispositivos ayuda a los analistas de seguridad a identificar actividades inusuales o maliciosas.

2. Un analista de Seguridad quiere determinar si un inicio de sesión sospechoso ha tenido éxito. ¿Qué tipo de registro sería más útil para este propósito?
- [ ] Firewall
- [ ] Sistema
- [ ] Red
- [x] Autenticación
> Un registro de autenticación sería muy útil para este propósito. Los registros A de autenticación registran los intentos de inicio de sesión, incluyendo si un inicio de sesión fue exitoso.

3. En el siguiente registro, ¿qué acción registra la entrada del registro? `[ALLOW: wikipedia.org] Source: 192.167.1.1 Friday, 10 June 2022 11:36:12`
- [ ] Friday, 10 June 2022 11:36:12
- [ ] 192.167.1.1
- [x] ALLOW
- [ ] Source
> ALLOW se refiere a la acción que se ha registrado. En este caso, permite acceder a wikipedia.org.

4. Rellene el espacio en blanco: _____ es el proceso de examinar los registros para identificar los Eventos de Interés
- [ ] Expedidor de registros
- [ ] Archivo de registro
- [x] Análisis de registros
- [ ] Registro de datos
> El análisis de registros es el proceso de examinar los registros para identificar los eventos de interés.