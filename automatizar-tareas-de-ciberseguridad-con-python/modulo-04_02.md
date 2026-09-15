# Trabajar con archivos en Python

## Acceder a un archivo de texto en Python
- Los profesionales de la Seguridad a menudo tienen la tarea de revisar archivos de registro.
- ​Estos archivos pueden tener miles de entradas, ​por lo que puede ser útil automatizar este proceso, y ahí es donde Python entra en juego.
- ​Vamos a empezar importando un simple archivo de texto que sólo contenga unas pocas palabras y ​luego restaurarlo como una cadena en Python.
- ​Todo lo que necesitamos es el archivo de texto, su ubicación y las palabras clave Python adecuadas.
- ​Vamos a empezar escribiendo una sentencia "with".
- ​La palabra clave with maneja errores y gestiona recursos externos.
- ​Al usar with, Python sabe que debe liberar automáticamente recursos que ​de otro modo mantendrían nuestro sistema ocupado hasta que el programa termine de ejecutarse.
- ​Suele usarse en el manejo de archivos para ​cerrar automáticamente un archivo después de leerlo.
- ​Para abrir archivos y luego leerlos, escribimos una sentencia que ​comienza con la palabra clave with.
- A continuación, utilizamos la función open(). ​Open() es una función que abre un archivo en Python.
- ​El primer parámetro es el nombre del archivo de texto en su computadora o ​un enlace a él en Internet.
- ​Dependiendo del entorno de Python, ​puede que también necesite incluir una ruta a este archivo.
- ​Recuerde incluir la extensión .txt en el nombre del archivo.
- ​Ahora hablemos del segundo parámetro.
- ​Este parámetro de la función open() indica a Python lo que queremos hacer con el archivo.
- ​En nuestro caso, queremos leer un archivo, por lo que utilizamos la letra "r" entre comillas.
- ​Si quisiéramos escribir en un archivo, sustituiríamos esta "r" por una "w".
- ​Pero aquí, nos estamos centrando en la lectura.
- ​Por último, file es una variable que contiene ​la información del archivo siempre que estemos dentro de la sentencia with.
- ​Al igual que con otros tipos de sentencias, terminamos nuestra sentencia with con dos puntos.
- ​El código que viene después de los dos puntos le dirá a Python qué hacer con ​el contenido del archivo.
- ​Vayamos a Python y utilicemos lo que hemos aprendido.
- ​Estamos listos para abrir un archivo de texto en Python.
- ​Ahora escribiremos nuestra sentencia with.
- ​A continuación, utilizaremos el método de lectura incorporado de Python.
- ​El método de lectura convierte los archivos en cadenas.
- ​Ahora volvamos a nuestra sentencia with.
- ​Similar a un bucle for, las sentencias with comienzan una sangría en la línea siguiente.
- ​Esto le dice a Python que este código está ocurriendo dentro de la sentencia with.
- ​Dentro de la sentencia, vamos a usar la función read() para convertir ​nuestro archivo en una cadena y almacenarla dentro de una nueva variable.
- ​Esta nueva variable puede usarse fuera de la sentencia with.
- ​Así que salgamos de la sentencia with eliminando la indentación e ​imprimamos la variable.
- ​¡Perfecto! La cadena del texto se imprime.

---

## Importar archivos a Python
- Trabajar con archivos en ciberseguridad
   - Los analistas de Seguridad pueden necesitar acceder a una variedad de archivos cuando trabajan en Python.
   - Muchos de estos archivos serán registros.
   - Un registro A es un registro de los eventos que ocurren dentro de los sistemas de una organización.
   - Por ejemplo, puede haber un registro que contenga información sobre los intentos de inicio de sesión.
   - Esto podría utilizarse para identificar una actividad inusual que señale los intentos realizados por un actor malicioso para acceder al sistema.
   - Como otro ejemplo, los actores maliciosos que hayan accedido al sistema podrían ser capaces de atacar aplicaciones de software.
   - Un analista puede necesitar acceder a un registro que contenga información sobre aplicaciones de software que estén experimentando problemas.

- Abrir archivos en Python
   - Para abrir un archivo llamado "update_log.txt" en Python con el fin de leerlo, puede incorporar la siguiente línea de código:
      - `with open("update_log.txt", "r") as file:`
   - Esta línea consta de la palabra clave with, la función open() con sus dos parámetros, y la palabra clave as seguida de un nombre de variable.
   - Debe colocar dos puntos (:) al final de la línea.

- with
   - La palabra clave with maneja errores y gestiona recursos externos cuando se utiliza con otras funciones.
   - En este caso, se utiliza con la función open() para abrir un archivo.
   - A continuación, gestionará los recursos cerrando el archivo tras salir de la sentencia with.
   - También puede utilizar la función open() sin la palabra clave with.
   - Sin embargo, debe cerrar el archivo que abrió para garantizar un manejo adecuado del mismo.

- open
   - La función open() abre un archivo en Python.
   - El primer parámetro identifica el archivo que desea abrir.
   - En la siguiente estructura de archivos, "update_log.txt" se encuentra en el mismo directorio que el archivo Python que accederá a él, "log_parser.ipynb":

<img src="./resources/image-001.png" alt="Estructura de archivos">

   - Como están en el mismo directorio, sólo se requiere el nombre del archivo.
   - El código puede escribirse como with open("update_log.txt", "r") as file:.
   - Sin embargo, "access_log.txt" no está en el mismo directorio que el archivo Python "log_parser.ipynb".
   - Por lo tanto, es necesario especificar su ruta de archivo absoluta.
   - Una ruta de archivo es la ubicación de un archivo o directorio.
   - Una ruta de archivo absoluta comienza en el directorio de nivel más alto, el raíz.
   - En el código siguiente, el primer parámetro de la función open() incluye la ruta de acceso absoluta a "access_log.txt":
   - `with open("/home/analyst/logs/access_log.txt", "r") as file:`
   - En Python, los nombres de archivos o sus rutas de acceso pueden manejarse como datos de cadena, y como todos los datos de cadena, debe colocarlos entre comillas.
   - El segundo parámetro de la función open() indica lo que desea hacer con el archivo.
   - En estos dos ejemplos, el segundo parámetro es "r", que indica que desea leer el archivo.
   - Alternativamente, puede utilizar "w" si desea escribir en un archivo o "a" si desea anexar a un archivo.

- how
   - Cuando abra un archivo utilizando with open(), debe proporcionar una variable que pueda almacenar el archivo mientras se encuentra dentro de la sentencia with.
   - Puede hacerlo mediante la palabra clave as seguida de este nombre de variable.
   - La palabra clave as asigna una variable que hace referencia a otro objeto.
   - El código with open("update_log.txt", "r") as file: asigna file para referenciar la salida de la función open() dentro del bloque de código con sangría que le sigue.

- Lectura de archivos en Python
   - Después de utilizar el código with open("update_log.txt", "r") as file: para importar "update_log.txt" a la variable file, debe indicar qué hacer con el archivo en las líneas con sangría que le siguen.
   - Por ejemplo, este código utiliza el método .read() para leer el contenido del archivo:
   - [file](./resources/code/modulo-04_02-002.py)
   - El método .read() convierte los archivos en cadenas.
   - Esto es necesario para poder utilizar y mostrar el contenido del archivo que se ha leído.
   - En este ejemplo, la variable file se utiliza para generar una cadena del contenido del archivo a través de .read().
   - A continuación, esta cadena se almacena en otra variable llamada updates.
   - A continuación, print(updates) muestra la cadena.
   - Una vez leído el archivo en la cadena updates, puede realizar sobre ella las mismas operaciones que podría realizar con cualquier otra cadena.
   - Por ejemplo, podría utilizar el método .index() para devolver el índice donde aparece un determinado carácter o subcadena.
   - O bien, podría utilizar len() para devolver la longitud de esta cadena.

- Escribir archivos en Python
   - Los analistas de Seguridad también pueden necesitar escribir en archivos.
   - Esto podría ocurrir por una variedad de razones.
   - Por ejemplo, podrían necesitar crear un archivo que contenga los nombres de usuario aprobados en una nueva lista de permitidos.
   - O puede que necesiten editar archivos existentes para añadir datos o adherirse a políticas de normalización.
   - Para escribir en un archivo, deberá abrirlo con "w" o "a" como segundo argumento de open().
   - Deberá utilizar el argumento "w" cuando desee sustituir el contenido de un archivo existente.
   - Cuando trabaje con el archivo existente update_log.txt, el código with open("update_log.txt", "w") as file: lo abre para poder reemplazar su contenido.
   - Además, puede utilizar el argumento "w" para crear un nuevo archivo.
   - Por ejemplo, with open("update_log2.txt", "w") as file: crea y abre un nuevo archivo llamado "update_log2.txt".
   - Debe utilizar el argumento "a" si desea añadir nueva información al final de un archivo existente en lugar de escribir sobre él.
   - El código with open("update_log.txt", "a") as file: abre "update_log.txt" para poder añadir nueva información al final.
   - La información existente no se borrará.
   - Al igual que cuando se abre un archivo para leer de él, se debe indicar qué hacer con el archivo en las líneas con sangría que siguen cuando se abre un archivo para escribir en él.
   - Tanto con "w" como con "a", puede utilizar el método .write().
   - El método .write() escribe datos de cadena en un archivo especificado.
   - El siguiente ejemplo utiliza el método .write() para añadir el contenido de la variable line al archivo "access_log.txt".
   - [file](./resources/code/modulo-04_02-003.py)
   - Si llama al método .write() sin utilizar la palabra clave with al importar el archivo, es posible que sus argumentos no se escriban completamente en el archivo si éste no se cierra correctamente de otra forma.

---

## Analizar un archivo de texto en Python
- ​Ahora que ya sabe cómo importar archivos de texto en Python, ​vamos a ir un paso ​más allá y aprender a darles una estructura.
- ​Esto nos permitirá analizarlos con mayor facilidad.
- ​Este proceso suele denominarse parsing.
- ​El parsing es el proceso de ​convertir datos en un formato más legible.
- ​Para ello, vamos a ​juntar todo lo que hemos aprendido sobre ​listas y cadenas y aprender ​otro método para trabajar con cadenas en Python.
- ​El método que necesitamos es el método split.
- ​El método split convierte una cadena en una lista.
- ​Lo hace separando ​la cadena basándose en un carácter especificado.
- ​O, si no se pasa ningún argumento, ​cada vez que encuentra un espacio en blanco, ​separa la cadena.
- ​Así, una división convertiría la cadena ​"¡Estamos aprendiendo sobre parsing!" en esta lista.
- ​Estamos utilizando el método de división ​para separar las cadenas en ​trozos más pequeños que podamos analizar más ​fácilmente que un gran bloque de texto.
- Trabajaremos con un ejemplo de ​registro de seguridad en el que ​cada línea representa un nuevo punto de datos.
- ​Para almacenar estos puntos en una lista, ​queremos separar el texto en función de la nueva línea.
- ​Python considera que una nueva línea es un tipo de espacio en blanco.
- ​Podemos usar el método split sin pasar un argumento.
- ​Recuerde, usamos este código para abrir ​un archivo y luego leerlo en una cadena.
- ​Ahora, dividamos esa cadena en ​una lista usando el método split y luego imprimamos la salida.
- ​Después de ejecutarlo, ​Python da como salida una lista de ​nombres de usuario en lugar de una gran cadena de ellos.
- ​Si queremos guardar esta lista, ​tendríamos que asignarla a otra variable.
- ​Por ejemplo, podemos llamar a la variable usernames.
- ​Y luego lo ejecutaremos de nuevo.
- ​Y ahora esta lista puede reutilizarse en otro código.
- ​¡Felicidades! ​Acaba de aprender lo básico de ​parsear un archivo de texto en Python.
- [file](./resources/code/modulo-04_02-004.py)

---

## Trabajar con archivos en Python
- Análisis sintáctico
   - Parte del trabajo con archivos implica estructurar su contenido para satisfacer sus necesidades.
   - Análisis sintáctico es el proceso de convertir los Datos a un formato más legible.
   - Los Datos pueden necesitar ser más legibles de un par de maneras diferentes.
   - En primer lugar, ciertas partes de su código Python pueden requerir la modificación a un formato específico.
   - Al convertir los Datos a este formato, permite a Python procesarlos de una forma específica.
   - En segundo lugar, los programadores necesitan leer e interpretar los resultados de su código, y el análisis sintáctico también puede hacer que los datos sean más legibles para ellos.
   - Entre los métodos que pueden ayudarle a analizar sus datos se incluyen .split() y .join().

- split()
   - Conceptos básicos de .split()
      - El método .split() convierte una cadena en una lista.
      - Separa la cadena en función de un carácter especificado que se pasa a .split() como argumento.
      - En el siguiente ejemplo, los nombres de usuario de la cadena approved_users están separados por una coma.
      - Por esta razón, una cadena que contiene la coma (",") se pasa a .split() para analizarla en forma de lista.
      - Ejecute este código y analice los diferentes contenidos de approved_users antes y después de que se le aplique el método .split():
      - [file](./resources/code/modulo-04_02-005.py)
      - Antes de aplicar el método .split() a approved_users, éste contiene una cadena, pero después de aplicarlo, esta cadena se convierte en una lista.
      - Si no pasa un argumento a .split(), éste separará la cadena cada vez que encuentre un espacio en blanco.
      - Python considera espacios en blanco una gran variedad de caracteres.
      - Estos caracteres incluyen espacios entre caracteres, retornos para nuevas líneas y otros.
      - El siguiente ejemplo muestra cómo una cadena de nombres de usuario separados por espacios puede dividirse en una lista mediante el método .split():
      - [file](./resources/code/modulo-04_02-006.py)
      - Como no se pasa un argumento a .split(), Python divide la cadena removed_users en cada espacio al separarla en una lista.
   - Aplicación de .split() a archivos
      - El método .split() le permite trabajar con el contenido de un archivo como una lista después de haberlo convertido en una cadena mediante el método .read().
      - Esto resulta útil de diversas maneras.
      - Por ejemplo, si desea iterar a través del contenido del archivo en un bucle for, esto puede hacerse fácilmente cuando se convierte en una lista.
      - El siguiente código abre el archivo "update_log.txt".
      - A continuación, lee todo el contenido del archivo en la variable updates como una cadena y divide la cadena en la variable updates en una lista mediante la creación de un nuevo elemento en cada espacio en blanco:
      - [file](./resources/code/modulo-04_02-007.py)
      - Después de esto, a través de la variable updates, puede trabajar con el contenido del archivo "update_log.txt" en partes de su código que requieran que esté estructurado como una lista.
      - Debido a que la línea que contiene .split() no tiene sangría como parte de la sentencia with, el archivo se cierra primero.
      - Cerrar un archivo tan pronto como ya no sea necesario ayuda a mantener la legibilidad del código.
      - Una vez que un archivo se lee en la variable updates, ya no se necesita y puede cerrarse.

- .join()
   - Conceptos básicos de .join()
      - Si necesita convertir una lista en una cadena, también existe un método para ello.
      - El método .join() concatena los elementos de un iterable en una cadena.
      - La sintaxis utilizada con .join() es distinta de la utilizada con .split() y otros métodos con los que ha trabajado, como .index().
      - En métodos como .split() o .index(), usted añade el método a la cadena o lista con la que está trabajando y luego pasa otros argumentos.
      - Por ejemplo, el código usernames.index(2), anexa el método .index() a la variable usernames, que contiene una lista. Pasa 2 como argumento para indicar qué elemento debe devolver.
      - Sin embargo, con .join(), debe pasar como argumento la lista que desea concatenar en una cadena.
      - Añade .join() al carácter con el que desea separar cada elemento una vez unidos en una cadena.
      - Por ejemplo, en el código siguiente, la variable approved_users contiene una lista.
      - Si desea unir esa lista en una cadena y separar cada elemento con una coma, puede utilizar ",".join(approved_users).
      - Ejecute el código y examine lo que devuelve:
      - [file](./resources/code/modulo-04_02-008.py)
      - Antes de que se aplique .join(), approved_users es una lista de cinco elementos.
      - Después de aplicarlo, es una cadena con cada nombre de usuario separado por una coma.
      - Otra forma de separar elementos cuando se utiliza el método .join() es utilizar "\n", que es el carácter de nueva línea.
      - El carácter "\n" indica que hay que separar los elementos colocándolos en nuevas líneas.
   - Aplicación de .join() a archivos
      - Al trabajar con archivos, también puede ser necesario volver a convertir su contenido en una cadena.
      - Por ejemplo, puede utilizar el método .write().
      - El método .write() escribe datos de cadena en un archivo.
      - Esto significa que si ha convertido el contenido de un archivo en una lista mientras trabajaba con él, tendrá que volver a convertirlo en una cadena antes de utilizar .write().
      - Para ello puede utilizar el método .join().
      - Ya ha examinado cómo podría aplicarse .split() al contenido del archivo "update_log.txt" una vez convertido en cadena mediante .read() y almacenado como updates:
      - [file](./resources/code/modulo-04_02-009.py)
      - Una vez que haya terminado de realizar operaciones utilizando la lista de la variable updates, es posible que desee sustituir "update_log.txt" por el nuevo contenido.
      - Para ello, primero tiene que volver a convertir las actualizaciones en una cadena mediante .join().
      - A continuación, puede abrir el archivo mediante una sentencia with y utilizar el método .write() para escribir la cadena updates en el archivo:
      - [file](./resources/code/modulo-04_02-010.py)
      - El Código " ".join(updates) indica que separe cada uno de los elementos de la lista en updates con un espacio una vez unidos de nuevo en una cadena.
      - Y como "w" se especifica como segundo argumento de open(), Python sobrescribirá el contenido de "update_log.txt" con la cadena que se encuentra actualmente en la variable updates.

---

## Actividad: Importar y analizar un archivo de texto
- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar el uso de funciones y otra sintaxis para importar y analizar archivos de texto en Python.
   - Se le presentará un escenario de Seguridad para que lo explore a lo largo del laboratorio.
   - Preparará un archivo de registro de seguridad para su análisis y creará un archivo de texto con las direcciones IP que tienen permiso para acceder a información restringida.
- Lo que hará
   - Importar y almacenar un archivo de texto como una cadena
   - Convertir el archivo de texto en una lista utilizando el método de cadena .split() 
   - Añadir información al archivo de texto
   - Crear otro archivo de texto

- Scenario
   - In this lab, you're working as a security analyst.
   - You're responsible for preparing a security log file for analysis and creating a text file with IP addresses that are allowed to access restricted information.

- Task 1
   - In this task, you'll import a security log text file and store it as a string to prepare it for analysis.
   - In Python, a with statement is often used in file handling to open a file and then automatically close the file after reading it.
   - You're given a variable named import_file that contains the name of the log file that you want to import.
   - Start by writing the first line of the with statement in the following code cell.
   - Use the open() function, setting the second parameter to "r".
   - Note that running this code will produce an error because it will only contain the first line of the with statement; you'll complete this with statement in the task after this.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code.
   - [file](./resources/code/lab_10/task_01.py)

- Task 2
   - Now, you'll use the .read() method to read the imported file, and you'll store the result in a variable named text.
   - Afterwards, display the text and explore what it contains by running the cell.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell. 
   - [file](./resources/code/lab_10/task_02.py)

- Task 3
   - The output in the previous step is one big string.
   - In this task, you'll explore how you can split the string that contains the entire imported log file into a list of strings, one string per line.
   - Use the .split() method to perform this split and then display the result.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Note that displaying .split() doesn’t change what is stored in the text variable.
   - Variable reassignment would be necessary if you want to store the result after splitting.
   - [file](./resources/code/lab_10/task_03.py)
   - What do you notice about the output before and after using the .split() method?
   > The output before using .split() is a single string containing all the lines of the file, while the output after using .split() is a list of strings, each representing a line from the file.

- Task 4
   - There is a missing entry in the log file.
   - You'll need to account for that by appending it to the log file.
   - You're given the missing entry stored in a variable named missing_entry.
   - Use the .write() method and the parameter "a" in the open() function.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - After the portion of the code that writes to the file, another with statement uses the .read() method to read the updated file into the text variable and then display it.
   - [file](./resources/code/lab_10/task_04.py)
   - What do you notice about the position of the entry that was added to the log file?
   > The entry that was added to the log file appears at the end of the file, as it was appended using the "a" parameter in the open() function.

- Task 5
   - The next task you're responsible for is creating a text file.
   - This text file should include a list of IP addresses that are allowed to access restricted information.
   - Documenting this in a text file will help you communicate your findings to your security team.
   - Start by creating a variable named import_file that stores the name of the file, which should be "allow_list.txt".
   - You're also given a variable named ip_addresses that stores a string containing the IP addresses that are allowed.
   - Run the code to display the two variables and explore what they contain.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_10/task_05.py)

- Task 6
   - Your next goal is to create a with statement in order to write the IP addresses to the text file you created in the previous step.
   - You'll first open the file using the "w" parameter.
   - Then, you'll write the IP addresses to the file.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Note that the code cell will contain a with statement that writes to a file but does not display information to the screen, so running it will not produce an output.
   - [file](./resources/code/lab_10/task_06.py)

- Task 7
   - In this final step, you'll complete the code you've been writing up to this point.
   - You'll add code to read the file containing IP addresses.
   - Complete a with statement that reads the text file and stores it in a new variable called text.
   - Afterwards, display the contents of text and run the cell to explore the result.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_10/task_07.py)

- Conclusion
   - In this lab, I practiced importing and analyzing a text file in Python.
   - I also created a text file that contains a list of IP addresses that are allowed to access restricted information.
   - I learned how to use the .split() method to convert a string into a list and the .join() method to convert a list back into a string.
   - I also learned how to use the .write() method to write data to a text file.

---

## Ejemplar: Importar y analizar un archivo de texto
- Mismo laboratorio que el anterior

- Conclusion
   - Python has functions and syntax that help you import and parse text files.
      - The with statement allows you to efficiently handle files.
      - The open() function allows you to import or open a file. It takes in the name of the file as the first parameter and a string that indicates the purpose of opening the file as the second parameter.
         - Specify "r" as the second parameter if you're opening the file for reading purposes.
         - Specify "a" as the second parameter if you're opening the file for appending purposes.
         - Specify "w" as the second parameter if you're opening the file for writing purposes.
      - The .read() method allows you to read in a file.
      - The .write() method allows you to append or write to a file.
   - The .split() method in Python allows you to convert a string to a list.

---

## Desarrollar un algoritmo de análisis sintáctico en Python
- ​Ahora vamos a unir todas las piezas para importar un archivo, ​analizarlo e implementar un algoritmo simple que nos ayude a detectar intentos de inicio de sesión sospechosos.
- Queremos crear un programa que se ejecute cada ​vez que un usuario nuevo inicie sesión y compruebe ​si ese usuario ha tenido tres o más intentos fallidos de inicio de sesión.
- ​Primero, analicemos la estructura de nuestros insumos para construir ​una estrategia para desarrollar nuestro programa.
- ​Tenemos un archivo de registro almacenado en formato.txt que contiene un nombre de usuario por línea.
- ​Cada nombre de usuario representa un intento fallido de inicio de sesión.
- ​Por lo tanto, cuando un usuario inicia sesión, queremos que nuestro programa compruebe su nombre de usuario y ​cuente cuántas veces ese nombre de usuario aparece en nuestro archivo de registro.
- ​Si ese nombre de usuario se repite tres o más veces, el programa devuelve una alerta.
- ​Empezaremos con el código que importa el archivo de intentos de registro​, lo divide y lo almacena en una variable denominada usernames.
- ​Intentemos imprimir los nombres de usuario de la variable para comprobar su contenido.
- ​Vamos a ejecutar esto.
- ¡Perfecto! Esto es exactamente lo que esperábamos.
- ​La variable usernames está lista para usarse en nuestro algoritmo.
- [file](./resources/code/modulo-04_02-011.py)
- ​Ahora desarrollemos una estrategia para contar las apariciones de nombres de usuario en la lista.
- ​Empezaremos con los ocho primeros elementos de la lista de nombres de usuario.
- ​Observamos que hay dos veces el nombre de usuario «eraab» ​en la lista, pero ¿cómo le diríamos a Python que lo cuente?<>
- ​Implementaremos un bucle for que recorre en iteración cada elemento.
- ​Vamos a representar la variable loop con una flecha.
- ​También definiremos una variable de contador que comience en 0.
- ​Por lo tanto, nuestro bucle for comienza con el nombre de usuario «elarson».
- ​En cada elemento, Python pregunta: ​«¿Es este elemento igual a la cadena 'eraab'?»
- ​Si la respuesta es sí, el contador sube uno.
- ​Si no lo es, entonces el contador permanece igual.
- ​Como «elarson» no es lo mismo que «eraab», ​el contador sigue siendo 0.
- ​Luego, pasamos al siguiente elemento.
- ​Nos encontramos con nuestra primera aparición de «eraab».
- ​En este punto, el contador aumenta en 1.
- Al pasar ​al siguiente elemento, encontramos otra aparición de «eraab», ​por lo que volvemos a aumentar nuestro contador en 1.
- ​Eso significa que nuestro contador está ahora en 2.
- ​Continuaremos con este proceso para el resto de la lista.
- ​Ahora que conocemos la solución, hablemos de cómo implementarla en Python.
- ​La solución del problema en Python implicará un bucle for, ​una variable de contador y una sentencia if.
- Volvamos a nuestro código.
- ​Crearemos una función que cuente los intentos fallidos de inicio de sesión de un usuario.
- ​Primero, definamos nuestra función. Lo llamaremos login_check().
- ​Se necesitan dos parámetros.
- La primera se llama login_list.
- ​Esto se usará para la lista de intentos fallidos de inicio de sesión.
- ​El segundo se llama current_user.
- Se utilizará para el usuario que inicie sesión.
- ​Dentro de esta función, empezamos por definir ​la variable contador y establecemos su valor en 0.
- ​Ahora iniciamos el bucle for.
- Usaremos i como nuestra variable de bucle e iremos ​recorriendo la lista de inicio de sesión.
- ​En otras palabras, a medida que el bucle se repita, ​recorrerá todos los intentos fallidos de inicio de sesión de la lista.
- ​Directamente dentro del bucle for, iniciamos la sentencia if.
- La sentencia if ​comprueba si nuestra variable de bucle es igual al current_user que estamos buscando.
- ​Si esta condición es verdadera, queremos añadir 1 al contador.
- ​Ya casi hemos terminado con nuestro algoritmo.
- ​Ahora, solo necesitamos la sentencia if-else final para imprimir la alerta.
- ​Si el contador suma 3 o más, ​debemos decirle al usuario que su cuenta está bloqueada para que no pueda iniciar sesión.
- ​También escribiremos una instrucción else para los usuarios que puedan iniciar sesión.
- ¡Nuestro algoritmo está completo!
- ​Probemos nuestra nueva función con un nombre de usuario de ejemplo.
- ​Podemos sacar algunos de los nombres de usuario de la lista y probar nuestra función con ellos.
- ​Usemos el primer nombre de la lista.
- ​Vamos a ejecutar el código.
- Según nuestro código, ​este usuario puede iniciar sesión.
- Tienen menos de tres intentos fallidos de inicio de sesión.
- ​Ahora volvamos a nuestro usuario «eraab».
- ​Recuerde que tenían dos entradas en la lista de los ocho primeros nombres en ​nuestros intentos fallidos de inicio de sesión.
- ​¿Crees que podrán iniciar sesión? Cuando corremos, ​recibimos un mensaje de «cuenta bloqueada».
- Esto significa ​que tuvieron tres o más intentos fallidos de inicio de sesión.
- [file](./resources/code/modulo-04_02-012.py)
- ¡ ​Excelente trabajo! Acaba de desarrollar su primer algoritmo de Seguridad que incluye un registro.
- ​A medida que vaya adquiriendo habilidades, aprenderá cómo hacer que este algoritmo sea más eficiente, ​pero esta solución funciona bien por ahora.
- ​En este vídeo, resumimos todo lo que hemos aprendido hasta ahora, ​desde las operaciones de listas hasta el desarrollo de algoritmos, pasando por el análisis de archivos.
- ​Lo hicimos mientras creábamos un algoritmo que podemos aplicar en un contexto de Seguridad. 

---

## Actividad: Crear otro algoritmo
- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar el desarrollo de otro algoritmo en Python.
   - Se le presentará un escenario de seguridad para que lo explore a lo largo del laboratorio.
   - Desarrollará un nuevo algoritmo que analiza un archivo que contiene direcciones IP que tienen permitido el acceso a contenido restringido y elimina las direcciones que ya no tienen acceso.

- Lo que hará
   - Importar un archivo de texto que contenga una lista de permitidos y almacenarla como una cadena
   - Desarrollar un algoritmo de análisis sintáctico que elimine de la lista de permitidos las direcciones IP que ya no tienen acceso a información restringida

- Scenario
   - In this lab, you're working as a security analyst and you're responsible for developing an algorithm that parses a file containing IP addresses that are allowed to access restricted content and removes addresses that no longer have access.

- Task 1
   - Your eventual goal is to develop an algorithm that parses a series of IP addresses that can access restricted information and removes the addresses that are no longer allowed.
   - Python can automate this process.
   - You're given a text file called "allow_list.txt" that contains a series of IP addresses that are allowed to access restricted information.
   - There are IP addresses that should no longer have access to this information, and their IP addresses need to be removed from the text file.
   - You're given a variable named remove_list that contains the list of IP addresses to be removed.
   - Display both variables to explore their contents, and run the cell.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before running the following cell.
   - [file](./resources/code/lab_11/task_01.py)
   - What do you observe about the output above?
   > The output shows the contents of the import_file variable, which contains the name of the text file "allow_list.txt", and the remove_list variable, which contains a list of IP addresses that need to be removed from the allow list. The import_file variable is a string, while the remove_list variable is a list of strings.

- Task 2
   - In this task, start by opening the text file using the import_file variable, the with keyword, and the open() function with the "r" parameter.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code.
   - For now, you'll write the first line of the with statement.
   - Running this code will produce an error because it will only contain the first line of the with statement; you'll complete this with statement in the task after this.
   - [file](./resources/code/lab_11/task_02.py)

- Task 3
   - Now, use the .read() method to read the imported file and store it in a variable named ip_addresses.
   - Afterwards, display ip_addresses to examine the data in its current format.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_11/task_03.py)
   - Do you notice any IP addresses in the allow list that are also in the remove_list?
   > Yes, there are IP addresses in the allow list that are also in the remove_list. These are the IP addresses that need to be removed from the allow list.

- Task 4
   - After reading the file, reassign the ip_addresses variable so its data type is updated from a string to a list.
   - Use the .split() method to achieve this.
   - Adding this step will allow you to iterate through each of the IP addresses in the allow list instead of navigating a large string that contains all the addresses merged together.
   - Afterwards, display the ip_addresses variable to verify that the update took place.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_11/task_04.py)

- Task 5
   - Now, you'll write code that removes the elements of remove_list from the ip_addresses list.
   - This will require both an iterative statement and a conditional statement.
   - First, build the iterative statement. Name the loop variable element, loop through ip_addresses, and display each element.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_11/task_05.py)

- Task 6
   - Now, build a conditional statement to remove the elements of remove_list from the ip_addresses list.
   - The conditional statement should be placed inside the iterative statement that loops through ip_addresses.
   - In every iteration, if the current element in the ip_addresses list is in the remove_list, the remove() method should be used to remove that element.
   - Afterwards, display the updated ip_addresses list to verify that the elements of remove_list are no longer in the ip_addresses.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_11/task_06.py)

- Task 7
   - The next step is to update the original file that was used to create the ip_addresses list.
   - A line of code containing the .join() method has been added to the code so that the file can be updated.
   - This is necessary because ip_addresses must be in string format when used inside the with statement to rewrite the file.
   - The .join() method takes in an iterable (such as a list) and concatenates every element of it into a string.
   - The .join() method is applied to a string consisting of the character that will be used to separate every element in the iterable once its converted into a string.
   - In the code below, the method is applied to the string " ", which contains just a space character.
   - The argument of the .join() method is the iterable you want to convert, and in this case, that's ip_addresses.
   - As a result, it converts ip_addresses from a list back into a string with a space between each element and the next.
   - After this line with the .join() method, build the with statement that rewrites the original file.
   - Use the "w" parameter when calling the open() function to delete the contents in the original file and replace it with what you want to write.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - This code cell will not produce an output.
   - [file](./resources/code/lab_11/task_07.py)

- Task 8
   - In this task, you'll verify that the original file was rewritten using the correct list.
   - Write another with statement, this time to read in the updated file.
   - Start by opening the file.
   - Then read the file and store its contents in the text variable.
   - Afterwards, display the text variable to examine the result.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_11/task_08.py)

- Task 9
   - The next step is to bring all of the code you've written leading up to this point and put it all into one function.
   - Define a function named update_file() that takes in two parameters.
   - The first parameter is the name of the text file that contains IP addresses (call this parameter import_file).
   - The second parameter is a list that contains IP addresses to be removed (call this parameter remove_list).
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Note that this code cell will not produce an output.
   - [file](./resources/code/lab_11/task_09.py)
   - What are the benefits of incorporating the algorithm into a single function?
   > Incorporating the algorithm into a single function provides several benefits:
   > 1. Reusability: The function can be called multiple times with different parameters
   > 2. Modularity: The code is organized into a single block, making it easier to read and maintain
   > 3. Abstraction: The function hides the implementation details, allowing users to focus on the input and output without worrying about the underlying logic

- Task 10
   - Finally, call the update_file() that you defined.
   - Apply the function to "allow_list.txt" and pass in a list of IP addresses as the second argument.
   - Use the following list of IP addresses as the second argument:
   - ["192.168.25.60", "192.168.140.81", "192.168.203.198"]
   - After the function call, use a with statement to read the contents of the allow list. Then display the contents of the allow list. Run it to verify that the file has been updated by the function.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_11/task_10.py)

- Conclusion
   - In this lab, I practiced developing an algorithm in Python that parses a file containing IP addresses that are allowed to access restricted content and removes addresses that no longer have access. I learned how to use the .split() method to convert a string into a list, the .join() method to convert a list back into a string, and the .write() method to write data to a text file. I also learned how to incorporate the algorithm into a single function for reusability, modularity, and abstraction.

---

## Ejemplar: Crear otro algoritmo
- Mismo laboratorio que el anterior

- Conclusion
   - Python has functions and syntax that help you import and parse text files.
      - The with statement allows you to efficiently handle files.
      - The open() function allows you to import or open a file. It takes in the name of the file as the first parameter and a string that indicates the purpose of opening the file as the second parameter.
         - Specify "r" as the second parameter if you're opening the file for reading purposes.
         - Specify "w" as the second parameter if you're opening the file for writing purposes.
      - The .read() method allows you to read in a file.
      - The .write() method allows you to append or write to a file.
   - You can use a for loop to iterate over a list.
   - You can use an if statement to check if a given value is in a list and execute a specific action if so.
   - You can use the .split() method to convert a string to a list.
   - You can use Python to compare contents of a text file against elements of a list.
   - Algorithms can be incorporated into functions. When defining a function, you must specify the parameters it takes in and the actions it should execute.

---

## Actividad de Portfolio: Actualizar un archivo mediante un algoritmo Python
- Resumen de la actividad
   - En esta actividad, crearás un nuevo documento de portafolio para demostrar tu experiencia usando Python para desarrollar algoritmos que involucran abrir archivos y analizar su contenido
   - Puedes agregar este documento a tu portafolio de ciberseguridad, el cual puedes compartir con posibles empleadores o reclutadores
   -  Explicarás el código que desarrollaste en ese laboratorio, y esto te ayudará a prepararte para futuras entrevistas de trabajo y otros pasos del proceso de contratación
- Escenario
   - Revise el siguiente escenario. A continuación, complete las instrucciones paso a paso.
   - Usted es un profesional de la seguridad que trabaja en una empresa de atención sanitaria.
   - Como parte de su trabajo, se le pide que actualice regularmente un archivo que identifica a los empleados que pueden acceder a contenido restringido.
   - El contenido del archivo se basa en quién trabaja con registros personales de pacientes.
   - El acceso de los empleados está restringido en función de su dirección IP.
   - Existe una lista de direcciones IP autorizadas a acceder a la subred restringida.
   - También hay una lista de eliminados que identifica qué empleados debes eliminar de esta lista de permitidos.
   - Tu tarea es crear un algoritmo que utilice código Python para comprobar si la lista de permitidos contiene alguna dirección IP identificada en la lista de eliminados.
   - Si es así, debes eliminar esas direcciones IP del archivo que contiene la lista de permitidos.
- Instrucciones paso a paso
   
1. Acceder a la plantilla
- [Plantilla](./resources/Algorithm-for-file-updates-in-Python.docx)

2. Acceso a los materiales de apoyo
- El siguiente material de apoyo le ayudará a completar esta actividad
- El documento Instrucciones para incluir código Python proporciona instrucciones y buenas prácticas para incluir muestras de código Python en su actividad del portafolio
- [Instrucciones para incluir código Python](./resources/Instructions-for-including-Python-code.docx)

3. Abra el archivo que contiene la lista de permitidos
- El fichero que desea abrir se llama "allow_list.txt".
- Asigne a la variable import_file una cadena que contenga este nombre de fichero.
- A continuación, utilice una sentencia with para abrirlo.
- Utiliza la variable file para almacenar el archivo mientras trabajas con él dentro de la sentencia with.
- Describe la sintaxis, funciones y palabras clave de Python que necesitas para lograr esto en la sección Abrir el archivo que contiene la lista de permitidos de la plantilla Algoritmo para actualizaciones de archivos en Python.
- En la sección Tarea 2 de Crear otro algoritmo de laboratorio, haz una captura de pantalla de esta parte de tu código.
- O bien, escriba este código directamente en la plantilla.

4. Leer el contenido del archivo
- A continuación, utilice el método .read() para convertir el contenido del archivo de la lista de permisos en una cadena de caracteres para poder leerla.
- Almacena esta cadena en una variable llamada ip_addresses.
- Describe la sintaxis, las funciones y las palabras clave de Python que necesitas para lograr esto en la sección Leer el contenido del archivo de la plantilla Algoritmo para actualizaciones de archivos en Python.
- En la sección Tarea 3 del laboratorio Crea otro algoritmo, haz una captura de pantalla de esta parte de tu código.
- O bien, escriba este código directamente en la plantilla.

5. Convertir la cadena en una lista
- Para eliminar direcciones IP individuales de la lista de permitidas, las direcciones IP deben estar en formato de lista.
- Por lo tanto, utilice el método .split() para convertir la cadena ip_addresses en una lista.
- Describe la sintaxis, funciones y palabras clave de Python que necesitas para lograr esto en la sección CONVERTIR la cadena en una lista de la plantilla Algoritmo para actualizaciones de archivos en Python.
- En la sección Tarea 4 del laboratorio Crea otro algoritmo, haz una captura de pantalla de esta parte de tu código.
- O bien, escriba este código directamente en la plantilla.

6. Recorrer la lista de eliminaciones
- Una segunda lista llamada remove_list contiene todas las direcciones IP que deben ser eliminadas de la lista ip_addresses.
- Establezca el encabezado de un bucle for que iterará a través de la lista remove_list.
- Use element como la variable del bucle.
- Describe la sintaxis, funciones y palabras clave de Python que necesitas para lograr esto en la sección Iterar a través de la lista de eliminados de la plantilla Algoritmo para actualizaciones de archivos en Python.
- En la sección Tarea 5 del laboratorio Crea otro algoritmo, haz una captura de pantalla de esta parte de tu código.
- O bien, escriba este código directamente en la plantilla.

7. Eliminar las direcciones IP que están en la lista de eliminación
- En el cuerpo de tu Sentencia iterativa, añade código que elimine todas las direcciones IP de la lista de permitidas que también estén en la lista de eliminadas.
- Primero, crea una condicional que evalúe si la variable de bucle element forma parte de la lista ip_addresses.
- Luego, dentro de esa condicional, aplica el método .remove() a la lista ip_addresses y elimina las direcciones IP identificadas en la variable de bucle element. 
- Describe la sintaxis, funciones y palabras clave de Python que necesitas para lograr esto en la sección Eliminar direcciones IP que están en la lista de eliminación de la plantilla Algoritmo para actualizaciones de archivos en Python.
- En la sección Tarea 6 del laboratorio Crear otro algoritmo, toma una captura de pantalla de esta parte de tu código.
- O bien, escriba este código directamente en la plantilla.
- Además, incluye una frase que explique que aplicar el método .remove() de esta manera es posible porque no hay duplicados en la lista ip_addresses.

8. Actualice el archivo con la lista revisada de direcciones IP
- Ahora que ha eliminado estas direcciones IP de la variable ip_address, puede completar el algoritmo actualizando el fichero con esta lista revisada.
- Para ello, primero debe convertir la lista ip_addresses de nuevo en una cadena utilizando el método .join().
- Aplique .join() a la cadena "\n" para separar los elementos del archivo colocándolos en una nueva línea.
- A continuación, utilice otra sentencia with y el método .write() para escribir sobre el archivo asignado a la variable import_file.
- Describe la sintaxis, funciones y palabras clave de Python que necesitas para lograr esto en la sección Actualizar el archivo con la lista revisada de direcciones IP de la plantilla Algoritmo para la actualización de archivos en Python.
- En la sección Tarea 7 del laboratorio Crea otro algoritmo, haz una captura de pantalla de esta parte de tu código.
- O bien, escriba este código directamente en la plantilla.

9. Finalice su documento
- Para finalizar el documento y dejar claro su propósito a los posibles empleadores, asegúrate de completar las secciones Descripción del proyecto y Resumen del proyecto de la plantilla Algoritmo para la actualización de archivos en Python.
- En la sección Descripción del proyecto, ofrece una visión general del escenario y de lo que has logrado en Python.
- Escribe de tres a cinco frases.
- En la sección Resumen, proporciona un breve resumen del algoritmo destacando sus componentes principales.
- Escribe de cuatro a seis frases.

- Qué incluir en tu respuesta
   - Capturas de pantalla de tu código Python o versiones escritas del código
   - Explicaciones de la sintaxis, funciones y palabras clave del código
   - Una descripción del proyecto al principio
   - Un resumen al final
   - Detalles sobre el uso de la sentencia with y la función open() en tu algoritmo
   - Detalles sobre el uso de los métodos .read() y .write() en el algoritmo
   - Utilización del método .split() en el algoritmo
   - Cómo utilizar un bucle for en el algoritmo
   - Utilización del método .remove() en el algoritmo

- Actividad

- Project description
> En este proyecto, desarrollé un algoritmo en Python que analiza un archivo de texto que contiene direcciones IP permitidas para acceder a contenido restringido. El objetivo del algoritmo es eliminar las direcciones IP que ya no tienen acceso, basándose en una lista de eliminados. Utilicé funciones y métodos de Python para abrir, leer, modificar y actualizar el archivo de texto de manera eficiente.

- Open the file that contains the allow list
```python
import_file = "allow_list.txt"
with open(import_file, "r") as file:
```

- Read the file contents
```python
   ip_addresses = file.read()
```

- Convert the string into a list
```python
   ip_addresses = ip_addresses.split("\n")
```

- Iterate through the remove list
```python
   for element in remove_list:
```

- Remove IP addresses that are on the remove list
```python
      if element in ip_addresses:
         ip_addresses.remove(element)
```

- Update the file with the revised list of IP addresses
```python
   with open(import_file, "w") as file:
      file.write("\n".join(ip_addresses))
```

- Códig completo del algoritmo
```python
def update_file(import_file, remove_list):
   with open(import_file, "r") as file:
      ip_addresses = file.read()
      ip_addresses = ip_addresses.split("\n")
      
   for element in remove_list:
      if element in ip_addresses:
         ip_addresses.remove(element)
   
   with open(import_file, "w") as file:
      file.write("\n".join(ip_addresses))
```

- Summary
> En resumen, el algoritmo desarrollado en Python permite automatizar la actualización de un archivo de texto que contiene direcciones IP permitidas. Utiliza la sentencia with para manejar archivos de manera eficiente, los métodos .read() y .write() para leer y escribir en el archivo, y el método .split() para convertir cadenas en listas. Además, emplea un bucle for para iterar sobre la lista de eliminados y el método .remove() para eliminar las direcciones IP correspondientes. Este enfoque modular y reutilizable facilita la gestión de accesos a contenido restringido en entornos de seguridad.

---

## Ejemplo de actividad de Portfolio: Actualizar un fichero mediante un algoritmo Python
- [Ejemplar completado](./resources/Exemplar---Update-a-file-through-a-Python-algorithm.docx)