# Introducción a los protocolos de redes

## Bienvenido al módulo 2
- En esta sección, aprenderá cómo ​operan las redes utilizando herramientas y protocolos
- Las herramientas y protocolos que aprenderá en esta sección del ​programa le ayudarán a proteger ​la red de su organización de los ataques
- ¿Sabía que los actores maliciosos pueden aprovecharse de ​los datos que se mueven de un dispositivo a otro en una red?
- Afortunadamente, existen herramientas y ​protocolos para garantizar que la red ​permanezca protegida frente a este tipo de amenaza
- Primero, hablaremos de algunos protocolos de red comunes
- Después, hablaremos de las redes privadas virtuales o VPN
- Y, por último, aprenderemos sobre ​cortafuegos, zonas de seguridad y servidores proxy

---

## Protocolos de red
- ​Las redes se benefician de tener reglas.
- ​Las reglas garantizan que los datos enviados a través ​de la red lleguen al lugar correcto.
- ​Estas reglas se conocen como protocolos de red. ​Los protocolos de red son un conjunto de ​reglas que utilizan dos o más dispositivos de ​una red para describir el orden de ​entrega y la estructura de los datos
- Utilicemos un escenario para demostrar ​algunos tipos diferentes de protocolos de red ​y cómo funcionan juntos en una red
   - Supongamos que quieres acceder a tu sitio web de recetas favorito.
   - ​Ve a la barra de direcciones en la parte superior de ​tu navegador y escribe la dirección del sitio web. 
   - Por ejemplo: www.yummyrecipesforme.org. 
   - Antes de acceder al sitio web, ​su dispositivo establecerá ​comunicaciones con un servidor web
   - Esa comunicación utiliza un protocolo denominado ​Protocolo de control de transmisión o TCP
   - TCP es un protocolo de comunicación de Internet que permite que ​dos dispositivos establezcan una conexión y transmitan datos
   - Tenga en cuenta que el protocolo TCP no se limita a dos dispositivos.
   - Establece una conexión directa entre dos puntos finales, pero la infraestructura de red subyacente puede encargarse del enrutamiento de paquetes de datos a través de múltiples dispositivos. 
   - El TCP también verifica ambos dispositivos ​antes de permitir que se lleve a cabo cualquier otra comunicación. ​Esto a menudo se denomina protocolo de enlace
   - Una vez que se establece la comunicación mediante un protocolo de enlace TCP, ​se realiza una solicitud a la red. 
   - ​Utilizando nuestro ejemplo, hemos solicitado ​datos del servidor Yummy Recipes For Me
   - Sus servidores responderán a esa solicitud y enviarán ​paquetes de datos a ​su dispositivo para que pueda ver la página web
   - ​A medida que los paquetes de datos se mueven por la red, ​se mueven entre los dispositivos de red, como los enrutadores
   - El protocolo de resolución de direcciones, o ARP, se usa para ​determinar la dirección MAC del siguiente ​router o dispositivo de la ruta de acceso
   - Esto garantiza que los datos lleguen al lugar correcto
   - Ahora que se ha ​establecido la comunicación y se conoce el dispositivo de destino, ​es hora de acceder al sitio web Yummy Recipes For Me
   - ​El Protocolo seguro de transferencia de hipertexto, o HTTPS, es ​un protocolo de red que proporciona un método seguro de ​comunicación entre los servidores del cliente y del sitio web. 
   - Permite que su navegador web envíe de forma segura una solicitud de ​una página web al servidor Yummy Recipes For Me ​y reciba una página web como respuesta
   - ​Luego viene un protocolo llamado ​Sistema de nombres de dominio, o DNS, ​que es un protocolo de red que ​traduce los nombres de dominio de Internet en direcciones IP
   - El protocolo DNS envía ​el nombre de dominio y la dirección web a ​un servidor DNS que recupera ​la dirección IP del sitio web al que intentaba acceder, ​en este caso, Yummy Recipes For Me
   - ​La dirección IP se incluye como dirección de destino para ​los paquetes de datos que viajan ​al servidor web Yummy Recipes For Me
   - Por lo tanto, con solo visitar un sitio web, ​el dispositivo de sus redes ​utiliza cuatro protocolos diferentes: ​TCP, ARP, HTTPS y DNS
   - Estos son solo algunos de los protocolos que ​se utilizan en las comunicaciones de red
   - ​Pero, ¿cómo se relacionan estos protocolos con la Seguridad? ​Bueno, en el ejemplo del sitio web Yummy Recipes For Me, ​utilizamos HTTPS, que es ​un protocolo seguro que ​solicita una página web desde un servidor web
   - HTTPS cifra los datos mediante ​la Capa de sockets seguros y la capa de Seguridad de transporte, ​también conocidas como SSL/TLS. 