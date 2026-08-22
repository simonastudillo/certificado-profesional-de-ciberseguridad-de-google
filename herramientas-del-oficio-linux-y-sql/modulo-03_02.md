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