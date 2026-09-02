# Inspección de paquetes

## Captura de paquetes con tcpdump
- ​Tcpdump es un popular analizador de redes.
- ​Está preinstalado en muchas distribuciones de Linux y puede ​instalarse en la mayoría de sistemas operativos tipo Unix, como macOS.
- ​Puede capturar y monitorizar fácilmente ​tráfico de redes como TCP, ​IP, ICMP y muchos más.
- ​Tcpdump es una herramienta de línea de comandos.
- ​Esto significa que no tiene ​una interfaz gráfica de usuario.
- ​Con tcpdump, puede aplicar ​opciones y flags a sus comandos para ​filtrar fácilmente el tráfico de red de modo que ​pueda encontrar exactamente lo que busca.
- ​Puede filtrar por una dirección IP específica, ​protocolo o número de puerto.
- ​Examinemos un sencillo comando tcpdump ​utilizado para capturar paquetes.
- ​Tenga en cuenta que el Tráfico de su computadora ​puede aparecer diferente cuando utilice este comando.
- ​A primera vista, esto parece mucha Información.
- ​Examinémoslo línea por línea.
- ​El comando que ejecutamos es: `sudo tcpdump -i any ​-v -c 1.`
- ​Usamos sudo porque la cuenta de Linux en la que hemos iniciado sesión ​no tiene permiso para ejecutar tcpdump.
- ​A continuación, especificamos tcpdump para iniciar tcpdump ​y -i para especificar en qué ​interfaz queremos olfatear el tráfico.
- ​La -v significa verbose, ​que muestra información detallada de los paquetes.
- ​La -c significa count, ​que especifica cuántos paquetes capturará tcpdump.
- ​Aquí hemos especificado uno.
- ​Ahora examinemos la salida.
- ​Tcpdump nos ha dicho que está escuchando en ​cualquier interfaz de red disponible, y también ​nos ha dado información adicional, como el tamaño de captura.
```bash
tcpdump: listening on any, link-type LINUX_SLL (Linux cooked v1), capture size 262144 bytes
```
- ​El primer Campo es la marca de tiempo del Paquete, ​que detalla el tiempo específico del viaje del paquete.
- ​Comienza con horas, minutos, ​segundos y fracciones de segundo.
- Las marcas de tiempo son especialmente útiles durante ​una investigación de incidentes cuando se quiere ​determinar líneas de tiempo y correlacionar el tráfico.
- ​A continuación, IP aparece como el campo de versión.
- ​Está listado como IP, ​lo que significa que es IPv4.
- ​La opción verbose nos ha dado ​más detalles sobre los campos de paquetes IP, ​como el tipo de protocolo y ​la longitud del paquete.
- ​El primer Campo, ToS significa Tipo de Servicio.
- ​Recordemos que esto nos indica si ​ciertos paquetes deben tratarse con diferente cuidado.
- ​Esto se representa mediante un valor en hexadecimal.
- ​El campo TTL es Tiempo de vida, ​que nos dice cuánto tiempo puede ​viajar un Paquete a través de una Red antes de que sea descartado.
- ​Los tres campos siguientes son ​Identificación, Offset y Banderas, ​que proporcionan tres campos con ​información relativa a la fragmentación.
- ​Estos campos proporcionan instrucciones sobre cómo ​ensamblar los paquetes en el orden correcto.
- ​Por ejemplo, el DF, ​junto a las banderas significa Don't Fragment.
- ​A continuación, el proto es el campo de protocolo
- Especifica el protocolo en uso y también ​nos proporciona el valor que ​corresponde al protocolo.
- ​Aquí el protocolo es tcp, ​que se representa con el número 6.
- ​El último campo, length, es la Longitud total del paquete, ​incluida la cabecera IP.
```bash
20:00:29.538395 IP (tos 0x10, ttl 64, id 32645, offset 0, flags [DF], proto TCP (6) length 196)
```
- ​A continuación, podemos observar ​las direcciones IP que se están comunicando entre sí.
- ​La dirección de la flecha ​indica la dirección del flujo de tráfico.
- ​El último trozo de la dirección IP ​indica el número o nombre del puerto.
- ​A continuación, el campo cksum o suma de comprobación corresponde a ​la suma de comprobación de encabezado, que almacena un valor que se ​utiliza para determinar si ​se ha producido algún error en el encabezado.
- ​Aquí nos está diciendo que es correcto sin errores.
- ​Los campos restantes están relacionados con TCP.
- ​Por ejemplo, Flags indica las banderas de TCP.
- ​La P es la bandera de empuje, y ​el punto indica que es una bandera ACK.
- ​Esto significa que el paquete está empujando datos.
- ​Éste es sólo uno de los muchos comandos que puede utilizar ​en tcpdump para capturar el Tráfico de red.
```bash
198.122.123.1.731843718:731843862, ack 2435699383, win 501, options [nop, nop, TS val 4106659748 ecr 2979487360], length 144
1 packet captured
21 packet received by filter
13 packets dropped by kernel
```

---

## Visión general de tcpdump
- Como analista de seguridad, utilizará analizadores de protocolos de red para ayudar a defenderse de cualquier intrusión en la red.
- Anteriormente, aprendió los siguientes términos relacionados con el Monitoreo y Análisis de redes:
   - Un analizador de protocolos de red (packet sniffer) es una herramienta diseñada para capturar y analizar el tráfico de datos dentro de una red.
   - El sniffing de paquetes es la práctica de capturar e inspeccionar paquetes de datos a través de una red.

- ¿Qué es tcpdump?
   - Tcpdump es un analizador de protocolos de red de línea de comandos.
   - Recordemos que una interfaz de línea de comandos (CLI ) es una interfaz de usuario basada en texto que utiliza comandos para interactuar con la computadora.
   - Tcpdump se utiliza para capturar el tráfico de red.
   - Este tráfico puede guardarse en una captura de paquetes (p-cap), que es un archivo que contiene paquetes de datos interceptados desde una interfaz o red.
   - Se puede acceder al archivo p-cap, analizarlo o compartirlo posteriormente.
   - Los analistas utilizan tcpdump por una gran variedad de razones, desde la solución de problemas de redes hasta la identificación de actividades maliciosas.
   - Tcpdump viene preinstalado en muchas distribuciones de Linux y también puede instalarse en otros sistemas operativos basados en Unix, como macOS®.
   - Es habitual que el tráfico de red esté encriptado, lo que significa que los datos están codificados y son ilegibles.
   - Inspeccionar los paquetes de red puede requerir desencriptar los datos utilizando las claves privadas adecuadas.

- Captura de paquetes con tcpdump
   - Anteriormente en este programa, usted aprendió que un usuario raíz de Linux (o superusuario) tiene privilegios elevados para modificar el sistema.
   - También aprendió que el comando sudo otorga temporalmente permisos elevados a usuarios específicos en Linux.
   - Como muchas otras herramientas de sniffing de paquetes, necesitará tener privilegios de administrador para capturar tráfico de redes utilizando tcpdump.
   - Esto significa que necesitará estar registrado como usuario raíz o tener la capacidad de utilizar el comando sudo.
   - He aquí un desglose de la sintaxis de tcpdump para capturar paquetes:
   - sudo tcpdump [-i interface] [option(s)] [expression(s)]
      - El comando sudo tcpdump inicia la ejecución de tcpdump utilizando permisos elevados como sudo.
      - El parámetro -i especifica la interfaz de red para capturar el tráfico de red.
         - Debe especificar una interfaz de red desde la que capturar para comenzar a capturar paquetes.
         - Por ejemplo, si especifica -i any olfateará el tráfico de todas las interfaces de red del sistema.
      - Los option(s) son opcionales y le ofrecen la posibilidad de alterar la ejecución del comando.
      - Los expression(s) son una forma de filtrar aún más los paquetes de tráfico de red para que pueda aislar el tráfico de red.
   - Antes de empezar a capturar el tráfico de red, debe identificar qué interfaz de red desea utilizar para capturar los paquetes.
   - Puede utilizar la bandera -D para listar las interfaces de red disponibles en un sistema.

- Opciones
   - Con tcpdump, puede aplicar opciones, también conocidas como banderas, al final de las órdenes para filtrar el tráfico de red.
   - Las opciones cortas se abrevian y se representan mediante un guión y un único carácter como -i.
   - Las opciones largas se deletrean utilizando un guión doble como --interface.
   - Tcpdump tiene más de cincuenta opciones que puede explorar utilizando [la página del manual](https://www.tcpdump.org/manpages/tcpdump.1.html).
   - Las opciones distinguen entre mayúsculas y minúsculas.
   - Por ejemplo, un -w en minúsculas es una opción independiente con un uso diferente que la opción con mayúsculas -W.
   - Las opciones de tcpdump que se escriben utilizando opciones cortas pueden escribirse con o sin un espacio entre la opción y su valor
   - Por ejemplo, sudo tcpdump -i any -c 3 y sudo tcpdump -iany -c3 son comandos equivalentes
   - Aquí, examinará un par de opciones esenciales de tcpdump incluyendo cómo escribir y leer archivos de captura de paquetes. 
   
- `-w`
   - Utilizando la bandera -w, puede escribir o guardar los paquetes de red olfateados en un archivo de captura de paquetes en lugar de simplemente imprimirlos en el terminal.
   - Esto es muy útil porque puede consultar este archivo guardado para su posterior análisis.
   - En este comando, tcpdump está capturando el tráfico de red de todas las interfaces de red y guardándolo en un archivo de captura de paquetes llamado packetcapture.pcap:
   - sudo tcpdump -i any -w packetcapture.pcap
- `-r`
   - Utilizando la bandera -r, puede leer un archivo de captura de paquetes especificando el nombre del archivo como parámetro.
   - He aquí un ejemplo de un comando tcpdump que lee un archivo llamado packetcapture.pcap:
   - sudo tcpdump -r packetcapture.pcap
- `-v`
   - Como ha aprendido, los paquetes contienen mucha información.
   - Por defecto, tcpdump no imprimirá toda la información de un Paquete.
   - Esta opción, que significa verborrea, le permite controlar cuánta información de los paquetes desea que imprima tcpdump.
   - Hay tres niveles de verbosidad que puede utilizar dependiendo de cuánta información de paquetes quiere que imprima tcpdump.
   - Los niveles son -v, -vv, y -vvv.
   - El nivel de verbosidad aumenta con cada v añadida.
   - La opción verbosa puede ser útil si está buscando información de paquetes como los detalles de los campos de cabecera IP de un paquete.
   - He aquí un ejemplo de un comando tcpdump que lee el archivo packetcapture.pcap con verbosidad:
   - sudo tcpdump -r packetcapture.pcap -v
- `-c`
   - La opción -c significa recuento.
   - Esta opción le permite controlar cuántos paquetes capturará tcpdump.
   - Por ejemplo, si especifica -c 1 sólo imprimirá un único paquete, mientras que -c 10 imprime 10 paquetes.
   - Este ejemplo le está diciendo a tcpdump que sólo capture los tres primeros paquetes que olfatea de la interfaz de red any:
   - sudo tcpdump -i any -c 3
- `-n`
   - Por defecto, tcpdump realizará la resolución de nombres.
   - Esto significa que tcpdump convierte automáticamente las direcciones IP en nombres.
   - También resolverá puertos a servicios comúnmente asociados que utilicen estos puertos.
   - Esto puede ser problemático porque tcpdump no siempre es preciso en la resolución de nombres.
   - Por ejemplo, tcpdump puede capturar Tráfico desde el puerto 80 y automáticamente traduce el puerto 80 a HTTP en la salida.
   - Sin embargo, esto es engañoso porque el puerto 80 no siempre va a estar utilizando HTTP; podría estar utilizando un protocolo diferente.
   - Además, la resolución de nombres utiliza lo que se conoce como una búsqueda DNS inversa.
   - Una búsqueda DNS inversa es una consulta que busca el nombre de dominio asociado a una dirección IP.
   - Si realiza una búsqueda DNS inversa en el sistema de un atacante, éste podría ser alertado de que lo está investigando a través de sus registros DNS.
   - El uso de la bandera -n desactiva esta asignación automática de números a nombres y se considera la mejor práctica a la hora de husmear o analizar el tráfico.
   - El uso de -n no resolverá nombres de host, mientras que -nn no resolverá ni nombres de host ni puertos.
   - He aquí un ejemplo de un comando tcpdump que lee el archivo packetcapture.pcap con verbosidad y desactiva la resolución de nombres:
   - sudo tcpdump -r packetcapture.pcap -v -n
- Puede combinar opciones entre sí.
- Por ejemplo, -v y -n pueden combinarse como -vn.
- Pero, si una opción acepta un parámetro justo después de ella como -c 1 o -r capture.pcap entonces no puede combinar otras opciones a ella.

- Expresividad
   - El uso de expresiones de filtrado en los comandos tcpdump también es opcional, pero saber cómo y cuándo utilizar expresiones de filtrado puede ser útil durante el análisis de paquetes.
   - Hay muchas formas de utilizar expresiones de filtrado.
   - Si desea buscar específicamente tráfico de red por protocolo, puede utilizar expresiones de filtrado para aislar paquetes de red.
   - Por ejemplo, puede filtrar para encontrar sólo tráfico IPv6 utilizando la expresión de filtrado ip6.
   - También puede utilizar operadores booleanos como and, or, o not para filtrar aún más el tráfico de red para direcciones IP, puertos y más específicos.
   - El ejemplo siguiente lee el archivo packetcapture.pcap y combina dos expresiones ip and port 80 utilizando el operador booleano and:
   - sudo tcpdump -r packetcapture.pcap -n 'ip and port 80'
   - Puede utilizar comillas simples o dobles para asegurarse de que tcpdump ejecuta todas las expresiones.
   - También puede utilizar paréntesis para agrupar y priorizar diferentes expresiones.
   - Agrupar expresiones es útil para comandos complejos o largos.
   - Por ejemplo, el comando ip and (port 80 or port 443) indica a tcpdump que priorice la ejecución de los filtros encerrados entre los paréntesis antes de filtrar para IPv4.

- Interpretar la salida
   - Una vez que ejecute un comando para capturar paquetes, tcpdump imprimirá la salida del comando como los paquetes olfateados.
   - En la salida, tcpdump imprime una línea de texto por cada paquete con cada línea comenzando con una marca de tiempo.
   - He aquí un ejemplo de un comando y la salida para un solo paquete TCP:
   - sudo tcpdump -i any -v -c 1
   - Este comando indica a tcpdump que capture paquetes en la interfaz de red -i any.
   - La opción -v imprime el paquete con información detallada y la opción -c 1 imprime sólo un paquete.
   - A continuación se muestra la salida de este Comando:

<img src="./resources/image-06.png" alt="Salida de un comando tcpdump con etiquetas para la marca de tiempo, IP de origen, puerto de origen, IP de destino y puerto de destino." width="600"/>

   - Timestamp: La salida comienza con la marca de tiempo, que empieza con horas, minutos, segundos y fracciones de segundo.
   - IP de origen: El origen del paquete lo proporciona su dirección IP de origen.
   - Puerto de origen: Este número de puerto es donde se originó el paquete.
   - IP de destino: La dirección IP de destino es hacia dónde se está transmitiendo el paquete.
   - Puerto de destino: Este número de puerto es hacia donde se está transmitiendo el paquete.
   - El resto de la salida contiene detalles de la conexión TCP, incluidas las banderas y el número de secuencia.
   - La información de options es información adicional del paquete que ha proporcionado la opción -v.

- Recursos
   - [Aprenda más con los tutoriales y guías de tcpdump, que incluye recursos educativos adicionales.](https://www.tcpdump.org/)
   - [Aprenda más sobre el uso de expresiones para filtrar el Tráfico con este tutorial de tcpdump por Daniel Miessler.](https://danielmiessler.com/p/tcpdump/)

---

## Actividad: Capture su primer Paquete
- Introducción
   - En esta actividad de laboratorio, capturará y analizará el tráfico de red en directo utilizando tcpdump.
   - Utilizará comandos de Linux en el shell Bash para completar estos pasos.

- Lo que hará
   - Identificar las interfaces de red disponibles
   - Utilizar tcpdump para capturar el tráfico de red en tiempo real
   - Guardar el tráfico de red en un archivo de captura de paquetes
   - Filtrar los datos de captura de paquetes

- Resumen de la actividad
   - Como analista de seguridad, es fundamental saber cómo capturar y filtrar tráfico de red en un entorno de Linux.
   - También debes saber los conceptos básicos relacionados con interfaces de red.
   - En este lab, realizarás tareas en las que debes usar tcpdump para capturar tráfico de red.
   - Capturarás los datos en un archivo de captura de paquetes (P-cap) y, luego, examinarás el contenido de los datos de paquetes capturados para centrarte en tipos específicos de tráfico.

- Situación
   - Trabajas como analista de redes y necesitas usar tcpdump para capturar y analizar tráfico de red en vivo desde una máquina virtual de Linux.
   - Cuando comiences el lab, verás que ya accediste a la terminal de Linux con tu cuenta de usuario, que se llama analyst.
   - El directorio principal (home) de tu usuario de Linux contiene un archivo de captura de paquetes de muestra que usarás al final del lab para responder unas preguntas sobre el tráfico de red que este contiene.
   - Estos son los pasos que seguirás: 
      1. Identificarás interfaces de red para capturar datos de paquetes de red.
      2. Usarás tcpdump para filtrar tráfico de red en vivo.
      3. Capturarás tráfico de red con tcpdump.
      4. Filtrarás los datos de paquetes capturados.

- Comienza el lab

1. Identifica interfaces de red

- En esta tarea, debes identificar qué interfaces de red se pueden usar para capturar datos de paquetes de red.
- Usa ifconfig para identificar las interfaces que estén disponibles:
```bash
sudo ifconfig
# Respuesta
# eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1460
#         inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
#         ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
#         RX packets 772  bytes 14039586 (13.3 MiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 393  bytes 36674 (35.8 KiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
#         inet 127.0.0.1  netmask 255.0.0.0
#         inet6 ::1  prefixlen 128  scopeid 0x10<host>
#         loop  txqueuelen 1000  (Local Loopback)
#         RX packets 67  bytes 9640 (9.4 KiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 67  bytes 9640 (9.4 KiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
- La interfaz de red de Ethernet se identifica mediante la entrada con el prefijo eth.
- Por lo tanto, en este lab, usarás eth0 como la interfaz de la que capturarás datos de paquetes de red en las tareas que siguen.
- Usa tcpdump para identificar las opciones de interfaz disponibles para la captura de paquetes:
```bash
sudo tcpdump -D
# Respuesta
# 1.eth0 [Up, Running, Connected]
# 2.any (Pseudo-device that captures on all interfaces) [Up, Running]
# 3.lo [Up, Running, Loopback]
# 4.bluetooth-monitor (Bluetooth Linux Monitor) [Wireless]
# 5.nflog (Linux netfilter log (NFLOG) interface) [none]
# 6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
# 7.dbus-system (D-Bus system bus) [none]
# 8.dbus-session (D-Bus session bus) [none]
```
- Este comando también te permitirá identificar qué interfaces de red están disponibles.
- Esto puede ser útil en sistemas que no incluyen el comando ifconfig.

2. Usa tcpdump para inspeccionar el tráfico de red de una interfaz de red

- En esta tarea, debes usar tcpdump para filtrar tráfico en vivo de paquetes de red en una interfaz.
- Usa tcpdump para filtrar datos en vivo de paquetes de red de la interfaz eth0:
```bash
sudo tcpdump -i eth0 -v -c5
# Respuesta
# tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
# 02:54:18.054166 IP (tos 0x0, ttl 64, id 4334, offset 0, flags [DF], proto TCP (6), length 121)
#     5c3d80dbbcbd.5000 > nginx-us-east1-b.c.qwiklabs-terminal-vms-prod-00.internal.40588: Flags [P.], cksum 0x599d (incorrect -> 0x7dc7), seq 4133190310:4133190379, ack 4028578038, win 499, options [nop,nop,TS val 791431414 ecr 2148810948], length 69
# 02:54:18.054516 IP (tos 0x0, ttl 63, id 36772, offset 0, flags [DF], proto TCP (6), length 52)
#     nginx-us-east1-b.c.qwiklabs-terminal-vms-prod-00.internal.40588 > 5c3d80dbbcbd.5000: Flags [.], cksum 0x95d0 (correct), ack 69, win 507, options [nop,nop,TS val 2148811031 ecr 791431414], length 0
# 02:54:18.082699 IP (tos 0x0, ttl 64, id 48295, offset 0, flags [DF], proto UDP (17), length 70)
#     5c3d80dbbcbd.37072 > metadata.google.internal.domain: 47924+ PTR? 12.1.18.172.in-addr.arpa. (42)
# 02:54:18.085395 IP (tos 0x0, ttl 64, id 4335, offset 0, flags [DF], proto TCP (6), length 140)
#     5c3d80dbbcbd.5000 > nginx-us-east1-b.c.qwiklabs-terminal-vms-prod-00.internal.40588: Flags [P.], cksum 0x59b0 (incorrect -> 0x719c), seq 69:157, ack 1, win 499, options [nop,nop,TS val 791431445 ecr 2148811031], length 88
# 02:54:18.085766 IP (tos 0x0, ttl 63, id 36773, offset 0, flags [DF], proto TCP (6), length 52)
#     nginx-us-east1-b.c.qwiklabs-terminal-vms-prod-00.internal.40588 > 5c3d80dbbcbd.5000: Flags [.], cksum 0x953a (correct), ack 157, win 507, options [nop,nop,TS val 2148811062 ecr 791431445], length 0
# 5 packets captured
# 10 packets received by filter
# 0 packets dropped by kernel
```
- Este comando ejecutará tcpdump con las siguientes opciones:
   - -i eth0: Captura datos de la interfaz eth0 específicamente.
   - -v: Muestra datos de un paquete en detalle.
   - -c5: Captura 5 paquetes de datos.
- Explora los detalles del paquete de red
   - En este ejemplo, identificarás algunas de las propiedades que tcpdump genera como resultado para los datos de captura de paquetes que vimos anteriormente.
   1. En los datos de muestra del comienzo de los resultados del paquete, tcpdump informó que escuchaba la interfaz eth0.
      - Además, proporcionó información sobre el tipo de vínculo y el tamaño de la captura en bytes:
      - `tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes`
   2. En la línea siguiente, el primer campo corresponde a la marca de tiempo del paquete, seguido del tipo de protocolo, que es IP:
      - `22:24:18.910372 IP `
   3. La opción que lista los detalles, -v, proporcionó más información sobre los campos del paquete IP, como el tipo de servicio; el TTL; la desviación; las marcas; el tipo de protocolo interno (en este caso, TCP (6)) y el tamaño del paquete IP externo en bytes:
      - `(tos 0x0, ttl 64, id 5802, offset 0, flags [DF], proto TCP (6), length 134)`
   4. En la sección siguiente, los datos muestran qué sistemas se comunican entre sí:
      - `7acb26dc1f44.5000 > nginx-us-east1-c.c.qwiklabs-terminal-vms-prod-00.internal.59788:`
      - De forma predeterminada, tcpdump convertirá las direcciones IP en nombres, como se muestra en la captura de pantalla.
      - El nombre de tu máquina virtual de Linux, que también se incluye en el símbolo del sistema, aparece aquí como el origen del primer paquete y el destino del segundo.
      - En tus datos en vivo, el nombre será un conjunto diferente de letras y números.
      - La flecha (>) indica la dirección del flujo de tráfico de este paquete.
      - Cada nombre de sistema incluye un sufijo con el número de puerto (.5000 en la captura de pantalla), que se usa para este paquete en los sistemas de origen y de destino.
   5. Los datos restantes filtran los datos del encabezado para el paquete TCP interno:
      - `Flags [P.], cksum 0x5851 (incorrect > 0x30d3), seq 1080713945:1080714027, ack 62760789, win 501, options [nop,nop,TS val 1017464119 ecr 3001513453], length 82`
      - El campo Flags identifica las marcas de TCP.
      - En este caso, la P representa la marca push, mientras que el punto indica que es una marca de ACK.
      - Esto significa que el paquete está enviando datos.
      - El campo siguiente es el valor de la suma de verificación de TCP.
      - Se usa para detectar errores en los datos.
      - Esta sección también incluye los números de secuencia y de confirmación de recepción, el tamaño de la ventana y el tamaño del paquete TCP interno en bytes.

3. Usa tcpdump para capturar tráfico de red

- En esta tarea, usarás tcpdump para guardar en un archivo de captura de paquetes los datos de tráfico de red capturados.
- En el comando anterior, usaste tcpdump para transmitir todo el tráfico de red.
- En este caso, usarás un filtro y otras opciones de configuración de tcpdump para guardar una pequeña muestra que contenga solo datos web del paquete de red (puerto TCP 80).
- Usa el siguiente código para capturar datos del paquete en un archivo llamado capture.pcap:
```bash
sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &
```
- Después de ejecutar este comando, presiona la tecla INTRO para recuperar el símbolo del sistema.
- Este comando ejecutará tcpdump en segundo plano con las siguientes opciones:
   - -i eth0: Captura datos de la interfaz eth0.
   - -nn: No intentes resolver direcciones IP o puertos con nombres.
      - Esta es una práctica recomendada de seguridad, ya que los datos de la búsqueda podrían no ser válidos.
      - También evita que se alerte a actores maliciosos de posibles investigaciones en curso.
   - -c9: Captura 9 paquetes de datos y luego sale.
   - port 80: Filtra solamente el tráfico del puerto 80. Este es el puerto HTTP predeterminado.
   - -w capture.pcap: Guarda los datos capturados en el archivo nombrado.
   - &: Esta es una instrucción para que la shell Bash ejecute el comando en segundo plano.
- Este comando se ejecuta en segundo plano, pero una parte del texto de resultado se mostrará en tu terminal.
- El texto no afectará los comandos cuando continúes con los pasos siguientes del lab.
- Usa curl para generar algo de tráfico HTTP (puerto 80):
```bash
curl opensource.google.com
```
- Cuando se usa el comando curl de esta forma (para abrir un sitio web), este genera algo de tráfico HTTP (puerto TCP 80) que puede capturarse.
- Verifica que capturaste datos del paquete:
```bash
ls -l capture.pcap
# -rw-r--r-- 1 tcpdump tcpdump 1411 Sep  2 03:04 capture.pcap
```
- La palabra "Done" del resultado indica que se capturó el paquete.

4. Filtra los datos de paquetes capturados

-  En esta tarea, utilizarás tcpdump para filtrar datos del archivo de captura de paquetes que guardaste previamente.
- Usa el comando tcpdump para filtrar datos del encabezado del paquete que se encuentren en el archivo de captura capture.pcap:
```bash
sudo tcpdump -nn -r capture.pcap -v
# Respuesta
# reading from file capture.pcap, link-type EN10MB (Ethernet), snapshot length 262144
# 03:04:28.241978 IP (tos 0x0, ttl 64, id 33995, offset 0, flags [DF], proto TCP (6), length 60)
#     172.17.0.2.46682 > 209.85.200.100.80: Flags [S], cksum 0x45fc (incorrect -> 0xad14), seq 3043633725, win 65320, options [mss 1420,sackOK,TS val 576232818 ecr 0,nop,wscale 7], length 0
# 03:04:28.244124 IP (tos 0x0, ttl 126, id 0, offset 0, flags [DF], proto TCP (6), length 60)
#     209.85.200.100.80 > 172.17.0.2.46682: Flags [S.], cksum 0xafe2 (correct), seq 313357220, ack 3043633726, win 65535, options [mss 1420,sackOK,TS val 3331632994 ecr 576232818,nop,wscale 8], length 0
# 03:04:28.244142 IP (tos 0x0, ttl 64, id 33996, offset 0, flags [DF], proto TCP (6), length 52)
#     172.17.0.2.46682 > 209.85.200.100.80: Flags [.], cksum 0x45f4 (incorrect -> 0xdc86), ack 1, win 511, options [nop,nop,TS val 576232820 ecr 3331632994], length 0
# 03:04:28.244224 IP (tos 0x0, ttl 64, id 33997, offset 0, flags [DF], proto TCP (6), length 137)
#     172.17.0.2.46682 > 209.85.200.100.80: Flags [P.], cksum 0x4649 (incorrect -> 0x4a3a), seq 1:86, ack 1, win 511, options [nop,nop,TS val 576232820 ecr 3331632994], length 85: HTTP, length: 85
#         GET / HTTP/1.1
#         Host: opensource.google.com
#         User-Agent: curl/7.74.0
#         Accept: */*

# 03:04:28.244398 IP (tos 0x0, ttl 126, id 0, offset 0, flags [DF], proto TCP (6), length 52)
#     209.85.200.100.80 > 172.17.0.2.46682: Flags [.], cksum 0xda14 (correct), ack 86, win 1051, options [nop,nop,TS val 3331632995 ecr 576232820], length 0
# 03:04:28.247194 IP (tos 0x0, ttl 126, id 0, offset 0, flags [DF], proto TCP (6), length 600)
#     209.85.200.100.80 > 172.17.0.2.46682: Flags [P.], cksum 0x742c (correct), seq 1:549, ack 86, win 1051, options [nop,nop,TS val 3331632998 ecr 576232820], length 548: HTTP, length: 548
#         HTTP/1.1 301 Moved Permanently
#         Location: https://opensource.google/
#         X-Content-Type-Options: nosniff
#         Server: sffe
#         Content-Length: 223
#         X-XSS-Protection: 0
#         Date: Wed, 02 Sep 2026 02:55:38 GMT
#         Expires: Wed, 02 Sep 2026 03:25:38 GMT
#         Cache-Control: public, max-age=1800
#         Content-Type: text/html; charset=UTF-8
#         Age: 530

#         <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
#         <TITLE>301 Moved</TITLE></HEAD><BODY>
#         <H1>301 Moved</H1>
#         The document has moved
#         <A HREF="https://opensource.google/">here</A>.
#         </BODY></HTML>
# 03:04:28.247208 IP (tos 0x0, ttl 64, id 33998, offset 0, flags [DF], proto TCP (6), length 52)
#     172.17.0.2.46682 > 209.85.200.100.80: Flags [.], cksum 0x45f4 (incorrect -> 0xda0a), ack 549, win 507, options [nop,nop,TS val 576232823 ecr 3331632998], length 0
# 03:04:28.247446 IP (tos 0x0, ttl 64, id 33999, offset 0, flags [DF], proto TCP (6), length 52)
#     172.17.0.2.46682 > 209.85.200.100.80: Flags [F.], cksum 0x45f4 (incorrect -> 0xda08), seq 86, ack 549, win 507, options [nop,nop,TS val 576232824 ecr 3331632998], length 0
# 03:04:28.247780 IP (tos 0x0, ttl 126, id 0, offset 0, flags [DF], proto TCP (6), length 52)
#     209.85.200.100.80 > 172.17.0.2.46682: Flags [F.], cksum 0xd7e7 (correct), seq 549, ack 87, win 1051, options [nop,nop,TS val 3331632998 ecr 576232824], length 0
```
- Este comando ejecutará tcpdump con las siguientes opciones:
   - -nn: Inhabilita la búsqueda de nombres de puerto y protocolos.
   - -r: Lee los datos capturados del archivo nombrado.
   - -v: Muestra datos de un paquete en detalle.
- Debes especificar el interruptor -nn nuevamente, ya que quieres asegurarte de que tcpdump no busque nombres de direcciones IP o puertos, ya que podría alertar a actores maliciosos.
- Se muestra un resultado similar al siguiente:
```bash
reading from file capture.pcap, link-type EN10MB (Ethernet)
20:53:27.669101 IP (tos 0x0, ttl 64, id 50874, offset 0, flags [DF], proto TCP (6), length 60)
    172.17.0.2:46498 > 146.75.38.132:80: Flags [S], cksum 0x5445 (incorrect), seq 4197622953, win 65320, options [mss 1420,sackOK,TS val 610940466 ecr 0, nop,wscale 7], length 0
20:53:27.669422 IP (tos 0x0, ttl 62, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    146.75.38.132:80: > 172.17.0.2:46498: Flags [S.], cksum 0xc272 (correct), seq 2026312556, ack 4197622953, win 65535, options [mss 1420,sackOK,TS val 155704241 ecr 610940466, nop,wscale 9], length 0
```
- Como en el ejemplo anterior, puedes ver la información del paquete IP junto con la relativa a los datos que contiene el paquete.
- Usa el comando tcpdump para filtrar los datos ampliados del paquete que se encuentren en el archivo de captura capture.pcap:
```bash
sudo tcpdump -nn -r capture.pcap -X
# Respuesta
reading from file capture.pcap, link-type EN10MB (Ethernet), snapshot length 262144
03:04:28.241978 IP 172.17.0.2.46682 > 209.85.200.100.80: Flags [S], seq 3043633725, win 65320, options [mss 1420,sackOK,TS val 576232818 ecr 0,nop,wscale 7], length 0
        0x0000:  4500 003c 84cb 4000 4006 7023 ac11 0002  E..<..@.@.p#....
        0x0010:  d155 c864 b65a 0050 b56a 2a3d 0000 0000  .U.d.Z.P.j*=....
        0x0020:  a002 ff28 45fc 0000 0204 058c 0402 080a  ...(E...........
        0x0030:  2258 9d72 0000 0000 0103 0307            "X.r........
03:04:28.244124 IP 209.85.200.100.80 > 172.17.0.2.46682: Flags [S.], seq 313357220, ack 3043633726, win 65535, options [mss 1420,sackOK,TS val 3331632994 ecr 576232818,nop,wscale 8], length 0
        0x0000:  4500 003c 0000 4000 7e06 b6ee d155 c864  E..<..@.~....U.d
        0x0010:  ac11 0002 0050 b65a 12ad 73a4 b56a 2a3e  .....P.Z..s..j*>
        0x0020:  a012 ffff afe2 0000 0204 058c 0402 080a  ................
        0x0030:  c694 af62 2258 9d72 0103 0308            ...b"X.r....
03:04:28.244142 IP 172.17.0.2.46682 > 209.85.200.100.80: Flags [.], ack 1, win 511, options [nop,nop,TS val 576232820 ecr 3331632994], length 0
        0x0000:  4500 0034 84cc 4000 4006 702a ac11 0002  E..4..@.@.p*....
        0x0010:  d155 c864 b65a 0050 b56a 2a3e 12ad 73a5  .U.d.Z.P.j*>..s.
        0x0020:  8010 01ff 45f4 0000 0101 080a 2258 9d74  ....E......."X.t
        0x0030:  c694 af62                                ...b
03:04:28.244224 IP 172.17.0.2.46682 > 209.85.200.100.80: Flags [P.], seq 1:86, ack 1, win 511, options [nop,nop,TS val 576232820 ecr 3331632994], length 85: HTTP: GET / HTTP/1.1
        0x0000:  4500 0089 84cd 4000 4006 6fd4 ac11 0002  E.....@.@.o.....
        0x0010:  d155 c864 b65a 0050 b56a 2a3e 12ad 73a5  .U.d.Z.P.j*>..s.
        0x0020:  8018 01ff 4649 0000 0101 080a 2258 9d74  ....FI......"X.t
        0x0030:  c694 af62 4745 5420 2f20 4854 5450 2f31  ...bGET./.HTTP/1
        0x0040:  2e31 0d0a 486f 7374 3a20 6f70 656e 736f  .1..Host:.openso
        0x0050:  7572 6365 2e67 6f6f 676c 652e 636f 6d0d  urce.google.com.
        0x0060:  0a55 7365 722d 4167 656e 743a 2063 7572  .User-Agent:.cur
        0x0070:  6c2f 372e 3734 2e30 0d0a 4163 6365 7074  l/7.74.0..Accept
        0x0080:  3a20 2a2f 2a0d 0a0d 0a                   :.*/*....
03:04:28.244398 IP 209.85.200.100.80 > 172.17.0.2.46682: Flags [.], ack 86, win 1051, options [nop,nop,TS val 3331632995 ecr 576232820], length 0
        0x0000:  4500 0034 0000 4000 7e06 b6f6 d155 c864  E..4..@.~....U.d
        0x0010:  ac11 0002 0050 b65a 12ad 73a5 b56a 2a93  .....P.Z..s..j*.
        0x0020:  8010 041b da14 0000 0101 080a c694 af63  ...............c
        0x0030:  2258 9d74                                "X.t
03:04:28.247194 IP 209.85.200.100.80 > 172.17.0.2.46682: Flags [P.], seq 1:549, ack 86, win 1051, options [nop,nop,TS val 3331632998 ecr 576232820], length 548: HTTP: HTTP/1.1 301 Moved Permanently
        0x0000:  4500 0258 0000 4000 7e06 b4d2 d155 c864  E..X..@.~....U.d
        0x0010:  ac11 0002 0050 b65a 12ad 73a5 b56a 2a93  .....P.Z..s..j*.
        0x0020:  8018 041b 742c 0000 0101 080a c694 af66  ....t,.........f
        0x0030:  2258 9d74 4854 5450 2f31 2e31 2033 3031  "X.tHTTP/1.1.301
        0x0040:  204d 6f76 6564 2050 6572 6d61 6e65 6e74  .Moved.Permanent
        0x0050:  6c79 0d0a 4c6f 6361 7469 6f6e 3a20 6874  ly..Location:.ht
        0x0060:  7470 733a 2f2f 6f70 656e 736f 7572 6365  tps://opensource
        0x0070:  2e67 6f6f 676c 652f 0d0a 582d 436f 6e74  .google/..X-Cont
        0x0080:  656e 742d 5479 7065 2d4f 7074 696f 6e73  ent-Type-Options
        0x0090:  3a20 6e6f 736e 6966 660d 0a53 6572 7665  :.nosniff..Serve
        0x00a0:  723a 2073 6666 650d 0a43 6f6e 7465 6e74  r:.sffe..Content
        0x00b0:  2d4c 656e 6774 683a 2032 3233 0d0a 582d  -Length:.223..X-
        0x00c0:  5853 532d 5072 6f74 6563 7469 6f6e 3a20  XSS-Protection:.
        0x00d0:  300d 0a44 6174 653a 2057 6564 2c20 3032  0..Date:.Wed,.02
        0x00e0:  2053 6570 2032 3032 3620 3032 3a35 353a  .Sep.2026.02:55:
        0x00f0:  3338 2047 4d54 0d0a 4578 7069 7265 733a  38.GMT..Expires:
        0x0100:  2057 6564 2c20 3032 2053 6570 2032 3032  .Wed,.02.Sep.202
        0x0110:  3620 3033 3a32 353a 3338 2047 4d54 0d0a  6.03:25:38.GMT..
        0x0120:  4361 6368 652d 436f 6e74 726f 6c3a 2070  Cache-Control:.p
        0x0130:  7562 6c69 632c 206d 6178 2d61 6765 3d31  ublic,.max-age=1
        0x0140:  3830 300d 0a43 6f6e 7465 6e74 2d54 7970  800..Content-Typ
        0x0150:  653a 2074 6578 742f 6874 6d6c 3b20 6368  e:.text/html;.ch
        0x0160:  6172 7365 743d 5554 462d 380d 0a41 6765  arset=UTF-8..Age
        0x0170:  3a20 3533 300d 0a0d 0a3c 4854 4d4c 3e3c  :.530....<HTML><
        0x0180:  4845 4144 3e3c 6d65 7461 2068 7474 702d  HEAD><meta.http-
        0x0190:  6571 7569 763d 2263 6f6e 7465 6e74 2d74  equiv="content-t
        0x01a0:  7970 6522 2063 6f6e 7465 6e74 3d22 7465  ype".content="te
        0x01b0:  7874 2f68 746d 6c3b 6368 6172 7365 743d  xt/html;charset=
        0x01c0:  7574 662d 3822 3e0a 3c54 4954 4c45 3e33  utf-8">.<TITLE>3
        0x01d0:  3031 204d 6f76 6564 3c2f 5449 544c 453e  01.Moved</TITLE>
        0x01e0:  3c2f 4845 4144 3e3c 424f 4459 3e0a 3c48  </HEAD><BODY>.<H
        0x01f0:  313e 3330 3120 4d6f 7665 643c 2f48 313e  1>301.Moved</H1>
        0x0200:  0a54 6865 2064 6f63 756d 656e 7420 6861  .The.document.ha
        0x0210:  7320 6d6f 7665 640a 3c41 2048 5245 463d  s.moved.<A.HREF=
        0x0220:  2268 7474 7073 3a2f 2f6f 7065 6e73 6f75  "https://opensou
        0x0230:  7263 652e 676f 6f67 6c65 2f22 3e68 6572  rce.google/">her
        0x0240:  653c 2f41 3e2e 0d0a 3c2f 424f 4459 3e3c  e</A>...</BODY><
        0x0250:  2f48 544d 4c3e 0d0a                      /HTML>..
03:04:28.247208 IP 172.17.0.2.46682 > 209.85.200.100.80: Flags [.], ack 549, win 507, options [nop,nop,TS val 576232823 ecr 3331632998], length 0
        0x0000:  4500 0034 84ce 4000 4006 7028 ac11 0002  E..4..@.@.p(....
        0x0010:  d155 c864 b65a 0050 b56a 2a93 12ad 75c9  .U.d.Z.P.j*...u.
        0x0020:  8010 01fb 45f4 0000 0101 080a 2258 9d77  ....E......."X.w
        0x0030:  c694 af66                                ...f
03:04:28.247446 IP 172.17.0.2.46682 > 209.85.200.100.80: Flags [F.], seq 86, ack 549, win 507, options [nop,nop,TS val 576232824 ecr 3331632998], length 0
        0x0000:  4500 0034 84cf 4000 4006 7027 ac11 0002  E..4..@.@.p'....
        0x0010:  d155 c864 b65a 0050 b56a 2a93 12ad 75c9  .U.d.Z.P.j*...u.
        0x0020:  8011 01fb 45f4 0000 0101 080a 2258 9d78  ....E......."X.x
        0x0030:  c694 af66                                ...f
03:04:28.247780 IP 209.85.200.100.80 > 172.17.0.2.46682: Flags [F.], seq 549, ack 87, win 1051, options [nop,nop,TS val 3331632998 ecr 576232824], length 0
        0x0000:  4500 0034 0000 4000 7e06 b6f6 d155 c864  E..4..@.~....U.d
        0x0010:  ac11 0002 0050 b65a 12ad 75c9 b56a 2a94  .....P.Z..u..j*.
        0x0020:  8011 041b d7e7 0000 0101 080a c694 af66  ...............f
        0x0030:  2258 9d78                                "X.x
```
- Este comando ejecutará tcpdump con las siguientes opciones:
   - -nn: Inhabilita la búsqueda de nombres de puerto y protocolos.
   - -r: Lee los datos capturados del archivo nombrado.
   - -X: Muestra los datos del paquete como resultados en formato ASCII y hexadecimal.
      - Los analistas de seguridad pueden analizar los resultados hexadecimales y ASCII para detectar patrones o anomalías durante un análisis forense o de software malicioso.
- El sistema hexadecimal, también conocido como hex o de base 16, utiliza 16 símbolos para representar valores, incluyendo los dígitos del 0 al 9 y las letras A, B, C, D, E y F.
- El American Standard Code for Information Interchange (ASCII) es un estándar de codificación de caracteres que utiliza un conjunto de caracteres para representar texto en forma digital.

- ¿Qué comando usarías para capturar 3 paquetes en cualquier interfaz con la opción detallada?
   - [ ] sudo tcpdump -n3 -i any -v
   - [ ] sudo tcpdump -N2 -i any -v
   - [ ] sudo tcpdump -s3 -i all -v
   - [x] sudo tcpdump -c3 -i any -v

- ¿Qué indica la opción -i?
   - [ ] La cantidad de paquetes para capturar
   - [ ] Capturar solo paquetes entrantes
   - [x] La interfaz de red para monitorear
   - [ ] Modo monitor incremental

- ¿Qué tipo de información incluye la opción -v?
   - [ ] Paquetes que incluyen la letra 'V'
   - [ ] Información de la versión
   - [x] Información detallada
   - [ ] Paquetes virtuales

- ¿Qué comando tcpdump puedes usar para identificar las interfaces disponibles en las que se puede realizar una captura de paquetes?
   - [ ] sudo capture p.cap
   - [x] sudo tcpdump -D
   - [ ] sudo ls
   - [ ] sudo tcpdump

---

## Ejemplar opcional: Capture su primer Paquete
- Mismo laboratorio que el anterior.

---

## Ejemplar: Capture su primer Paquete
- Se explica lo mismo que en el laboratorio anterior.
- Conclusión
   - identificar interfaces de red,
   - utilizar el comandotcpdump para capturar datos de red para su inspección,
   - interpretar la información quetcpdump proporciona sobre un paquete, y
   - guardar y cargar datos de paquetes para su posterior análisis.

---

## Ponga a prueba sus Conocimientos: Inspección de paquetes

1. ¿Qué opción de tcpdump se utiliza para especificar la interfaz de red?
- [ ] -v
- [x] -i
- [ ] -c
- [ ] -n
> La opción -i se utiliza para especificar la interfaz de red; -i significa interfaz.

2. ¿Qué se necesita para acceder al analizador de protocolos de red tcpdump?
- [ ] Captura de paquetes
- [x] Interfaz de línea de comandos
- [ ] Interfaz gráfica de usuario
- [ ] Salida
> tcpdump es un analizador de protocolos de red al que se accede a través de una interfaz de línea de comandos (CLI).

3. ¿Cuál es el primer campo que se encuentra en la salida de un comando tcpdump?
- [ ] Versión
- [ ] IP de origen
- [ ] Protocolo
- [x] Marca de tiempo
> El primer campo que se encuentra en la salida de un comando tcpdump es la marca de tiempo del paquete.

4. Está utilizando tcpdump para capturar el tráfico de red en su computadora local. Le gustaría guardar el tráfico de red en un archivo de captura de paquetes para su posterior análisis. ¿Qué opción de tcpdump debería utilizar?
- [ ] -r
- [x] -w
- [ ] -v
- [ ] -c
> Debe utilizar la opción -w. La opción -w le permite guardar los paquetes de red en un archivo de captura de paquetes para su posterior análisis.