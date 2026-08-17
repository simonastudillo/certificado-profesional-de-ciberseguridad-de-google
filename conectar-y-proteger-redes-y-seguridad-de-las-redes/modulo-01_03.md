# Comunicación en red

## Introducción a la comunicación en red
- ​Las redes ayudan a las organizaciones a comunicarse y conectarse.
- ​Pero la comunicación hace que los ataques a la red sean más probables porque da a un ​actor malicioso la oportunidad de aprovecharse de dispositivos vulnerables y ​redes desprotegidas
- La comunicación a través de una red se produce cuando los datos se transfieren de un punto a ​otro
- Los fragmentos de datos suelen denominarse paquetes de datos
- Un paquete de datos es una unidad básica de información que viaja de un ​dispositivo a otro dentro de una red
- Cuando los datos se envían de un dispositivo a otro a través de una red, se envían como ​un paquete que contiene información sobre a dónde va el paquete, de dónde ​viene y el contenido del mensaje
- Piense en los paquetes de datos como si fueran un trozo de correo físico. 
- Imagínese que quiere enviar una carta a un amigo
- ​En el sobre tendrá que figurar la dirección a la que quiere que llegue la carta ​y su dirección de remitente
- Dentro del sobre hay una carta que contiene ​el mensaje que quiere que su amigo lea
- Un paquete de datos es muy similar a una carta física. ​Contiene un encabezado que incluye la dirección del protocolo de Internet, la dirección IP ​y la dirección MAC (Media Access Control) del dispositivo de destino
- También incluye un número de protocolo que indica al dispositivo receptor qué hacer con ​la información del paquete
- ​Luego está el cuerpo del paquete, que contiene el mensaje que debe ​transmitirse al dispositivo receptor. 
- Por último, al final del paquete, hay un pie de página, ​similar a la firma de una carta, ​el pie de página indica al dispositivo receptor que el paquete ha finalizado
- El movimiento de los paquetes de datos a través de una red puede proporcionar una indicación de lo ​bien que funciona la red
- El rendimiento de la red puede medirse por el ancho de banda
- ​El ancho de banda se refiere a la cantidad de datos que recibe un dispositivo cada segundo.
- ​Puede calcular el ancho de banda dividiendo la cantidad de datos por el tiempo en ​segundos
- La Velocidad se refiere a la velocidad a la que se reciben o descargan los paquetes de datos. 
- El personal de seguridad está interesado en el ancho de banda y la Velocidad de la red ​porque si cualquiera de ellos es irregular, podría ser un indicio de un ataque. 
- ​El sniffing de paquetes es la práctica de capturar e ​inspeccionar paquetes de datos a través de la red
- La comunicación en la red es importante para compartir recursos y ​datos porque permite que las organizaciones funcionen con eficacia

---

## Modelo TCP/IP
- ​TCP/IP son las siglas de ​Protocolo de control de transmisión y Protocolo de Internet
- TCP/IP es el modelo estándar ​utilizado para la comunicación en red
- En primer lugar, TCP, o Protocolo de Control de Transmisión, ​es un protocolo de comunicación de Internet que permite ​a dos dispositivos formar una conexión y transmitir datos
- El protocolo incluye un conjunto de instrucciones para ​organizar los datos, de forma que puedan enviarse a través de una red. 
- ​También establece una conexión entre dos dispositivos ​y se asegura de que los paquetes ​lleguen a su destino apropiado
- El IP en TCP/IP significa Protocolo de Internet.
- IP tiene un conjunto de Estándares utilizados para enrutar y direccionar ​paquetes de datos a medida que viajan ​entre dispositivos en una red
- Incluida en el Protocolo de Internet (IP) está la dirección IP ​que funciona como una dirección para cada red privada
- Cuando se envían y reciben paquetes de datos a través de una red, ​se les asigna un puerto. 
- Dentro del sistema operativo de un dispositivo de red, ​un puerto es una ubicación basada en software que organiza ​el envío y recepción de datos ​entre dispositivos de una red. 
- ​Los puertos dividen el Tráfico de red en segmentos ​basados en el servicio que realizarán ​entre dos dispositivos
- Las computadoras que envían y ​reciben estos segmentos de datos saben cómo ​priorizar y procesar estos segmentos ​basándose en su número de puerto
- Los paquetes de datos incluyen instrucciones que indican ​al dispositivo receptor qué hacer con la información
- Estas instrucciones vienen en forma de número de puerto
- Los números de puerto permiten a las computadoras ​dividir el Tráfico de red y ​priorizar las operaciones que ​realizarán con los datos. 
- Algunos números de puerto comunes son: ​el puerto 25, que se utiliza para el correo electrónico, ​el puerto 443, que se ​utiliza para la comunicación segura en Internet, ​y el puerto 20, para las transferencias de archivos de gran tamaño

---

## Las cuatro capas del Modelo TCP/IP
- El modelo TCP/IP es un marco que se utiliza para ​visualizar cómo se ​organizan y transmiten los datos a través de la red
- El modelo TCP/IP tiene cuatro capas
   - La capa de acceso a la red
      - La capa de acceso a la red se ocupa de la creación de ​paquetes de datos y su transmisión a través de una red
      - Esto incluye los dispositivos de hardware conectados a ​cables físicos y conmutadores ​que dirigen los datos a su destino
   - La capa de Internet
      - La capa de Internet es donde se adjuntan las direcciones IP a los ​paquetes de datos para indicar ​la ubicación del emisor y el receptor
      - La capa de Internet también se centra ​en cómo se conectan las redes entre sí
      - Por ejemplo, los paquetes de datos ​contienen información que determina si ​se quedarán en la LAN o se enviarán ​a una red remota, como Internet
   - La capa de transporte
      - La capa de transporte incluye protocolos para ​controlar el flujo de tráfico a través de una red. 
      - ​Estos protocolos permiten o deniegan la comunicación con ​otros dispositivos e incluyen ​información sobre el estado de la conexión
      - Las actividades de esta capa incluyen el control de errores, ​que garantiza que los datos fluyen ​sin problemas por la red
   - La capa de aplicación
      - los protocolos determinan cómo los paquetes de datos ​interactuarán con los dispositivos receptores
      - Las funciones que se organizan en la capa de aplicación ​incluyen la transferencia de archivos y los servicios de correo electrónico
- Saber cómo organiza el modelo TCP/IP la actividad de la red ​permite a los profesionales de la seguridad ​vigilar y protegerse contra los riesgos