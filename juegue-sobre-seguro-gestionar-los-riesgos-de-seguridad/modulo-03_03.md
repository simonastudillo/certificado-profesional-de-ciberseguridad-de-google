# Repaso: Introducción a las herramientas de ciberseguridad

## Diálogo de entrenadores: Exploración de SIEM y registros mediante el análisis de escenarios
- ¡Bienvenido! En este Diálogo, exploraremos cómo las herramientas SIEM (Security Information and Event Management) se utilizan para proteger las operaciones comerciales.
- Esto es lo que cubriremos:
1. Explorar un escenario de operaciones comerciales.
2. Discutir los registros (logs) y SIEM.
3. Explorar cómo las herramientas SIEM protegen las operaciones comerciales.
4. Resumir la importancia de los registros y las herramientas SIEM en la ciberseguridad.

- Durante la sesión de hoy, que cubrió cómo las herramientas SIEM se utilizan para proteger las operaciones comerciales, nos enfocamos en explorar un escenario de interrupción de un sitio web, discutir la importancia de los logs y las herramientas SIEM, y cómo estas últimas protegen las operaciones comerciales.

- Tus fortalezas:
   - Analizaste proactivamente el escenario, identificando logs relevantes como los de red, servidor y firewall, y explicando su importancia.
   - Proporcionaste explicaciones perspicaces sobre cómo las funcionalidades de SIEM, como la gestión centralizada de logs, las alertas automatizadas y la visualización, contribuyen a la defensa proactiva y la respuesta efectiva a incidentes.
- Áreas de mejora:
   - Podrías profundizar en cómo los SIEM no solo detectan, sino que también ayudan en la contención y erradicación de las amenazas, y en la recuperación de las operaciones, más allá de la detección inicial.

---

## Resumen
- Empezamos por analizar la importancia de los registros y la ciberseguridad, ​y exploramos diferentes tipos de registros, como los registros del firewall, de la red y del servidor
- A continuación, analizamos los paneles de SIEM y ​cómo utilizan las representaciones visuales para proporcionar a los equipos de seguridad ​información rápida y clara sobre la postura de seguridad de una organización
- Por último, presentamos las herramientas SIEM más comunes que se utilizan en la ​industria de la ciberseguridad, como Splunk y Chronicle
- Exploraremos aún más herramientas de Seguridad más adelante en el programa y ​tendrás la oportunidad de practicar su uso
- Próximamente, analizaremos las estrategias y cómo ayudan a los profesionales de Seguridad a ​responder adecuadamente para identificar las amenazas, los riesgos y las vulnerabilidades.

---

## Glosario de términos del módulo 3
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 3

1. ¿Cuál de las siguientes afirmaciones describe correctamente los registros? Seleccione tres respuestas
- [x] Los eventos relacionados con sitios web, correos electrónicos o archivos compartidos se registran en un registro del servidor. 
- [x] Un registro A es un registro de los eventos que se producen en los sistemas y redes de una organización.
- [ ] Acciones como el uso de un nombre de usuario o una contraseña se registran en un registro del firewall.
- [x] Un registro de red es un registro de todas las computadoras y dispositivos que entran y salen de una red.
> Correcto
- [x] Las herramientas SIEM se basan en los registros para monitorizar los sistemas y detectar las amenazas a la Seguridad.
- [x] Un registro A de las conexiones entre dispositivos y servicios de una red forma parte de un registro de red.
- [x] Un registro A de los eventos relacionados con los inicios de sesión de los empleados y las solicitudes de nombres de usuario forma parte de un registro del servidor.
- [ ] Acciones como las solicitudes de nombres de usuario se registran en un registro de red.
> Correcto

2. ¿Cuáles son algunos de los beneficios clave de las herramientas SIEM? Seleccione tres respuestas
- [ ] Elimine la necesidad de revisar manualmente los registros
- [x] Ahorre tiempo
- [x] Proporcionar seguimiento y análisis de los Eventos
- [x] Recopilar datos de registro de distintas fuentes
> Correcto

3. Rellene el espacio en blanco: Un profesional de la seguridad crea un panel de control que muestra atributos técnicos sobre las operaciones comerciales denominado ______, como el tráfico de red entrante y saliente
- [x] métricas
- [ ] promedios
- [ ] registros
- [ ] Herramientas SIEM
> Correcto

3. Rellene el espacio en blanco: Para evaluar el rendimiento de una aplicación de software, los profesionales de la Seguridad utilizan _____, que incluye el tiempo de respuesta, la disponibilidad y la tasa de fallos
- [ ] paneles de control
- [x] métricas
- [ ] Herramientas SIEM
- [ ] registros
> Correcto

4. Un Equipo de Seguridad decide implementar una herramienta SIEM que instalará, operará y mantendrá utilizando su propia infraestructura física. ¿Qué tipo de herramienta están utilizando?
- [x] Autoalojado
- [ ] Alojado en el registro
- [ ] Híbrido
- [ ] Alojado en la Nube
> Correcto

5. Usted es un analista de seguridad y desea una solución de seguridad cuyo mantenimiento y gestión corran a cargo de su proveedor de herramientas SIEM. ¿Qué tipo de herramienta elige?
- [x] Solución alojada
- [ ] Alojado en la Nube
- [ ] Autoalojado
- [ ] Híbrido
> Incorrecto

5. Usted es un profesional de la Seguridad y desea una herramienta SIEM que requiera tanto una infraestructura in situ como soluciones basadas en Internet. ¿Qué tipo de herramienta elige?
- [ ] Componente alojado
- [ ] Autoalojado
- [ ] Alojado en la Nube
- [x] Híbrido
> Correcto

6. Rellene el espacio en blanco: Las herramientas SIEM se utilizan para buscar, analizar y _____ los datos de registro de una organización para proporcionar información de seguridad y alertas en tiempo real
- [ ] modifique
- [x] retenga
- [ ] publicable
- [ ] separar
> Correcto

6. Rellene el espacio en blanco: _____ se utilizan para conservar, analizar y buscar los datos de registro de una organización con el fin de proporcionar información y alertas de seguridad en tiempo real
- [ ] Sistemas operativos
- [x] Herramientas SIEM
- [ ] Manuales de estrategias
- [ ] analizadores de protocolos de red (rastreadores de paquetes)
> Correcto

7. Tras recibir una alerta sobre un intento de inicio de sesión sospechoso, un analista de seguridad puede acceder a su _____ para recopilar información sobre la alerta
- [ ] infraestructura interna
- [x] Panel de herramientas SIEM
- [ ] manual de estrategias 
- [ ] analizador de protocolos de red (packet sniffer)
> Correcto

8. Rellene el espacio en blanco: las herramientas de _____ suelen ser de uso gratuito
- [x] Código abierto 
- [ ] Línea de comandos
- [ ] Propietario
- [ ] Alojado en la Nube
> Correcto