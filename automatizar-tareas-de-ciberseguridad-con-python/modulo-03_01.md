# Trabajar con strings

## Bienvenido al Módulo 3
- ​Como analista de Seguridad, ​trabajará con una gran cantidad de datos.
- ​Es muy importante poder desarrollar soluciones para administrar estos datos.
- ​Lo que estamos a punto de aprender en ​Python le ayudará con eso.
- ​Anteriormente, sentamos ​las bases de lo que vamos a hacer en esta sección.
- ​Aprendimos todo sobre los tipos de datos y las variables.
- ​También abordamos las declaraciones condicionales e iterativas.
- ​Aprendimos a crear ​funciones e incluso creamos nuestras propias funciones.
- ​Aquí, nos basaremos en eso de diferentes maneras.
- ​En primer lugar, obtendrá más información sobre cómo ​trabajar con strings y listas.
- ​Ampliaremos las formas en las que ​puedes trabajar con estos tipos de datos, ​incluida la extracción de caracteres de ​strings o elementos de listas.
- ​Nuestro próximo objetivo es escribir algoritmos.
- ​Considerará un conjunto de reglas que se pueden aplicar en ​Python para resolver un problema relacionado con la seguridad.
- ​Por último, ampliaremos aún más las formas en las que podemos ​buscar strings cuando exploremos el uso de expresiones regulares.

---

## Operaciones con strings
- ​Saber cómo trabajar con ​los datos de string en seguridad es importante.
- ​Por ejemplo, puede que se encuentre trabajando con ​nombres de usuario para encontrar patrones en la información de inicio de sesión.
- ​Vamos a revisar ​el tipo de datos de string y aprender ​cómo trabajar con él en Python.
- ​Primero, vamos a hacer un rápido repaso a las strings.
- ​Definimos los datos de string como ​datos que consisten en una secuencia ordenada de caracteres.
- ​En Python, las strings se ​escriben entre comillas.
- ​Puede utilizar comillas dobles o simples, ​pero en este curso, hemos ​utilizado comillas dobles.
- ​Como ejemplos, tenemos las strings "Hola", ​"123", y "¡Número 1!"
- ​También hemos tratado anteriormente las variables.
- ​Aquí, la variable mi_string ​está almacenando actualmente la string "Seguridad".
- ​También puede crear una string a partir de otro tipo de datos, ​como un entero o un flotante.
- ​Para ello, necesitamos introducir ​una nueva función integrada, la función string.
- ​La función string es una función que ​convierte el objeto de entrada en una string.
- ​Convertir objetos en strings nos permite ​realizar tareas que sólo son posibles para strings.
- ​Por ejemplo, podríamos convertir un entero en ​una string para eliminar elementos de ella o para reordenarla.
- ​Ambas cosas son difíciles para un tipo de datos entero.
- ​Practiquemos la conversión de un entero a una string.
- ​Aplicaremos la función string al entero 123.
- ​Ahora, la variable string_nueva ​contiene una string de tres caracteres: ​1, 2 y 3.
- ​Imprimamos su tipo para comprobarlo.
- ​Ejecutémoslo. ¡Perfecto, nos dice ​que ahora tenemos una string!
- [file](./resources/code/modulo-03_01-001.py)
- Hasta ahora, ​conocemos distintas formas de crear y almacenar una string.
- ​Ahora, vamos a explorar cómo ​realizar algunas operaciones básicas con strings.
- ​Nuestro primer ejemplo es la función de longitud.
- ​La función de longitud es una función que ​devuelve el número de elementos de un objeto.
- ​Usándola en una string nos dice ​cuántos caracteres tiene la string.
- ​Al principio del programa, ​aprendimos que las direcciones IP tienen ​dos versiones, IPv4 o IPv6.
- ​Las direcciones IPv4 tienen un máximo de 15 caracteres.
- ​Así que un profesional de la seguridad podría utilizar ​la función de longitud para comprobar si una dirección IPv4 es válida.
- ​Si su longitud es superior a 15 caracteres, ​entonces sabríamos que se trata de una dirección IPv4 no válida.
- ​Usemos esta función para imprimir ​la longitud de la string "Hola" ​Anidaremos la función longitud ​dentro de la función imprimir porque ​queremos calcular primero la longitud de ​esta string y luego imprimirla en la pantalla.
- ​Muy bien, vamos a ejecutar esto y comprobar ​cuántos caracteres cuenta Python.
- ​La salida es 5, ​uno por cada letra de la palabra Hola.
- [file](./resources/code/modulo-03_01-002.py)
- ​También podemos utilizar el operador de suma en las strings.
- ​Esto se llama concatenación de strings.
- ​La concatenación de strings es ​el proceso de unir dos strings.
- ​Por ejemplo, podemos sumar ​las strings "Hola" y "mundo".
- ​Para concatenar strings, podemos utilizar el símbolo +.
- ​Después de ejecutarlo, ​obtenemos "Helloworld" con ​sin espacios entre las dos strings.
- ​Es importante tener en cuenta que ​algunos operadores no funcionan con strings.
- ​Por ejemplo, no se puede utilizar ​un signo menos para restar las dos strings.
- ​Por último, vamos a hablar de los métodos de string.
- ​Un método es una función ​que pertenece a un tipo de datos específico.
- ​Por lo tanto, utilizar un método de string en otro tipo de datos, ​como un entero, provocaría un error.
- ​A diferencia de otras funciones, los métodos aparecen después de la string.
- ​Dos métodos de string comunes son ​los métodos superior e inferior.
- ​El método superior devuelve una copia de ​la string en todas las letras mayúsculas.
- ​Apliquemos el método superior a la string "Hola"
- ​Colocaremos esto dentro de ​una función de impresión para que salga por la pantalla.
- ​Centrémonos en la sintaxis Única de los métodos.
- ​Después de nuestra string "Hola", ​colocamos un punto o una coma, ​y luego especificamos el método que queremos utilizar.
- ​Aquí, es upper()
- ​Bien, ahora estamos listos para ejecutar esto.
- ​HELLO se imprime en la pantalla en todas las letras mayúsculas.
- ​De forma similar, el método lower devuelve ​una copia de la string en todas las letras minúsculas.
- ​Apliquemos el método lower a la string "Hola".
- ​Recordemos que tenemos que poner la string y el método ​dentro de una función print para imprimir los resultados.
- ​Y ahora, tenemos la string ​impresa en todas las letras minúsculas.
- [file](./resources/code/modulo-03_01-003.py)

---

## Índices y cortes de string
- ​En Seguridad, hay varias ​razones por las que podríamos necesitar buscar en una string.
- ​Por ejemplo, es posible que necesitemos ​localizar un nombre de usuario en un registro de Seguridad.
- ​O bien, si descubrimos que ​una dirección IP determinada está asociada a un software malicioso, es ​posible que busquemos esta dirección en un registro de red.
- ​Y el primer paso para poder usar Python de ​esta manera es aprender ​sobre el índice de caracteres de una string.
- ​El índice es un número asignado a ​cada elemento de una secuencia que indica su posición.
- ​​Por lo tanto, el índice es ​la posición de cada carácter en una string.
- ​Empecemos con la string «HELLO».
- A ​cada carácter de la string se le asigna un índice.
- ​En Python, empezamos a contar los índices desde 0.
- ​Por lo tanto, el carácter «H» tiene un índice de 0, ​y «E» tiene un índice de 1, y así sucesivamente.
- ​Llevemos esto a Python y practiquemos el uso de índices.
- ​Al colocar un índice entre corchetes después de ​una string, se devuelve el carácter de ese índice.
- ​Coloquemos el índice 1 ​entre corchetes después de «HOLA» y ejecutémoslo.
- ​Esto devolvió el carácter «E».
- ​Recuerde que los índices comienzan en 0, ​por lo que un índice de 1 no es el primer carácter de la palabra.
- ​Pero, ¿y si queremos que ​devuelva más de un caracter?
- ​Podemos extraer una mayor parte de ​una string especificando un conjunto de índices.
- ​Esto se denomina rebanada.
- ​Al tomar un sector de una string, ​especificamos dónde ​comienza el sector y dónde termina el sector.
- ​Por lo tanto, proporcionamos dos índices.
- ​El primer índice es el principio, ​que se incluye en la salida.
- ​El segundo índice es el final, ​pero no se incluye en el resultado final.
- ​En su lugar, Python detiene ​el segmento en el elemento anterior al segundo índice.
- ​Por ejemplo, si quisiéramos tomar las letras E-L-L ​de «HOLA», ​comenzaríamos el intervalo desde el índice 1, ​pero terminaríamos antes del índice 4.
- ​Probemos este ejemplo y ​extraigamos un segmento de una string en Python.
- ​Escribamos la string y tomemos el segmento que comienza ​en el índice 1 y termina antes del índice 4.
- ​Ahora, ejecutemos el código y examinemos el resultado. 
- ​Ahí está la porción que queríamos.
- [file](./resources/code/modulo-03_01-004.py)
- ​Ahora que sabemos cómo describir ​la ubicación de un carácter en una string, ​aprendamos cómo buscar en una string.
- ​Para hacer esto, necesitamos usar el método index.
- ​El método index busca la primera aparición de ​la entrada en una string y devuelve su ubicación.
- ​Practiquemos el uso del método index en Python.
- ​Supongamos que queremos usar el método index ​para encontrar el carácter «E» en la string «HELLO».
- ​Localizaremos la primera instancia ​del carácter «E».
- Examinemos esta línea con más detalle.
- ​Después de escribir la string y el método index, ​usamos el carácter que queremos ​encontrar como argumento del método index.
- ​Recuerda que las strings en Python distinguen entre mayúsculas y minúsculas, ​por lo que ​debemos asegurarnos de usar las mayúsculas y minúsculas apropiadas con el método index.
- ​Vamos a ejecutar este código ahora.
- ​Esto devolvió el número 1.
- ​Esto se debe a que «E» tiene un valor de índice de 1.
- [file](./resources/code/modulo-03_01-005.py)
- ​Ahora, exploremos un ejemplo en el ​que un carácter se repite varias veces en la string.
- ​Intentemos buscar ​el carácter «L».
- Empezamos con un código similar al anterior, ​pasando el argumento «L» en lugar de «E» al método index.
- ​Ahora, ejecutemos este código e investiguemos el resultado.
- ​El resultado es el índice 2.
- ​Esto nos indica que el método solo ​identificó la primera aparición ​del carácter «L» y no la segunda.
- ​Este es un detalle importante a tener en ​cuenta cuando se trabaja con el método index.
- [file](./resources/code/modulo-03_01-006.py)
- ​Como analista de Seguridad, ​aprender a trabajar con índices ​te permite encontrar ciertas partes de una string.
- ​Por ejemplo, si necesitas encontrar ​la ubicación del símbolo @ en un correo electrónico, ​puedes usar el método index para encontrar ​lo que buscas con una línea de código.
- ​Ahora vamos a centrar nuestra atención ​en una propiedad importante de los strings.
- ​¿Alguna vez has escuchado la expresión ​«algunas cosas nunca cambian»?
- ​Se podría decir acerca de ​la sensación cómoda que tienes con un buen amigo, ​incluso cuando hace mucho que no lo ves.
- ​Bueno, en Python, también podemos decir esto acerca de las strings.
- ​Las strings son inmutables.
- ​En Python, «inmutable» significa que ​no se puede cambiar una vez ​creado y asignado un valor.
- ​Vamos a desglosar esto con un ejemplo.
- ​Vamos a asignar la string «HELLO» a la variable my_string.
- ​Ahora, si queremos cambiar el carácter «E» por una «A» para ​que my_string tenga el valor «HALLO», ​entonces podríamos optar por usar la notación de índice.
- ​Pero aquí tenemos un error. ​My_string es inmutable, por lo que no podemos ​hacer cambios como este.
- ​Acabas de aprender a indexar y dividir strings. ​También has visto que las strings son inmutables.
- ​No puede reasignar caracteres ​después de que se haya definido una string.
- [file](./resources/code/modulo-03_01-007.py)

---

## Strings y el analista de Seguridad
- Datos de strings en un entorno de seguridad
   - Como analista, los datos de string son uno de los tipos de datos más comunes que encontrará en Python.
   - Datos de string son datos que consisten en una secuencia ordenada de caracteres.
   - Se utiliza para almacenar cualquier tipo de información que no necesite manipular matemáticamente (como mediante una división o una resta).
   - En un contexto de ciberseguridad, esto incluye direcciones IP, nombres de usuario, URL e identificaciones de empleados.
   - Tendrá que trabajar con estos strings de varias maneras.
   - Por ejemplo, podría extraer ciertas partes de una dirección IP, o podría verificar si los nombres de usuario cumplen los criterios requeridos.

- Trabajar con índices en strings

- Índices
   - Un índice es un número asignado a cada elemento de una secuencia que indica su posición.
   - En el caso de las strings, esto significa que cada carácter de la string tiene su propio índice.
   - Los índices comienzan en 0.
   - Por ejemplo, podría estar trabajando con esta string que contiene un identificador de dispositivo: "h32rb17".
   - La siguiente tabla indica el índice de cada carácter de esta string:

| Carácter | índice | índice negativo |
|----------|--------|-----------------|
| h        | 0      | -7              |
| 3        | 1      | -6              |
| 2        | 2      | -5              |
| r        | 3      | -4              |
| b        | 4      | -3              |
| 1        | 5      | -2              |
| 7        | 6      | -1              |

- Notación entre corchetes
   - La notación entre corchetes se refiere a los índices colocados entre corchetes.
   - Puede utilizar la notación entre corchetes para extraer una parte de una string.
   - Por ejemplo, el primer carácter del ID del dispositivo puede representar una determinada característica del mismo.
   - Si desea extraerla, puede utilizar la notación entre corchetes para ello: `device_id = "h32rb17"`, `device_id[0]`
   - En ambos casos, la notación entre corchetes da como resultado el carácter h cuando esta notación entre corchetes se coloca dentro de una función print().
   - Puede observar esto ejecutando el siguiente código:
   - [file](./resources/code/modulo-03_01-008.py)
   - También puede tomar una rebanada de una string.
   - Cuando toma un slice de una string, extrae más de un carácter de ella.
   - Suele hacerse en contextos de ciberseguridad cuando sólo le interesa una parte específica de una string.
   - Por ejemplo, podrían ser ciertos números de una dirección IP o ciertas partes de una URL.
   - En el ejemplo de la identificación del dispositivo, podría necesitar los tres primeros caracteres para determinar una calidad concreta del dispositivo.
   - Para ello, puede tomar un trozo de la string utilizando la notación entre corchetes.
   - Puede ejecutar esta línea de código para observar que da salida a "h32":
   - [file](./resources/code/modulo-03_01-009.py)

- Funciones y métodos de string
   - Las funciones str() y len() son útiles para trabajar con strings.
   - También puede aplicar métodos a las strings, como los métodos .upper(), .lower() y .index().
   - Un método es una función que pertenece a un tipo de datos específico.

- str() y len()
   - La función str() convierte su objeto de entrada en una string.
   - Como analista, podría utilizarla en los registros de Seguridad cuando trabaje con IDs numéricos que no vayan a ser utilizados con procesos matemáticos.
   - Convertir un número entero en una string le da la posibilidad de buscar en ella y extraer trozos de la misma.
   - Considere el ejemplo de un ID de empleado 19329302 que necesita convertir en una string.
   - Puede utilizar la siguiente línea de programación para convertirlo en una string y almacenarlo en una variable: `string_id = str(19329302)`
   - La segunda función que aprendió para strings es la función len(), que devuelve el número de elementos de un objeto.
   - Por ejemplo, si desea verificar que el ID de un determinado dispositivo cumple la norma de contener siete caracteres, puede utilizar la función len() y un condicional.
   - Cuando ejecute el código siguiente, imprimirá un mensaje si "h32rb17" tiene siete caracteres:
   - [file](./resources/code/modulo-03_01-010.py)

- .upper() y .lower()
   - El método .upper() devuelve una copia de la string con todos sus caracteres en mayúsculas.
   - Por ejemplo, puede cambiar el nombre de este departamento a todo en mayúsculas ejecutando el código "Information Technology".upper().
   - Devolvería la string "INFORMATION TECHNOLOGY".
   - Mientras tanto, el método .lower() devuelve una copia de la string con todos sus caracteres en minúsculas.
   - "Information Technology".lower() devolvería la string "information technology".

- .index()
   - El método .index()  encuentra la primera aparición de la entrada en una string y devuelve su ubicación.
   - Por ejemplo, este Código utiliza el método .index() para encontrar la primera aparición del carácter "r" en el ID del dispositivo "h32rb17":
   - [file](./resources/code/modulo-03_01-011.py)
   - El método .index() devuelve 3 porque la primera aparición del carácter "r" se encuentra en el índice 3.
   - En otros casos, es posible que no se encuentre la entrada.
   - Cuando esto ocurre, Python devuelve un error.
   - Por ejemplo, el Código print("h32rb17".index("a")) devuelve un error porque "a" no se encuentra en la string "h32rb17".
   - Tenga en cuenta también que si una string contiene más de una instancia de un carácter, sólo se devolverá la primera.
   - Por ejemplo, el identificador de dispositivo "r45rt46" contiene dos instancias de "r". Puede ejecutar el siguiente código para explorar su resultado:
   - [file](./resources/code/modulo-03_01-012.py)
   - La salida es 0 porque .index() devuelve sólo la primera instancia de "r", que se encuentra en el índice 0.
   - La instancia de "r" en el índice 3 no se devuelve.

- Encontrar substrings con .index()
   - Una Substring es una secuencia continua de caracteres dentro de una string.
   - Por ejemplo, "llo" es una substring de "hello".
   - El método .index() también puede utilizarse para encontrar el índice de la primera aparición de una substring.
   - Devuelve el índice del primer carácter de esa substring.
   - Considere este ejemplo que encuentra la primera instancia del usuario "tshah" en una string:
   - [file](./resources/code/modulo-03_01-013.py)
   - El método .index() devuelve el índice 7, que es donde empieza la substring "tshah".
   - Cuando utilice el método .index() para buscar substrings, debe tener cuidado.
   - En el ejemplo anterior, quiere localizar la instancia de "tshah". 
   - Si busca sólo "ts", Python le devolverá 0 en lugar de 7 porque "ts" también es una substring de "tsnow".

---

## Practique: Trabajar con valores índice
- Review a series of code examples and match them to the right character, slice, or index. Note that code examples may wrap on your screen.

|  Code example | Extracted Character |
|---------------|--------------------|
| "Security"[2:5] | "cur" |
| "Security"[1] | "e" |
| "Security"[0] | "S" |
| "Security"[2:4] | "cu" |
| str_var = "encryption" str_var[0] | "e" |
| str_var = "encryption" str_var[5:7] | "pt" |
| str_var = "encryption" str_var[3:6] | "ryp" |
| str_var = "encryption" str_var[1] | "n" |
| "system".index("s") | 0 |
| "system".index("y") | 1 |
| "system".index("t") | 3 |
| "system".index("e") | 4 |

---

## Actividad: Trabajar con cadenas en Python

- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar el trabajo con datos de Cadena en Python.
   - Se le presentará un escenario de seguridad para que lo explore a lo largo del laboratorio.
   - Practicará la creación de código Python que involucre cadenas relacionadas con IDs de empleados, IDs de dispositivos y URLs.

- Lo que hará
   - Utilizar las funciones str() y len() y para concatenar datos de cadenas relacionados con los ID de los empleados
   - Utilizar la notación de corchetes para extraer los componentes de un ID de dispositivo
   - Utilizar la notación de corchetes y el método .index() para extraer componentes de una URL

- Scenario
   - You're working as a security analyst, and you are responsible for writing programs in Python to automate updating employee IDs, extracting characters from a device ID, and extracting components from a URL.

- Task 1
   - In your organization, employee IDs are currently either four digits or five digits in length.
   - In this task, you're given a four-digit numeric employee ID stored in a variable called employee_id.
   - Convert this to a string format and store the result in the same variable.
   - Later, you'll update this employee ID string so that it complies with a new standardized format.
   - Complete the following code. Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_01.py)
   - What do you observe about the data type of employee_id the first time it's displayed? What do you observe about the data type of employee_id the second time it's displayed (after the variable is reassigned)?
   > The first time, the data type of employee_id is <class 'int'>. The second time, after converting it to a string, the data type is <class 'str'>.

- Task 2
   - Imagine that you have just been informed of a new criteria for employee IDs.
   - They must all be five digits long for standardization purposes.
   - In this task, you will write a conditional statement that displays a message if the length of the employee ID is less than five digits.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_02.py)

- Task 3
   - In this task, you'll build upon the previous code.
   - If an employee ID is only four digits, you'll use concatenation to create a five-digit employee ID number.
   - Concatenation is a process that allows you to merge strings together.
   - The addition operator (+) in Python allows you to concatenate two strings.
   - Write an if statement that evaluates whether the length of employee_id is less than 5.
   - When the condition evaluates to True, reassign employee_id by concatenating "E" in front of the four-digit employee ID to create a five character employee ID.
   - Then, display employee_id again.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_03.py)

- Task 4
   - Now you'll move on to the next part of your task.
   - Imagine that the characters in a device ID convey technical information about the device.
   - You'll need to extract characters in specific positions from the device ID.
   - Start off by extracting the fourth character.
   - The variable device_id represents a device ID containing alphanumeric characters; it's already stored as a string.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_04.py)

- Task 5
   - Now you will also need to extract the first through the third characters in the device ID.
   - So take a slice of the device ID. You can achieve this using bracket notation in Python.
   - Then, display the slice to examine the result.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_05.py)

- Task 6
   - You'll now proceed to the last part of your task.
   -  This involves extracting components of a URL.
   - You'll work with string indices to display various components of a URL that's stored in the URL variable.
   - First, you'll extract and display the protocol of the URL and the :// characters that follow it using string slicing.
   - Consider that the protocol is in the secure format of https when determining the indices for your slice.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_06.py)

- Task 7
   - Later in this lab, you'll extract the domain extension.
   - To prepare for this, use the .index() method to identify the index where the domain extension .com is located in the given URL.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_07.py)

- Task 8
   - It's a good idea to save important data in variables when programming.
   - This allows for quick and easy tracking and reuse of information.
   - Store the output of the .index() method in a variable called ind, which is short for index.
   - This index represents the position where the domain extension ".com" starts in the url.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Note that running this cell will not produce an output.
   - [file](./resources/code/lab_07/task_08.py)

- Task 9
   - You can use string slicing to also extract the domain extension of a URL.
   - To do so, you can create a slice.
   - The starting index should be the ind variable.
   - This contains the index where the domain extension begins.
   - The ending index should be ind + 4 (since ".com" is four characters long).
   - Sometimes, like in this situation, it's easier to express the ending index in relation to the starting index.
   - Examine the following code, run it as is, and observe the output.
   - [file](./resources/code/lab_07/task_09.py)
   - What does this code output and why?
   > The code outputs ".com" because the slice starts at the index where ".com" begins and ends four characters later, capturing the entire domain extension.

- Task 10
   - Finally, extract the website name from the given URL using string slicing and the ind variable that you defined earlier.
   - In the given URL, the website name is "exampleURL1".
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_07/task_10.py)

- Conclusion
   - In this lab, you learned how to extract different components of a URL using string slicing and the `.index()` method.
   - You also learned how to store important indices in variables for easier reuse and readability.
   - You practiced extracting specific parts of a URL, such as the protocol, domain name, and domain extension, using string slicing and indices.
   - You reinforced your understanding of how to manipulate and extract information from strings in Python.