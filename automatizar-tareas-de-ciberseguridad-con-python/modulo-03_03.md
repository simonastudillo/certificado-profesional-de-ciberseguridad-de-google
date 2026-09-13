# Expresiones regulares

## Expresiones regulares en Python
- ​Aprenderemos a buscar patrones en cadenas mediante expresiones regulares.
- ​Una expresión regular, abreviada como regex ​, es una secuencia de caracteres que forma un patrón.
- ​Este patrón se puede utilizar al buscar en los archivos de registro.
- ​Podemos usarlos para buscar cualquier tipo de patrón.
- ​Por ejemplo, podemos encontrar todas las cadenas que comienzan con un determinado prefijo, ​o podemos encontrar todas las cadenas que tienen una longitud determinada.
- ​Podemos aplicar esto a un contexto de seguridad de varias maneras.
- ​Por ejemplo, supongamos que necesitamos encontrar todas las direcciones IP con un identificador ​de red de 184.
- Las expresiones regulares nos permitirían buscar este patrón de manera eficiente.
- ​Examinaremos otro ejemplo a lo largo de este vídeo.
- ​Supongamos que queremos extraer todas las direcciones de correo electrónico contenidas en un registro.
- ​Si intentamos hacerlo mediante el método de índice, ​necesitaremos las direcciones de correo electrónico exactas que estábamos buscando.
- ​Como analistas de seguridad, rara vez tenemos ese tipo de información.
- ​Pero si utilizamos una expresión regular que le diga a ​Python cómo está estructurada una dirección de correo electrónico, ​devolverá todas las cadenas que tienen los mismos elementos que una dirección de correo electrónico.
- ​Incluso si nos dieran un archivo de registro con miles de líneas y ​entradas, podríamos extraer todos los correos electrónicos del archivo buscando ​la estructura de una dirección de correo electrónico mediante una expresión regular.
- ​No necesitaríamos conocer los correos electrónicos específicos para extraerlos.
- ​Exploremos los símbolos de expresión regular que necesitamos para hacer esto.
- ​Para empezar, aprendamos sobre el signo más.
- ​El signo más es un símbolo de expresión regular que representa una o ​más apariciones de un carácter específico.
- ​Vamos a explicar esto con un patrón de ejemplo.
- ​El patrón de expresión regular a+ ​coincide con una cadena de cualquier longitud en la que se repite «a».
- ​Por ejemplo, solo una «a», tres «a» seguidas o ​cinco «a» seguidas.
- Incluso podrían ser 1000 «a» seguidas.
- ​Podemos empezar a trabajar con un ejemplo rápido para ver qué cadenas ​extraería este patrón.
- ​Empecemos con esta cadena de identificadores de dispositivos.
- ​Estas son todas las instancias de la letra «a» escritas una o varias veces seguidas.
- ​La primera instancia tiene una «a», la segunda tiene dos «a», ​la tercera tiene una «a» y la cuarta tiene tres «a».
- ​Por lo tanto, si le dijéramos a Python que busque coincidencias con la expresión regular del signo a+, ​devolvería esta lista de «a».
- ​El otro elemento básico que necesitamos es el símbolo \w.
- ​Coincide con cualquier carácter alfanumérico, ​pero no con los símbolos. «1", «k» e ​«i» son solo tres ejemplos de lo que coincide con «\ w».
- ​Las expresiones regulares se pueden combinar fácilmente para incluir ​aún más patrones en una búsqueda.
- ​Antes de aplicar esto a nuestro contexto de correo electrónico, exploremos ​los patrones que podemos buscar si combinamos la «\ w» con el signo más.
- ​«\ w» coincide con cualquier carácter alfanumérico y ​el signo más coincide con cualquier número de veces que aparezca el carácter anterior.
- ​Esto significa que la combinación de «\ w+» ​coincide con una cadena alfanumérica de cualquier longitud.
- ​«\ w» proporciona flexibilidad en los caracteres alfanuméricos con los que ​coincide esta expresión regular, ​y el signo más proporciona flexibilidad en la longitud de la cadena con la que coincide.
- ​Las cadenas «192", «abc123" y «security» son solo ​tres cadenas posibles que coinciden con «\ w+».
- ​Ahora vamos a aplicarlos para extraer direcciones de correo electrónico de un registro.
- ​Las direcciones de correo electrónico constan de texto separado por ciertos símbolos, ​como el símbolo @ y el punto.
- ​Aprendamos cómo podemos representar esto como una expresión regular.
- ​Para empezar, pensemos en el formato de una dirección de correo electrónico típica; ​por ejemplo, user1@email1.com.
- ​El primer segmento de una dirección de correo electrónico contiene caracteres alfanuméricos ​y la longitud del número de caracteres alfanuméricos puede variar.
- ​Podemos usar nuestra expresión regular «\ w+» para que ​esta parte coincida con una cadena alfanumérica de cualquier longitud.
- ​El siguiente segmento de una dirección de correo electrónico es el símbolo @.
- ​Este segmento siempre está presente.
- ​Ingresaremos esto directamente en nuestra expresión regular.
- Incluir esto es esencial ​para garantizar que Python distinga las direcciones de correo electrónico de otras cadenas.
- ​Tras el símbolo @ está el nombre de dominio.
- ​Al igual que el primer segmento, este varía según la dirección de correo electrónico, ​pero siempre contiene caracteres alfanuméricos, por lo que ​podemos volver a usar «\ w+» para permitir esta variación.
- ​A continuación, al igual que el símbolo @, ​un punto siempre forma parte de una dirección de correo electrónico.
- Pero a diferencia del símbolo @, ​en las expresiones regulares, el punto tiene un significado especial.
- ​Por esta razón, necesitamos usar el punto de barra invertida aquí.
- ​Cuando añadimos una barra invertida delante de ella, le ​hacemos saber a Python que no pretendemos usarla como operador ​y que nuestro patrón debe incluir un punto en esta ubicación.
- ​Para el último segmento, también podemos usar «\ w+».
- ​La parte final de una dirección de correo electrónico suele ser «com», pero ​puede incluir otras cadenas como «net».
- ​Cuando juntamos las piezas, ​obtenemos la expresión regular que usaremos para buscar las direcciones de correo electrónico en nuestra fila.
- ​Este patrón coincidirá con todas las direcciones de correo electrónico.
- ​Excluirá todo lo demás de nuestra cadena.
- ​Esto se debe a que hemos incluido el símbolo @ y ​el punto en el que aparecen en la estructura de una dirección de correo electrónico.
- ​Llevemos esto a Python. ​Usaremos expresiones regulares para extraer las direcciones de correo electrónico de una cadena.
- ​Las expresiones regulares se pueden usar cuando el módulo re se importa a Python, ​por lo que comenzamos con ese paso.
- Más adelante, ​aprenderemos cómo importar y abrir archivos como registros.
- ​Pero por ahora, hemos restaurado nuestro registro como una variable de cadena llamada email_log.
- ​Como se trata de una cadena de varias líneas, ​utilizamos tres conjuntos de comillas en lugar de solo uno.
- ​A continuación, aplicaremos la función findall () del módulo re a una expresión ​regular.
- re.findall () devuelve una lista de coincidencias con una expresión regular.
- ​Usemos esto con la expresión regular que creamos anteriormente para las direcciones de correo electrónico.
- ​El primer argumento es el patrón que queremos igualar.
- ​Observe que lo colocamos entre comillas.
- ​El segundo argumento indica dónde buscar el patrón.
- ​En este caso, estamos buscando en la cadena contenida en la ​variable de registro de correo electrónico.
- ​Cuando ejecutamos esto, obtenemos una lista de todos los correos electrónicos de la cadena.
- ​Imagine aplicar esto a un registro con miles de entradas.
- Bastante útil, ​¿verdad?
- [file](./resources/code/modulo-03_03-001.py)
- ​Esto fue solo una introducción al poder de las expresiones regulares.
- ​Hay muchos más símbolos que puedes usar.
- ​Te animo a que explores las expresiones regulares por tu cuenta y aprendas más. 

---

## Más información sobre expresiones regulares
- Conceptos básicos de las expresiones regulares
   - Una expresión regular (regex) es una secuencia de caracteres que forma un patrón.
   - En Python, puedes usar regex para buscar eficientemente patrones complejos como direcciones IP, correos electrónicos, o IDs de dispositivos dentro de cadenas.
   - Para acceder a las expresiones regulares y funciones relacionadas en Python, primero debe importar el módulo re.
   - Debe utilizar la siguiente línea de código para importar el módulo re:
      - `import re`
   - Las expresiones regulares se almacenan en Python como cadenas.
   - Luego, estas cadenas se utilizan en las funciones del módulo re para buscar en otras cadenas.
   - Hay muchas funciones en el módulo re, pero explorarás cómo funcionan las expresiones regulares a través de re.findall().
   - La función re.findall() devuelve una lista de coincidencias con una expresión regular.
   - Requiere dos parámetros.
   - El primero es la cadena que contiene el patrón de la expresión regular, y el segundo es la cadena en la que se desea buscar.
   - Los patrones que componen una expresión regular están formados por caracteres alfanuméricos y símbolos especiales.
   - Si un patrón de expresión regular está formado sólo por caracteres alfanuméricos, Python revisará la cadena especificada en busca de coincidencias con este patrón y las devolverá.
   - En el siguiente ejemplo, el primer parámetro es un patrón de expresión regular formado únicamente por los caracteres alfanuméricos "ts".
   - El segundo parámetro, "tsnow, tshah, bmoreno", es la cadena que buscará.
   - Puede ejecutar el siguiente código para explorar lo que devuelve:
   - [file](./resources/code/modulo-03_03-002.py)
   - La salida es una lista de sólo dos elementos, las dos coincidencias con "ts": ['ts', 'ts'].
   - Si desea hacer algo más que buscar cadenas específicas, debe incorporar símbolos especiales a sus expresiones regulares.

- Símbolos de expresiones regulares
   - Símbolos para tipos de caracteres
      - Puede utilizar diversos símbolos para formar un patrón para su expresión regular.
      - Algunos de estos símbolos identifican un tipo concreto de carácter.
      - Por ejemplo, \w coincide con cualquier carácter alfanumérico.
      - El símbolo \w también coincide con el guión bajo ( _ ).
      - Puede ejecutar este código para explorar lo que devuelve re.findall() al aplicar la expresión regular de "\w" al ID de dispositivo de "h32rb17".
      - [file](./resources/code/modulo-03_03-003.py)
      - Dado que cada carácter de este ID de dispositivo es un carácter alfanumérico, Python devuelve una lista con siete elementos.
      - Cada elemento representa uno de los caracteres del ID de dispositivo.
      - Estos símbolos coinciden con un único carácter de un tipo específico.

| Símbolo | Descripción | Ejemplo Match |
| ---- | ----------- | ------------- |
| \w | Coincide con cualquier carácter alfanumérico (A-z, 0-9) O un guión bajo (_). | En "ID_A17", coincide con I,D,_,A,1,7. |
| \d | Coincide con cualquier dígito (0-9). | En "ID_A17", coincide con 1,7. |
| \s | Coincide con cualquier carácter de espacio en blanco (espacio, tabulador, nueva línea). | En "usuario 1", coincide con el espacio. |
| . | Coincide con cualquier carácter (letras, dígitos, símbolos, espacios), excepto una nueva línea. | En "a.b", coincide con a, ., b. |
| \. | Coincide con el punto literal (.). La barra invertida \ es necesaria para escapar del significado especial del punto. | En "a.b", coincide con el punto. |

   - El siguiente código busca en el mismo ID de dispositivo que el ejemplo anterior, pero cambia el patrón de expresión regular a "\d".
   - Cuando lo ejecute, devolverá una lista diferente:
   - [file](./resources/code/modulo-03_03-004.py)
   - Esta vez, la lista contiene sólo cuatro elementos.
   - Cada elemento es uno de los dígitos numéricos de la cadena.

- Símbolos para cuantificar ocurrencias
   - Otros símbolos cuantifican el número de apariciones de un carácter específico en el patrón.
   - En un patrón de expresión regular, puede añadirlos después de un carácter o de un símbolo que identifique un tipo de carácter para especificar el número de repeticiones que coinciden con el patrón.

| Símbolo | Descripción | Ejemplo Match |
| ---- | ----------- | ------------- |
| + | Una o más repeticiones. (por ejemplo, \d+ coincide con 1,12,12345). | |
| * | Cero, una o más ocurrencias. | |
| {n} | Exactamente n ocurrencias. | \d{4} coincide con cuatro dígitos consecutivos (por ejemplo, 1234). |
| {m,n} | Entre m (mínimo) y n (máximo) ocurrencias. | \d{1,3} coincide con 1,12 ó 123. |

   - Por ejemplo, el símbolo + representa una o más apariciones consecutivas del carácter o tipo de carácter precedente.
   - Cuando se utiliza con \d+, encuentra coincidencias de uno o más dígitos en una fila, como 1, 12 o 123.
   - En el siguiente ejemplo, el patrón lo coloca después del símbolo \d para encontrar coincidencias con uno o más dígitos consecutivos:
   - [file](./resources/code/modulo-03_03-005.py)
   - Con la expresión regular "\d+", la lista contiene las dos coincidencias de "32" y "17".
   - Observe que + coincide con una secuencia de dígitos diferentes, no sólo con un dígito repetido.
   - Otro símbolo utilizado para cuantificar el número de ocurrencias es el símbolo *.
   - El símbolo * representa cero, una o más ocurrencias de un carácter específico.
   - El código siguiente sustituye el símbolo + utilizado en el ejemplo anterior por el símbolo *.
   - Puede ejecutarlo para examinar la diferencia:
   - [file](./resources/code/modulo-03_03-006.py)
   - Como también coincide con cero apariciones, la lista contiene ahora cadenas vacías para los caracteres que no eran de un solo dígito, así como una cadena vacía al final.
   - Si desea indicar un número específico de repeticiones permitidas, puede colocar este número entre llaves ({ }) después del carácter o símbolo.
   - En el siguiente ejemplo, el patrón de expresión regular "\d{2}" indica a Python que devuelva todas las coincidencias de exactamente dos dígitos simples en una fila de una cadena de varios ID de dispositivo:
   - [file](./resources/code/modulo-03_03-007.py)
   - Como coincide con dos repeticiones, cuando Python encuentra un dígito único, comprueba si hay otro a continuación.
   - Si lo hay, Python añade los dos dígitos a la lista y pasa al siguiente.
   - Si no, pasa al siguiente dígito sin añadir el primer dígito a la lista.
   - Python escanea las cadenas de izquierda a derecha cuando las compara con una expresión regular.
   - Cuando Python encuentra una parte de la cadena que coincide con el primer carácter esperado definido en la expresión regular, continúa comparando los caracteres siguientes con el patrón esperado.
   - Cuando el patrón está completo, comienza este proceso de nuevo en el carácter inmediatamente posterior a la coincidencia.
   - Así, en los casos en los que aparecen tres dígitos seguidos (por ejemplo, 123), \d{2} coincidiría con 12, y el proceso comenzaría de nuevo en el tercer dígito (3).
   - También puede especificar un intervalo dentro de las llaves separando dos números con una coma.
   - El primer número es el número mínimo de repeticiones y el segundo el número máximo de repeticiones.
   - El siguiente ejemplo devuelve todas las coincidencias que tienen entre una y tres repeticiones de un solo dígito:
   - [file](./resources/code/modulo-03_03-008.py)
   - La lista devuelta contiene elementos de un dígito como "0", dos dígitos como "32" y tres dígitos como "825".

- Construcción de un patrón
   - Para construir una expresión regular es necesario dividir el patrón buscado en partes más pequeñas y representarlas con los símbolos aprendidos.
   - Considere un ejemplo de una cadena que contiene múltiples piezas de información sobre los empleados de una organización.
   - Para cada empleado, la siguiente cadena contiene su ID de empleado, su nombre de usuario seguido de dos puntos (:), sus intentos de inicio de sesión del día y su departamento:
   - `employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"`
   - Su tarea es extraer el nombre de usuario y los intentos de inicio de sesión, sin el número de identificación del empleado ni el departamento.
   - Para completar esta tarea con expresiones regulares, debe dividir lo que está buscando en componentes más pequeños.
   - En este caso, esos componentes son el número variable de caracteres de un nombre de usuario, dos puntos, un espacio y un número variable de dígitos simples.
   - Los símbolos de expresión regular correspondientes son \w+, :, \s y \d+ respectivamente.
   - Utilizando estos símbolos como su expresión regular, puede ejecutar el siguiente código para extraer las cadenas:
   - [file](./resources/code/modulo-03_03-009.py)
   - Trabajar con expresiones regulares puede conllevar el riesgo de devolver información innecesaria o de excluir cadenas que desea devolver.
   - Por lo tanto, es útil probar las expresiones regulares.

---

## Actividad: Utilizar expresiones regulares para encontrar patrones
- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar el uso de expresiones regulares para extraer información en Python.
   - Se le presentará un escenario de Seguridad para que lo explore a lo largo del laboratorio.
   - Creará patrones de expresiones regulares y funciones para extraer información importante de cadenas.

- Lo que hará
   - Extraer IDs de dispositivos que contengan ciertos caracteres de un registro
   - Extraer todas las direcciones IP de un registro y compararlas con las direcciones IP marcadas en una Lista

- Scenario
   - Extracting device IDs containing certain characters from a log; these characters correspond with a certain operating system that requires an update.
   - Extracting all IP addresses from a log and then comparing them to those that are flagged in a list.

- Task 1
   - In order to work with regular expressions in Python, start by importing the re module.
   - This module contains many functions that will help you work with regular expressions.
   - By running the following code cell, the module will be available through the rest of the notebook.
   - [file](./resources/code/lab_09/task_01.py)

- Task 2
   - Currently, you are looking for device IDs that begin with "r15".
   - These characters indicate that the device is running an operating system that must be updated.
   - You're given a log of device IDs, stored in a variable named devices.
   - Your eventual goal is to extract the device IDs that start with the characters "r15".
   - For now, display the contents of the whole string to examine what it contains.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_02.py)

- Task 3
   - In this task, you'll write a pattern to find devices that start with the character combination of "r15".
   - Use the regular expression symbols \w and + to create the pattern, and store it as a string in a variable named target_pattern.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Note that the code cell will contain only variable assignments, so running it will not produce an output.
   - [file](./resources/code/lab_09/task_03.py)
   - What regular expression pattern did you use? For each component of the pattern, what would happen if it were missing?
   > The regular expression pattern used is "r15\w+". The "r15" part ensures that the device ID starts with "r15". The "\w" matches any alphanumeric character, and the "+" indicates that one or more of these characters should follow. If "r15" were missing, the pattern would match any device ID, not just those starting with "r15". If "\w" were missing, the pattern would only match "r15" exactly, without any additional characters. If "+" were missing, the pattern would only match "r15" followed by exactly one alphanumeric character.

- Task 4
   - Use the findall() function from the re module to find the device IDs that the target_pattern matches with.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - In order to use re.findall() in Tasks 4, 7, 8, 9 and 11, you must have previously run the code import re in Task 1.
   - [file](./resources/code/lab_09/task_04.py)

- Task 5
   - Now, the next task you're responsible for is analyzing a network security log file and determining which IP addresses have been flagged for unusual activity.
   - You're given the log file as a string stored in a variable named log_file.
   - There are some invalid IP addresses in the log file due to issues in data collection.
   - Your eventual goal is to use regular expressions to extract the valid IP addresses from the string.
   - Start by displaying the contents of the log_file to examine the details inside.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_05.py)

- Task 6
   - In this task, you'll build a regular expression pattern that you can use later on to extract IP addresses that are in the form of xxx.xxx.xxx.xxx.
   - In other words, you'll extract all IP addresses that contain four segments of three digits that are separated by periods.
   - Write a regular expression pattern that will match with these IP addresses and store it in a variable named pattern.
   - Use the regular expression symbols \d and \. in your pattern.
   - Note that the symbol \d matches with digits, in other words, any integer between 0 and 9.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code.
   - Since you'll just build the pattern here, there won't be any output when you run this cell.
   - [file](./resources/code/lab_09/task_06.py)

- Task 7
   - In this task, you'll use the re.findall() function on the regular expression pattern stored in the pattern variable and the provided log_file to extract the corresponding IP addresses.
   - Afterwards, run the cell and take note of what it outputs.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_07.py)
   - What are some examples of IP addresses that were extracted? What are some examples of IP addresses that were not extracted? Do any that were not extracted seem to be valid IP addresses?
   > Some examples of IP addresses that were extracted include '192.168.152.148', '192.168.190.178', '192.168.213.128', '192.168.247.153', '192.168.174.117', '192.168.148.115', '192.168.103.106', and '192.168.168.144'. Some examples of IP addresses that were not extracted include '1923.1689.3.24', '1924.1680.27.57', '1921.168.1283.75', and '19245.168.2345.49'. Among the IP addresses that were not extracted, none of them seem to be valid IP addresses as they do not follow the standard xxx.xxx.xxx.xxx format with each segment being a number between 0 and 255.

- Task 8
   - There are some valid IP addresses in the log_file that you haven't extracted yet.
   - This is because each segment of digits in a valid IP address can have anywhere between one and three digits.
   - Adjust the regular expression in the pattern to allow for variation in the number of digits in each segment.
   - You can do this by using the + symbol after the \d symbol.
   - Afterwards, use the updated pattern to extract remaining IP addresses.
   - Then, run the cell to analyze the results.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_08.py)
   - What gets extracted here? Do all extracted IP addresses have between one and three digits in every segment?
   > The extracted IP addresses include '192.168.152.148', '192.168.22.115', '192.168.190.178', '192.168.213.128', '192.168.96.200', '192.168.247.153', '192.168.174.117', '192.168.148.115', '192.168.103.106', and '192.168.168.144'. All extracted IP addresses have between one and three digits in every segment.

- Task 9
   - Note that all the IP addresses are now extracted but they also include invalid IP addresses with more than three digits per segment.
   - In this task, you'll update the pattern using curly brackets instead of the + symbol.
   - In regular expressions, curly brackets can be used to represent an exact number of repetitions between two numbers.
   - For example, {2,4} in a regular expression means between 2 and 4 occurrences of something.
   - Applying this to an example, \w{2,4} would match with two, three, or four alphanumeric characters.
   - Afterwards, you'll call the re.findall() function on the updated pattern and the log_file and store the output in a variable named valid_ip_addresses.
   - Then, display the contents of valid_ip_addresses and run the cell to analyze the results.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_09.py)
   - What do you notice about the extracted IP addresses here compared to those extracted in the previous two tasks?
   > The extracted IP addresses now only include valid IP addresses with each segment having between one and three digits. Invalid IP addresses with more than three digits per segment are excluded compared to the previous task.

- Task 10
   - Now, all of the valid IP addresses have been extracted.
   - The next step is to identify flagged IP addresses.
   - You're given a list of IP addresses that have been previously flagged for unusual activity, stored in a variable named flagged_addresses.
   - When these addresses are encountered, they should be investigated further.
   - This list is just for educational purposes and contains examples of private IP addresses that are found only within internal networks.
   - Display this list and examine what it contains by running the cell.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_10.py)

- Task 11
   - Finally, you will write an iterative statement that loops through the valid_ip_addresses list and checks if each IP address is flagged.
   - In the following code, the address will be the loop variable.
   - Also, include a conditional that checks if the address belongs to the flagged_addresses list.
   - If so, it should display "The IP address ______ has been flagged for further analysis."
   - If not, it should display "The IP address ______ does not require further analysis."
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_09/task_11.py)

- Conclusion
   - In this module, you learned how to extract valid IP addresses from a log file using regular expressions and how to identify flagged IP addresses for further analysis.
   - You also practiced using iterative statements and conditionals to analyze and respond to specific patterns in data.
   - This module provided hands-on experience with regular expressions, list operations, and control flow in Python, which are essential skills for automating cybersecurity tasks.
   - By completing this module, you have built a foundation for more advanced cybersecurity automation tasks using Python.

---

## Ejemplo: Utilizar expresiones regulares para encontrar patrones
- Mismo laboratorio que el anterior.

- Conclusion
   - Regular expressions in Python allow you to create patterns that you can then use to find important strings.
   - Regular expression patterns can be built to match specific characters and character combinations.
   - Examples of regular expression symbols practiced in this lab:
      - \w represents any alphanumeric character.
      - + represents one or more occurrences of the previous character in the regular expression.
      - \d represents any digit.
      - \. represents a period.
      - {x,y} represents anywhere between x and y number of occurrences of the previous character in the regular expression. The x and y can be replaced with any two positive integers to indicate an exact range for the number of occurrences.
   - The re module in Python contains functions that are useful when working with regular expressions.
      - One example is the re.findall() function, which takes in a regular expression pattern as well as a string, checks for all instances in the string that match with the pattern and outputs a list of the matches.

---

## Ponga a prueba sus Conocimientos: Expresiones regulares

1. ¿Qué símbolo de expresión regular representa una o más apariciones de un carácter específico?
   - [ ] \d
   - [x] +
   - [ ] *
   - [ ] \w
> El símbolo + representa una o varias apariciones de un carácter específico.

2. Como analista de Seguridad, usted es responsable de encontrar los ID de los empleados que terminan con la secuencia de caracteres y números "a6v". Dado que los ID de los empleados constan tanto de números como de caracteres alfabéticos y tienen una longitud mínima de cuatro caracteres, ¿qué patrón de expresión regular utilizaría?
   - [ ] "\wa6v"
   - [x] "\w+a6v"
   - [ ] "a6v"
   - [ ] "\w*a6v"
> La expresión regular "\w+a6v" coincide con cadenas que constan tanto de números como de caracteres alfabéticos, tienen al menos cuatro caracteres y terminan con la secuencia "a6v". Debe haber al menos otro carácter antes de "a6v", por lo que se necesita "\w+" para que coincida con uno o más caracteres alfanuméricos. Entonces, la secuencia final requerida es "a6v".

3. Ha importado el Módulo re en Python con el Código import re. Desea utilizar la función findall() para buscar a través de una cadena. ¿Qué llamada a la función le permite buscar a través de la cadena contenida en la variable text para devolver todas las coincidencias con una expresión regular almacenada en la variable pattern?
   - [ ] re.findall(text, pattern)
   - [ ] findall(text, pattern)
   - [x] re.findall(pattern, text)
   - [ ] findall(pattern, text)
> La llamada a la función re.findall(pattern, text) le permite hacerlo. La función re.findall() devuelve una lista de coincidencias con una expresión regular. Debe especificar que esta función procede del módulo re. El primer argumento es el patrón de expresión regular con el que desea obtener coincidencias. En este caso, se encuentra en la variable pattern. El segundo argumento indica dónde buscar este patrón. En este caso, se trata de la cadena asignada a la variable text. 

4. ¿Cuál de las siguientes cadenas devolvería Python como coincidencias con el patrón de expresión regular "\w+"? Seleccione todas las que correspondan
   - [ ] ""
   - [x] "3"
   - [x] "FirstName"
   - [ ] "#name"
> Las cadenas "3" y "FirstName" coinciden con el patrón de expresión regular "\w+". El símbolo \w coincide con cualquier carácter alfanumérico. Cuando se combina con el símbolo +, representa una o más apariciones de cualquier carácter alfanumérico. Dado que "3" es una cadena que contiene un carácter alfanumérico, coincide con la expresión regular.