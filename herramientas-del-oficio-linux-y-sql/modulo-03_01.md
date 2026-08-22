# Navegar por el sistema de archivos de Linux

## Bienvenido al Módulo 3
- ​​En esta sección, seguiremos aprendiendo más sobre ​Linux y cómo ​comunicarnos con el SO a través de su shell.
- ​Utilizará la línea de comandos ​para comunicarse con el SO.
- ​Aprenderá a introducir ​comandos en el shell y conocerá algunos de ​los principales comandos de Linux que ​utilizará como analista de seguridad.
- ​Específicamente, esto incluye ​navegar y gestionar el sistema de archivos.
- ​También se centrará en ​autenticar y autorizar usuarios.
- ​Esto significa que podrá ​utilizar una línea de comandos para añadir y ​eliminar usuarios del sistema y ​controlar a qué tienen acceso.
- ​Por último, siempre hay algo más que aprender.
- ​Cubriremos el acceso a recursos que ​apoyan el aprendizaje de nuevos comandos de Linux.

---

## Comandos Linux a través del shell Bash
- Como analista de seguridad, trabajará con ​registros de servidor y necesitará saber cómo navegar, ​gestionar y analizar archivos ​de forma remota sin una interfaz gráfica de usuario.
- ​Además, necesitará saber cómo ​verificar y configurar el acceso de usuarios y grupos.
- ​También necesitará dar autorización ​y establecer permisos de archivo.
- ​Esto significa que desarrollar habilidades con la línea de comandos ​es esencial para su trabajo como analista de seguridad.
- Utilizaremos el shell Bash.
- ​Bash es el shell por defecto en la mayoría de las distribuciones de Linux.
- ​En su mayor parte, los comandos clave de Linux que ​estará aprendiendo en esta sección son los mismos en todos los shells.
- ​Usted teclea comandos, y el OS ​responde con una respuesta a su comando.
- ​Un comando es una instrucción ​que le dice a la computadora que haga algo.
- Algunos comandos pueden decirle a la computadora que ​encuentre algo como un archivo específico.
- ​Otros pueden decirle que lance un programa. 
- ​O, puede ser que emita una cadena específica de texto.
- ​​Volvamos a introducir el comando echo.
- ​Puede que note que el comando ​que acabamos de introducir no está completo.
- ​Si vamos a usar el comando echo ​para dar salida a una cadena específica de ​texto, necesitamos especificar cuál es la cadena de texto.
- ​Para eso están los argumentos.
- ​Un argumento es la información específica que necesita un comando.
- ​Algunos comandos aceptan varios argumentos.
- ​​En este ejemplo, nuestro argumento era una cadena de texto. ​Los argumentos también pueden proporcionar otro tipo de información.
- ​Una cosa que es realmente importante en Linux es que ​todos los comandos y argumentos distinguen entre mayúsculas y minúsculas. 
- ​Esto incluye los nombres de archivos y directorios.
- ​Tenga esto en cuenta mientras aprende más sobre cómo ​utilizar Linux en sus tareas diarias como analista de seguridad.

---

## Comandos principales para la navegación y la lectura de archivos
- ​Imagine un árbol.
- ​¿Qué es lo primero en lo que se fijó del árbol? ​¿Diría que el tronco o las ramas?
- ​Estas últimas podrían llamar definitivamente su atención, ​¿pero qué hay de sus raíces?
- ​Todo en un árbol comienza en las raíces. 
- Algo similar ocurre cuando ​pensamos en el sistema de archivos de Linux.
- ​El Estándar de jerarquía del sistema de archivos, ​o FHS, es ​el componente del OS Linux que organiza los datos.
- ​Este sistema de archivos es ​una parte muy importante de Linux porque ​todo lo que hacemos en Linux se considera ​un archivo en algún lugar del Directorio del sistema.
- ​El FHS es un sistema jerárquico, ​y al igual que con un árbol, ​todo crece y se ramifica desde la raíz.
- ​El directorio raíz es ​el directorio de más alto nivel en Linux.
- ​Se designa con una única barra.
- ​Los subdirectorios se ramifican a partir del directorio raíz.
- ​Los subdirectorios se ramifican ​cada vez más lejos del directorio raíz. 
- Cuando se describe la estructura de directorios en Linux, se utilizan barras inclinadas ​al trazar ​hacia atrás a través de estas ramas hasta la raíz. 
- ​Por ejemplo, `/home/analyst/`, ​la primera barra indica el directorio raíz.
- ​Después se ramifica un nivel hacia el subdirectorio home.
- ​Otra barra indica que se está ramificando de nuevo.
- ​Esta vez es hacia ​el subdirectorio analyst que se encuentra dentro de home.
- ​Analizará estos archivos de registro para ​el uso de aplicaciones y la autenticación.
- Comandos de navegación y lectura de archivos
- pwd imprime el directorio de trabajo en la pantalla.
- ​Cuando utilice este comando, ​la salida le indicará en qué directorio se encuentra actualmente. 
- ​ls muestra los nombres de los archivos y ​directorios del directorio de trabajo actual.
- ​cd navega entre directorios.
- Este es el comando que utilizará ​cuando desee cambiar de directorio.
- ​Utilicemos estos comandos en Bash.
- ​Primero, escribiremos el comando ​pwd para mostrar la ubicación actual y, a continuación, pulsaremos intro.
- ​La salida es la ruta de acceso al ​directorio del analista en el que estamos trabajando actualmente.
- ​A continuación, introduzcamos ls para mostrar ​los archivos y directorios dentro del directorio del analista.
- ​La salida es el nombre de ​cuatro directorios: registros, informes antiguos, ​proyectos e informes, y un archivo llamado updates.txt.
- ​Digamos que ahora queremos entrar en ​el directorio logs para comprobar si hay accesos no autorizados.
- ​Introduciremos: cd logs ​para cambiar de directorio.
- ​No obtendremos ninguna salida ​en pantalla del comando cd, ​pero si volvemos a introducir pwd, ​su salida indica que el directorio de trabajo es logs.
- ​Logs es un subdirectorio del directorio analyst.
- ​Como analista de seguridad, ​también necesitará saber cómo ​leer el contenido de archivos en Linux.
- Por ejemplo, puede que necesite leer ​archivos que contengan ajustes de configuración para ​identificar posibles vulnerabilidades.
- O, podría mirar ​los informes de acceso de usuarios ​mientras investiga accesos no autorizados.
- ​Al leer el contenido de archivos, ​hay algunos comandos que le ayudarán.
- cat muestra el contenido de un archivo.
- ​Esto es útil, pero a veces ​no querrá el contenido completo de un archivo grande.
- ​En estos casos, puede utilizar el comando head.
- ​Muestra sólo el principio de ​un archivo, por defecto diez líneas.
- ​Probemos estos comandos.
- ​Imaginemos que queremos leer el contenido de ​acceso.txt, y que ya estamos ​en el directorio de trabajo donde se encuentra.
- ​Primero, introducimos el comando cat ​y luego lo seguimos con el nombre del archivo, ​acceso.txt.
- Y ​Bash devuelve el contenido completo de este archivo.
- ​Comparemos esto con el comando head.
- ​Cuando introducimos el comando head seguido de nuestro nombre de archivo, ​sólo se muestran las 10 primeras líneas de este archivo.