# El shell

## Introducción al shell
- ​El shell es el intérprete de la línea de comandos.
- ​Esto significa que le ayuda a comunicarse con el sistema operativo a través de ​la línea de comandos.
- ​El shell proporciona la interfaz de línea de comandos para que usted interactúe con el OS.
- ​Para decirle al OS lo que debe hacer, usted introduce comandos en esta interfaz.
- ​Un comando es una instrucción que le dice al ordenador que haga algo.
- El shell se comunica con el kernel para ejecutar estos comandos.
- ​Piense en él como un intérprete de lenguaje muy útil entre usted y su sistema.
- ​Como usted no habla lenguaje informático o binario, ​no puede comunicarse directamente con su sistema.
- ​Aquí es donde el shell entra para ayudarle.
- ​Su SO no necesita el shell para la mayor parte de su trabajo, pero ​es una interfaz entre usted y lo que su sistema puede ofrecerle.
- ​Le permite realizar operaciones matemáticas, ejecutar pruebas y ejecutar aplicaciones.
- ​Más importante aún, le permite combinar estas operaciones y ​conectar aplicaciones entre sí ​para realizar tareas complejas y automatizadas.

---

## Diferentes tipos de shells
- Saber trabajar con los shells de Linux es una habilidad importante para los profesionales de la ciberseguridad.
- Los shells se pueden utilizar para muchas tareas comunes.

- Comunicación a través de un shell
   - Como exploró anteriormente, el shell es el intérprete de la línea de comandos.
   - Puede pensar en un shell como un traductor entre usted y el sistema informático.
   - Las shell le permiten dar órdenes a la computadora y recibir respuestas de ella.
   - Cuando introduce una orden en un shell, éste ejecuta muchos procesos internos para interpretar su orden, enviarla al kernel y devolverle los resultados.

- Tipos de shell
   - Entre los diferentes tipos de shell de Linux se incluyen los siguientes:
      - Bourne-Again Shell (bash)
      - C Shell (csh)
      - Shell Korn (ksh)
      - Shell C mejorada (tcsh)
      - Shell Z (zsh)
- Todas las shell de Linux utilizan los comandos comunes de Linux, pero pueden diferir en otras características.
- Por ejemplo, ksh y Bash utilizan el signo del dólar ($) para indicar dónde teclea el usuario sus comandos.
- Otros shells, como zsh, utilizan el signo de porcentaje (%) para este propósito.

- Bash
   - Bash es el shell por defecto en la mayoría de las distribuciones de Linux.
   - Se considera un shell fácil de usar.
   - Puede utilizar Bash para los comandos básicos de Linux, así como para proyectos más grandes.
   - Bash es también el shell más popular en la profesión de la ciberseguridad.

---

## Entrada y salida en el shell
- Comunicarse con una computadora es ​como tener una conversación con un amigo.
- ​Una persona hace una pregunta ​y la otra responde con una respuesta.
- ​Si no sabe la respuesta, ​puede simplemente decir que no sabe la respuesta.
- ​Cuando se comunica con el shell, ​los comandos del shell pueden tomar entrada, ​dar salida o dar mensajes de error.
- ​Exploremos la entrada estándar, ​la salida estándar y los mensajes de error con más detalle.
- La entrada estándar (stdin) consiste en información ​recibida por el OS a través de la línea de comandos.
- ​Es como si le hiciera una pregunta a su amigo ​durante una conversación.
- ​La información se introduce desde su teclado al shell.
- ​Si el shell puede interpretar su petición, ​pide al kernel los recursos que ​necesita para ejecutar la tarea relacionada.
- Veamos esto a través de echo, ​un comando de Linux que da salida a una cadena de texto especificada.
- ​Datos de cadena son datos que consisten ​en una secuencia ordenada de caracteres.
- ​En nuestro ejemplo, sólo haremos que ​emita la cadena de texto: hola.
- ​Así que, como entrada, escribiremos: echo hola en el shell.
- Más tarde, cuando pulsemos intro, obtendremos la salida
- ​Pero antes de hacer eso, ​discutiremos primero el concepto de salida con más detalle.
- La salida estándar (stdout) es la información ​devolvida por el OS a través del shell.
- ​De la misma forma que su amigo ​le da una respuesta a su pregunta, ​la salida es la respuesta de una computadora a la orden que usted introduce.
- ​La salida es lo que usted recibe.
- ​Retomemos donde lo dejamos en nuestro ejemplo y enviemos ​la entrada de: echo hola al OS pulsando enter.
- ​Inmediatamente, la shell devuelve la salida de: hola.
- ​Por último, el error estándar (stderr) contiene ​mensajes de error devueltos por el OS a través del shell.
- ​Al igual que su amigo podría ​indicar que no puede responder a una pregunta, ​el sistema responde con ​un mensaje de error si no puede responder a su comando.
- ​A veces esto puede ocurrir cuando escribimos mal ​un comando o el sistema ​no conoce la respuesta al comando.
- Otras veces, puede ocurrir porque no tenemos ​los permisos adecuados para ejecutar una orden.
- ​Vamos a explorar otro ejemplo ​que demuestra el error estándar.
- ​Introduzcamos: eco hola en el shell.
- Note que intencionadamente he escrito mal eco como e-c-o.
- ​Cuando pulsamos intro, ​aparece un mensaje de error.
- ​Para terminar, hemos cubierto ​los aspectos básicos de la comunicación con el shell.
- ​La comunicación con el intérprete de comandos sólo puede realizarse de una de ​tres maneras: el sistema ​recibe un comando, esto es, una entrada; ​el sistema responde al comando y produce una salida; ​y, por último, el sistema no sabe cómo responder, ​lo que produce un error.