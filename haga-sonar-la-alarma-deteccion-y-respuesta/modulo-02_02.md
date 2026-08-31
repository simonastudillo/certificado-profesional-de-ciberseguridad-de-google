# Captura y visualización del tráfico de red

## Paquetes y capturas de paquetes
- ​Ya sea que se trate de un empleado que envía un correo electrónico o de ​un actor malintencionado que ​intenta filtrar datos confidenciales, ​las acciones que se realizan en una red se pueden ​identificar mediante el examen de los flujos de tráfico de la red.
- La ​comprensión de estas comunicaciones de red proporciona ​una valiosa información estadística sobre las actividades ​que tienen lugar en una red.
- ​De esta manera, puede comprender mejor lo que sucede en ​un entorno y defenderse de posibles amenazas.
- ​Con esto en mente, examinemos cómo ​registrar el tráfico de red a través de capturas de paquetes.
- ​Anteriormente, en el programa, ​aprendiste que cuando se envían datos, ​se dividen en paquetes.
- ​Al igual que un sobre con dirección en el correo, ​los paquetes contienen información de entrega que ​se utiliza para dirigirlo a su destino.
- ​Esta información incluye la ​dirección IP del remitente y del destinatario, ​el tipo de paquete que se envía y más.
- ​Los paquetes pueden proporcionar mucha información sobre ​las comunicaciones que se producen entre ​los dispositivos a través de una red.
- ​También puede recordar que ​un paquete tiene varios componentes.
- ​Está el encabezado, que incluye información como ​el tipo de protocolo de red y el puerto que se está utilizando.
- ​Imagínese que es el nombre y la ​dirección postal que se encuentran en un sobre.
- ​Los Protocolos de red son un conjunto de reglas que determinan ​la transmisión de datos entre los dispositivos de una red.
- ​Los puertos son ubicaciones no físicas de una computadora ​que organizan la transmisión de datos ​entre los dispositivos de una red.
- ​El encabezado también contiene ​la dirección IP de origen y destino del paquete.
- ​Exploraremos más información ​incluida en el encabezado en una sección posterior.
- ​A continuación, está la carga útil, que ​contiene los datos reales que se están entregando.
- ​Es como el contenido de ​una carta dentro de un sobre.
- ​Y está el pie de página, ​que significa el final del paquete.
- ​Entonces, ¿cómo se puede observar exactamente un paquete de red?
- ​Al igual que los aromas son invisibles pero se pueden oler, ​los paquetes son invisibles pero se pueden ​capturar con herramientas llamadas rastreadores de paquetes.
- ​Es posible que recuerde los rastreadores de paquetes de una sección anterior.
- ​Un analizador de protocolos de red, o rastreador de paquetes, ​es una herramienta diseñada para capturar y ​analizar el tráfico de datos dentro de una red.
- ​Como analista de seguridad, ​utilizará rastreadores de paquetes para inspeccionar los ​paquetes en busca de indicadores de riesgo.
- ​Mediante el sniffing de paquetes, podemos obtener una ​instantánea detallada de los paquetes que ​viajan por una red en forma de captura de paquetes.
- ​Una captura de paquetes, o P-cap, es un archivo ​que contiene paquetes de datos interceptados desde ​una interfaz o red.
- ​Es como interceptar un sobre en el correo.
- ​Las capturas de paquetes son increíblemente útiles ​durante la investigación de incidentes.
- ​Al tener acceso a las comunicaciones ​que se producen entre los dispositivos a través de una red, ​puede observar las interacciones de la red y empezar a crear ​una historia para determinar qué sucedió exactamente.

---

## Más información sobre la captura de paquetes
- La función de los analistas de seguridad consiste en supervisar y analizar los flujos de tráfico de la red.
- Una forma de hacerlo es generando capturas de paquetes y luego analizando el tráfico capturado para identificar actividad inusual en una red.

- Paquetes
   - La detección de intrusiones en la red comienza a nivel de paquetes.
   - Esto se debe a que los paquetes forman la base del intercambio de información a través de una red.
   - Cada vez que usted realiza una actividad en Internet -como visitar un sitio web- se envían y reciben paquetes entre su ordenador y el servidor del sitio web.
   - Estos paquetes son los que ayudan a transmitir información a través de una red.
   - Por ejemplo, al subir una imagen a un sitio web, los datos se dividen en varios paquetes, que luego se envían al destino previsto y se vuelven a ensamblar en el momento de la entrega.
   - En ciberseguridad, los paquetes proporcionan información valiosa que ayuda a contextualizar los sucesos durante las investigaciones.
   - Comprender la transferencia de información a través de paquetes no sólo le ayudará a desarrollar una visión de la actividad de la red, sino que también le ayudará a identificar anomalías y a defender mejor las redes de los ataques.
   - Los paquetes contienen tres componentes: la cabecera, la carga útil y el pie de página.
   
- Cabecera
   - Los paquetes comienzan con el componente más esencial: la cabecera.
   - Los paquetes pueden tener varias cabeceras en función de los protocolos utilizados, como una cabecera Ethernet, una cabecera IP, una cabecera TCP y más.
   - Las cabeceras proporcionan información que se utiliza para encaminar los paquetes a su destino.
   - Esto incluye información sobre las direcciones IP de origen y destino, la longitud del paquete, el protocolo, los números de identificación del paquete, etc. 
   - A continuación se muestra una cabecera IPv4 con la información que proporciona:

<img src="./resources/image-02.png" alt="Una cabecera IPv4 con sus trece campos" width="600"/>

- Carga útil
   - El componente de carga útil de sigue directamente a la cabecera y contiene los datos reales que se entregan.
   - Piensa en el ejemplo de subir una imagen a un sitio web; la carga útil de este paquete sería la propia imagen.

- Pie de página
   - El pie de página, también conocido como trailer, se encuentra al final del paquete.
   - El protocolo Ethernet utiliza los pies de página para proporcionar información de comprobación de errores para determinar si los datos se han corrompido.
   - Además, es posible que los paquetes de red Ethernet que se analizan no muestren información de pie de página debido a las configuraciones de red.
   - La mayoría de los protocolos, como el Protocolo de Internet (IP), no utilizan pies de página. 
   
- Analizadores de protocolos de red
   - Los analizadores de protocolos de red (packet sniffers) son herramientas diseñadas para capturar y analizar el tráfico de datos dentro de una red.
   - Algunos ejemplos de analizadores de protocolos de red son tcpdump, Wireshark y TShark.
   - Más allá de su uso en seguridad como herramienta de investigación utilizada para supervisar redes e identificar actividades sospechosas, los analizadores de protocolos de red pueden utilizarse para recopilar estadísticas de red, como el ancho de banda o la velocidad, y solucionar problemas de rendimiento de la red, como ralentizaciones.
   - Los analizadores de protocolos de red también pueden utilizarse con fines maliciosos.
   - Por ejemplo, los actores maliciosos pueden utilizar los analizadores de protocolos de red para capturar paquetes que contengan datos confidenciales, como la información de inicio de sesión de una cuenta.
   
- Funcionamiento de los analizadores de protocolos de red
   - Los analizadores de protocolos de red utilizan capacidades tanto de software como de hardware para capturar el tráfico de red y mostrarlo para que los analistas de seguridad puedan examinarlo y analizarlo.
      1. Los paquetes deben recogerse de la red a través de la tarjeta de interfaz de red (NIC), que es el hardware que conecta los ordenadores a una red, como un enrutador.
         - Las NIC reciben y transmiten tráfico de red, pero por defecto sólo escuchan el tráfico de red dirigido a ellas.
         - Para capturar todo el tráfico de red que se envía a través de la red, una NIC debe cambiarse a un modo que tenga acceso a todos los paquetes de datos de red visibles.
         - En las interfaces inalámbricas, esto suele denominarse modo de monitorización, y en otros sistemas puede llamarse modo promiscuo.
         - Este modo permite que la NIC tenga acceso a todos los paquetes de datos de red visibles, pero no ayudará a los analistas a acceder a todos los paquetes de una red.
         - Un analizador de protocolos de red debe situarse en un segmento de red adecuado para acceder a todo el tráfico entre distintos hosts.
      2. El analizador de protocolos de red recoge el tráfico de red en formato binario sin procesar.
         - El formato binario se compone de 0s y 1s y no es tan fácil de interpretar para los humanos.
         - El analizador de protocolos de red toma el formato binario y lo convierte para que se muestre en un formato legible para el ser humano, de modo que los analistas puedan leer y comprender fácilmente la información.
   - Activar promiscuo puede exponer su dispositivo a posibles ataques porque permite capturar información sensible como contraseñas y otros datos confidenciales.
   - Es importante utilizar las herramientas que funcionan en modo promiscuo de forma responsable y con precaución.

- Captura de paquetes
   - El sniffing de paquetes es la práctica de capturar e inspeccionar paquetes de datos a través de una red.
   - Una captura de paquetes (p-cap) es un archivo que contiene paquetes de datos interceptados desde una interfaz o red.
   - Las capturas de paquetes pueden visualizarse y analizarse posteriormente mediante analizadores de protocolos de red.
   - Por ejemplo, puede filtrar las capturas de paquetes para mostrar sólo la información más relevante para su investigación, como los paquetes enviados desde una dirección IP específica.
   - El uso de analizadores de protocolo de red para interceptar y examinar comunicaciones de red privadas sin permiso se considera ilegal en muchos lugares.
   - Los archivos P-cap pueden tener muchos formatos dependiendo de la biblioteca de captura de paquetes que se utilice.
   - Cada formato tiene diferentes usos y las herramientas de red pueden usar o soportar formatos específicos de archivos de captura de paquetes por defecto.
   - Deberías estar familiarizado con las siguientes librerías y formatos:
      - Libpcap es una librería de captura de paquetes diseñada para ser utilizada por sistemas tipo Unix, como Linux y MacOS®. Herramientas como tcpdump utilizan Libpcap como formato de archivo de captura de paquetes por defecto.
      - WinPcap es una librería de captura de paquetes de código abierto diseñada para dispositivos con sistemas operativos Windows. Se considera un formato de archivo antiguo y no se utiliza predominantemente.
      - Npcap es una biblioteca diseñada por la herramienta de escaneo de puertos Nmap que se utiliza habitualmente en sistemas operativos Windows.
      - PCAPng es un formato de archivo moderno que puede capturar paquetes y almacenar datos simultáneamente. Su capacidad para hacer ambas cosas explica la "ng", que significa "próxima generación"
   - Analizar tu red doméstica puede ser una buena forma de practicar el uso de estas herramientas.

- Recursos
   - [Packet Crafting](https://www.infosecinstitute.com/resources/hacking/packet-crafting-a-serious-crime/)