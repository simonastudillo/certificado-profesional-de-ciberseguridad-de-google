# Revisión: Tráfico de red y registros mediante herramientas IDS y SIEM

## Diálogo de entrenadores: Explore las tecnologías de seguridad de red

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

---

## Glosario: Tráfico de red y registros mediante ID y herramientas SIEM
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 4

1. ¿Cuál de los siguientes se refiere a un registro log de los eventos que se producen en los sistemas de una organización?
- [x] Fuentes de registro
- [ ] Ocurrencias
- [ ] Registros
- [ ] Expedidor de registros (Incorrecto)
> Incorrecto

1. ¿Qué detalles contienen los registros? Seleccione todo lo que corresponda
- [x] Ubicación
- [ ] Remitente (Incorrecto)
- [x] Tiempo
- [x] Fecha
> Correcto

2. ¿Cuál es la diferencia entre un registro y un análisis de registros?
- [ ] Tanto un registro log como un análisis de registros contienen detalles de los eventos, pero registran detalles de fuentes distintas.
- [ ] Un registro contiene detalles del archivo de registro. El análisis de registros implica la recopilación y el almacenamiento de registros.
- [x] Un registro log es un registro de los eventos que se producen en los sistemas de una organización. El análisis de registros es el proceso de examinar los registros para identificar los eventos de interés.
- [ ] Un registro log registra los detalles en archivos de registro. El análisis de registros implica una visión general de alto nivel de todos los eventos que se producen en la red.
> Correcto

2. Examine el siguiente registro:
```syslog
LoginEvent[2021/10/13 10:32:08.958711] auth_session_authenticator.cc:304 Regular user login 1
```
- ¿Qué tipo de registro es este?
- [ ] Ubicación
- [ ] Aplicación
- [x] Autenticación
- [ ] Red
> Correcto

2. Examine el siguiente registro:
```
[2022/12/21 17:46:35.232748] NOTIFY: NetworkPropertiesUpdated: wifi_psk_13
```
- ¿Qué tipo de registro es este?
- [x] Red
- [ ] Aplicación
- [ ] Ubicación
- [ ] Autenticación
> Correcto

3. Examine el siguiente registro
```json
{
	“name”: “System test”,
	“host”: "167.155.183.139",
	“id”: 11111,
	“Message”: [error] test,
}
```
- ¿En qué formato de registro se encuentra esta entrada?
- [ ] CSV
- [ ] XML
- [x] JSON
- [ ] Syslog
> Correcto

3. Examine el siguiente registro:
```
<111>1 2020-04-12T23:20:50.52Z my.machine.com evntslog - ID01 [user@98274 iut="2" eventSource="Mobile" eventID="24"][Priority@98274 class="low"] Computer A
```
- ¿Qué valor de campo indica el tipo de dispositivo del que procede este Evento?
- [ ] Mobile
- [x] my.machine.com
- [ ] low
- [ ] Computer A (Incorrecto)
> Incorrecto

4. Considere el siguiente escenario:
- Un analista de seguridad de una empresa mediana recibe el encargo de instalar y configurar un Sistema de detección de intrusiones basado en el anfitrión (HIDS) en un ordenador portátil. El analista de Seguridad instala el HIDS y quiere probar si funciona correctamente simulando una actividad maliciosa. El analista de Seguridad ejecuta programas no autorizados en el portátil, que el HIDS detecta con éxito y sobre los que alerta.
- ¿De qué es un ejemplo el portátil?
- [x] Un punto de conexión
- [ ] Un reenviador de registros
- [ ] Un agente (Incorrecto)
- [ ] Una Firma
> Incorrecto

4. ¿Cuál es la diferencia entre un Sistema de detección de intrusiones basado en la red (NIDS) y un Sistema de detección de intrusiones basado en el anfitrión (HIDS)?
- [ ] Un NIDS registra y genera alertas. Un sistema HIDS monitoriza la actividad de los puntos finales.
- [ ] Un NIDS monitorea la actividad del host en el que está instalado. Un HIDS utiliza el análisis de firmas para analizar la actividad de la red.
- [ ] Tanto los NIDS como los HIDS monitorizan los sistemas y generan alertas, pero un NIDS utiliza agentes.
- [x] Un NIDS recoge y monitorea el Tráfico de red y los Datos de red. Un HIDS monitoriza la actividad del host en el que está instalado.
> Correcto

5. ¿Qué información se incluye en el Encabezado de una Firma? Seleccione todo lo que corresponda
- [x] Número de puerto
- [x] Dirección IP
- [ ] Acción
- [x] Protocolo
> Correcto

5. ¿Qué opción de regla se utiliza para indicar el número de veces que se actualiza una firma?
- [x] rev
- [ ] sid
- [ ] msg
- [ ] tcp
> Correcto

6. ¿Qué símbolo se utiliza para indicar un Comentario y se ignora en un fichero de Firma Suricata?
- [x] #
- [ ] >
- [ ] $
- [ ] :
> Correcto

6. Examine esta Firma Suricata:
```suricata
alert http 167.215.72.95 any -> 156.150.71.141 80 (msg:"GET on wire"; flow:established,to_server; content:"GET"; sid:12345; rev:2;)
```
- ¿Cuál es el puerto de destino?
- [ ] 2
- [x] 80
- [ ] 12345
- [ ] 141
> Correcto

7. Rellene el espacio en blanco: Suricata utiliza el formato _____ para la salida de eventos y alertas
- [ ] HTTP
- [ ] CEF
- [ ] HTML
- [x] EVE JSON
> Correcto

7. ¿Qué tipo de datos de registro genera Suricata? Seleccione todo lo que corresponda
- [x] Alerta
- [ ] Firma
- [ ] Protocolo
- [x] Telemetría de redes
> Correcto

8. Rellene el espacio en blanco: El símbolo del asterisco también se conoce como a(n) _____
- [ ] opción
- [x] comodín
- [ ] Operador booleano
- [ ] etiqueta
> Correcto

8. ¿Qué lenguaje de consulta utiliza Splunk?
- [ ] Lenguaje de Consulta Estructurada
- [ ] Lenguaje de proceso SIEM
- [x] Lenguaje de Procesamiento de Búsqueda
- [ ] Lenguaje de procesamiento estructurado
> Correcto

9. ¿Cuál es el Método para buscar Datos normalizados en Chronicle?
- [x] Búsqueda UDM
- [ ] YARA-L
- [ ] Búsqueda de registros en bruto
- [ ] Unificado
> Correcto

9. ¿Qué búsqueda de campo del Modelo Unificado de Datos (UDM) especifica una acción de seguridad?
- [ ] action
- [ ] block
- [ ] metadata.event_type
- [x] security_result.action
> Correcto

10. ¿Cuáles son los pasos del proceso SIEM para la recopilación de datos? Seleccione tres respuestas.
- [x] Recoja
- [x] Índice
- [ ] Unificar
- [x] Normalización
> Correcto

10. Rellene el espacio en blanco: Herramientas SIEM _____ datos en bruto para que su formato sea coherente
- [ ] recoja
- [ ] proceso
- [x] normalización
- [ ] ingerir
> Correcto

10. ¿Qué paso del proceso SIEM implica el procesamiento de datos brutos en un formato estandarizado y estructurado?
- [ ] Recoja
- [x] Normalización
- [ ] Proceso
- [ ] Índice
> Correcto