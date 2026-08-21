# Todo sobre Linux

## Bienvenido al Módulo 2
- ​Aprendió sobre ​sistemas operativos e interfaces de usuario.
- ​Aprendió cómo funcionan los sistemas operativos y ​cómo se asignan los recursos en las computadoras. 
- También revisamos varios sistemas operativos comunes.
- ​Es común escuchar que la gente es fanática de uno ​sobre otro, pero en el mundo de la Seguridad, ​Linux es de uso común.
- ​En esta sección, aprenderá más sobre ​el sistema operativo Linux y cómo ​se utiliza en las tareas cotidianas en materia de Seguridad.
- ​Primero, aprenderá sobre la arquitectura de Linux.
- ​Después de esto, compararemos ​las diferentes distribuciones de Linux que hay disponibles.
- ​Por último, explorará el shell, ​un componente clave de Linux que ​le permite comunicarse con el sistema.

---

## Introducción a Linux
-  ​Linux es un sistema operativo de código abierto.
- ​Se creó en dos partes.
- ​A principios de la década de 1990, dos personas diferentes trabajaban por separado en proyectos para ​mejorar la ingeniería informática.
- ​La primera persona fue Linus Torvalds.
- ​En aquel momento, el sistema operativo UNIX ya estaba en uso.
- ​Quería mejorarlo y hacerlo de código abierto y accesible para cualquiera.
- ​Lo revolucionario fue su introducción del kernel Linux.
- ​Por la misma época, Richard Stallman empezó a trabajar en GNU.
- ​GNU también era un sistema operativo basado en UNIX.
- ​Stallman compartía el objetivo de Torvalds de crear un software que fuera libre y ​abierto a cualquiera.
- ​Después de trabajar en GNU durante unos años, el elemento que le faltaba ​al software era un kernel.
- Juntas, las innovaciones de Torvalds y Stallman crearon lo que comúnmente se conoce ​como Linux.
- ​Ahora que ya conoce la historia de Linux, ​echemos un vistazo a lo que hace que Linux sea único.
- ​Como ya se ha mencionado, Linux es de código abierto, ​lo que significa que cualquiera puede tener acceso al sistema operativo y al código fuente.
- ​Linux y muchos de los programas que vienen con Linux están licenciados bajo los términos ​de la Licencia Pública GNU, que le permiten utilizarlos, compartirlos y modificarlos libremente.
- ​Gracias a la filosofía de código abierto de Linux, así como a un sólido conjunto de características, ​toda una comunidad de desarrolladores ha adoptado este sistema operativo.
- ​Estos desarrolladores pueden colaborar en proyectos y ​avanzar juntos en la informática.
- ​Como analista de seguridad, ​descubrirá que Linux se utiliza en diferentes organizaciones.
- ​Más concretamente, Linux se utiliza en muchos programas de seguridad.
- ​Otra Característica Única de Linux son las diferentes distribuciones, o ​variedades, que se han desarrollado.
- ​Como analista de seguridad, utilizará muchas herramientas y programas en el trabajo diario.
- ​Puede que examine diferentes tipos de registros para identificar qué está pasando en el sistema.
- ​Por ejemplo, ​puede que se encuentre mirando un registro de errores al investigar un problema.
- ​Otro lugar en el que utilizará Linux es para verificar el acceso y ​autorización en un sistema de Gestión de identidad y acceso.
- ​En seguridad, la gestión del acceso es clave para garantizar un sistema seguro.
- ​Por último, como analista, podría encontrarse trabajando ​con distribuciones específicas diseñadas para una tarea concreta.
- ​Por ejemplo, podría utilizar una distribución que tenga una herramienta forense digital ​para investigar lo ocurrido en una alerta de evento.
- ​También podría utilizar una distribución que sea para ​pruebas de penetración en seguridad ofensiva para buscar vulnerabilidades en el sistema.

---

## Phil: Aprender y crecer en el campo de la ciberseguridad
-  ​Cuando te adentras por primera vez en la ciberseguridad, ​es importante que no te sientas abrumado.
- ​Es un espacio muy grande.
- ​Y todos empezamos donde estás hoy. ​Y tuvimos que aprender a hacerlo.
- ​En un momento dado, no conocía Linux, ​no sabía programar.
- ​No conocía varias partes de otros sistemas operativos.
- ​Y tuve que aprender paso a paso ​cómo funcionaba todo eso y ​acumular gradualmente ese conocimiento con el tiempo.
- E incluso ahora todavía tengo que ​buscar cosas de vez en cuando porque ​no guardo todo en mi cabeza de ​una vez y eso está totalmente bien.
- ​Cuando te acercas a una nueva situación, ​siempre tendrás cierto grado de ansiedad ​por saber si vas ​a poder aprenderla con la suficiente rapidez.
- ​Y, en general, con suficiente experiencia, poco a ​poco te sientes cómodo de que lo harás.
- ​Pero, una vez más, es importante recordar que no es ​necesario que aprendas todo sobre todo de una sola vez.
- ​La mayoría de las veces aprendes lo suficiente como para ​ser lo suficientemente valioso en la parte inicial del proceso, y ​luego aprendes sobre la marcha.
- ​Empieza escribiendo unas líneas de ​código simple o mirando el ​código de otra persona e intentando ​entender lo que hace y luego cámbialo un ​poco y trabaja gradualmente en ello.
- ​Construya esa base de conocimiento ​que le dé la capacidad de aprender otras cosas, ​y creo que las cosas se derivarán de eso. 

---

## Arquitectura Linux
- ​Al igual que los edificios, los sistemas operativos también tienen ​una arquitectura y se componen de ​componentes discretos que trabajan juntos para formar un todo. 
- ​Los componentes de Linux incluyen el usuario, las aplicaciones, ​el shell, el Estándar de jerarquía del sistema de archivos, ​el kernel y el hardware.
- ​No se preocupe, analizaremos ​estos componentes uno por uno.
- ​En primer lugar, usted es el usuario.
   - ​El usuario es la persona que interactúa con la computadora.
   - ​En Linux, usted es el primer elemento ​de la arquitectura del sistema operativo.
   - ​Estás iniciando las tareas o ​los comandos que va a ejecutar el sistema operativo.
   - ​Linux es un sistema multiusuario.
   - Esto significa que más de un usuario puede ​usar los recursos del sistema al mismo tiempo.
- ​El segundo elemento de la arquitectura ​son las aplicaciones dentro de un sistema.
   - ​Una aplicación es un programa ​que realiza una tarea específica, ​como un procesador de textos o una calculadora.
   - ​Es posible que escuche que las palabras «aplicaciones» ​y «programas» se usan indistintamente.
   - ​Como ejemplo, ​una aplicación popular de Linux ​sobre la que aprenderemos más adelante es Nano.
   - ​Nano es un editor de texto. ​Esta sencilla aplicación ​te ayuda a mantener las notas en la pantalla.
   - Las aplicaciones de Linux se ​distribuyen normalmente a través de administradores de paquetes.
- ​El siguiente componente de la arquitectura ​de Linux es el shell.
   - ​Este es un elemento importante porque ​es la forma en que se comunicará con el sistema.
   - ​El shell es un intérprete de línea de comandos. ​Procesa los comandos y genera los resultados.
   - ​Puede que esto te suene familiar.
- ​Otro elemento de la arquitectura de ​Linux es el Estándar de jerarquía del sistema de archivos, ​o FHS.
   - Es ​el componente del sistema operativo Linux que organiza los datos.
   - ​Una manera fácil de pensar en ​el FHS es considerarlo como un archivador de datos.
   - ​El FHS es la forma en que se almacenan los datos en un sistema.
   - ​Es una forma de organizar los datos para poder ​encontrarlos cuando el sistema acceda a ellos.
- Esto nos lleva al kernel.
   - ​El kernel es un componente ​del sistema operativo Linux que administra los procesos y la memoria.
   - ​El kernel se comunica con el hardware ​para ejecutar los comandos enviados por el shell.
   - ​El kernel usa controladores para permitir que ​las aplicaciones ejecuten tareas.
   - ​El kernel de Linux ayuda a garantizar que el sistema ​asigna los recursos de manera más eficiente ​y hace que el sistema funcione más rápido.
- ​Por último, el último componente de ​la arquitectura es el hardware.
   - El ​hardware se refiere a los componentes físicos de una computadora.
   - ​Puede compararlo con las aplicaciones de software ​que se pueden descargar en un sistema.
   - ​El hardware de su computadora son cosas ​como la CPU, el mouse y el teclado.

---

## Explicación de la arquitectura de Linux
- Comprender la arquitectura de Linux es importante para un analista de seguridad.
- Cuando se comprende cómo está organizado un sistema, resulta más fácil entender cómo funciona.

- Usuario
   - El usuario es la persona que interactúa con una computadora.
   - Inicia y gestiona las tareas de la computadora.
   - Linux es un sistema multiusuario, lo que significa que varios usuarios pueden utilizar los mismos recursos al mismo tiempo.
- Aplicaciones
   - Una aplicación es un programa que realiza una tarea específica.
   - Algunas aplicaciones suelen venir preinstaladas en su computadora, como las calculadoras o los calendarios.
   - Otras aplicaciones pueden tener que ser instaladas, como algunos navegadores web o clientes de correo electrónico.
   - En Linux, a menudo utilizará un administrador de paquetes para instalar aplicaciones.
   - Un administrador de paquetes es una herramienta que ayuda a los usuarios a instalar, gestionar y eliminar paquetes o aplicaciones.
   - Un paquete es una pieza de software que puede combinarse con otros paquetes para formar una aplicación.
- Shell
   - El shell es el intérprete de la línea de comandos.
   - Todo lo que se introduce en el shell está basado en texto.
   - El shell permite a los usuarios dar comandos al kernel y recibir respuestas del mismo.
   - Puede pensar en el shell como un traductor entre usted y su computadora.
   - El shell traduce las órdenes que usted introduce para que la computadora pueda realizar las tareas que usted desea.
- Estándar de jerarquía del sistema de archivos (FHS)
   - El Estándar de jerarquía del sistema de archivos (FHS) es el componente del OS Linux que organiza los datos.
   - Especifica la ubicación donde se almacenan los Datos en el sistema operativo.
   - Un Directorio es un archivo que organiza dónde se almacenan otros archivos.
   - Los directorios se denominan a veces "carpetas", y pueden contener archivos u otros directorios.
   - El FHS define cómo se organizan los directorios, el contenido de los directorios y otros tipos de almacenamiento para que el sistema operativo sepa dónde encontrar datos específicos.
- Kernel
   - El kernel es el componente del OS Linux que gestiona los procesos y la memoria.
   - Se comunica con las aplicaciones para enrutar comandos.
   - El kernel Linux es único para el OS Linux y es crítico para asignar recursos en el sistema.
   - El kernel controla todas las funciones principales del hardware, lo que puede ayudar a agilizar las tareas de forma más eficiente.
- Hardware
   - El hardware son los componentes físicos de una computadora.
   - Es posible que esté familiarizado con algunos componentes de hardware, como los discos duros o las CPU.
   - El hardware se clasifica como periférico o interno.
- Dispositivos periféricos
   - Los dispositivos periféricos son componentes de hardware conectados y controlados por el sistema de la computadora.
   - No son componentes básicos necesarios para el funcionamiento del sistema informático.
   - Los dispositivos periféricos pueden añadirse o eliminarse libremente.
   - Algunos ejemplos de dispositivos periféricos son los monitores, las impresoras, el teclado y el ratón.
- Hardware interno
   - El hardware interno son los componentes necesarios para hacer funcionar la computadora.
   - El hardware interno incluye una placa de circuito principal y todos los componentes conectados a ella.
   - Esta placa de circuito principal también se denomina motherboard.
   - El hardware interno incluye lo siguiente:
      - La Unidad central de procesamiento (CPU)
         - Es el procesador principal de una computadora, que se utiliza para realizar tareas generales de computación en una computadora.
         - La CPU ejecuta las instrucciones proporcionadas por los programas, lo que permite que éstos se ejecuten.
      - Memoria de acceso aleatorio (RAM)
         - Es un componente de hardware utilizado para la memoria a corto plazo.
         - Es donde se almacenan temporalmente los Datos mientras usted realiza tareas en su computadora.
         - Por ejemplo, si está escribiendo un Informe en su computadora, los datos necesarios para ello se almacenan en la RAM.
         - Una vez que ha terminado de escribir el Informe y ha cerrado el Programa, estos datos se borran de la RAM.
         - No se puede acceder a la Información de la RAM una vez que se ha apagado la computadora.
         - La CPU toma los datos de la RAM para ejecutar programas.
      - El disco duro es un componente de hardware utilizado para la memoria a largo plazo.
         - Es donde se almacenan los programas y archivos para que la computadora pueda acceder a ellos más tarde.
         - Se puede acceder a la Información del disco duro incluso después de apagar y volver a encender la computadora.
         - Una computadora puede tener varios discos duros.

---

## Explore: Componentes del OS Linux
- User: The user decides to create a new file.
- Application: The user opens the application for communicating with the shell
- Shell: The user enters commands in the shell to indicate they want to create a new file.
- Filesystem Hierarchy Standard (FHS): The shell creates the new file in the FHS.
- Kernel: The contents and location of the new file are passed to the kernel.
- Hardware: The kernel tells the hardware how and where to save this new file.

---

## Ponga a prueba sus Conocimientos: Todo sobre Linux

1. Como analista de Seguridad, podría utilizar Linux para revisar los registros cuando investigue un Problema
- [x] Verdadero
- [ ] Falso
> Como analista de Seguridad, podría utilizar Linux para revisar los registros cuando investigue un Problema. Otra razón por la que podría utilizar Linux es para verificar el acceso y la autorización

2. ¿Cuáles de los siguientes son componentes de la arquitectura Linux? Seleccione todo lo que corresponda
- [x] El kernel
- [ ] El sistema operativo
- [x] Aplicaciones
- [x] El shell
> Los componentes de la arquitectura Linux incluyen las aplicaciones, el shell y el kernel. El usuario, el Estándar de jerarquía del sistema de archivos (FHS) y el hardware también son componentes de la arquitectura Linux.

3. Rellene el espacio en blanco: El Estándar de jerarquía del sistema de archivos (FHS) es el componente de la arquitectura Linux que _____.
- [ ] consiste en los componentes físicos de una computadora
- [ ] gestiona los procesos y la memoria
- [ ] permite a las personas comunicarse con el sistema
- [x] organiza los datos
> El Estándar de jerarquía del sistema de archivos (FHS) es el componente del OS Linux que organiza los datos.

4. ¿Cuáles de los siguientes componentes de hardware son dispositivos periféricos? Seleccione todos los que correspondan
- [ ] una CPU
- [x] una impresora
- [x] un monitor
- [ ] RAM
> Los monitores y las impresoras son dispositivos periféricos. Los dispositivos periféricos son componentes de hardware que están conectados y controlados por el sistema de la computadora. La CPU y la RAM son hardware interno. Hardware interno son los componentes necesarios para hacer funcionar la computadora.