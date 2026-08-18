# Redes seguras contra ataques de denegación de servicio (DoS)

## Ataques de denegación de servicio (DoS)
- Un ataque de denegación de servicio es ​un ataque que tiene como objetivo una red o un servidor ​y lo inunda de tráfico de red.
   - ​El objetivo de un ataque de denegación de servicio, ​o un ataque DoS, es interrumpir ​las operaciones comerciales normales ​al sobrecargar la red de una organización.
   - ​El objetivo del ataque es enviar ​tanta información a un dispositivo de red ​que se bloquee o ​no pueda responder a los usuarios legítimos.
   - ​Esto significa que la organización no ​podrá llevar a cabo sus operaciones comerciales normales, ​lo que puede costarles tiempo y dinero.
   - ​Una caída de la red también puede dejarlos ​vulnerables a otras amenazas y ataques de Seguridad.
- ​Un ataque de denegación de servicio distribuido, o DDoS, ​es un tipo de ataque DoS que utiliza ​varios dispositivos o servidores en ​diferentes ubicaciones para inundar ​la red objetivo con tráfico no deseado.
   - El ​uso de numerosos dispositivos aumenta las probabilidades de que ​la cantidad total de tráfico ​enviado abrume al servidor de destino.
- ​Recuerde que DoS significa denegación de servicio.
- ​Por lo tanto, no importa qué parte ​de la red sobrecargue el atacante; ​si sobrecarga algo, gana.
- ​Un ejemplo desafortunado que he ​visto es el de un atacante que creó ​un paquete muy cuidadoso que provocó que ​un router dedicara más tiempo a procesar la solicitud.
- ​El volumen total de tráfico no sobrecargó el router; ​sí lo hicieron los detalles del paquete.
- ​Ahora analizaremos los ataques DoS a nivel de red ​que tienen como objetivo el ancho de banda de la red para reducir el tráfico. 
- ​Conozcamos tres ataques DoS comunes a nivel de red.
   - ​El primero se denomina Ataque de SYN flood.
      - ​Un ataque de inundación SYN es un tipo ​de ataque DoS que simula la ​conexión TCP e inunda el servidor con paquetes SYN.
      - ​Analicemos un poco ​más esta definición analizando más de cerca ​el proceso de protocolo de enlace que se utiliza para establecer ​una conexión TCP entre un dispositivo y un servidor.
      - ​El primer paso del protocolo de enlace es que el dispositivo envíe ​una solicitud SYN o sincronice al servidor.
      - ​A continuación, el servidor responde con ​un paquete SYN/ACK para ​confirmar la recepción de la solicitud del dispositivo ​y deja un puerto abierto para ​el paso final del protocolo de enlace.
      - ​Una vez que ​el servidor recibe el paquete ACK final del dispositivo, ​se establece una conexión TCP.
      - Los actores malintencionados pueden aprovechar el protocolo ​inundando un servidor con ​solicitudes de paquetes SYN para la primera parte del protocolo de enlace.
      - ​Sin embargo, si el número de solicitudes SYN es ​mayor que el número de puertos disponibles en el servidor, ​el servidor se saturará ​y no podrá funcionar.
   - Analicemos otros dos ataques DoS comunes ​que utilizan otro protocolo llamado ICMP. ​ICMP son las siglas de Protocolo de mensajes de control de Internet.
      - El ​ICMP es un protocolo de Internet que utilizan los dispositivos ​para informarse unos a otros sobre ​los errores de transmisión de datos en la red.
      - ​Piense en ICMP como una solicitud de ​actualización de estado desde un dispositivo.
      - ​El dispositivo devolverá ​mensajes de error si hay algún problema con la red. 
      - ​Puede pensar en esto como ​la solicitud ICMP que se registra en ​el dispositivo para asegurarse de que todo está bien.
      - ​Un ataque de Inundación ICMP ​es un tipo de ataque DoS realizado por un atacante que envía ​repetidamente paquetes ICMP a un servidor de red.
      - ​Esto obliga al servidor a enviar un paquete ICMP.
      - Con el ​tiempo, esto consume todo el ancho de banda para el ​tráfico entrante y saliente y hace que el servidor se bloquee.
- ​Los dos ataques de los que hemos hablado hasta ahora, la ​inundación SYN y la inundación ​ICMP, aprovechan ​los protocolos de comunicación al enviar una cantidad abrumadora de solicitudes.
- ​También hay ataques que pueden abrumar ​el servidor con una gran solicitud.
- Un ejemplo del que hablaremos ​es el llamado ping de la muerte. 
- Un ataque de ping of death es ​un tipo de ataque DoS que se produce cuando un hacker hace ​ping a un sistema enviándole ​un paquete ICMP sobredimensionado de ​más de 64 kilobytes, ​el tamaño máximo de un paquete ICMP formado correctamente.
- ​Hacer ping a un servidor de red vulnerable con ​un paquete ICMP sobredimensionado ​sobrecargará el sistema y provocará que se bloquee.
- ​Piensa en esto como dejar caer una piedra sobre un pequeño hormiguero.
- ​Cada hormiga individual puede cargar una cierta cantidad de ​peso mientras transporta comida hacia y desde el hormiguero.
- ​Pero si se deja caer una roca grande sobre el hormiguero, ​muchas hormigas serán aplastadas y la colonia no podrá ​funcionar hasta que reconstruya sus operaciones en otros lugares.

---

## Leer registros de tcpdump
- Un analizador de protocolos de red, a veces denominado sniffer de paquetes o analizador de paquetes, es una herramienta diseñada para capturar y analizar el tráfico de datos dentro de una red.
- Suelen utilizarse como herramientas de investigación para monitorizar redes e identificar actividades sospechosas.
- Existe una gran variedad de analizadores de protocolos de red, pero algunos de los más comunes son:
   - Analizador de Tráfico NetFlow de SolarWinds
   - ManageEngine OpManager
   - Observador de redes Azure
   - Wireshark
   - tcpdump
- tcpdump
   - tcpdump es un analizador de protocolos de red de línea de comandos.
   - Es popular, ligero -lo que significa que utiliza poca memoria y tiene un bajo uso de CPU- y utiliza la biblioteca de código abierto libpcap.
   - tcpdump está basado en texto, lo que significa que todos los comandos de tcpdump se ejecutan en el terminal.
   - También puede instalarse en otros sistemas operativos basados en Unix, como macOS.
   - Está preinstalado en muchas distribuciones de Linux.
   - tcpdump proporciona un breve análisis de paquetes y convierte la información clave sobre el tráfico de red en formatos fácilmente legibles por humanos.
   - Imprime información sobre cada paquete directamente en su terminal.
   - tcpdump también muestra la dirección IP de origen, las direcciones IP de destino y los números de puerto que se están utilizando en las comunicaciones. 
- Interpretar la salida
   - tcpdump imprime la salida del comando como los paquetes olfateados en la línea de comandos, y opcionalmente en un archivo de registro, después de ejecutar un comando.
   - La salida de una captura de paquetes contiene muchas piezas de información importante sobre el tráfico de la red.

<img src="./resources/image-14.png" alt="Tipos de información presentados en una captura de paquetes tcpdump" width="700">

- Alguna de la información que recibe de una captura de paquetes incluye:
   - Marca de tiempo: La salida comienza con la marca de tiempo, formateada como horas, minutos, segundos y fracciones de segundo.
   - IP de origen: El origen del paquete lo proporciona su dirección IP de origen.
   - Puerto de origen: Este número de puerto es donde se originó el paquete.
   - IP de destino: La dirección IP de destino es hacia dónde se está transmitiendo el paquete.
   - Puerto de destino: Este número de puerto es hacia donde se está transmitiendo el paquete.

- Por defecto, tcpdump intentará resolver las direcciones de host a nombres de host. También sustituirá los números de puerto por servicios comúnmente asociados que utilicen estos puertos.
- Usos comunes
   - tcpdump y otros analizadores de protocolos de red se utilizan habitualmente para capturar y visualizar las comunicaciones de red y para recopilar estadísticas sobre la red, como la solución de problemas de rendimiento de la red.
   - También pueden utilizarse para:
      - Establecer una línea de base para los patrones de tráfico de red y las métricas de utilización de la red.
      - Detectar e identificar el tráfico malicioso
      - Crear alertas personalizadas para enviar las notificaciones adecuadas cuando surjan problemas en la red o amenazas a la seguridad.
      - Localizar la mensajería instantánea (MI), el tráfico o los puntos de acceso inalámbricos no autorizados.
   - Sin embargo, los atacantes también pueden utilizar los analizadores de protocolos de red de forma maliciosa para obtener información sobre una red específica.
   - Por ejemplo, los atacantes pueden capturar paquetes de datos que contengan información confidencial, como nombres de usuario de cuentas y contraseñas.
   - Como analista de ciberseguridad, es importante comprender la finalidad y los usos de los analizadores de protocolos de red.

---

## Ataque DDoS en la vida real
- Los ataques DoS distribuidos volumétricamente (DDoS) saturan una red enviando paquetes de datos no deseados en cantidades tan grandes que los servidores se vuelven incapaces de dar servicio a los usuarios normales.
- Esto puede ser perjudicial para una organización.
- Cuando los sistemas fallan, las organizaciones no pueden satisfacer las necesidades de sus clientes.
- A menudo pierden dinero y, en algunos casos, incurren en otras pérdidas.
- La Reputación de una organización también puede sufrir si las noticias de un ataque DDoS exitoso llegan a los consumidores, que entonces cuestionan la Seguridad de la organización.

- Un DDoS dirigido a un servidor DNS muy utilizado
   - Los servidores DNS traducen los nombres de dominio de los sitios web en la dirección IP del sistema que contiene la información del sitio web.
   - Por ejemplo, si un usuario tecleara la URL de un sitio web, un servidor DNS la traduciría en una dirección IP numérica que dirige el tráfico de red a la ubicación del servidor del sitio web.
   - El día del ataque DDoS que estamos estudiando, muchas grandes empresas utilizaban un proveedor de servicios DNS.
   - El proveedor de servicios alojaba el sistema DNS para estas empresas.
   - Esto significaba que cuando los usuarios de Internet tecleaban la URL del sitio web al que querían acceder, sus dispositivos eran dirigidos al lugar correcto.
   - El 21 de octubre de 2016, el proveedor de servicios fue víctima de un ataque DDoS.
- Antes del ataque
   - Antes del ataque al proveedor de servicios, un grupo de estudiantes universitarios creó una botnet con la intención de atacar varios servidores y redes de juegos.
   - Una botnet es una colección de computadoras infectadas por software malicioso que están bajo el control de un único agente de amenaza, conocido como "bot-herder".
   - Cada computadora de la botnet puede ser controlada a distancia para enviar un paquete de datos a un sistema objetivo.
   - En un ataque de botnet, los ciberdelincuentes ordenan a todos los bots de la botnet que envíen paquetes de datos al sistema objetivo al mismo tiempo, lo que da lugar a un ataque DDoS.
   - El grupo de estudiantes universitarios publicó en línea el código de la botnet para que fuera accesible a miles de usuarios de Internet y las autoridades no pudieran rastrear la botnet hasta los estudiantes.
   - Al hacerlo, hicieron posible que otros actores maliciosos aprendieran el código de la botnet y la controlaran a distancia.
   - Esto incluyó a los ciberdelincuentes que atacaron al proveedor de servicios DNS.
- El día del ataque
   - A las 7 de la mañana del día del ataque, la botnet envió decenas de millones de peticiones DNS al proveedor de servicios.
   - Esto desbordó el sistema y el servicio DNS se desconectó.
   - Esto significaba que no se podía acceder a todos los sitios web que utilizaban el proveedor de servicios.
   - Cuando los usuarios intentaban acceder a los distintos sitios web que utilizaban el proveedor de servicios, no eran dirigidos al sitio web que habían tecleado en su navegador.
   - Las interrupciones de cada servicio web se produjeron en toda Norteamérica y Europa.
   - Los sistemas del proveedor de servicios se restablecieron tras sólo dos horas de inactividad.
   - Aunque los ciberdelincuentes enviaron oleadas posteriores de ataques de botnet, la empresa de DNS estaba preparada y fue capaz de mitigar el impacto. 