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