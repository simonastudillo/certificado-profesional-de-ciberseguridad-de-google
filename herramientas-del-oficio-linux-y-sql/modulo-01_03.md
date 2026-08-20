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