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

---

## Actividad: Examinar la entrada y salida en el shell
- Introducción
   - En este laboratorio, utilizará el comando echo para examinar cómo se recibe la entrada y cómo se devuelve la salida en el shell.
   - También utilizará otros comandos de Linux en el shell Bash para explorar más sobre la entrada y la salida y otras funciones básicas del shell.

- Lo que hará
   - Generar salida en el shell el comando echo 
   - Realizar cálculos básicos el comando expr 
   - Limpiar la ventana del shell el comando clear 
   - Explorar más a fondo los comandos

- Resumen de la actividad
   - Anteriormente, vimos cómo la shell Bash sirve para comunicarse con el sistema operativo de una computadora.
   - Cuando te comunicas mediante la shell, los comandos de esta reciben las entradas de comandos y muestran resultados o mensajes de error.
   - En esta actividad de lab, usarás el comando echo para examinar cómo se reciben las entradas y se transforman en resultados en la shell.
   - Luego, usarás el comando expr para explorar aún más las entradas y resultados mientras realizas algunos cálculos básicos en la shell.
   - En esta actividad, sentaremos las bases para comprender cómo comunicarse con el sistema operativo Linux mediante la shell.
   - Como analista de seguridad, deberás poder ingresar comandos en la shell y reconocer cuándo se generan resultados o un mensaje de error.

- Situación
   - Como profesional de la seguridad, es importante comprender el concepto de comunicación con tu computadora mediante la shell.
   - En este contexto, ingresarás una cadena de texto específica que quieras que la shell genere como resultado.
   - También deberás ingresar algunos cálculos matemáticos, de modo que el SO (sistema operativo) pueda generar el resultado.
   - Estos son los pasos que seguirás:
      1. Usarás el comando echo para generar algunos resultados en la shell.
      2. Usarás el comando expr para realizar algunos cálculos matemáticos básicos.
      3. Usarás el comando clear para despejar la ventana de la shell Bash.
      4. Explorarás los comandos echo y expr en mayor profundidad.

- Comienza el lab

1. Genera resultados con el comando echo
- Ejecutamos el comando echo hello
   - echo hello es la entrada (stdin) que le damos al sistema operativo.
   - hello es la salida (stdout) que el sistema operativo nos devuelve.
- Ejecutamos el comando echo "<name>" donde <name> es tu nombre.
   - echo "<name>" es la entrada (stdin) que le damos al sistema operativo.
   - <name> es la salida (stdout) que el sistema operativo nos devuelve.
- Con echo podemos usar comillas dobles o simples para generar resultados.

2. Genera resultados con el comando expr
- Ejecutamos el comando expr 32 - 8
   - expr 32 - 8 es la entrada (stdin) que le damos al sistema operativo.
   - 24 es la salida (stdout) que el sistema operativo nos devuelve.
   - expr es la aplicación que realiza la operación matemática en la shell.
- Ejecutamos el comando expr 3500 * 12
   - expr 3500 * 12 es la entrada (stdin) que le damos al sistema operativo.
   - 42000 es la salida (stdout) que el sistema operativo nos devuelve.
- El comando expr requiere que los términos y operadores de una expresión matemática estén separados por espacios.

3. Despeja la shell Bash
- Ejecutaremos el comando clear para despejar la ventana de la shell Bash.
   - clear es la entrada (stdin) que le damos al sistema operativo.
   - La salida (stdout) que el sistema operativo nos devuelve es una ventana de shell limpia.

4. Tarea opcional: Realiza más cálculos con el comando expr
- Ejecuta el comando expr 100 / 4
   - expr 100 / 4 es la entrada (stdin) que le damos al sistema operativo.
   - 25 es la salida (stdout) que el sistema operativo nos devuelve.

- Listado de comandos utilizados en este laboratorio
```bash
# Comando echo
echo hello
echo "hello"
echo "simon"

# Comando expr
expr 32 - 8
expr 3500 * 12

# comando clear
clear

# comandos opcionales
expr 100 / 4
```