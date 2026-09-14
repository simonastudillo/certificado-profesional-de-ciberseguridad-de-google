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