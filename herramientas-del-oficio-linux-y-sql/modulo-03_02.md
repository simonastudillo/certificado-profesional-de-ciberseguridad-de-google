# Gestionar el contenido de los archivos en Bash

## Encuentre lo que necesita con Linux
- ​​Como analista de seguridad, ​su trabajo probablemente implique ​filtrar en busca de la información que necesita.
- ​Filtrado significa buscar en su sistema ​información específica que pueda ​ayudarle a resolver problemas complejos.
- ​Por ejemplo, imagine que su Equipo ​determina que una pieza de ​software malicioso contiene una cadena de caracteres.
- ​Podría tener la tarea de encontrar otros archivos con ​la misma cadena para determinar si ​esos archivos contienen el mismo software malicioso.
- ​Más adelante, aprenderemos más sobre cómo ​puede utilizar SQL para filtrar una Base de datos, ​pero Linux es un buen lugar para empezar con el filtrado básico.
- ​Primero, empezaremos con grep.
   - El comando grep busca en un archivo especificado y ​devuelve todas las líneas en ​el archivo que contengan una cadena especificada.
   - ​Aquí hay un ejemplo de esto.
   - ​Digamos que tenemos un archivo llamado updates.txt, ​y actualmente estamos buscando líneas que ​contengan la palabra: OS.
   - ​Si el archivo es grande, ​nos llevaría mucho tiempo escanearlo visualmente.
   - ​En su lugar, después de navegar hasta ​el directorio que contiene updates.txt, ​escribiremos el comando: ​grep OS updates.txt en el shell.
   - ​Note cómo el comando grep va seguido de dos argumentos.
   - ​El primer argumento es la cadena que estamos buscando; ​en este caso, OS.
   - ​El segundo argumento es el nombre del archivo ​que estamos buscando, updates.txt.
   - ​Cuando pulsamos intro, ​Bash nos devuelve todas las líneas que contienen la palabra OS.
- Ahora hablemos de piping.
   - ​Piping es un comando de Linux que ​puede utilizarse para una gran variedad de propósitos.
   - ​En un momento, nos centraremos en ​cómo puede utilizarse para el filtrado.
   - ​Pero primero, hablemos de la idea general de piping.
   - El comando piping envía una salida estándar de ​un comando como entrada estándar ​a otro comando para su posterior procesamiento.
   - ​Se representa mediante el carácter de barra vertical.
   - ​En nuestro Contexto, ​podemos referirnos a esto como el carácter de tubería.
   - ​Tómese un momento e imagine una tubería física.
   - ​Las tuberías físicas tienen dos extremos.
   - ​En un extremo, por ejemplo, ​el agua puede entrar en la tubería desde un depósito de agua caliente.
   - ​Luego, viaja a través de la tubería y ​sale por el otro extremo en un fregadero.
   - ​De forma similar, en Linux, ​la tubería también implica redirección.
   - ​La salida de un comando se envía a través ​de la tubería y luego se utiliza en el otro lado de la tubería.
- ​Grep también se puede incorporar después de una tubería.
   - ​El primer comando, ls, ​indica al sistema operativo que muestre el contenido del archivo ​y directorio de su subdirectorio de informes.
   - ​Pero como el comando va seguido de la tubería, ​la salida no se devuelve a la pantalla.
   - ​En su lugar, se envía al siguiente comando.
   - ​Como acabamos de aprender, ​grep busca una cadena de caracteres especificada; ​en este caso, son los usuarios.
   - ​¿Pero dónde busca?
   - ​Dado que grep sigue una tubería, ​la salida del comando anterior ​indica dónde buscar.
   - ​En este caso, esa salida es una lista de ​archivos y directorios dentro del subdirectorio reports.
   - ​Devolverá todos los archivos y ​directorios que contengan la palabra: users.
- ​Exploremos esto en Bash.
   - ​Para que podamos entender mejor cómo funciona el filtro, ​primero saquemos todo lo que hay en el directorio reports.
   - ​Si ya estuviéramos en el directorio, ​sólo tendríamos que introducir ls.
   - ​Pero como no lo estamos, también ​especificaremos la ruta a este directorio.
   - ​Cuando pulsemos intro, ​la salida indica que hay ​siete archivos en el directorio de informes.
   - ​Como queremos devolver ​sólo los archivos que contengan la palabra usuarios, ​combinaremos este comando ls ​con piping y el comando grep. 
   - Como demuestra la salida, ​Linux ha recibido instrucciones para devolver ​sólo los archivos que contienen la palabra usuarios.
   - ​Los dos archivos que no contienen ​esta cadena ya no aparecen.

---

## Filtrado de contenidos en Linux
- Filtrar información
   - Filtrar es seleccionar datos que coincidan con una determinada condición.
   - Por ejemplo, si tuviera un virus en su sistema que sólo afectara a los archivos .txt, podría utilizar el filtrado para encontrar estos archivos rápidamente.
   - El filtrado te permite buscar basándote en criterios específicos, como la extensión de archivo o una cadena de texto.
- grep
   - El comando grep busca en un archivo especificado y devuelve todas las líneas del archivo que contengan una cadena o texto especificado.
   - El comando grep suele tomar dos argumentos: una cadena específica que buscar y un archivo específico en el que buscar.
   - Por ejemplo, si se introduce grep OS updates.txt, se obtendrán todas las líneas que contengan OS en el archivo updates.txt.
   - En este ejemplo, OS es la cadena específica que se busca y updates. txt es el archivo específico que se busca.
   - Veamos otro ejemplo: grep error time_logs.txt.
      - Aquí se utiliza grep para buscar el patrón de texto.
      - error es el término que se busca en el archivo time_logs.
      - txt. Cuando ejecutes este comando, grep escaneará el archivo time_logs.txt e imprimirá sólo las líneas que contengan la palabra error.
- Canalización
   - Para acceder al comando pipe se utiliza el carácter pipe (|).
   - El comando pipe envía la salida estándar de un comando como entrada estándar a otro comando para su posterior procesamiento.
   - Como recordatorio, la salida estándar es la información devuelta por el OS a través del shell, y la entrada estándar es la información recibida por el OS a través de la línea de comandos.
   - El carácter pipe (|) se encuentra en varios lugares del teclado.
   - En muchos teclados, se encuentra en la misma tecla que el carácter de barra invertida (\).
   - En algunos teclados, el | puede parecer diferente y tener un pequeño espacio en medio de la línea.
   - Si no encuentra el |, busque en Internet su ubicación en su teclado concreto.
   - Cuando se utiliza con grep, la tubería puede ayudarle a encontrar directorios y archivos que contengan una palabra específica en sus nombres.
   - Por ejemplo, ls /home/analyst/reports | grep users devuelve los nombres de archivos y directorios del directorio reports que contienen users.
   - Antes de la tubería, ls indica que se listen los nombres de los archivos y directorios en reports.
   - Luego, envía esta salida al comando después de la tubería.
   - En este caso, grep users devuelve todos los nombres de archivos o directorios que contienen users de la entrada que recibió.
   - La canalización es una forma general de redirección en Linux y puede utilizarse para múltiples tareas además del filtrado.
   - Puedes pensar en piping como una herramienta general que puedes usar siempre que quieras que la salida de un comando se convierta en la entrada de otro comando.

- find
   - El comando find busca directorios y archivos que cumplan los criterios especificados.
   - Existe una amplia gama de criterios que pueden especificarse con find.
   - Por ejemplo, puede buscar archivos y directorios que
      - Contengan una cadena específica en el nombre,
      - Tengan un determinado tamaño, o
      - Hayan sido modificados por última vez en un periodo de tiempo determinado.
   - Cuando se utiliza find, el primer argumento después de find indica dónde empezar a buscar.
   - Por ejemplo, si se introduce find /home/analyst/projects, se buscará todo a partir del directorio projects. 
   - Después de este primer argumento, debe indicar sus criterios para la búsqueda.
   - Si no incluye un criterio de búsqueda específico con el segundo argumento, es probable que la búsqueda devuelva muchos directorios y archivos.
   - La especificación de criterios implica opciones.
   - Las opciones modifican el comportamiento de un comando y suelen comenzar con un guión (-).
      - -name y -iname
         - Un criterio clave que los analistas pueden utilizar con find es encontrar nombres de archivos o directorios que contengan una cadena específica.
         - La cadena específica que se busca debe introducirse entre comillas después de las opciones -name o -iname.
         - La diferencia entre estas dos opciones es que -name distingue entre mayúsculas y minúsculas, y -iname no.
         - Por ejemplo, puede que desee encontrar todos los archivos del directorio projects que contengan la palabra "log" en el nombre del archivo.
         - Para ello, escriba find /home/analyst/projects -name "*log*". También podría introducir find /home/analyst/projects -iname "*log*".
         - En estos ejemplos, el resultado serían todos los archivos del directorio projects que contengan log rodeado de cero o más caracteres.
         - La parte "*log*" del comando es el criterio de búsqueda que indica que se busque la cadena "log".
         - Cuando -name es la opción, los archivos con nombres que incluyan Log o LOG, por ejemplo, no se devolverían porque esta opción distingue entre mayúsculas y minúsculas.
         - Sin embargo, sí se devolverán si la opción es -iname.
         - Se utiliza un asterisco (*) como comodín para representar cero o más caracteres desconocidos.
      - -mtime
         - Los analistas de seguridad también pueden utilizar find para buscar archivos o directorios modificados por última vez en un periodo de tiempo determinado.
         - Para esta búsqueda se puede utilizar la opción -mtime.
         - Por ejemplo, al introducir find /home/analyst/projects -mtime -3 se obtienen todos los archivos y directorios del directorio projects que se han modificado en los últimos tres días.
         - La búsqueda de la opción -mtime se basa en días, por lo que al introducir -mtime +1 se indican todos los archivos o directorios modificados por última vez hace más de un día, y al introducir -mtime -1 se indican todos los archivos o directorios modificados por última vez hace menos de un día.
         - Puede utilizarse la opción -mmin en lugar de -mtime si se desea basar la búsqueda en minutos en lugar de días.

---

## Actividad: Filtrado con grep
- Introducción
   - En este laboratorio, aprenderá a utilizar el comando grep y las tuberías para buscar archivos y devolver información específica.
   - Obtendrá información de diferentes archivos, incluidos los archivos de registro del servidor y los archivos de datos del usuario.
   - Utilizará comandos de Linux en el shell Bash para completar estos pasos.

- Lo que hará
   - Buscar mensajes de error en un archivo
   - Buscar archivos que contengan una cadena específica
   - Buscar información en archivos de usuario

- Resumen de la actividad
   - Anteriormente, aprendiste sobre herramientas que puedes usar para filtrar información en Linux.
   - También conoces los comandos básicos para navegar por el sistema de archivos de Linux.
   - En este lab, usarás el comando grep y la canalización para buscar archivos y obtener información específica en ellos.
   - Como analista de seguridad, es fundamental saber cómo encontrar la información que necesitas.
   - La habilidad de buscar cadenas específicas puede ayudarte a encontrar lo que necesitas de forma más eficiente.

- Situación
   - En esta situación, debes obtener información que se encuentra en el registro del servidor y los archivos de datos del usuario.
   - También debes encontrar archivos con nombres específicos.
   - Estos son los pasos que seguirás:
      1. Navegarás hasta el directorio logs y obtendrás los mensajes de error del archivo server_logs.txt.
      2. Navegarás hasta el directorio users y buscarás archivos cuyos nombres contengan una cadena específica.
      3. Buscarás información en archivos de usuarios.

- Comienza el lab

1. Busca mensajes de error en un archivo de registro
- Navega hasta el directorio /home/analyst/logs.
- Usa grep para filtrar el archivo server_logs.txt y obtener todas las líneas que contienen la cadena de texto error.
- ¿Cuántas líneas de error hay en el archivo server_logs.txt?
   - [ ] 8
   - [ ] 2
   - [ ] 4
   - [x] 6

2. Encuentra archivos que contengan cadenas específicas
- Navega hasta el directorio /home/analyst/reports/users.
- Usa el carácter de barra vertical (|), canaliza el resultado del comando ls al comando grep para enumerar únicamente los archivos que contengan la cadena Q1 en su nombre.
- ¿Cuántos archivos del subdirectorio /home/analyst/reports/users incluyen “Q1” en el nombre?
   - [ ] 2
   - [ ] 1
   - [ ] 5
   - [x] 3
- Enumera los archivos que contienen la palabra access en su nombre.
- ¿Cuántos archivos del directorio /home/analyst/reports/users incluyen “access” en el nombre?
   - [ ] 5
   - [ ] 3
   - [x] 4
   - [ ] Ninguno

3. Busca más contenido en archivos
- Muestra los archivos en el directorio /home/analyst/reports/users.
- Busca el nombre de usuario jhill en el archivo Q2_deleted_users.txt.
- Realiza una búsqueda en el archivo Q4_added_users.txt para enumerar todos los usuarios que se agregaron al departamento de Human Resources.
- ¿Cuántos usuarios se agregaron al departamento de Human Resources en el cuarto trimestre?
   - [ ] 5
   - [ ] 1
   - [x] 2
   - [ ] 3

- Listado de comandos utilizados en este laboratorio
```bash
pwd
cd logs
cat server_logs.txt | grep error
cd ~/reports/users
ls -l | grep Q1
ls -l | grep access
cat Q2_deleted_users.txt | grep jhill
cat Q4_added_users.txt | grep "Human Resources"
```

---

## Ejemplar opcional: Filtrado con grep
- Mismo laboratorio que el anterior.

---

## Ejemplar: Filtrado con grep
- Resumen de actividades
   - Anteriormente, aprendiste acerca de las herramientas que puedes usar para filtrar información en Linux.
   - También estás familiarizado con los comandos básicos para navegar por el sistema de archivos de Linux.
   - En esta actividad de laboratorio, utilizarás el comandogrep y tuberías para buscar archivos y devolver información específica de archivos.
   - Como analista de seguridad, es clave saber cómo encontrar la información que necesitas.
   - La capacidad de buscar cadenas específicas puede ayudarlo a localizar lo que necesita de manera más eficiente.

---

## Crear y modificar directorios y archivos
- Pensemos de nuevo en ​el sistema de directorios de archivos como un árbol.
- ​Los subdirectorios son las ramas del árbol.
- ​Todos están conectados desde la misma raíz​, pero pueden crecer hasta formar un árbol complejo.
- ​Cuando se trata de trabajar con datos en ​Seguridad, la organización es clave.
- ​Si sabemos dónde se encuentra la información, ​es más fácil detectar ​problemas y mantener la información segura.
- ​Es posible que esté familiarizado con el concepto ​de carpetas para organizar la información.
- ​En Linux, tenemos directorios.
- ​Los directorios ayudan a organizar los archivos y subdirectorios.
- ​Por ejemplo, dentro de un directorio de informes, ​un analista puede necesitar crear dos subdirectorios:
   - ​uno para los borradores
   - otro para los informes finales.
- Ahora que sabemos por qué necesitamos directorios, ​echemos un vistazo a ​algunos comandos esenciales de Linux para ​administrar directorios y archivos.
- ​En primer lugar, tomemos nota de ​los comandos para crear y eliminar directorios.
   - mkdir
      - crea un directorio nuevo. ​
   - rmdir
      - elimina o borra un directorio.
- ​Una característica útil de este comando es ​su advertencia integrada que le permite ​saber que un directorio no está vacío.
- ​Esto evita la eliminación accidental de archivos.
- ​Ahora, echemos un vistazo a algunos comandos para manejar archivos.
   - touch
      - crea un archivo nuevo
   - rm
      - elimina o borra un archivo.
   - mv
      - mueve un archivo o directorio a una nueva ubicación
   - cp
      - copia un archivo o directorio a una nueva ubicación.
- ​En primer lugar, usemos el comando pwd ​y, a continuación, mostremos los nombres de los archivos y ​directorios del directorio de analistas con el comando ls.
- ​Imagina que ya no necesitamos ​el directorio oldreports que ​aparece entre el contenido del archivo.
- ​Veamos cómo eliminarlo.
- Ingresamos el comando rmdir y lo seguimos con ​el nombre del directorio que queremos eliminar: oldreports.
- Podemos usar el comando ls para confirmar que ​los informes antiguos se han eliminado ​y ya no aparecen en el contenido.
- ​Ahora, hagamos otro cambio.
- ​Queremos un nuevo directorio para los borradores de informes.
- ​Necesitamos usar el comando: mkdir ​y especificar un nombre para este directorio: drafts
- ​Si volvemos a introducir ls, ​veremos que los borradores del nuevo directorio ​están incluidos en el contenido del directorio de analistas.
- ​Cambiemos a este nuevo directorio ​ingresando: cd drafts. 
- ​Si ejecutamos ls, ​no devuelve ningún resultado, ​lo que indica que este directorio está vacío actualmente.
- ​Pero a continuación, le añadiremos algunos archivos.
- ​Supongamos que queremos elaborar nuevos informes sobre los ​parches del sistema operativo y el correo electrónico instalados recientemente.
- Para crear estos archivos, ​ingresamos: touch email_patches.txt ​y luego: touch OS_patches.txt.
- La ​ejecución de ls indica que ​estos archivos están ahora en el directorio de borradores.
- ​¿Qué pasa si nos damos cuenta de que solo necesitamos un nuevo informe sobre los ​parches del sistema operativo y queremos ​eliminar el informe de parches de correo electrónico?
- ​Para hacer esto, ingresamos el comando rm y especificamos el archivo ​a eliminar como: email_patches.txt.
- ​Al ejecutar ls, se confirma que se ha eliminado.
- ​Ahora, centrémonos en nuestros comandos para mover y copiar.
- ​Nos dimos cuenta de que tenemos un archivo llamado ​política de correo electrónico en la carpeta de informes ​que actualmente está en formato de borrador.
- ​Queremos moverlo a la carpeta de borradores recién creada.
- ​Para hacer esto, necesitamos cambiar ​al directorio que actualmente tiene ese archivo.
- La ​ejecución de ls en ese directorio indica que contiene ​varios archivos, incluido email_policy.txt.
- ​Luego, para mover ese archivo, ​ingresaremos el comando mv seguido de dos argumentos.
- ​El primer argumento ​después de mv identifica el archivo que se va a mover.
- ​El segundo argumento indica dónde moverlo.
- Si cambiamos los directorios por ​borradores y, a continuación, mostramos su contenido, ​notaremos que el archivo de política de correo electrónico ​se ha movido a este directorio.
- ​Volveremos a convertirnos en informes.
- Al mostrar el contenido del archivo, se confirma que ​email_policy ya no existe.
- vulnerabilities.txt es ​un archivo que queremos mantener en el directorio de informes.
- ​Pero dado que afecta a un proyecto próximo, ​también queremos copiarlo en el directorio del proyecto.
- ​Como ya estamos en el directorio que contiene este archivo, ​usaremos el comando cp para ​copiarlo en el directorio de proyectos.
- ​Observe que el primer argumento ​indica qué archivo se va a copiar ​y el segundo argumento proporciona ​la ruta de acceso al directorio en el que se copiará.
- ​Cuando presionamos Entrar, ​se copia el archivo de vulnerabilidades en ​el directorio de proyectos y, al mismo tiempo, se ​deja el original en los informes.
- ​¿No es genial lo que podemos hacer con estos comandos? 
- Ahora, centrémonos en ​un concepto más relacionado con la modificación de archivos. 
- ​Como analista de seguridad, ​los editores de archivos suelen ser necesarios para ​sus tareas diarias, como escribir o editar informes.
- ​Un editor de archivos popular es nano.
- ​Es bueno para los principiantes.
- ​Puede acceder a esta herramienta mediante el comando nano.
- ​Familiaricémonos juntos con el nano.
- ​Añadiremos un título a ​nuestro nuevo borrador de informe: OS_patches.txt.
- Primero, cambiamos ​al directorio que contiene ese archivo, ​luego ingresamos nano ​seguido del nombre del archivo que ​queremos editar: OS_patches.txt.
- ​Esto abre el editor de archivos nano con ese archivo abierto.
- Por ahora, solo escribiremos ​el título OS Patches escribiéndolo en el editor.
- ​Necesitamos guardar esto antes de ​volver a la línea de comandos, y para hacerlo, ​presionamos Ctrl+O ​y luego ingresamos para guardarlo con el nombre del archivo actual.
- ​Luego, para salir, presionamos Ctrl+X. 

---

## Gestionar directorios y archivos
- Creación y modificación de directorios
   - mkdir
      - El comando mkdir crea un nuevo directorio. 
      - Como todos los comandos presentados en esta lectura, puede proporcionar el nuevo directorio como una ruta de archivo absoluta, que comienza desde la raíz, o como una ruta de archivo relativa, que comienza desde su directorio actual.
      - Por ejemplo, si desea crear un nuevo directorio llamado network en su directorio /home/analyst/logs, puede introducir mkdir /home/analyst/logs/network para crear este nuevo directorio.
      - Si ya se encuentra en el directorio /home/analyst/logs, también puede crear este nuevo directorio introduciendo mkdir network.
      - Puede utilizar el comando ls para confirmar que se ha añadido el nuevo directorio.
   - rmdir
      - El comando rmdir elimina, o borra, un directorio.
      - Por ejemplo, si introduce rmdir /home/analyst/logs/network eliminará este directorio vacío del sistema de archivos.
      - El comando rmdir no puede eliminar directorios con archivos o subdirectorios en su interior.
      - Por ejemplo, introducir rmdir /home/analyst devuelve un mensaje de error.

- Creación y modificación de archivos
   - touch y rm
      - El comando touch crea un nuevo archivo.
      - Este archivo no tendrá ningún contenido en su interior.
      - Si su directorio actual es /home/analyst/reports, al introducir touch permissions.txt se crea un nuevo archivo en el subdirectorio reports llamado permissions.txt.
      - El comando rm elimina, o borra, un archivo.
      - Este comando debe utilizarse con cuidado porque no es fácil recuperar los archivos borrados con rm.
      - Para eliminar el archivo de permisos que acaba de crear, introduzca rm permissions.txt.
      - Puede verificar que permissions.txt se ha creado o eliminado correctamente introduciendo ls.
   - mv y cp
      - También puede utilizar mv y cp cuando trabaje con archivos.
      - El comando mv mueve un archivo o directorio a una nueva ubicación, y el comando cp copia un archivo o directorio en una nueva ubicación.
      - El primer argumento después de mv o cp es el archivo o directorio que desea mover o copiar, y el segundo argumento es la ubicación a la que desea moverlo o copiarlo.
      - Para mover permissions.txt al subdirectorio logs, introduzca mv permissions.txt /home/analyst/logs.
      - Al mover un archivo, éste se elimina de su ubicación original.
      - Sin embargo, copiar un archivo no lo elimina de su ubicación original.
      - Para copiar permissions.txt en el subdirectorio logs manteniéndolo también en su ubicación original, introduzca cp permissions.txt /home/analyst/logs.
      - El comando mv también puede utilizarse para renombrar archivos.
      - Para renombrar un archivo, introduzca el nuevo nombre como segundo argumento en lugar de la nueva ubicación.
      - Por ejemplo, si introduce mv permissions.txt perm.txt renombrará el archivo permissions.txt a perm.txt.

- Editor de texto nano
   - nano es un editor de archivos de línea de comandos que está disponible por defecto en muchas distribuciones de Linux.
   - Muchos principiantes lo encuentran fácil de usar, y es muy utilizado en la profesión de Seguridad.
   - Puede realizar múltiples tareas básicas en nano, como crear nuevos archivos y modificar su contenido.
   - Para abrir un archivo existente en nano desde el directorio que lo contiene, introduzca nano seguido del nombre del archivo.
   - Por ejemplo, si introduce nano permissions.txt desde el directorio /home/analyst/reports, se abrirá una nueva ventana de edición de nano con el archivo permissions.txt abierto para su edición.
   - También puede proporcionar la ruta de acceso absoluta al archivo si no se encuentra en el directorio que lo contiene.
   - También puede crear un nuevo archivo en nano introduciendo nano seguido de un nuevo nombre de archivo.
   - Por ejemplo, al introducir nano authorized_users.txt desde el directorio /home/analyst/reports se crea el archivo authorized_users.txt dentro de ese directorio y se abre en una nueva ventana de edición de nano.
   - Dado que no existe una función de autoguardado en nano, es importante que guarde su trabajo antes de salir.
   - Para guardar un archivo en nano, utilice el acceso directo del teclado Ctrl + O.
   - Se le pedirá que confirme el nombre del archivo antes de guardarlo.
   - Para salir de nano, utilice el acceso directo del teclado Ctrl + X.
   - Vim y Emacs también son editores de texto de línea de comandos muy populares.

- Redirección de la salida estándar
   - Hay una forma adicional de escribir en archivos.
   - Anteriormente, aprendió sobre la entrada estándar y la salida estándar.
   - La entrada estándar es la información que recibe el OS a través de la línea de comandos, y la salida estándar es la información que devuelve el OS a través del shell.
   - También ha aprendido sobre la canalización.
   - La canalización envía la salida estándar de un comando como entrada estándar a otro comando para su posterior proceso.
   - Utiliza el carácter de tubería (|).
   - Además de la tubería (|), también puede utilizar los operadores corchete de ángulo recto (>) y doble corchete de ángulo recto (>>) para redirigir la salida estándar.
   - Cuando se utilizan con echo, los operadores > y >> pueden emplearse para enviar la salida de echo a un archivo especificado en lugar de a la pantalla.
   - La diferencia entre ambos es que > sobrescribe el archivo existente, y >> añade su contenido al final del archivo existente en lugar de sobrescribirlo.
   - El operador > debe utilizarse con cuidado, porque no es fácil recuperar los archivos sobrescritos.
   - Cuando se encuentre dentro del directorio que contiene el archivo permissions.txt, al introducir echo "last updated date" >> permissions.txt se añade la cadena "última fecha de actualización" al contenido del archivo.
   - Si introduce echo "time" > permissions.txt después de este comando, se sobrescribirá todo el contenido del archivo permissions.txt con la cadena "hora".
   - Tanto el operador > como el >> crearán un nuevo archivo si no existe ya uno con el nombre especificado.