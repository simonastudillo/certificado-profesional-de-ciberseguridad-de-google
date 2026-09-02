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