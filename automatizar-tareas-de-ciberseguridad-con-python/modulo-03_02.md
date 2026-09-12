# Trabajar con listas y desarrollar algoritmos

## Operaciones de Lista en Python
- ​Otro tipo de datos del que hemos hablado anteriormente es la lista.
- ​Las listas son útiles porque le permiten ​almacenar múltiples datos en una sola variable.
- ​En la profesión de la seguridad, trabajará con una gran variedad de listas.
- ​Por ejemplo, puede tener una lista de direcciones IP que han accedido a una red, y ​otra lista puede contener información sobre aplicaciones que ​tienen bloqueada su ejecución en el sistema.
- ​Recapitulemos cómo crear una lista en Python.
- En este caso, ​los elementos de nuestra lista son las letras de la A a la E.
- ​Los separamos mediante comas y los rodeamos de corchetes.
- ​También podemos asignar nuestra lista a una variable para facilitar su uso posterior.
- ​Aquí, hemos llamado a nuestra variable mi_lista.
- ​Cuando accedemos a elementos específicos de las listas, ​utilizamos una sintaxis similar a cuando accedemos a los elementos específicos de las cadenas.
- ​Colocamos su valor de índice entre paréntesis después de la variable que almacena la lista.
- ​Así accederíamos al segundo elemento de la lista.
- ​Esto se debe a que en Python, ​empezamos a contar los elementos de la lista en cero y no en uno.
- ​Así que el índice del primer elemento es cero y ​el índice del segundo elemento es uno.
- ​Intentemos extraer algunos elementos de una lista.
- ​Extraeremos el segundo elemento poniendo 1 entre paréntesis después de la variable.
- ​Colocamos esto en una función print() para dar salida a los resultados, y ​después de ejecutarla, Python da salida a la letra "b".
- [file](./resources/code/modulo-03_02-001.py)
- ​Al igual que con las cadenas, también podemos concatenar listas con el signo más.
- ​La concatenación de listas consiste en combinar dos listas en una colocando ​los elementos de la segunda lista directamente después de los elementos de la primera.
- ​Trabajemos con esto en Python.
- Vamos a concatenar dos listas.
- ​Primero, definimos la misma lista que en el ejemplo anterior y ​la almacenamos en la variable mi_lista.
- ​Ahora, vamos a definir una lista adicional con los números del 1 al 4.
- ​Por último, vamos a concatenar las dos listas con un signo más y ​imprimimos el resultado.
- Y cuando lo ejecutamos, tenemos una lista concatenada final.
- [file](./resources/code/modulo-03_02-002.py)
- ​Habiendo discutido las similitudes, ​exploremos ahora las diferencias entre las listas y las cadenas.
- ​Hemos mencionado antes que las cadenas son inmutables, lo que significa ​que, una vez definidas, no pueden modificarse.
- ​Las listas, por otro lado, no tienen esta propiedad, y ​podemos cambiar, añadir y eliminar libremente valores de la lista.
- ​Así, por ejemplo, si tenemos una lista de direcciones IP maliciosas, ​entonces cada vez que se identifique una nueva dirección IP maliciosa, ​podemos añadirla fácilmente a la lista.
- ​Intentemos primero cambiar un elemento específico de una lista en Python.
- Empezaremos con ​la lista utilizada en el ejemplo anterior.
- Para cambiar un elemento de una lista, ​combinamos lo que hemos aprendido sobre la notación entre corchetes ​con lo que hemos aprendido sobre la asignación de variables.
- ​Cambiemos el segundo elemento de mi_lista, ​que es la Cadena "b", por el número 7.
- ​Colocamos el objeto que queremos cambiar en el lado izquierdo de ​la asignación de variables.
- ​En este caso, cambiaremos el segundo elemento de mi_lista.
- ​A continuación, colocamos un signo igual para indicar ​que estamos reasignando este elemento de la lista.
- ​Por último, colocamos el objeto que ocupará su lugar en el lado derecho.
- ​Aquí, reasignaremos el segundo elemento de la lista a un valor de 7.
- ​Ahora imprimamos la lista y ejecutemos el código para examinar el cambio.
- La letra "b" se ha cambiado ahora por el número 7.
- [file](./resources/code/modulo-03_02-003.py)
- ​Ahora, echemos un vistazo a los métodos para insertar y eliminar elementos en las listas.
- ​El primer método con el que trabajaremos en este vídeo es el método de inserción.
- ​El método de inserción añade un elemento en una posición específica ​dentro de una lista.
- El Método toma dos argumentos: ​el primero es la posición en la que vamos a añadir el elemento, y ​el segundo es el elemento que queremos añadir.
- Utilicemos el método insert.
- ​Empezaremos con la lista que hemos definido en nuestra variable my_list.
- ​Entonces escribimos my_list.insert y le pasamos dos argumentos.
- ​El primer argumento es la posición en la que queremos insertar ​la nueva información.
- En este caso, queremos insertar en el índice 1.
- ​El segundo argumento es la información que queremos añadir ​a la lista; en este caso, el número entero 7.
- ​Ahora imprimamos mi_lista. Nuestra lista sigue empezando con "a", ​el elemento con índice 0, ​y ahora, tenemos el entero 7 en la siguiente posición, ​la posición representada con índice 1.
- ​Note que la letra "b", que originalmente estaba en el índice 1, ​no se sustituye como cuando utilizamos la notación de corchetes.
- ​Con el método de inserción, ​cada elemento más allá del índice 1 simplemente se desplaza ​una posición hacia abajo.
- El índice de "b" es ahora 2.
- [file](./resources/code/modulo-03_02-004.py)
- ​A veces puede que queramos eliminar de una lista un elemento que ya no es ​necesario.
- Para ello, podemos utilizar el método remove.
- ​El método removed ​elimina la primera aparición de un elemento específico en la lista.
- ​A diferencia de insert, el argumento de removed no es un valor de índice.
- ​En su lugar, se escribe directamente el elemento que se desea eliminar.
- ​El método remove elimina la primera instancia del mismo en la lista.
- ​Utilicemos el método remove para eliminar la letra "d" de nuestra lista.
- ​Escribiremos el nombre de nuestra variable mi_lista y, a continuación, añadiremos el método remove.
- ​Queremos eliminar "d "de esta lista.
- Así que, ​la pondremos entre comillas ​como nuestro argumento. Luego imprimiremos mi_lista.
- ​Y vamos a ejecutar esto. Perfecto "d" ha sido eliminada de la lista.
- ​Al igual que con las cadenas, ser capaz de buscar en listas ​es una habilidad necesaria para los analistas de Seguridad.
- [file](./resources/code/modulo-03_02-005.py)

---

## Escriba un algoritmo sencillo
- ​En nuestra vida cotidiana, ​con frecuencia seguimos reglas para resolver problemas.
- ​Como ejemplo sencillo, ​imagine que quiere una taza de café.
- ​Si ha hecho café muchas veces, ​entonces es probable que siga un proceso para prepararlo.
- ​Primero, coge su taza favorita.
- ​Luego, pone agua en ​la cafetera y añade los posos del café.
- ​Pulsa el botón de inicio y espera unos minutos.
- ​Por último, disfruta de su taza de café recién hecho.
- ​Incluso si tiene un enfoque diferente para ​hacer café o no bebe café en absoluto, ​es probable que siga un conjunto de reglas ​para completar tareas cotidianas similares.
- ​Cuando completa estas tareas rutinarias, ​está siguiendo un algoritmo.
- ​Un algoritmo es un conjunto de reglas que resuelven un problema.
- ​En más detalle, un algoritmo es un conjunto ​de pasos que toma una entrada de un problema, ​utiliza esta entrada para realizar tareas, ​y devuelve una solución como salida.
- ​Exploremos cómo los algoritmos ​pueden utilizarse para resolver problemas en Python.
- ​Imagine que usted, como analista de Seguridad, ​tiene una lista de direcciones IP.
- ​Quiere extraer ​los tres primeros dígitos de cada dirección IP, ​lo que le dará información sobre ​las redes a las que pertenecen estas direcciones IP.
- ​Para ello, vamos a escribir un algoritmo que ​involucra múltiples conceptos de Python ​que hemos cubierto hasta ahora: ​bucles, listas y cadenas.
- ​Aquí tiene una lista con direcciones IP ​que están almacenadas como cadenas.
- ​Por razones de privacidad, en nuestro ejemplo, ​no vamos a mostrar las direcciones IP completas.
- ​Nuestro objetivo es extraer los tres primeros números ​de cada dirección y almacenarlos en una nueva lista.
- ​Antes de escribir cualquier código Python, ​vamos a desglosar un enfoque para ​resolver este problema con un algoritmo.
- ​¿Qué pasaría si tuviera una dirección IP en lugar de una lista entera?
- ​Bueno, entonces el problema se simplifica mucho.
- ​El primer paso para resolver ​el problema será utilizar el troceado de cadenas ​para extraer los tres primeros dígitos ​de una dirección IP.
- ​Ahora consideremos cómo aplicarlos a una lista entera.
- ​Como segundo paso, ​utilizaremos un bucle para aplicar ​esa solución a cada dirección IP de la lista.
- ​Previamente, ha aprendido sobre el corte de cadenas, ​así que vamos a escribir algo de código Python ​para resolver el problema para una dirección IP.
- ​Aquí vamos a empezar con una dirección IP ​que comienza por 198.567.
- ​Y escribiremos unas líneas de código para ​extraer los tres primeros caracteres.
- ​Usaremos la notación entre corchetes para trocear la cadena.
- ​Dentro de la sentencia print, ​tenemos la variable address, ​que contiene la dirección IP que queremos trocear.
- ​Recuerde que Python empieza a contar en 0.
- ​Para obtener los tres primeros caracteres, ​empezamos nuestro corte en el índice 0 ​y continuamos hasta el índice 3.
- ​Recuerde, que Python excluye el índice final.
- ​En otras palabras, Python ​devolverá los caracteres en los índices 0, ​1 y 2.
- ​Ahora, vamos a ejecutar esto. ​Obtenemos los tres primeros dígitos de la dirección: 198.
- [file](resources/code/modulo-03_02-006.py)
- ​Ahora que somos capaces de resolver ​este problema para una dirección IP, ​podemos poner este código en un bucle y ​aplicarlo a todas las direcciones IP de la lista original.
- ​Antes de hacerlo, ​introduzcamos un método más que utilizaremos ​en este código: el método append.
- ​El método append añade entradas al final de una lista.
- ​Por ejemplo, digamos que mi lista contiene 1, ​2 y 3.
- ​Con este código, podemos utilizar ​el método append para añadir 4 a esta lista.
- ​Primero, se nos da la lista de IP.
- ​Ahora, estamos listos para extraer ​los tres primeros caracteres de ​cada elemento de esta lista.
- ​Creemos una lista vacía para almacenar ​los tres primeros caracteres de cada IP de la lista.
- ​Ahora podemos empezar el bucle for.
- ​Dividamos esto. ​La palabra "for" le dice a Python ​que estamos a punto de iniciar un bucle for.
- ​Entonces elegimos dirección ​como variable dentro del bucle for, ​y especificamos la lista llamada IP como iterable.
- ​A medida que el bucle se ejecuta, ​cada elemento de la lista IP será ​almacenado temporalmente en la variable dirección.
- ​Dentro del bucle for, ​tenemos una línea de código para añadir ​el trozo de dirección a la lista de redes.
- ​Desglosando esto, usamos el código que escribimos ​antes para obtener los tres primeros caracteres ​de una dirección IP.
- ​Usaremos nuestro método append ​para añadir un elemento al final de una lista.
- ​En este caso, estamos añadiendo a la lista de redes.
- ​Por último, imprimamos la lista de redes y ejecutemos el código.
- ​La variable networks contiene ahora una lista de ​los tres primeros dígitos de ​cada dirección IP de la lista original: IP
- ​Eso ha sido un montón de Información. ​Diseñar algoritmos puede ser todo un reto.
- ​Es una buena idea dividirlos en ​problemas más pequeños antes de lanzarse a escribir su código.
- [file](resources/code/modulo-03_02-007.py)

---

## Listas y el analista de Seguridad
- Datos de lista en un entorno de seguridad
   - Como analista de Seguridad, trabajará frecuentemente con listas en Python.
   - Datos de lista es una estructura de datos que consiste en una colección de datos en forma secuencial.
   - Puede utilizar listas para almacenar múltiples elementos en una única variable.
   - Una sola lista puede contener múltiples tipos de datos.
   - En un contexto de ciberseguridad, las listas pueden utilizarse para almacenar nombres de usuario, direcciones IP, URL, ID de dispositivos y datos.
   - Colocar datos dentro de una lista le permite trabajar con ellos de diversas maneras.
   - Por ejemplo, podría iterar a través de una lista de ID de dispositivos utilizando un bucle for para realizar las mismas acciones para todos los elementos de la lista.
   - Podría incorporar una sentencia condicional para realizar estas acciones sólo si los ID de dispositivo cumplen determinadas condiciones. 

- Trabajar con índices en listas

- Índices
   - Al igual que las cadenas, puede trabajar con listas a través de sus índices, y los índices comienzan en 0.
   - En una lista, se asigna un índice a cada elemento de la lista.
   - Esta tabla contiene el índice de cada elemento de la lista ["elarson", "fgarcia", "tshah", "sgilmore"]:

| Elemento | Índice |
|----------|--------|
| elarson  | 0      |
| fgarcia  | 1      |
| tshah    | 2      |
| sgilmore | 3      |

- Notación entre corchetes
   - De forma similar a las cadenas, puede utilizar la notación entre corchetes para extraer elementos o trozos de una lista.
   - Para extraer un elemento de una lista, después de la lista o de la variable que la contiene, añada corchetes que contengan el índice del elemento.
   - El siguiente ejemplo extrae el elemento con índice 2 de la variable username_list y lo imprime.
   - Puede ejecutar este código para examinar su resultado:
   - [file](resources/code/modulo-03_02-008.py)
   - Este ejemplo extrae el elemento con índice 2 directamente de la lista:
   - [file](resources/code/modulo-03_02-008.py)

- Extracción de un trozo de una lista
   - Al igual que con las cadenas, también es posible utilizar la notación entre corchetes para extraer un trozo de una lista.
   - Con las listas, esto significa extraer más de un elemento de la lista.
   - Cuando se extrae un trozo de una lista, el resultado es otra lista.
   - Esta lista extraída se denomina sublista porque forma parte de la lista original, más grande.
   - Para extraer una sublista utilizando la notación entre corchetes, debe incluir dos índices.
   - Puede ejecutar el siguiente código que toma un trozo de una lista y explorar la sublista que devuelve:
   - [file](resources/code/modulo-03_02-009.py)
   - El código devuelve una sublista de ["elarson", "fgarcia"].
   - Esto se debe a que el elemento en el índice 0, "elarson", está incluido en la rebanada, pero el elemento en el índice 2, "tshah", está excluido.
   - La rebanada termina un elemento antes de este índice.

- Cambio de los elementos de una lista
   - A diferencia de las cadenas, también puede utilizar la notación entre corchetes para cambiar los elementos de una lista.
   - Esto se debe a que una cadena es inmutable y no puede cambiarse después de crearla y asignarle un valor, pero las listas no son inmutables.
   - Para cambiar un elemento de la lista, utilice una sintaxis similar a la que utilizaría al reasignar una variable, pero coloque el elemento específico que desea cambiar entre corchetes después del nombre de la variable.
   - Por ejemplo, el siguiente Código cambia el elemento en el índice 1 de la variable username_list a "bmoreno".
   - [file](resources/code/modulo-03_02-010.py)
   - Este código ha actualizado el elemento en el índice 1 de "fgarcia" a "bmoreno".

- Métodos de lista
   - Los métodos de lista son funciones específicas del tipo de datos de lista.
   - Entre ellos se incluyen .insert(), .remove(), .append() y .index().

- .insert()
   - El método .insert() añade un elemento en una posición específica dentro de una lista.
   - Tiene dos parámetros.
   - El primero es el índice donde insertará el nuevo elemento, y el segundo es el elemento que desea insertar.
   - Puede ejecutar el siguiente código para explorar cómo se puede utilizar este método para insertar un nuevo nombre de usuario en una lista de nombres de usuario:
   - [file](resources/code/modulo-03_02-011.py)
   - Como el primer parámetro es 2 y el segundo es "wjaffrey", "wjaffrey" se inserta en el índice 2, que es la tercera posición.
   - Los demás elementos de la lista se desplazan una posición en la lista.
   - Por ejemplo, "tshah" se encontraba originalmente en el índice 2 y ahora se encuentra en el índice 3.

- .remove()
   - El método .remove() elimina la primera aparición de un elemento específico en una lista.
   - Sólo tiene un parámetro, el elemento que desea eliminar.
   - El siguiente código elimina "elarson" de la lista username_list:
   - [file](resources/code/modulo-03_02-012.py)
   - Este código elimina "elarson" de la lista.
   - Los elementos que siguen a "elarson" se desplazan todos una posición más cerca del principio de la lista.
   - Si hay dos del mismo elemento en una lista, el método .remove() sólo elimina la primera instancia de ese elemento y no todas las apariciones.

- .append()
   - El método .append() añade un elemento al final de una lista.
   - Su único parámetro es el elemento que desea añadir al final de la lista.
   - Por ejemplo, podría utilizar .append() para añadir "btang" al final de username_list:
   - [file](resources/code/modulo-03_02-013.py)
   - Este código coloca "btang" al final de username_list, y todos los demás elementos permanecen en sus posiciones originales.
   - El Método .append() se utiliza a menudo con los bucles for para rellenar una lista vacía con elementos.
   - Puede explorar cómo funciona esto con el siguiente código:
   - [file](resources/code/modulo-03_02-014.py)
   - Antes del bucle for, la variable numbers_list no contiene ningún elemento.
   - Cuando se imprime, aparece la lista vacía.
   - A continuación, el bucle for itera a través de una secuencia de números y utiliza el método .append() para añadir cada uno de estos números a numbers_list.
   - Después del bucle, cuando se imprime la variable numbers_list, muestra estos números.

- .index()
   - Similar al método .index() utilizado para cadenas, el método .index() utilizado para listas encuentra la primera aparición de un elemento en una lista y devuelve su índice.
   - Toma como entrada el elemento buscado.
   - Aunque tiene el mismo nombre y uso que el método .index() utilizado para cadenas, el método .index() utilizado para listas no es el mismo método.
   - Los métodos se definen al definir un tipo de datos, y como las cadenas y las listas se definen de forma diferente, los métodos también son diferentes.
   - Utilizando la variable username_list, puede utilizar el método .index() para encontrar el índice del nombre de usuario "tshah":
   - [file](resources/code/modulo-03_02-015.py)
   - Como el índice de "tshah" es 2, se obtiene este número.
   - Al igual que el método .index() utilizado para las cadenas, sólo devuelve el índice de la primera aparición de un elemento de lista.
   - Así, si el nombre de usuario "tshah" se repitiera dos veces, devolvería el índice de la primera instancia, y no el de la segunda.

---

## Actividad: Desarrollar un algoritmo

- Lo que hará
   - Utilizar los métodos .append() y .remove() para gestionar una lista de usuarios y una lista de dispositivos de usuario
   - Indicar si un usuario está aprobado para acceder al sistema
   - Trabajar con índices y con el método .index() para determinar si un dispositivo específico corresponde a un usuario específico

- Introduction
   - An algorithm is a set of steps that can be used to solve a problem.
   - Security analysts develop algorithms to provide the solutions that they need for their work.
   - For example, an analyst may work with users who bring them devices.
   - The analyst may need an algorithm that first checks if a user is approved to access the system and then checks if the device that they have brought is the one assigned to them.
   - In this lab, you'll develop an algorithm in Python that automates this process.

- Scenario
   - In this lab, you're working as a security analyst and you're responsible for developing an algorithm that connects users to their assigned devices.
   - You'll write code that indicates if a user is approved on the system and has brought their assigned device to the security team.

- Task 1
   - You'll work with a list of approved usernames along with a list of the approved devices assigned to these users.
   - The elements of the two lists are synchronized.
   - In other words, the user at index 0 in approved_users uses the device at index 0 in approved_devices.
   - Later, this will allow you to verify if the username and device ID entered by a user correspond to each other.
   - First, to explore how indices in lists work, run the following code cell as is and observe the output.
   - Then, replace each 0 with another index and run the cell to observe what happens.
   - [file](./resources/code/lab_08/task_01.py)
   - What did you observe about the output when approved_users[0] is displayed and when approved_devices[0] is displayed? What happens when you replace each 0 with another index?
   > When approved_users[0] is displayed, it shows the first username in the list. When approved_devices[0] is displayed, it shows the first device ID in the list. Replacing 0 with another index displays the corresponding elements at that index in both lists.

- Task 2
   - There's a new employee joining the organization, and they need to be provided with a username and device ID.
   - In the following code cell, you are given a username and device ID of this new user, stored in the variables new_user and new_device, respectively.
   - Use the .append() method to add these variables to the approved_users and approved_devices respectively.
   - Afterwards, display the approved_users and approved_devices variables to confirm the added information.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_02.py)
   - After the new approved user is added, what did you observe about the output when approved_users is displayed and when approved_devices is displayed?
   > After the new approved user is added, the output shows the updated lists with the new user's username appended to approved_users and the new device ID appended to approved_devices.

- Task 3
   - An employee has left the team and should no longer have access to the system.
   - In the following code cell, you are given the username and device ID of the user to be removed, stored in the variables removed_user and removed_device respectively.
   - Use the .remove() method to remove each of these elements from the corresponding list.
   - Afterwards, display both the approved_users and the approved_devices variables to view the removed users.
   - Run the code and observe the results.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_03.py)
   - After the user who left the team is removed, what did you observe about the output when approved_users is displayed and when approved_devices is displayed?
   > After the user who left the team is removed, the output shows the updated lists with the removed user's username no longer in approved_users and the removed device ID no longer in approved_devices.

- Task 4
   - As part of verifying a user's identity in the system, you'll need to check if the user is one of the approved users.
   - Write a conditional statement that verifies if a given username is an element of the list of approved usernames.
   - If it is, display "The user ______ is approved to access the system.".
   - Otherwise, display "The user ______ is not approved to access the system.".
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_04.py)
   - What message do you observe in the output when username is "sgilmore"?
   > The user sgilmore is approved to access the system.

- Task 5
   - The next part of the algorithm uses the .index() method to find the index of username in the approved_users and store that index in a variable named ind.
   - When used on a list, the .index() method will return the position of the given value in the list.
   - Add a statement to display ind in the following code cell to explore the value it contains.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_05.py)
   - What do you observe from the output when username is "sgilmore"?
   > The output shows the index of "sgilmore" in the approved_users list, which is 2.

- Task 6
   - This task will allow you to build your understanding of list operations for the algorithm that you'll eventually build.
   - It will demonstrate how you can find an index in one list and then use this index to display connected information in another list.
   - First, use the .index() method again to find the index of username in the approved_users and store that in a variable named ind.
   - Then, connect ind to the approved_devices and display the device ID located at the index ind.
   - Afterwards, run the cell to observe the result.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_06.py)
   - What do you observe from the output when username is "sgilmore"?
   > The output shows the device ID corresponding to "sgilmore" in the approved_devices list, which is "4n482ts".

- Task 7
   - Your next step in creating the algorithm is to determine if a username and device ID correspond.
   - To do this, write a conditional that checks if the username is an element of the approved_devices and if the device_id stored at the same index as username matches the device_id entered.
   - You'll use the logical operator and to connect the two conditions.
   - When both conditions evaluate to True, display a message that the username is approved and another message that the user has their assigned device.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_07.py)
   - What do you observe from the output when username is "sgilmore" and device_id is "4n482ts"?
   > The output shows that the username "sgilmore" is approved to access the system and that "4n482ts" is the assigned device for "sgilmore".

- Task 8
   - It would also be helpful for users to receive messages when their username is not approved or their device ID is incorrect.
   - Add to the code by writing an elif statement.
   - This elif statement should run when the username is part of the approved_users but the device_id doesn't match the corresponding device ID in the approved_devices.
   - The statement should also display two messages conveying that information.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - (After you run the code once with a device_id of "4n482ts", you might want to explore what happens if you assign a different value to device_id.)
   - [file](./resources/code/lab_08/task_08.py)
   - What do you observe from the output when username is "sgilmore" and device_id is "4n482ts"?
   > The output shows that the username "sgilmore" is approved to access the system and that "4n482ts" is the assigned device for "sgilmore".

- Task 9
   - In this task, you'll complete your algorithm by developing a function that uses some of the code you've written in earlier tasks.
   - This will automate the login process.
   - There are multiple ways to use conditionals to automate the login process.
   - In the following code, a nested conditional is used to achieve the goals of the algorithm.
   - There is a conditional statement inside of another conditional statement.
   - The outer conditional handles the case when the username is approved and the case when username is not approved.
   - The inner conditional, which is placed inside the first if statement, handles the case when the username is approved and the device_id is correct, as well as the case when the username is approved and the device_id is incorrect.
   - To complete this task, you must define a function named login that takes in two parameters, username and device_id.
   - Afterwards, call the function and pass in different username and device ID combinations to experiment and observe the function's behavior.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_08/task_09.py)
   - After Python enters the inner conditional, what happens when the device_id is correct, and what happens when the device_id is incorrect?
   > When the device_id is correct, the function displays a message indicating that the device is the assigned device for the username. When the device_id is incorrect, the function displays a message indicating that the device is not the assigned device for the username.

- Conclusion
   - This module demonstrated how to use conditionals and nested conditionals to control the flow of a program based on user input, specifically for a login system that checks both usernames and device IDs.
   - It also highlighted the importance of providing clear feedback to users when their login attempts fail due to unapproved usernames or incorrect device IDs.
   - Overall, it reinforced the concept of using nested conditionals to handle complex decision-making scenarios in Python programs.
   - It emphasized the practical application of nested conditionals in real-world scenarios, such as managing access control based on multiple criteria.

---

## Ejemplar: Desarrollar un algoritmo
- Mismo laboratorio que el anterior

- Conclusion
   - Indexing a list is similar to indexing a string. Index values start at 0.
   - The .append() method helps you add new elements to the end of lists.
   - The .remove() method helps you remove elements from lists.
   - The .index() method can be used on different types of sequences. They can be used not only with strings, but also with lists.
   - With a list, the .index() method allows you to identify the position where a specified element is located in that list.
   - If two lists contain information that correspond to each other in a specific order, you can use indices to pair elements from the lists together.
   - Functions can be used to develop algorithms. When defining a function, you must specify the parameters it takes in and the actions it should execute.

---

## Ponga a prueba sus Conocimientos: Trabaje con listas y desarrolle algoritmos

1. Revise el siguiente código:
```python
my_list = ["a", "b", "c", "d"]
my_list[2] = 4
print(my_list)
```
- ¿Qué mostrará?
   - [x] ["a", "b", 4, "d"]
   - [ ] Un mensaje de error
   - [ ] ["a", "b", "4", "d"]
   - [ ] ["a", 4, "c", "d"]
> El Código mostrará ["a", "b", 4, "d"]. Reasigna el elemento my_list al índice 2. Se trata del tercer elemento de la lista, por lo que "c" se sustituye por el entero 4.

2. Está trabajando con la lista ["cwvQSQ","QvPvX5","ISyT3a","S7vgN0"]. Sus elementos representan IDs de máquinas, y la lista se almacena en una variable llamada machine_ids. ¿Qué línea de código añadirá el ID de "yihhLL" en el índice 3?
   - [ ] machine_ids.append("yihhLL")
   - [x] machine_ids.insert(3,"yihhLL")
   - [ ] machine_ids.append("yihhLL",3)
   - [ ] machine_ids.insert("yihhLL",3)
> El Código machine_ids.insert(3,"yihhLL") añadirá el ID de "yihhLL" en el índice 3. El método .insert() añade un elemento en una posición específica dentro de una lista. Recibe dos parámetros. El primero indica el índice en el que desea añadir un nuevo elemento, y el segundo indica el elemento que desea añadir.

3. ¿Qué línea de programación eliminará el nombre de usuario "tshah" de la siguiente Lista? `access_list = ["elarson", "bmoreno", "tshah", "sgilmore"]`
   - [x] access_list.remove("tshah")
   - [ ] access_list["tshah"].remove()
   - [ ] access_list.remove(2)
   - [ ] access_list.remove(3)
> El código access_list.remove("tshah") eliminará el nombre de usuario "tshah" de la lista. El método .remove() elimina la primera aparición de un elemento específico en una lista. Toma como argumento el elemento a eliminar, así access_list.remove("tshah") elimina el nombre de usuario "tshah".

4. Como analista de Seguridad, usted es responsable de desarrollar un algoritmo que automatice la eliminación de nombres de usuario que coincidan con criterios específicos de una lista de acceso. ¿Qué componentes de Python le ayudarían a implementarlo? Seleccione tres respuestas
   - [ ] El método .append() 
   - [x] Una declaración if que compara un nombre de usuario con los criterios de eliminación
   - [x] Un Bucle for que itera a través de los nombres de usuario de la Lista de acceso
   - [x] El método .remove() 
> El algoritmo debe iterar a través de los nombres de usuario en una Lista de accesibilidad. En cada iteración, debe comprobar si el nombre de usuario actual coincide con los criterios específicos y eliminarlo cuando así sea. La sentencia if comprueba si el nombre de usuario actual coincide con los criterios específicos.