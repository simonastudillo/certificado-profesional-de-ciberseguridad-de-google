# Revisión: Tráfico de red y registros mediante herramientas IDS y SIEM

## Diálogo de entrenadores: Explore las tecnologías de seguridad de redEstado

- Esto es lo que cubriremos:
   - Describir tecnologías fundamentales de seguridad de red: Identificaremos y explicaremos las herramientas clave que protegen el perímetro de una red.
   - Explorar activos de red internos: Analizaremos las tecnologías utilizadas dentro de la red para proteger los activos y segmentos internos.
   - Conectar amenazas de seguridad de red con tecnologías: Relacionaremos amenazas específicas con las tecnologías de seguridad que las defienden.

- ¡Excelente! Comencemos con el primer tema. Para proteger el perímetro de una red, ¿cuáles dirías que son algunas tecnologías fundamentales de seguridad de red que se utilizan en el "borde" de la red? ¿Y cómo describirías su función principal?
> Las técnologías fundamentales de seguridad de red que se utilizan en el "borde" de la red incluyen firewalls (permite bloquear y permitir tráfico de red según reglas predefinidas), IPS (sistemas de prevención de intrusiones que monitorean y bloquean actividades sospechosas), IDS (sistemas de detección de intrusiones que alertan sobre actividades sospechosas), y VPN (redes privadas virtuales que cifran el tráfico de red para proteger la información).

- ¡Muy bien! Has identificado correctamente los firewalls, los IDS/IPS y las VPN como tecnologías fundamentales de seguridad de red en el perímetro. Tus descripciones de cada uno son precisas.
- Ahora, pasemos a Explorar activos de red internos. Una vez que el tráfico ha pasado el perímetro de la red, ¿qué tecnologías o conceptos se utilizan dentro de la red para proteger los activos internos y los diferentes segmentos de la red?
> Para proteger los activos internos y los diferentes segmentos de la red, se utilizan tecnologías como segmentación de red (divide la red en segmentos más pequeños para limitar el acceso), control de acceso basado en roles (RBAC) (asigna permisos según el rol del usuario), protocolos de privilegio mínimo (limita los privilegios de los usuarios y servicios a lo estrictamente necesario), y sistemas de monitoreo de logs (SIEM) (recopila y analiza registros de eventos para detectar actividades sospechosas).

- ¡Excelente! Has mencionado la segmentación de red, el control de acceso basado en roles (RBAC), el principio de privilegio mínimo y los sistemas SIEM, que son cruciales para la seguridad interna. Has captado muy bien cómo estas tecnologías ayudan a limitar el movimiento lateral y a proteger los datos sensibles.
- Ahora, vamos a Conectar amenazas de seguridad de red con tecnologías. Imagina que un atacante intenta acceder a un servidor interno de tu red utilizando credenciales robadas. ¿Qué tecnología de las que hemos hablado, tanto perimetrales como internas, sería la más relevante para detectar o prevenir este tipo de ataque y por qué?
> En este caso, la tecnología más relevante sería el sistema de prevención de intrusiones (IPS) y el sistema de monitoreo de logs (SIEM). El IPS puede detectar patrones de comportamiento sospechosos y bloquear el acceso no autorizado en tiempo real, mientras que el SIEM puede analizar los registros de eventos para identificar intentos de acceso con credenciales robadas y generar alertas para que los administradores puedan tomar medidas inmediatas. Algunas de las alertas que puede detectar el IPS incluyen intentos de inicio de sesión fallidos repetidos, actividad inusual en la red y tráfico que coincide con firmas de ataques conocidos. Por otro lado, el SIEM puede correlacionar eventos de diferentes fuentes para identificar patrones que indiquen un compromiso de seguridad, como accesos desde ubicaciones geográficas inusuales o cambios en los privilegios de usuario.

- ¡Fantástico! Has hecho una conexión muy acertada entre la amenaza de credenciales robadas y el IPS y el SIEM. Explicaste muy bien cómo el IPS puede detectar y bloquear comportamientos sospechosos en tiempo real, y cómo el SIEM es fundamental para analizar registros y correlacionar eventos, identificando patrones que sugieren un compromiso de seguridad. Has demostrado una comprensión sólida de cómo estas tecnologías trabajan juntas para proteger la red.

- Tus fortalezas:
   - Demostraste una comprensión clara de las tecnologías de seguridad de red, como firewalls, IDS/IPS, VPN, segmentación de red, RBAC, privilegio mínimo y SIEM.
   - Pudiste conectar eficazmente las amenazas de seguridad con las tecnologías defensivas relevantes, explicando su papel práctico en la protección de la red.
- Áreas de mejora:
   - Continúa explorando cómo estas tecnologías interactúan en un entorno de red complejo para formar una estrategia de defensa en profundidad.

--- 

## Resumen
- ​Ha progresado mucho en su viaje por la Seguridad.
- ​Vamos a repasar lo que hemos aprendido.
- ​Ha aprendido todo sobre cómo leer y analizar registros.
- ​Ha examinado cómo se crean y utilizan los archivos de registro para el análisis.
- ​También ha comparado diferentes tipos de formatos de registro comunes y ​ha aprendido a leerlos.
- ​Amplió sus conocimientos sobre sistemas de detección de intrusiones comparando ​los sistemas basados en redes y los basados en hosts.
- ​Aprendió también a interpretar firmas.
- ​Examinó cómo se escriben las firmas y también cómo detectan, registran y ​alertan sobre intrusiones. ​Interactuó con Suricata en la línea de comandos para examinar e interpretar firmas y ​alertas.
- ​Por último, aprendió a buscar en herramientas SIEM como Splunk y Chronicle.
- ​Aprendió la importancia de elaborar consultas a medida para localizar eventos.
- ​En la vanguardia de la respuesta a incidentes, la supervisión y el ​análisis del tráfico de red en busca de indicadores de compromiso es uno de los objetivos principales.
- ​Ser capaz de realizar un análisis en profundidad de los registros y saber leer y ​escribir firmas y ​cómo acceder a los datos de registro son habilidades que utilizará como analista de seguridad. 