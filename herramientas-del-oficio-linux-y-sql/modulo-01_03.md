# El sistema operativo en funcionamiento

## Dentro del sistema operativo
- Aprenderá lo que ocurre con ​un sistema operativo, o OS, ​cuando alguien utiliza una computadora para realizar una tarea.
- ​Piense en cuando alguien conduce un coche. ​Pisa el acelerador y el coche avanza.
- No necesita prestar atención a ​todos los mecanismos que permiten que el coche se mueva.
- ​Al igual que un coche no puede funcionar sin su motor, ​un ordenador no puede funcionar sin su sistema operativo.
- ​El trabajo de un OS es ayudar a que ​otros programas de ordenador funcionen de forma eficiente.
- ​El OS hace esto ocupándose de ​todos los detalles engorrosos relacionados con el control, ​del hardware de la computadora, para que usted no tenga que hacerlo.
- ​Cuando presiona el botón de encendido, ​está interactuando con el hardware.
- ​Esto arranca el ordenador e ​instala el sistema operativo.
- Arrancar el ordenador significa que ​se activa un microchip especial llamado BIOS.
- ​En muchos ordenadores fabricados después de 2007, ​el chip fue sustituido por la UEFI.
- ​Tanto la BIOS como la UEFI contienen instrucciones de arranque que son ​responsables de cargar un programa especial ​llamado cargador de arranque.
- ​A continuación, el cargador de arranque es ​responsable de iniciar el sistema operativo.
- ​Así de sencillo, su computadora está encendida.
- ​Como analista de seguridad, ​comprender estos procesos puede serle útil.
- ​Las vulnerabilidades pueden ocurrir en ​algo como un proceso de arranque.
- ​A menudo, la BIOS no es ​explorada por el software antivirus, ​por lo que puede ser vulnerable a la infección por software malicioso.
- Pasos de una tarea
   - El proceso comienza con usted, el usuario.
   - ​Y para completar tareas, usted utiliza aplicaciones en su computadora.
   - ​Una aplicación es un programa ​que realiza una tarea específica. 
   - Cuando usted hace esto, la aplicación ​envía su solicitud al sistema operativo.
   - ​Desde allí, el sistema operativo interpreta esta solicitud ​y la dirige al componente apropiado ​del hardware de la computadora.
   - ​El hardware también enviará ​información de vuelta al sistema operativo.
   - ​Y ésta, a su vez, se envía de vuelta a la aplicación. 
- Visión general de cómo funciona ​cuando desea utilizar la calculadora en su computadora.
   - ​Utiliza el ratón para hacer clic en ​la aplicación de calculadora de su ordenador.
   - ​Cuando escribe el número que desea calcular, ​la aplicación se comunica con el sistema operativo.
   - ​A continuación, su sistema operativo envía ​un cálculo a un componente del hardware, ​la unidad central de procesamiento o CPU.
   - ​Una vez que el hardware realiza el trabajo ​de determinar el número final, ​envía la respuesta de vuelta a su sistema operativo.
   - ​Entonces, puede mostrarse en su aplicación de calculadora.
- ​Comprender este proceso es ​útil a la hora de investigar eventos de seguridad.
- ​Los analistas de seguridad deben ser capaces de ​rastrear este flujo de procesos ​para analizar dónde podría haberse producido un evento de seguridad.

---

## Solicitudes al sistema operativo
- Los sistemas operativos son un componente fundamental de una computadora.
- Establecen conexiones entre las aplicaciones y el hardware para permitir a los usuarios realizar tareas.

- Iniciar la computadora
   - Cuando usted inicia, o enciende, su computadora, se activa un microchip BIOS o UEFI.
   - El Sistema básico de entrada/salida (BIOS) es un microchip que contiene instrucciones de carga para la computadora y que prevalece en los sistemas más antiguos.
   - La Interfaz de Firmware Extensible Unificada (UEFI ) es un microchip que contiene instrucciones de carga para la computadora y sustituye a la BIOS en los sistemas más modernos.
   - Tanto el chip BIOS como el UEFI realizan la misma función para iniciar la computadora.
   - BIOS fue el chip estándar hasta 2007, cuando aumentó el uso de los chips UEFI.
   - Ahora, la mayoría de las computadoras nuevas incluyen un chip UEFI.
   - UEFI proporciona características de Seguridad mejoradas.
   - Los microchips BIOS o UEFI contienen una gran variedad de instrucciones de carga para que las siga la computadora.
   - Por ejemplo, una de las instrucciones de carga es verificar la salud del hardware de la computadora.
   - La última instrucción FROM de la BIOS o la UEFI activa el Cargador de arranque.
   - El Cargador de arranque es un programa de software que inicia el sistema operativo.
   - Una vez que el sistema operativo ha terminado de iniciarse, su computadora está lista para ser utilizada.

- Finalización de una tarea
   - Los sistemas operativos nos ayudan a utilizar las computadoras de forma más eficiente.
   - Una vez que la computadora ha pasado por el proceso de arranque, completar una tarea en una computadora es un proceso de cuatro partes.

<img src="./resources/image-01.png" alt="Muestra un proceso que pasa del usuario a la aplicación, a los sistemas operativos y, por último, al hardware." width="700">

- Usuario
   - La primera parte del proceso es el usuario.
   - El usuario inicia el proceso teniendo algo que quiere realizar en la computadora.

- Aplicación
   - La aplicación es el programa de software con el que interactúan los usuarios para completar una tarea.
   - Por ejemplo, si quiere calcular algo, utilizaría la aplicación calculadora.
   - Si quiere escribir un informe, utilizaría una aplicación de tratamiento de textos.
   - Esta es la segunda parte del proceso.

- Sistema operativo
   - El sistema operativo recibe la solicitud del usuario desde la aplicación.
   - Es tarea del sistema operativo interpretar la solicitud y dirigir su flujo.
   - Para completar la tarea, el sistema operativo la envía a los componentes aplicables del hardware.

- Hardware
   - El hardware es donde se realiza todo el proceso para completar las tareas iniciadas por el usuario.
   - Por ejemplo, cuando un usuario quiere calcular un número, la CPU calcula la respuesta.
   - Como otro ejemplo, cuando un usuario quiere guardar un archivo, otro componente del hardware, el disco duro, se encarga de esta tarea.
   - Una vez que el hardware ha realizado el trabajo, devuelve el resultado a través del sistema operativo a la aplicación para que ésta pueda mostrar los resultados al usuario.

- El OS trabajando entre bastidores
   - Considere una vez más en qué se parece una computadora a un coche.
   - Hay procesos que alguien no observará directamente cuando maneja un coche, pero sí siente cómo avanza cuando pisa el acelerador.
   - Lo mismo ocurre con una computadora.
   - Dentro de una computadora ocurre un trabajo importante que usted no experimenta directamente.
   - Este trabajo implica al sistema operativo.
   - Puede explorar esto a través de otra analogía.
   - El proceso de utilización de un sistema operativo también es similar al de hacer un pedido en un restaurante.
   - En un restaurante usted hace un pedido y recibe su comida, pero no ve lo que ocurre en la cocina cuando los cocineros preparan la comida.
   - Pedir comida es similar a utilizar una aplicación en una computadora.
   - Cuando pide su comida, hace una petición específica como "una sopa pequeña, muy caliente"
   - Cuando utiliza una aplicación, también hace peticiones específicas como "imprima tres copias a doble cara de este documento".
   - Puede comparar la comida que recibe con lo que ocurre cuando el hardware envía la salida.
   - Usted recibe la comida que pidió.
   - Recibe el documento que quería imprimir.
   - Por último, la cocina es como el OS.
   - Usted no sabe lo que ocurre en la cocina, pero es fundamental para interpretar la solicitud y asegurarse de que usted recibe lo que pidió.
   - Del mismo modo, aunque el trabajo del OS no es directamente transparente para usted, es fundamental para completar sus tareas.

- Un ejemplo: Descargar un archivo desde un navegador de Internet
   - Anteriormente, exploró cómo los sistemas operativos, las aplicaciones y el hardware trabajan juntos examinando una tarea que implicaba un cálculo.
   - Puede ampliar esta comprensión explorando cómo el OS completa otra tarea, la descarga de un archivo desde un navegador de Internet:
      - En primer lugar, el usuario decide que quiere descargar un archivo que ha encontrado en Internet, por lo que hace clic en un botón de descarga situado cerca del archivo en la aplicación del navegador de Internet.
      - A continuación, el navegador de Internet comunica esta acción al OS.
      - El OS envía la solicitud de descarga del archivo al hardware adecuado para su proceso.
      - El hardware comienza a descargar el archivo y el OS envía esta información a la aplicación del navegador de Internet.
      - A continuación, el navegador de Internet informa al usuario de que el archivo se ha descargado.

---

## Práctica: Orden de las operaciones en el OS
- First, order the steps involved in booting a computer. Then, order the steps involved in saving a file

1. Step 1: The user powers on the computer.
2. Step 2: BIOS or UEFI loads the bootloader.
3. Step 3: The bootloader program loads the OS.

1. User opens a word processing application and types a document.
2. When the user saves the document, the application communicates with the OS
3. OS saves the file to a hardware component, called the hard drive.
4. Hard drive confirms file was saved, communicates this to OS. OS indicates this within the application

---

## Asignación de Recursos a través del OS
- ​No sólo el OS ​interactúa con otras partes de su computadora, ​sino que también es responsable de ​gestionar los recursos del sistema.
- ​Esta es una gran tarea que requiere mucho equilibrio para ​asegurarse de que todos los recursos de ​la computadora se utilizan de manera eficiente.
- ​Piense en esto como en el concepto de energía.
- ​Una persona necesita energía para completar diferentes tareas.
- ​Algunas tareas necesitan más energía, ​mientras que otras requieren menos. 
- Por ejemplo, salir a correr ​requiere más energía que ver la televisión.
- ​El OS de una computadora también necesita asegurarse de que ​tiene suficiente energía para ​funcionar correctamente en determinadas tareas.
- ​Ejecutar un antivirus en su computadora consumirá ​más energía que utilizar la aplicación de la calculadora.
- ​Imagínese que su computadora es una orquesta.
- ​Muchos instrumentos diferentes como violines, ​batería y trompetas forman parte de la orquesta.
- ​Una orquesta también tiene ​un director para dirigir el flujo de la música. 
- En una computadora, el OS es el director.
- ​El OS se encarga de la administración de los recursos y la memoria para garantizar ​que la capacidad limitada del ​sistema informático se utilice donde más se necesita.
- ​Una variedad de programas, tareas, ​y procesos compiten constantemente por ​los recursos de la unidad central de procesamiento, o CPU.
- ​Todos ellos tienen sus propias razones por las que necesitan memoria, ​almacenamiento y ancho de banda de entrada/salida.
- ​El OS se encarga de garantizar que ​cada programa asigne y desasigne recursos.
- ​Todo esto ocurre en su computadora al ​mismo tiempo para que su sistema funcione eficientemente.
- ​Mucho de esto está oculto para usted como usuario.
- ​Pero su gestor de tareas ​le mostrará una lista de todas ​las tareas que se están procesando, ​junto con su uso de memoria y CPU.
- ​Como analista, es útil saber ​dónde se utilizan los recursos de un sistema.
- ​Comprender el uso de los recursos puede ayudarle a responder ​a un incidente y a solucionar ​problemas de aplicaciones en el sistema.
- ​Por ejemplo, si una computadora funciona con lentitud, ​un analista podría descubrir ​que está asignando recursos a software malicioso.

---

## Tecnología de virtualización
- ¿Qué es una máquina virtual?
   - Una máquina virtual (VM ) es una versión virtual de una computadora física.
   - Las máquinas virtuales son un ejemplo de virtualización.
   - La virtualización es el proceso de utilizar software para crear representaciones virtuales de varias máquinas físicas.
   - El término "virtual" se refiere a máquinas que no existen físicamente, pero que funcionan como si lo hicieran porque su software simula el hardware físico.
   - Los sistemas virtuales no utilizan hardware físico dedicado.
   - En su lugar, utilizan versiones definidas por software del hardware físico.
   - Esto significa que una sola máquina virtual tiene una CPU virtual, almacenamiento virtual y otro hardware virtual.
   - Los sistemas virtuales son sólo código.
- Puede ejecutar varias máquinas virtuales utilizando el hardware físico de una sola computadora.
- Esto implica dividir los recursos de la computadora anfitriona para compartirlos entre todos los componentes físicos y virtuales.
- Por ejemplo, la Memoria de acceso aleatorio (RAM) es un componente de hardware utilizado para la memoria a corto plazo.
- Si una computadora tiene 16 GB de RAM, puede alojar tres máquinas virtuales de modo que la computadora física y las máquinas virtuales tengan cada una 4 GB de RAM.
- Además, cada una de estas máquinas virtuales tendría su propio sistema operativo y funcionaría de forma similar a una computadora típica.

- Beneficios de las máquinas virtuales
   - Los profesionales de la Seguridad utilizan habitualmente la virtualización y las máquinas virtuales.
   - La virtualización puede aumentar la Seguridad de muchas tareas y también puede aumentar la eficacia.
- Seguridad
   - Uno de los beneficios es que la virtualización puede proporcionar un entorno aislado, o un sandbox, en la máquina anfitriona física. 
   - Cuando una computadora tiene varias máquinas virtuales, estas máquinas virtuales son "invitados" de la computadora.
   - En concreto, están aisladas de la computadora host y de otras máquinas virtuales invitadas.
   - Esto proporciona una capa de Seguridad, ya que las máquinas virtuales pueden mantenerse separadas de los demás sistemas.
   - Por ejemplo, si una máquina virtual individual se infecta con software malicioso, puede tratarse de forma más segura porque está aislada de las demás máquinas.
   - Un profesional de la Seguridad también podría colocar intencionadamente software malicioso en una máquina virtual para examinarla en un entorno más seguro.
   - Aunque el uso de máquinas virtuales es útil cuando se investigan máquinas potencialmente infectadas o se ejecuta software malicioso en un entorno restringido, siguen existiendo algunos riesgos.
   - Por ejemplo, un programa malicioso puede escapar a la virtualización y acceder a la máquina anfitriona.
   - Esta es la razón por la que nunca debe confiar completamente en los sistemas virtualizados.
- Eficiencia
   - El uso de máquinas virtuales también puede ser una forma eficaz y cómoda de realizar tareas de Seguridad.
   - Puede abrir varias máquinas virtuales a la vez y cambiar fácilmente de una a otra.
   - Esto le permite agilizar las tareas de Seguridad, como probar y explorar varias aplicaciones.
   - Puede comparar la eficacia de una máquina virtual con la de un autobús urbano.
   - Un solo autobús urbano tiene mucho espacio y es una forma eficaz de transportar a muchas personas simultáneamente.
   - Si no existieran los autobuses urbanos, cada persona tendría que conducir su propio coche.
   - Esto consume más gasolina, coches y otros Recursos que montar en el autobús urbano.
   - Del mismo modo que muchas personas pueden viajar en un autobús, muchas máquinas virtuales pueden alojarse en la misma máquina física.
   - De esta forma, no se necesitan máquinas físicas separadas para realizar ciertas tareas.

- Gestionar máquinas virtuales
   - Las máquinas virtuales pueden gestionarse con un software denominado hipervisor.
   - Los hipervisores ayudan a los usuarios a gestionar varias máquinas virtuales y a conectar el hardware virtual y el físico.
   - Los hipervisores también ayudan a asignar los recursos compartidos de la máquina anfitriona física a una o más máquinas virtuales.
   - Un hipervisor con el que le resultará útil familiarizarse es la máquina virtual basada en kernel (KVM).
   - KVM es un hipervisor de código abierto compatible con la mayoría de las principales distribuciones de Linux.
   - Está integrado en el kernel de Linux, lo que significa que puede utilizarse para crear máquinas virtuales en cualquier máquina que ejecute un sistema operativo Linux sin necesidad de software adicional.
- Otras formas de virtualización
   - Además de las máquinas virtuales, existen otras formas de virtualización.
   - Algunas de estas tecnologías de virtualización no utilizan sistemas operativos.
   - Por ejemplo, se pueden crear varios servidores virtuales a partir de un único servidor físico. 
   - También pueden crearse redes virtuales para utilizar de forma más eficiente el hardware de una red física.