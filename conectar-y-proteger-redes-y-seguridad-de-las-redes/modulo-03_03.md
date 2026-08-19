# Tácticas de ataque y defensa de redes

## Sniffing de paquetes malicioso
- Analizaremos el ​sniffing de paquetes, centrándonos ​en cómo los actores de amenazas pueden utilizar esta ​técnica para obtener acceso no autorizado a la información.
- ​Los paquetes incluyen un encabezado que contiene ​las direcciones IP del remitente y del receptor.
- ​Los paquetes también contienen un cuerpo, que ​puede contener información valiosa como nombres, ​fechas de nacimiento, mensajes personales ​, información financiera y números de tarjetas de crédito.
- La ​detección de paquetes es la práctica de utilizar ​herramientas de software para observar ​los datos a medida que se mueven por una red.
- ​Como analista de Seguridad, ​puede usar el sniffing de paquetes para analizar ​y capturar paquetes al investigar ​incidentes en curso o al depurar problemas de red.
- Sin embargo, los actores malintencionados también pueden usar el ​sniffing de paquetes para ​analizar los datos que no se les han enviado.
- Es un poco como abrir el correo de otra persona.
- ​Es importante que conozca cómo los ​actores de amenazas utilizan el sniffing ​de paquetes con intenciones dañinas para que ​pueda estar preparado para protegerse contra estos actos maliciosos.
- ​Los actores malintencionados pueden meterse en medio de ​una conexión autorizada entre dos dispositivos.
- ​Luego, pueden usar el sniffing de paquetes para ​espiar cada paquete de datos a medida que llega a su dispositivo.
- ​El objetivo es encontrar información valiosa en ​los paquetes de datos que ​luego puedan utilizar en su beneficio.
- ​Los atacantes pueden usar aplicaciones de software ​o un dispositivo de hardware para examinar los paquetes de datos.
- ​Los actores malintencionados pueden acceder a un paquete de red con ​un rastreador de paquetes y realizar cambios en los datos.
- ​Pueden cambiar la información ​del cuerpo del paquete, ​como modificar el número de cuenta bancaria del destinatario.
- La ​detección de paquetes puede ser pasiva o activa.
- ​El Rastreo pasivo de paquetes es un tipo de ​ataque en el que los paquetes de datos se leen en tránsito.
- ​Como todo el tráfico de una red ​es visible para cualquier host del concentrador​, los actores malintencionados pueden ​ver toda la información que ​entra y sale del dispositivo al que se dirigen. 
- Pensando en el ejemplo de la entrega de una carta, ​podemos comparar un ​ataque pasivo de sniffing de paquetes con el de un ​repartidor postal que lee maliciosamente el correo de alguien.
- ​El empleado postal, o ​rastreador de paquetes, tiene derecho a entregar el correo, ​pero no a leer la información que contiene.
- ​El Rastreo activo de paquetes es un tipo de ​ataque en el que los paquetes de datos se manipulan en tránsito.
- ​Esto puede incluir inyectar ​protocolos de Internet para redirigir los paquetes a ​un puerto no deseado o ​cambiar la información que contiene el paquete.
- Un ​ataque de Rastreo activo de paquetes ​sería como si un vecino le dijera al ​repartidor: «Te entregaré el correo», y luego lee el ​correo o cambia la carta antes de ponerla en tu buzón.
- ​A pesar de que su vecino lo conoce ​y aunque lo entregue en la casa correcta, ​está haciendo todo lo posible por ​participar en un comportamiento malintencionado.
- ​La buena noticia es que se puede prevenir el ​sniffing de paquetes malintencionado.
- ​Veamos algunas maneras en las que ​el profesional de Seguridad de redes ​puede prevenir estos ataques.
- ​Una forma de protegerse contra el ​sniffing de paquetes malintencionados es ​usar una VPN para cifrar ​y proteger los datos a medida que viajan por la red. 
- Cuando usas una VPN, ​los piratas informáticos pueden interferir con tu tráfico, ​pero no podrán decodificarlo ​para leerlo y leer tu información privada.
- ​Otra forma de agregar una capa de ​protección contra el sniffing de paquetes es ​asegurarse de que los sitios web que tiene ​usen HTTPS al principio de la dirección de dominio.
- ​Anteriormente, analizamos cómo HTTPS usa SSL/TLS para ​cifrar los datos y evitar las escuchas clandestinas cuando actores malintencionados espían las transmisiones de la red.
- Una última forma de protegerse contra el ​sniffing de paquetes malintencionados ​es evitar el uso de redes WiFi sin protección.
- ​Por lo general, encontrarás WiFi sin protección en ​lugares públicos como cafeterías ​, restaurantes o aeropuertos.
- ​Estas redes no usan encriptación.
- Esto significa que cualquier usuario de la red puede acceder a ​todos los datos que viajan hacia y desde tu dispositivo.
- ​Una precaución que puedes tomar es evitar las redes ​WiFi públicas gratuitas, a menos que ​ya tengas un servicio de VPN instalado en tu dispositivo.

---

## Suplantación de IP
- ​La suplantación de IP es un ​ataque de red que se realiza cuando un atacante cambia la ​IP de origen de un paquete de datos ​para hacerse pasar por un sistema autorizado y obtener acceso a una red.
- ​En este tipo de ataque, ​el hacker se hace pasar por alguien que ​no es para poder comunicarse a través de ​la red con la computadora objetivo y ​superar las reglas del firewall que pueden impedir el tráfico externo.
- ​Algunos ataques de suplantación de IP más comunes son los ataques en ruta​, los ataques de repetición y los ataques de smurf.
   - ​Un ataque en ruta es ​un ataque en el que el actor malintencionado se coloca en ​medio de una conexión autorizada ​e intercepta o altera los datos en tránsito.
      - ​Los atacantes en ruta obtienen acceso a ​la red y se interponen entre dos dispositivos, ​como un navegador web y un servidor web.
      - ​Luego, rastrean la ​información del paquete para conocer las ​direcciones IP y MAC de los dispositivos ​que se comunican entre sí.
      - ​Una vez que tengan esta información, ​pueden fingir ser cualquiera de estos dispositivos. 
   - ​Un ataque de reproducción es ​un ataque de red que se realiza cuando ​un actor malintencionado intercepta ​un paquete de datos en tránsito y ​lo retrasa o lo repite en otro momento.
      - ​Un paquete retrasado puede provocar ​problemas de conexión entre los equipos de destino, ​o un actor malintencionado puede tomar ​una transmisión de red enviada por ​un usuario autorizado y repetirla ​más adelante para hacerse pasar por el usuario autorizado.
   - ​Un ataque de smurf es una combinación de un ataque ​DDoS y un ataque de suplantación de IP.
      - ​El atacante olfatea la dirección IP de un usuario autorizado ​y la inunda de paquetes.
      - ​Esto abruma al equipo de destino y puede ​provocar la caída de un servidor o de toda la red.
- ​Como aprendió anteriormente, el ​cifrado siempre debe implementarse para que los datos de las ​transferencias de red no puedan ​ser leídos por actores malintencionados.
- ​Los firewalls se pueden configurar ​para protegerlos contra la suplantación de IP.
- ​La suplantación de IP hace que ​parezca que el actor malintencionado es un ​usuario autorizado al cambiar la ​dirección del remitente del paquete de datos para que coincida con la dirección de la red de destino.
- ​Por lo tanto, si un firewall recibe un paquete de datos de Internet ​en el que la dirección IP del remitente ​es la misma que la de la red privada, ​el firewall denegará la transmisión, ​ya que todos los dispositivos con esa dirección IP ​ya deberían estar en la red local.
- ​Puede asegurarse de que sus firewalls se ​configuren correctamente creando una regla para ​rechazar todo el tráfico entrante que tenga ​la misma dirección IP que la red local.

---

## Visión general de las tácticas de interceptación
- Una revisión más detallada del sniffing de paquetes
   - El sniffing de paquetes es la práctica de capturar e inspeccionar paquetes de datos a través de una red.
   - En una red privada, los paquetes de datos se dirigen al dispositivo de destino correspondiente de la red.
   - La tarjeta de interfaz de red (NIC) del dispositivo es una pieza de hardware que conecta el dispositivo a una red.
   - La NIC lee la transmisión de datos y, si contiene la dirección MAC del dispositivo, acepta el paquete y lo envía al dispositivo para que procese la información basándose en el protocolo.
   - Esto ocurre en todas las operaciones de red estándar.
   - Sin embargo, una NIC puede configurarse en modo promiscuo, lo que significa que acepta todo el tráfico de la red, incluso los paquetes que no están dirigidos al dispositivo de la NIC.
   - Los actores maliciosos podrían utilizar software como Wireshark para capturar los datos de una red privada y almacenarlos para su uso posterior.
   - A continuación, pueden utilizar la información personal en su propio beneficio.
   - Otra posibilidad es que utilicen las direcciones IP y MAC de los usuarios autorizados de la red privada para realizar la suplantación de IP.
- Un examen más detallado de la Suplantación de IP
   - Después de que un actor malicioso haya olfateado paquetes en la red, puede suplantar las direcciones IP y MAC de dispositivos autorizados para realizar un ataque de suplantación de IP.
   - Los cortafuegos pueden evitar los ataques de suplantación de IP configurándolos para que rechacen los paquetes IP no autorizados y el tráfico sospechoso.
   - A continuación, examinará algunos ataques comunes de suplantación de IP con los que es importante familiarizarse como analista de Seguridad.
- Ataque en ruta
   - Un ataque en ruta se produce cuando un hacker intercepta la comunicación entre dos dispositivos o servidores que tienen una relación de confianza.
   - La transmisión entre estos dos dispositivos de red de confianza podría contener información valiosa como nombres de usuario y contraseñas que el actor malicioso puede recopilar.
   - Un ataque en ruta se denomina a veces ataque de intermediario porque el hacker se esconde en medio de las comunicaciones entre dos partes de confianza.
   - También puede ocurrir que la transmisión interceptada contenga una búsqueda en el sistema DNS.
   - Si un agente malicioso intercepta una transmisión que contiene una búsqueda DNS, podría falsificar la respuesta DNS del servidor y redirigir un nombre de dominio a una dirección IP diferente, quizás una que contenga código malicioso u otras amenazas.
   - La forma más importante de protegerse contra un ataque en ruta es la encriptación de sus Datos en tránsito, por ejemplo utilizando TLS.
- Ataque Smurf
   - Un Ataque Smurf es un ataque a la red que se realiza cuando un atacante olfatea la dirección IP de un usuario autorizado y lo inunda de paquetes.
   - Una vez que el paquete falsificado alcanza la dirección de broadcast, se envía a todos los dispositivos y servidores de la red.
   - En un ataque Smurf, la suplantación de IP se combina con otra técnica de denegación de servicio (DoS) para inundar la red con tráfico no deseado.
   - Por ejemplo, el Paquete falsificado podría incluir un ping del Protocolo de mensajes de control de Internet (ICMP).
   - Como ya ha aprendido, el ICMP se utiliza para solucionar problemas en una red.
   - Pero si se transmiten demasiados mensajes ICMP, las respuestas de eco ICMP abruman a los servidores de la red y éstos se apagan.
   - Esto crea una denegación de servicio y puede paralizar las operaciones de una organización.
   - Una forma importante de protegerse contra un ataque smurf es utilizar un firewall avanzado que pueda supervisar cualquier tráfico inusual en la red.
   - La mayoría de los firewalls de nueva generación (NGFW) incluyen características que detectan anomalías en la red para garantizar que se detectan las broadcast de tamaño excesivo antes de que tengan la oportunidad de hacer caer la red.
- Ataque DoS
   - Una vez que el actor malicioso ha olfateado el tráfico de red, puede hacerse pasar por un usuario autorizado.
   - Un ataque de denegación de servicio es una clase de ataques en los que el atacante impide que el sistema comprometido realice una actividad legítima o responda al tráfico legítimo.
   - Sin embargo, a diferencia de la suplantación de IP, el atacante no recibirá respuesta del host atacado.
   - Todo en el paquete de datos está autorizado, incluida la dirección IP en el Encabezado del paquete.
   - En los ataques de suplantación de IP, el actor malicioso utiliza paquetes IP que contienen direcciones IP falsas.
   - Los atacantes siguen enviando paquetes IP que contienen direcciones IP falsas hasta que el servidor de red se bloquea.

>[!NOTE] Recuerde el principio de defensa en profundidad. No existe una estrategia perfecta para detener cada tipo de ataque. Puede estratificar su defensa utilizando múltiples estrategias. En este caso, el uso de la encriptación estándar del sector reforzará su Seguridad y le ayudará a defenderse de los ataques DoS en más de un nivel.

----

## Identificar: Ataques a la red
- Review the flashcards to familiarize yourself with common types of network attacks and how these attacks can impact an organization’s network.

1. Denial of service attack (DoS): A network attack that targets a network or server and floods it with network traffic
2. Distributed denial of service attack (DDoS): A type of denial or service attack that uses multiple devices or servers in different locations to flood the target network with unwanted traffic
3. SYN flood attack: A type of DoS attack that simulates a TCP/IP connection and floods a server with SYN packets
4. Packet sniffing: The practice of capturing and inspecting data packets across a network
5. IP spoofing: A network attack performed when an attacker changes the source IP of a data packet to impersonate an authorized system and gain access to a network
6. On-path attack: An attack where a malicious actor places themselves in the middle of an authorized connection and intercepts or alters the data in transit

---

## Actividad: Analizar los ataques a la red
- Resumen de la actividad
   - En esta actividad, estudiará un escenario en el que un cliente de la empresa para la que trabaja experimenta un problema de seguridad al acceder al sitio web de la empresa.
   - Identificará la causa probable de la interrupción del servicio.
   - A continuación, explicará cómo se produjo el ataque y el impacto negativo que tuvo en el sitio web.
   - Comprender cómo afectan los ataques a una red le ayudará a solucionar los problemas de la red de su organización.
   - También le ayudará a tomar medidas para mitigar los daños y proteger una red de futuros ataques.
   - Asegúrese de completar esta actividad antes de continuar. El siguiente punto del curso le proporcionará un ejemplo completado para que lo compare con su propio trabajo. 
- Escenario
   - Revise el siguiente escenario. A continuación, complete las instrucciones paso a paso.
   - Usted trabaja como analista de seguridad para una agencia de viajes que anuncia ventas y promociones en el sitio web de la empresa.
   - Los empleados de la empresa acceden regularmente a la página web de ventas de la empresa para buscar paquetes vacacionales que puedan gustar a sus clientes.
   - Una tarde, recibe una alerta automática de su sistema de supervisión que le indica un problema con el servidor web.
   - Intenta visitar la página web de la empresa, pero recibe un mensaje de error de tiempo de espera de conexión en su navegador.
   - Utiliza un rastreador de paquetes para capturar los paquetes de datos en tránsito hacia y desde el servidor web.
   - Observa un gran número de solicitudes TCP SYN procedentes de una dirección IP desconocida.
   - El servidor web parece estar desbordado por el volumen de tráfico entrante y está perdiendo su capacidad para responder al número anormalmente elevado de peticiones SYN.
   - Usted sospecha que el servidor está siendo atacado por un actor malicioso.
   - Usted desconecta temporalmente el servidor para que la máquina pueda recuperarse y volver a un estado operativo normal.
   - También configura el cortafuegos de la empresa para que bloquee la dirección IP que estaba enviando el número anormal de peticiones SYN.
   - Sabe que su solución de bloqueo de IP no durará mucho, ya que un atacante puede suplantar otras direcciones IP para burlar este bloqueo.
   - Tiene que alertar rápidamente a su jefe sobre este problema y discutir los pasos a seguir para detener a este atacante y evitar que este problema se repita.
   - Tendrá que estar preparado para contarle a su jefe el tipo de ataque que ha descubierto y cómo estaba afectando al servidor web y a los empleados.
- Instrucciones paso a paso

1. Acceder a la plantilla
   - [Plantilla: Informe sobre incidentes de ciberseguridad](./resources/Cybersecurity-incident-report.docx)
2. Acceso a los materiales de apoyo
   - Los siguientes materiales de apoyo te ayudarán a completar esta actividad
   - [Registro TCP/HTTP de Wireshark](./resources/HTTP-log.xlsx)
   - [Cómo leer un registro TCP/HTTP de Wireshark](./resources/How-to-read-a-Wireshark-TCP_HTTP-log.docx)
3. Identificar el tipo de ataque causante de esta interrupción de la red
   - Reflexione sobre los tipos de ataques de intrusión en la red que ha conocido hasta ahora en este curso.
   - Como analista de seguridad, identificar el tipo de ataque a la red en función del incidente es el primer paso para gestionar el ataque y prevenir ataques similares en el futuro.
   - He aquí algunas preguntas a tener en cuenta a la hora de determinar qué tipo de ataque se ha producido:
      - ¿Qué entiende actualmente sobre los ataques a la red?
      - ¿Qué tipo de ataque provocaría probablemente los síntomas descritos en el escenario?
      - ¿Cuál es la diferencia entre una denegación de servicio (DoS) y una denegación de servicio distribuida (DDoS)?
      - ¿Por qué el sitio web tarda mucho en cargarse e informa de un error de tiempo de espera de conexión?
   - Revise la lectura de Wireshark del paso 2 e intente identificar patrones en el tráfico de red registrado.
   - Analice los patrones para determinar qué tipo de ataque de red se ha producido.
   - Escriba su análisis en la sección uno de la plantilla de informe de incidentes de ciberseguridad proporcionada. 
4. Explicar cómo el ataque está provocando el mal funcionamiento del sitio web
   - Revise la lectura de Wireshark del paso 2 y, a continuación, escriba su análisis en la sección dos de la plantilla de Informe de Incidentes de Ciberseguridad que se proporciona.
   - Cuando redacte su informe, hable de los dispositivos y actividades de red implicados en la interrupción. Incluya la siguiente Información en su explicación:
   - Describa el ataque. ¿Cuáles son los principales síntomas o características de este tipo específico de ataque? 
   - Explique cómo afectó a la red de la organización. ¿Cómo afecta este ataque específico a la red a la página web y a su funcionamiento?
   - Describa las posibles consecuencias de este ataque y cómo afecta negativamente a la organización. 
   - Opcional: Sugiera posibles formas de asegurar la red para poder evitar este ataque en el futuro.

Cybersecurity Incident Report:
1. Identify the type of attack that may have caused this network interruption:
Según lo revisado en el registro log TCP/HTTP de Wireshark, se reciben múltiples paquetes SYN de la dirección IP 203.0.113.0, lo cual indica un posible ataque de denegación de servicio (DoS) del tipo SYN flood. Este tipo de ataque se caracteriza por inundar el servidor con solicitudes de conexión TCP incompletas, lo que provoca que el servidor se quede sin recursos para atender solicitudes legítimas. El registro log demuestra que el servidor responde correctamente a las solicitudes hasta que en un punto solo recibe solicitudes SYN sin completar, lo que confirma la naturaleza del ataque.

2. Explain how the attack is causing the website to malfunction:
El servidor estaba recibiendo correctamente paquetes SYN, retornaba SYN-ACK (acknowledgment) luego retornaba la web solicitada con el método GET. Luego se detecta un aumento incremental de solicitudes SYN provenientes de la dirección IP 203.0.113.0, lo que indica un ataque de inundación SYN. Este aumento de solicitudes provoca que el servidor se sature y no pueda procesar las solicitudes legítimas de los usuarios, resultando en tiempos de espera altos al punto de fallar en responder a las solicitudes de los usuarios. 

---

## Ejemplo de actividad: Analizar los ataques a la red
- Aquí tiene un ejemplar completado junto con una explicación de cómo el ejemplar cumple las expectativas de la actividad.
- [Ejemplar de Informe de Incidente de Ciberseguridad](./resources/Cybersecurity-incident-report-exemplar.docx)
- Evaluación del Ejemplar
   - Compare el ejemplar con su actividad finalizada. Revise su trabajo utilizando cada uno de los criterios del ejemplar.
   - ¿Qué ha hecho bien? ¿En qué puede mejorar? Utilice sus respuestas a estas preguntas como guía para seguir avanzando en el curso.
- El ejemplar representa una posible explicación de los problemas a los que se enfrenta el usuario. Es probable que la suya difiera en ciertos aspectos. Lo importante es que ha identificado los protocolos de red implicados y ha creado un Informe. En su función de analista de seguridad, usted y su Equipo harían la mejor conjetura sobre lo ocurrido y luego investigarían más a fondo para solucionar el Problema y reforzar la seguridad general de su red.
- El ejemplo identifica que el mensaje de tiempo de espera de la conexión es el resultado de un ataque DoS.
- En esta Instancia, el ataque DoS específico es un Ataque de SYN flood.
- Para determinarlo, analice los datos presentados en el extracto del archivo de registro adjunto a esta actividad.
- A continuación, reflexione sobre su conocimiento actual de los ataques de red para identificar qué tipo de ataque se está produciendo en función de los datos disponibles.
- Tras identificar un posible tipo de ataque a la red, proceda a explicar cómo llegó a identificar el ataque.
- A continuación, documente cómo este tipo específico de ataque pudo afectar a la red e incluya una descripción general de cómo el atacante explotó la vulnerabilidad de la red.
- Por último, describa cómo este ataque provocó que la página web mostrara el error de tiempo de espera de la conexión.
- El ejemplo sólo ofrece un ejemplo de explicación del suceso.
- Describir un Evento normalmente requiere presentar sus pruebas y explicar cómo llegó a su decisión.
- Todos los patrones que observe en los registros y datos son fundamentales para determinar el origen y el tipo de ataque a la red.
- Cuanta más práctica tenga en la identificación de estos patrones, más fácil le resultará detectar los ataques a la red en el momento en que se producen.
- Esto le permitirá responder a los incidentes con mayor rapidez y eficacia.