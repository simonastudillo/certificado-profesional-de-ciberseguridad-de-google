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