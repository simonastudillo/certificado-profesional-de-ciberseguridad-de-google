# Sentencias condicionales e iterativas

## Sentencias condicionales en Python
- La ​automatización es el uso de la tecnología para reducir el ​esfuerzo humano y manual para realizar tareas comunes y repetitivas.
- ​Permite que las computadoras realicen estas tareas por nosotros para ​que podamos dedicar más tiempo a nuestras vidas a realizar otras actividades.
- ​Las declaraciones condicionales son importantes para la automatización.
- ​Una sentencia condicional es una sentencia que evalúa el código ​para determinar si cumple un conjunto específico de condiciones.
- ​La palabra clave `if` es importante en las declaraciones condicionales.
- `if` inicia una declaración condicional.
- Después de esta palabra clave, ​especificamos la condición que debe cumplirse y qué pasará si se cumple.
- ​Usamos declaraciones `if` todos los días.
- Por ejemplo, si hace frío afuera, ​usaremos una chaqueta.
- O si está lloviendo, llevaremos un paraguas.
- `if` las sentencias están estructuradas con la condición que queremos evaluar y ​la acción que Python realizará si se cumple esta condición.
- ​Python siempre evalúa si la condición es verdadera o falsa y, ​si es verdadera, realiza la acción específica.
- ​Exploremos un ejemplo de esto.
- Daremos instrucciones a Python para que imprima un ​mensaje de «cuenta bloqueada» siempre que los intentos fallidos de inicio de sesión superen más de cinco.
- Nuestra palabra clave `if` le dice a Python que inicie una declaración condicional.
- Tras esto, ​indicamos la condición que queremos comprobar.
- ​En este caso, estamos comprobando si el usuario ha realizado más de cinco intentos fallidos de inicio de sesión.
- ​Observe cómo utilizamos una variable llamada failed_attempts.
- ​En nuestro código completo, ​habremos asignado un valor a failed_attempts antes de esta sentencia `if` a.
- ​Después de esta afección, siempre colocamos un colon.
- ​Esto indica que lo que sigue es lo que queremos que suceda cuando se cumpla la condición. 
- ​En este caso, cuando el usuario tiene más de cinco intentos fallidos de inicio de sesión, ​imprime un mensaje que indica que la cuenta está bloqueada.
- ​En Python, este mensaje siempre debe estar indentado ​en al menos un espacio para que se ejecute solo cuando la condición sea verdadera.
- ​Es habitual denominar «cabecera» a esta primera línea y ​denominar «cuerpo» a las acciones que se producen cuando se cumple la condición.
- ​Esta condición se basaba en que una variable era mayor que un número específico, ​pero podemos definir nuestra condición mediante una variedad de operadores.
- [file example](./resources/code/modulo-01_04-001.py)
- ​Por ejemplo, también podemos comprobar si algo es «menor que» ​un valor específico, o podemos comprobar si es «mayor que» o ​«igual a» o «menor o igual que» el valor.
- ​También podemos comparar si algo es igual a un valor.
- ​Cuando hacemos esto dentro de un condicional, necesitamos usar una sintaxis especial.
- ​No es solo el signo igual, sino un doble igual.
- ​El doble signo igual es un operador importante que se utiliza con frecuencia en ​las sentencias condicionales.
- ​Un valor doble igual evalúa si dos objetos coinciden.
- ​Asigna un valor Booleano de Verdadero cuando coinciden y Falso cuando no coinciden.
- ​Hay un operador más del que deberíamos hablar.
- Un signo de exclamación ​seguido de un signo igual representa la condición de «no igual».
- ​Este operador de «no igual» evalúa si dos objetos son diferentes.
- ​Asigna un valor Booleano de ​Verdadero cuando no coinciden y False cuando coinciden.
- ​Investiguemos más de cerca un ejemplo que usa el doble signo igual.
- ​Nos centraremos en un ejemplo que imprime un ​mensaje de «se necesitan actualizaciones» cuando se está ejecutando un sistema operativo en particular.
- ​En este caso, hemos creado una condición que comprueba si el ​sistema operativo de un dispositivo coincide con una cadena específica que identifica este sistema operativo.
- ​Para ello, necesitaremos usar el doble signo igual en nuestra condición.
- ​Cuando coincida, nuestro programa imprimirá un mensaje indicando que se necesitan actualizaciones.
- ​La variable operating_system está a la izquierda del doble signo igual.
- ​La cadena «OS 2" está a la derecha.
- ​Si la condición se evalúa como Verdadera, ​realiza la acción que está indentada en la siguiente línea de código.
- ​Aquí, si el sistema_operativo es OS 2, imprimirá «actualizaciones necesarias».
- ​Si es False, el mensaje no se imprimirá.
- ​Observe cómo está indentada esta línea.
- Esto le indica a Python que ​la tarea depende de que la sentencia if se evalúe como True.
- [File example](./resources/code/modulo-01_04-002.py)
- ​Ahora escribamos un código que incorpore este condicional y obtengamos los resultados.
- ​Antes de escribir la sentencia condicional, ​necesitamos asignar un valor a la variable de nuestro sistema operativo.
- ​Haremos que este valor sea el mismo que el del sistema operativo que comprobaremos ​en el condicional.
- ​A continuación, escribiremos la condición de nuestra sentencia if y usaremos el doble ​signo igual para comprobar si la variable operating_system es equivalente a OS 2.
- ​Ahora escribiremos la acción que ejecutaremos si la condición de la ​línea anterior se evalúa como Verdadera.
- Le ​diremos a Python que imprima un mensaje de «se necesitan actualizaciones».
- ​Como configuramos nuestra variable operating_system en OS 2, se ejecutará la sentencia print.
- ​Vale, vamos a ejecutar esto.
- ​Como era de esperar, imprimió «actualizaciones necesarias» porque el valor ​asignado a la variable operating_system era igual a OS 2.
- [File example](./resources/code/modulo-01_04-002.py)
- ​A veces, queremos que nuestras sentencias condicionales ejecuten otro ​conjunto de instrucciones en caso de que nuestra primera condición no sea verdadera.
- ​En nuestro ejemplo, si no ​es True significa que el dispositivo ejecuta un sistema operativo que no es OS 2.
- ​Aquí es cuando necesitamos incorporar ​la palabra clave else en nuestras declaraciones condicionales.
- ​else precede a una sección de código que solo se evalúa cuando todas las condiciones que ​lo preceden en la declaración condicional se evalúan como False.
- ​las sentencias else siempre van seguidas de una sentencia if y terminan en dos puntos.
- ​Usemos nuestro condicional anterior y agreguemos una sentencia else.
- ​Hemos incluido la misma sentencia if, ​pero esta vez configuramos la variable del sistema operativo ​para que contenga un sistema operativo diferente, OS 3.
- ​Como no coincide con el valor de la condición de la ​instrucción if, el mensaje «se necesitan actualizaciones» no se imprimirá.
- ​Pero podemos añadir una declaración diferente y decirle que haga otra cosa en su lugar.
- ​Escribimos la palabra clave else seguida de dos puntos.
- A continuación, hacemos una sangría en la siguiente línea ​y le pedimos que imprima el mensaje «no se necesitan actualizaciones».
- ​Cuando ejecutamos este código, procesa la sentencia else después de la sentencia if.
- ​Como nuestra sentencia if se evaluará como ​False, pasará a la instrucción «else».
- ​Vamos a intentarlo.
- ​Como era de esperar, solo imprime el mensaje «no se necesitan actualizaciones».
- [File example](./resources/code/modulo-01_04-002.py)

---

## Más sobre condicionales en Python
- Cómo funcionan las sentencias condicionales
   - Una sentencia condicional es una sentencia que evalúa el código para determinar si cumple un conjunto específico de condiciones.
   - Cuando se cumple una condición, se evalúa a un valor booleano de True y realiza las acciones especificadas.
   - Cuando la condición no se cumple, evalúa un valor booleano de False y no realiza las acciones especificadas. 
   - En las sentencias condicionales, la condición suele basarse en la comparación de dos valores.
   - Esta tabla resume los operadores de comparación más comunes utilizados para comparar valores numéricos.
   - Los operadores igual a (==) y no igual a (!=) también se utilizan habitualmente para comparar datos de cadenas.

| Operador | Uso |
| --- | --- |
| > | mayor que |
| < | menor que |
| >= | mayor que o igual a |
| <= | menor o igual que |
| == | igual a |
| != | no igual a |

- sentencias if
   - La palabra clave if inicia una sentencia condicional.
   - Es un componente necesario de cualquier sentencia condicional.
   - En el siguiente ejemplo, if inicia una sentencia que indica a Python que imprima un mensaje "OK" cuando el código de estado de la respuesta HTTP sea igual a 200:
   - [file example](./resources/code/modulo-01_04-003.py)
   - Este código consta de una cabecera y un cuerpo.

- Encabezado de una sentencia if
   - La primera línea de este código es el encabezado.
   - En la cabecera de una sentencia if, la palabra clave if va seguida de la condición.
   - Aquí, la condición es que la variable status sea igual a un valor de 200.
   - La condición puede colocarse entre paréntesis:
   - [file example](./resources/code/modulo-01_04-003.py)
   - En casos como éste, colocar paréntesis alrededor de las condiciones en Python es opcional.
   - Puede incluirlos si le ayuda con la legibilidad del código.
   - Sin embargo, esta condición se procesará de la misma manera si se escribe sin paréntesis.
   - En otras situaciones, debido a que Python evalúa primero las condiciones entre paréntesis, los paréntesis pueden afectar a la forma en que Python procesa las condiciones.
   - Leerá más sobre una de ellas en la sección de esta lectura sobre not.
   - Siempre debe colocar dos puntos (:) al final del encabezado.
   - Sin esta sintaxis, el código producirá un error.

- El cuerpo de una sentencia if
   - Después del encabezado de una sentencia if viene el cuerpo de la sentencia if.
   - Esto le dice a Python qué acción o acciones debe realizar cuando la condición se evalúa a True.
   - En este ejemplo, sólo hay una acción, imprimir "OK" en la pantalla.
   - En otros casos, puede haber más líneas de programación con acciones adicionales.
   - Para que el cuerpo de la sentencia if se ejecute según lo previsto, debe tener una sangría mayor que la de la cabecera.
   - Además, si hay varias líneas de código dentro del cuerpo, todas deben tener una sangría coherente.

- Continuación de condicionales con else y elif
   - En el ejemplo anterior, si el código de respuesta de estado HTTP no fuera igual a 200, la condición se evaluaría como False y Python continuaría con el resto del programa.
   - Sin embargo, también es posible especificar acciones alternativas con else y elif.

- Sentencias else
   - La palabra clave else precede a una sección de código que sólo se evalúa cuando todas las condiciones que la preceden dentro de la sentencia condicional se evalúan a False.
   - En el siguiente ejemplo, cuando el código de estado de la respuesta HTTP no es igual a 200, imprime un mensaje alternativo de "check other status":
   - [file example](./resources/code/modulo-01_04-004.py)
   - Al igual que con if, se requieren dos puntos (:) después de else, y el cuerpo que sigue al encabezado else está sangrado.

- Sentencias elif
   - En algunos casos, puede tener múltiples acciones alternativas que dependen de nuevas condiciones.
   - En ese caso, puede utilizar elif.
   - La palabra clave elif precede a una condición que sólo se evalúa cuando las condiciones previas se evalúan a False.
   - A diferencia de else, puede haber múltiples sentencias elif a continuación de if.
   - Por ejemplo, es posible que desee imprimir un mensaje si el código de estado de respuesta HTTP es 200, otro mensaje si es 400, y otro si es 500.
   - El siguiente código demuestra cómo puede utilizar elif para ello:
   - [file example](./resources/code/modulo-01_04-005.py)
   - Python comprobará primero si el valor de status es 200, y si éste se evalúa como False, pasará a la primera sentencia elif.
   - Allí, comprobará si el valor de status es 400.
   - Si se evalúa como True, imprimirá "Bad Request", pero si se evalúa como False, pasará a la siguiente sentencia elif.
   - Si desea que el código imprima otro mensaje cuando todas las condiciones se evalúen a False, entonces puede incorporar else después de la última elif.
   - En este ejemplo, si llega a la sentencia else, imprime un mensaje para comprobar el estado:
   - [file example](./resources/code/modulo-01_04-006.py)
   - Al igual que con if y else, es importante colocar dos puntos (:) después del encabezado elif y aplicar una sangría al código que sigue a este encabezado.
   - Python procesa las sentencias elif múltiples de forma diferente a las sentencias if múltiples.
   - Cuando llega a una sentencia elif que se evalúa como True, no comprobará las siguientes sentencias elif.
   - En cambio, Python ejecutará todas las sentencias if.

- Operadores lógicos para condiciones múltiples
   - En algunos casos, puede querer que Python realice una acción basándose en una condición más compleja.
   - Podría requerir que dos condiciones se evalúen en True.
   - O puede necesitar que sólo una de las dos condiciones se evalúe en True.
   - O puede que quiera que Python realice una acción cuando una condición se evalúe a False.
   - Los operadores and, or, y not se pueden utilizar en estos casos.

- AND
   - El operador and requiere que ambas condiciones a ambos lados del operador se evalúen a True.
   - Por ejemplo, todos los códigos de estado HTTP entre 200 y 226 se refieren a respuestas satisfactorias.
   - Puede utilizar and para unir una condición de ser mayor o igual que 200 con otra condición de ser menor o igual que 226:
   - [file example](./resources/code/modulo-01_04-007.py)
   - Si ambas condiciones son True, se imprimirá el mensaje "successful response".

- OR
   - El operador or requiere que sólo una de las condiciones a ambos lados del operador se evalúe como True.
   - Por ejemplo, tanto un código de estado de 100 como un código de estado de 102 son respuestas informativas.
   - Utilizando or, podría pedir a Python que imprima un mensaje "informational response" cuando el código sea 100 o 102:
   - [file example](./resources/code/modulo-01_04-008.py)
   - Sólo es necesario que se cumpla una de estas condiciones para que Python imprima el mensaje.

- NOT
   - El operador not niega una condición dada de forma que se evalúa a False si la condición es True y a True si es False.
   - Por ejemplo, si quiere indicar que Python debe comprobar el código de estado cuando es algo fuera del rango de éxito, puede utilizar not:
   - [file example](./resources/code/modulo-01_04-009.py)
   - Python comprueba primero si el valor de estado es mayor o igual que 200 y menor o igual que 226, y luego, debido al operador not, lo invierte.
   - Esto significa que imprimirá el mensaje si status es menor que 200 o mayor que 226.
   - En este caso, los paréntesis son necesarios para que el código aplique not a ambas condiciones.
   - Python evaluará primero las condiciones dentro de los paréntesis.
   - Esto significa que primero evaluará las condiciones a ambos lados del operador and y después aplicará not a ambas.

---

## Actividad: Crear una Sentencia condicional

- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar la escritura de sentencias condicionales en Python.
   - Se le presentará un escenario de Seguridad para que lo explore a lo largo del laboratorio.
   - Practicará la aplicación de sentencias condicionales para automatizar procesos en una organización.

- Lo que hará
   - Escribir código que determine si el sistema operativo de un usuario requiere una actualización
   - Escribir código que determine si los intentos de inicio de sesión fueron realizados por usuarios aprobados y si los intentos de inicio de sesión se produjeron durante el horario de la organización

- Scenario
   - You're working as a security analyst.
   - First, you are responsible for checking whether a user's operating system requires an update.
   - Then, you need to investigate login attempts to a specific device.
   - You must determine if login attempts were made by users approved to access this device and if the login attempts occurred during organization hours.

- Task 1
   - You are asked to help automate the process of checking whether a user's operating system requires an update.
   - Imagine that a user's device can be running one of the following operating systems: OS 1, OS 2, or OS 3.
   - While OS 2 is up-to-date, OS 1 and OS 3 are not.
   - Your task is to check whether the user's system is up-to-date, and if it is, display a message accordingly.
   - To do this, complete the conditional statement using the keyword if.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_03/task_01.py)

- Task 2
   - Now try assigning the system variable to different values ("OS 1", "OS 2", and "OS 3"), run the cell, and observe what happens.
   - Keep the conditional statement as is.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code.
   - [file example](./resources/code/lab_03/task_02.py)
   - What happens when OS 2 is running? What happens when OS 1 is running?
   > When OS 2 is running, the message "no update needed" is displayed. When OS 1 is running, nothing is displayed because the condition didn't evaluate to True.

- Task 3
   - Nothing is displayed when the system is not equal to "OS 2".
   - This is because the condition didn't evaluate to True.
   - It would be beneficial if an alternative message is provided to them when updates are needed.
   - In the following cell, add the appropriate keyword after the first conditional so that it will display a message that conveys that an update is needed when the system is not running OS 2.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code.
   - Then, set the value of the system variable to indicate that OS 2 is running and run the cell.
   - After observing what happens, set the value of system to indicate either that OS 1 is running or that OS 3 is running and run the cell.
   - [file example](./resources/code/lab_03/task_03.py)
   - In this setup what happens when OS 2 is running? And what happens when OS 2 is not running?
   > When OS 2 is running, the message "no update needed" is displayed. When OS 2 is not running, the message "update needed" is displayed.

- Task 4
   - This setup is still not ideal.
   - If the variable system contains a random string or integer, the conditional above would still display update needed.
   - To improve the conditional, you will need to add the elif keyword.
   - In the following cell, you will add two elif statements after the if statement, to create the final code.
   - The first elif statement will display update needed if system is "OS 1".
   - The second elif statement will display the same message, if system is "OS 3".
   - Complete the second elif statement, and then run the cell with the variable system set to a different string each time.
   - Observe what happens when each operating system is running.
   - Also try assigning the system variable to some strings other than "OS 1", "OS 2", and "OS 3" (for example "OS 4").
   - Be sure to replace each ### YOUR CODE HERE ### with your own code.
   - [file example](./resources/code/lab_03/task_04.py)
   - Under this setup what happens when OS 2 is running? What happens when OS 1 is running? What happens when OS 3 is running? What happens when neither of those three operating systems are running?
   > When OS 2 is running, the message "no update needed" is displayed. When OS 1 is running, the message "update needed" is displayed. When OS 3 is running, the message "update needed" is displayed. When neither of those three operating systems are running, nothing is displayed because none of the conditions evaluated to True.

- Task 5
   - Writing code that is readable and concise is a best practice in programming.
   - The conditional above can be written more concisely.
   - In the following cell, use a logical operator to combine the two elif statements from the previous setup into one elif statement.
   - Be sure to replace each ### YOUR CODE HERE ###.
   - Then, assign the system variable to a value and run the cell.
   - Like you did in the previous task, use "OS 1", "OS 2", "OS 3", and other strings.
   - [file example](./resources/code/lab_03/task_05.py)
   - What do you observe about this conditional?
   > This conditional is more concise than the previous one. It still displays the same messages when OS 2, OS 1, or OS 3 are running. When neither of those three operating systems are running, nothing is displayed because none of the conditions evaluated to True.

- Task 6
   - Now you'll move on to the next part of your work.
   - You've been asked to investigate login attempts to a specific device.
   - Only approved users should log on to this device.
   - You'll start with two authorized users, stored in the variables approved_user1 and approved_user2.
   - You'll need to write a conditional statement that compares those variables to a third variable, username.
   - This will be the username of a specific user trying to log in.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code.
   - [file example](./resources/code/lab_03/task_06.py)

- Task 7
   - The number of approved users has now expanded to five.
   - Rather than storing each of the approved users' usernames individually, it would be more concise to store them in an allow list called approved_list.
   - The in operator in Python can be used to determine whether a given value is an element of a sequence.
   - Using the in operator in a condition can help you check whether a specific username is part of a list of approved usernames.
   - For example, in the code below, username in approved_list evaluates to True if the value of the username variable is included in approved_list.
   - Complete the code in the following cell to display the same messages that you used in the previous step.
   - When the condition evaluates to True, the following message will be displayed: "This user has access to this device."
   - When it evaluates to False, the following message will be displayed: "This user does not have access to this device."
   - Then, run the cell to observe its behavior.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code.
   - Afterwards, reassign the username variable to a username that is not approved and run the cell to observe what happens.
   - [file example](./resources/code/lab_03/task_07.py)
   - What happens when an approved user tries to log in? What happens when an unapproved user tries to log in?
   > When an approved user tries to log in, the message "This user has access to this device." is displayed. When an unapproved user tries to log in, the message "This user does not have access to this device." is displayed.

- Task 8
   - Now you'll write another conditional statement.
   - This one will use a organization_hours variable to check if the user logged in during specific organization hours.
   - When that condition is met, the code should display the string "Login attempt made during organization hours.".
   - When that condition isn't met, the code should display the string "Login attempt made outside of organization hours.".
   - The organization_hours variable will have a Boolean data type.
   - If organization_hours has a Boolean value of True, that means the user is logged in during the specified organization hours.
   - If organization_hours has a Boolean value of False, that means the user is not logged in during those hours.
   - Complete the conditional in the following cell. Be sure to replace each ### YOUR CODE HERE ### with your own code before running the following cell.
   - [file example](./resources/code/lab_03/task_08.py)
   - What happens when the user logs in during organization hours? What happens when they log in outside of organization hours?
   > When the user logs in during organization hours, the message "Login attempt made during organization hours." is displayed. When they log in outside of organization hours, the message "Login attempt made outside of organization hours." is displayed.

- Task 9
   - The following cell assembles the code from the previous tasks.
   - It includes the conditional statement that checks if a user is on the allow list and the conditional statement that checks if the user logged in during organization hours.
   - Run the cell below a few times.
   - Each time, enter a different combination of values for username and organization_hours to observe how that affects the output.
   - [file example](./resources/code/lab_03/task_09.py)
   - What happens when the user trying to log in is not among the approved users? What happens when the user trying to log in is among the approved users? What happens when the user tries to log in outside of organization hours?
   > When the user trying to log in is not among the approved users, the message "This user does not have access to this device." is displayed. When the user trying to log in is among the approved users, the message "This user has access to this device." is displayed. When the user tries to log in outside of organization hours, the message "Login attempt made outside of organization hours." is displayed.

- Task 10
   - You can also provide a single message about the login attempt.
   - To do this, you can join both conditions into a single conditional statement using a logical operator.
   - This will make the code more concise.
   - Examine the code in the following cell and add the missing operator that would allow for a single message.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before running the following cell.
   - Then run the cell, entering different combinations of information, and observe what happens.
   - [file example](./resources/code/lab_03/task_10.py)
   - In this setup, what happens when the user trying to log in is an approved user and doing so during organization hours? What happens when the user either is not approved or attempts to log in outside of organization hours?
   > When the user trying to log in is an approved user and doing so during organization hours, the message "This user has access to this device and logged in during organization hours." is displayed. When the user either is not approved or attempts to log in outside of organization hours, the message "This user does not have access to this device or logged in outside of organization hours." is displayed.

- Conclusion
   - In this lab, you practiced writing conditional statements in Python.
   - You wrote code that checked whether a user's operating system required an update.
   - You also wrote code that checked whether a user was approved to log in to a device and whether they logged in during organization hours.

---

## Ejemplo: Crear una Sentencia condicional
- Mismo laboratorio que el anterior.

- Conclusion
   - Conditional statements, comparison operators, and logical operators play a major role in automating important processes to maintain security, such as detecting when a user's operating system requires updates and detecting when a user is allowed to access a device.
   - Conditional statements allow you to determine whether a specific set of conditions has been met.
   - Comparison operators allow you to compare pairs of values. Specifically, the == operator allows you to determine whether one value is equal to another.
   - Logical operators such as and and or allow you to check more than one condition at a time.

---

## Bucles For
- Acabamos de aprender sobre ​las declaraciones condicionales y cómo ​se pueden desarrollar para permitir que las computadoras tomen decisiones.
- ​Pero a veces necesitamos que nuestros programas simplemente ​cuenten o realicen una tarea una y otra vez.
- ​Cuando se trata de tareas tediosas, ​es normal que los humanos pierdan la concentración y la energía.
- ​Es en situaciones como estas en las que ​los ordenadores pueden resultar especialmente útiles.
- ​Una sentencia iterativa es un código ​que ejecuta repetidamente un conjunto de instrucciones.
- ​Los enunciados iterativos también se denominan «bucles».
- ​La configuración de un bucle nos permite usar repetidamente ​una línea de código sin tener que escribirla varias veces.
- ​Antes de analizar la sintaxis, ​ejecutemos un bucle para que puedas experimentar lo que sucede.
- ​Observe cómo este código imprimió todos los números de la lista ​con una sola declaración de impresión.
- Eso es un bucle.
- [file example](./resources/code/modulo-01_04_010.py)
- ​Hay dos tipos de bucles que exploraremos: ​bucles for y bucles while.
- ​Acabamos de hacer un bucle y ​seguiremos centrándonos en ellos en este vídeo.
- ​Más adelante, exploraremos los bucles temporales.
- for loops, repita el código para una secuencia especificada.
- ​Un ejemplo de esto sería usar un ​bucle for para imprimir todos los elementos de una lista.
- ​Los bucles For comienzan con la palabra clave for.
- ​para señales el principio de un bucle for.
- ​Al igual que las sentencias condicionales, ​las sentencias iterativas constan de dos partes principales.
- ​Las partes de un bucle son ​la cabecera del bucle y el cuerpo del bucle.
- ​Examinemos el bucle for que ​acabamos de ejecutar y usémoslo para explorar estas partes.
- ​El encabezado del bucle es la línea que contiene ​la palabra clave for y termina con dos puntos.
- ​Le dice a Python que inicie un bucle.
- ​Se compone de la palabra clave for, ​una variable de bucle ​y la secuencia por la que se repetirá el bucle.
- ​La variable loop es una variable que se ​usa para controlar las iteraciones de un bucle.
- ​La variable loop viene justo después de for. ​Un nombre común es la letra i, ​pero puedes darle cualquier otro nombre que desees.
- ​En los bucles, esta variable temporal solo se ​usa dentro del bucle y no ​fuera de él en el resto del código.
- ​La variable loop va seguida ​del operador in y la ​secuencia por la que se iterará el bucle.
- ​En este ejemplo, esta secuencia es ​una lista que contiene números del uno al cuatro.
- ​Ejecuta cada uno de estos números a través de una acción específica.
- ​Debemos recordar poner dos puntos al ​final del encabezado del bucle para introducir este código.
- ​El cuerpo del bucle hace referencia a ​las líneas indentadas después del encabezado del bucle.
- ​Esto representa las acciones que ​se repiten mientras el bucle se repite.
- ​En este caso, imprimirá cada número de la lista: ​primero uno, luego dos, y así sucesivamente.
- ​Otro uso importante de for ​loops es repetir un proceso específico ​un número determinado de veces.
- ​Esto se hace ​combinándolo con la función de rango.
- ​La función de rango genera una secuencia de números.
- ​Por ejemplo, el rango de ​cero a 10 establece una secuencia que va desde cero ​, uno, dos hasta el número nueve.
- ​Cuando usamos el rango, ​empezamos a contar desde el número en la primera posición; ​en este caso, cero.
- ​Luego, cuando alcancemos el número en la segunda posición ​, nos dice dónde detenernos.
- ​Se excluye ese número.
- ​En este caso, donde el número es 10, ​la secuencia solo sube hasta nueve.
- ​Un detalle importante sobre la función de rango ​es que si no proporcionamos un punto de inicio ​, automáticamente comienza desde cero.
- ​10 representa el punto de parada.
- ​Como se excluye el punto de parada, ​los números incluidos en la secuencia comienzan en ​cero y terminan en nueve.
- ​Una secuencia que comience en cero y termine en ​nueve se repetirá 10 veces.
- ​Vamos a ejecutar un bucle for que ​incorpore la función range.
- ​Usaremos el rango para pedirle a Python que ​repita una acción 10 veces.
- ​Luego indicaremos la acción que queremos repetir.
- ​Esta acción imprime un mensaje de error que ​indica que «no se puede conectar al destino».
- ​Vamos a ejecutar esto.
- El uso de un bucle for con ​la función range nos permitió repetir ​el mismo mensaje de error 10 veces, ​en lugar de escribirlo una y otra vez nosotros mismos.
- [file example](./resources/code/modulo-01_04-011.py)

---

## Bucles while
- ​Anteriormente, introdujimos las sentencias iterativas ​en Python y nos centramos en los bucles for.
- ​Una sentencia iterativa es código que ​ejecuta repetidamente un conjunto de instrucciones.
- ​Cuando utilizábamos bucles for, ​el código se ejecutaba repetidamente ​basándose en una secuencia especificada.
- ​Los bucles while siguen ejecutándose repetidamente, ​pero esta repetición se basa en una condición.
- ​Mientras la condición sea verdadera, ​el bucle continúa ejecutándose.
- ​Pero cuando se convierte en falsa, ​el bucle while se detiene.
- ​Este bucle while, por ejemplo, ​establece una condición en la que la variable tiempo ​debe ser menor o igual que 10.
- ​Esto significa que seguirá ejecutándose ​hasta que la variable tiempo sea mayor que 10.
- ​De forma similar al bucle for, ​un bucle while tiene un encabezado.
- ​Está formado por la palabra clave ​while, la condición y dos puntos.
- ​El bucle while comienza con la palabra clave while.
- ​La palabra clave while señala el comienzo de un bucle while ​y va seguida de la condición que se evalúa a ​un valor booleano de Verdadero o Falso.
- ​La condición contiene la variable de bucle.
- ​Esta variable se utiliza para ​controlar el número de iteraciones del bucle.
- ​Sin embargo, existe una distinción importante en ​las variables utilizadas en los bucles for y while.
- ​Con los bucles while, la variable no se ​crea dentro de la propia sentencia del bucle.
- ​Antes de escribir el bucle while, ​debe asignar la variable.
- ​Entonces podrá hacer referencia a ella en el bucle.
- ​Cuando la condición que contiene la variable del bucle ​se evalúa a True, el bucle itera.
- ​Si no lo hace, ​entonces el bucle se detiene.
- ​Esta condición se evaluará a True mientras ​el tiempo de la variable sea menor o igual a 10.
- ​Finalmente, la cabecera del bucle termina con dos puntos.
- ​Al igual que un bucle for, ​un bucle while tiene un cuerpo indentado que ​consiste en las acciones a tomar mientras el bucle itera.
- ​La intención de este código es ​imprimir el valor de una variable que representa ​el tiempo e incrementar su valor en ​dos, hasta que sea mayor que 10.
- ​Esto significa que la primera acción en este bucle while ​es simplemente imprimir ​el valor actual de la variable del tiempo.
- ​Dado que los bucles while no ​incluyen una secuencia para iterar a través de ellos, ​tenemos que definir explícitamente ​cómo cambia la variable del bucle ​en el cuerpo del bucle while.
- ​Por ejemplo, en este bucle while, ​aumentamos la variable de bucle ​tiempo en dos en cada iteración.
- ​Esto se debe a que sólo queremos ​imprimir el tiempo cada dos minutos, ​así que este bucle while imprime todos los ​números pares menores o iguales que 10.
- [file example](./resources/code/modulo-01_04-012.py)
- ​Ahora que conocemos los conceptos básicos de los bucles while, ​exploremos un ejemplo práctico.
- ​Imaginemos que tenemos una limitación sobre ​cuántos dispositivos puede conectar un usuario.
- ​Podemos utilizar un bucle while para imprimir un mensaje cuando el usuario ​haya alcanzado su número máximo de dispositivos conectados.
- ​Creemos un bucle while para ello.
- ​Antes de iniciar nuestro bucle while, ​necesitamos asignar valores a dos variables.
- ​En primer lugar, estableceremos ​el valor máximo de dispositivos conectados en cinco.
- ​A continuación, estableceremos nuestra variable de bucle.
- ​Usaremos i para ello y la estableceremos en un valor de uno.
- ​A diferencia de lo que ocurre con los bucles for, ​con los bucles while, establecemos ​esta variable fuera del bucle.
- ​A continuación, crearemos el encabezado de nuestro bucle while.
- ​En este caso, la condición es que ​la primera variable sea menor que la segunda.
- ​Estas variables son la variable de bucle "i" y max_dispositivos.
- ​Como sabemos que el valor de max_dispositivos es cinco, ​podemos entender que este bucle se ejecutará mientras ​el valor actual de "i" sea menor que cinco.
- ​Entonces indicamos lo que queremos que haga nuestro bucle while.
- ​Dado que este bucle se ejecuta mientras ​el usuario aún pueda conectarse a dispositivos, ​primero haremos que imprima ​un mensaje de "el usuario aún puede conectarse a dispositivos adicionales".
- ​Después de esto, con cada iteración, incrementaremos i en uno.
- ​Cuando el bucle se repita, ​utilizará el nuevo valor de la variable i.
- ​Python saldrá del bucle cuando ​i ya no sea menor que cinco.
- ​También imprimiremos un mensaje cuando esto ocurra.
- ​Dejamos de indentar porque ​esta siguiente acción ocurre fuera del bucle.
- ​Entonces imprimiremos "el usuario ha ​alcanzado el número máximo de dispositivos conectados."
- ​Estamos listos para ejecutar esto.
- ​Debido al bucle, ​el primer mensaje se imprime un total de cuatro veces.
- ​El bucle se detiene cuando el valor de i aumenta a cinco.
- ​En este punto, sale ​del bucle e imprime el segundo mensaje.
- ​Cuando combina esta nueva comprensión de los bucles for y ​while con lo que ya ​sabe sobre sentencias condicionales y variables, ​tiene un montón de opciones en Python.

---

## Más sobre bucles en Python
- Una sentencia iterativa es código que ejecuta repetidamente un conjunto de instrucciones
- Dependiendo de los criterios, las sentencias iterativas se ejecutan cero o más veces

- bucles for
   - Si necesita iterar a través de una secuencia especificada, debe utilizar un bucle for.
   - El siguiente bucle for itera a través de una secuencia de nombres de usuario
   - [file example](./resources/code/modulo-01_04-014.py)
   - La primera línea de este código es la cabecera del bucle.
   - En la cabecera del bucle, la palabra clave for señala el comienzo de un bucle for.
   - Directamente después de for, aparece la variable de bucle.
   - La variable de bucle es una variable que se utiliza para controlar las iteraciones de un bucle.
   - En los bucles for, la variable de bucle forma parte de la cabecera.
   - En este ejemplo, la variable de bucle es i.
   - El resto del encabezado del bucle indica la secuencia a iterar.
   - El operador in aparece antes de la secuencia para indicar a Python que ejecute el bucle para cada elemento de la secuencia.
   - En este ejemplo, la secuencia es la lista de nombres de usuario.
   - El encabezado del bucle debe terminar con dos puntos (:).
   - La segunda línea de este ejemplo de bucle for es el cuerpo del bucle.
   - El cuerpo del bucle for puede constar de varias líneas de programación.
   - En el cuerpo, se indica lo que el bucle debe hacer en cada iteración.
   - En este caso, es print(i), o lo que es lo mismo, mostrar el valor actual de la variable del bucle durante esa iteración del bucle.
   - Para que Python ejecute el código correctamente, el cuerpo del bucle debe tener una sangría mayor que la cabecera del bucle. 
   - Cuando se utiliza en un bucle for, el operador in precede a la secuencia sobre la que iterará el bucle for.
   - Cuando se utiliza en una sentencia condicional, el operador in se utiliza para evaluar si un objeto forma parte de una secuencia.
   - En el ejemplo if "elarson" in ["tshah", "bmoreno", "elarson"] se evalúa como True porque "elarson" forma parte de la secuencia que sigue a in.

- Bucle a través de una lista
   - El uso de bucles for en Python le permite iterar fácilmente a través de listas, como una lista de recursos informáticos.
   - En el siguiente bucle for, asset es la variable de bucle y otra variable, computer_assets, es la secuencia.
   - La variable computer_assets almacena una lista.
   - Esto significa que en la primera iteración el valor de asset será el primer elemento de esa lista, y en la segunda iteración, el valor de asset será el segundo elemento de esa lista.
   - Puede ejecutar el código para observar su resultado:
   - [file example](./resources/code/modulo-01_04-015.py)
   - También es posible hacer un bucle a través de una cadena.
   - Esto devolverá cada carácter uno a uno.
   - Puede observarlo ejecutando el siguiente bloque de código que itera a través de la cadena "security":
   - [file example](./resources/code/modulo-01_04-016.py)

- Uso de range()
   - Otra forma de iterar a través de un bucle for se basa en una secuencia de números, y esto puede hacerse con range().
   - La función range() genera una secuencia de números.
   - Acepta entradas para el punto inicial, el punto final y el incremento entre paréntesis.
   - Por ejemplo, el siguiente código indica que se inicie la secuencia de números en 0, se detenga en 5, y se incremente cada vez en 1: `range(0, 5, 1)`.
   - El punto de inicio es inclusivo, lo que significa que 0 se incluirá en la secuencia de números, pero el punto de parada es exclusivo, lo que significa que 5 se excluirá de la secuencia.
   - Concluirá un número entero antes del punto de parada.
   - Cuando ejecute este código, podrá observar cómo 5 queda excluido de la secuencia
   - [file example](./resources/code/modulo-01_04-017.py)
   - Debe tener en cuenta que siempre es necesario incluir el punto de parada, pero si el punto de inicio es el valor por defecto de 0 y el incremento es el valor por defecto de 1, no es necesario especificarlos en el código.
   - Si ejecuta este código, obtendrá los mismos resultados:
   - [file example](./resources/code/modulo-01_04-018.py)
   - Si el punto de inicio es cualquier otro que 0 o el incremento es cualquier otro que 1, deben especificarse

- bucles while
   - Si desea que un bucle itere basándose en una condición, debe utilizar un bucle while.
   - Mientras la condición sea True, el bucle continúa, pero cuando se evalúa a False, el bucle while sale.
   - El siguiente bucle while continúa mientras la condición que i < 5 sea True:
   - [file example](./resources/code/modulo-01_04-019.py)
   - En este bucle while, el encabezado del bucle es la línea while i < 5:.
   - A diferencia de los bucles for, el valor de una variable de bucle utilizada para controlar las iteraciones no se asigna dentro de la cabecera del bucle en un bucle while.
   - En su lugar, se asigna fuera del bucle.
   - En este ejemplo, a i se le asigna un valor inicial de 1 en una línea que precede al bucle.
   - La palabra clave while indica el inicio de un bucle while.
   - A continuación, el encabezado del bucle indica la condición que determina cuándo termina el bucle.
   - Esta condición utiliza los mismos operadores de comparación que las sentencias condicionales.
   - Al igual que en un bucle for, la cabecera de un bucle while debe terminar con dos puntos (:).
   - El cuerpo de un bucle while indica las acciones a realizar en cada iteración.
   - En este ejemplo, se trata de mostrar el valor de i e incrementar el valor de i en 1.
   - Para que el valor de i cambie con cada iteración, es necesario indicarlo en el cuerpo del bucle while.
   - En este ejemplo, el bucle itera cuatro veces hasta alcanzar un valor de 5.

- Enteros en la condición de bucle
   - A menudo, como se acaba de demostrar, la condición del bucle se basa en valores enteros.
   - Por ejemplo, es posible que desee permitir que un usuario se registre siempre que lo haya hecho menos de cinco veces.
   - Entonces, su variable de bucle, login_attempts, puede ser inicializada a 0, incrementada por 1 en el bucle, y la condición de bucle puede especificar iterar sólo cuando la variable sea menor que 5.
   - Puede ejecutar el código siguiente y revisar la iteración de cada intento de inicio de sesión:
   - [file example](./resources/code/modulo-01_04-020.py)
   - El valor de login_attempts pasó de 0 a 4 antes de que la condición del bucle evaluara a False.
   - Por lo tanto, los valores de 0 a 4 se imprimen, y el valor 5 no se imprime.

- Valores booleanos en la condición del bucle
   - Las condiciones de los bucles while también pueden depender de otros tipos de datos, incluidas las comparaciones de Datos booleanos.
   - En las comparaciones de datos booleanos, su condición de bucle puede comprobar si una variable de bucle es igual a un valor como True o False.
   - El bucle itera un número indeterminado de veces hasta que la condición booleana deja de ser True.
   - En el ejemplo siguiente, se utiliza un valor booleano para salir de un bucle cuando un usuario ha realizado cinco intentos de inicio de sesión.
   - Una variable llamada count realiza un seguimiento de cada intento de inicio de sesión y cambia la variable login_status a False cuando count es igual a 4.
   - El incremento de count de 0 a 4 representa cinco intentos de inicio de sesión.
   - Dado que la condición while sólo itera cuando login_status es True, saldrá del bucle.
   - Puede ejecutarlo para explorar esta salida:
   - [file example](./resources/code/modulo-01_04-021.py)
   - El código imprime un mensaje para que lo intente de nuevo cuatro veces, pero sale del bucle una vez que login_status se establece en False.

- Gestionar bucles
   - Puede utilizar las palabras clave break y continue para controlar aún más sus iteraciones de bucle.
   - Ambas se incorporan a una sentencia condicional dentro del cuerpo del bucle.
   - Pueden insertarse para ejecutarse cuando la condición en una sentencia if es True.
   - La palabra clave break se utiliza para salir de un bucle.
   - La palabra clave continue se utiliza para saltarse una iteración y continuar con la siguiente.

- break
   - Cuando desee salir de un bucle for o while basándose en que una condición concreta de una sentencia if sea True, puede escribir una sentencia condicional en el cuerpo del bucle y escribir la palabra clave break en el cuerpo de la condicional.
   - El siguiente ejemplo lo demuestra.
   - La sentencia condicional con break ordena a Python salir del bucle for si el valor de la variable de bucle asset es igual a "desktop20".
   - En la segunda iteración, esta condición se evalúa a True. Puede ejecutar este código para observar esto en la salida:
   - [file example](./resources/code/modulo-01_04-022.py)
   - Como era de esperar, los valores de "desktop20" y "smartphone03" no se imprimen porque el bucle se rompe en la segunda iteración.

- continue
   - Cuando desee saltarse una iteración basándose en una determinada condición en una sentencia if siendo True, puede añadir la palabra clave continue en el cuerpo de una sentencia condicional dentro del bucle.
   - En este ejemplo, continue se ejecutará cuando la variable de bucle de asset sea igual a "desktop20".
   - Puede ejecutar este código para observar cómo difiere esta salida del ejemplo anterior con break:
   - [file example](./resources/code/modulo-01_04-023.py)
   - El valor "desktop20" en la segunda iteración no se imprime.
   - Sin embargo, en este caso, el bucle continúa hasta la siguiente iteración y se imprime "smartphone03".

- Bucle infinito
   - Si crea un bucle que no sale, se denomina bucle infinito.
   - En estos casos, debe pulsar CTRL-C o CTRL-Z en su teclado para detener el bucle infinito.
   - Puede que necesite hacer esto cuando ejecute un servicio que procese datos constantemente, como un servidor web.

---

## Identifique: Seleccionar la Sentencia iterativa correcta
- Identify the iterative statement that prints the desired output. Note that code examples may wrap on your screen.

- You want to print 3 numbers from a list.
```python
for i in [8, 9, 10]:
   print(i)
```

- You want to print the message “Access denied” 5 times.
```python
for i in range(5):
   print("Access denied")
```

- You want to print out a sequence of numbers starting at 10 and ending at 30.
```python
for i in range(10, 31):
   print(i)
```

- You want to print a message that tells the user to “try again” as long as the value of the attempt variable is 5 or less, and you want to increase the value of this variable by 1 each time it passes through the loop.
```python
attempt = 1
while attempt <= 5:
   print("try again")
   attempt += 1
```

- You want to print out the numbers 20, 19, 18, 17, and 16.
```python
i = 20
while i > 15:
   print(i)
   i -= 1
```

- You want to welcome 3 users from a list by their name (for example, “Welcome, Emerick Larson”).
```python
name = ["Emerick Larson", "Estrella Ortiz", "Troy Shah"]
for i in name:
   print("Welcome, " + i)
```

---

## Actividad: Crear bucles
- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar la escritura de sentencias iterativas en Python.
   - Se le presentará un escenario de seguridad para que lo explore a lo largo del laboratorio.
   - Practicará la creación de bucles para automatizar procesos repetitivos y hacerlos más eficientes.

- Lo que hará
   - Crear un bucle simple relacionado con la conexión a una red
   - Utilizar un bucle for para investigar la actividad de inicio de sesión comparando una lista de direcciones IP permitidas con una lista de direcciones IP desde las que los usuarios han intentado iniciar sesión
   - Utilice un bucle while para generar identificadores únicos de empleados iterando a través de números

- Scenario
   - You're working as a security analyst, and you're writing programs in Python to automate displaying messages regarding network connection attempts, detecting IP addresses that are attempting to access restricted data, and generating employee ID numbers for a Sales department.

- Task 1
   - In this task, you'll create a loop related to connecting to a network.
   - Write an iterative statement that displays Connection could not be established three times.
   - Use the for keyword, the range() function, and a loop variable of i.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_01.py)

- Task 2
   - The range() function can also take in a variable.
   - To repeat a specified action a certain number of times, you can first assign an integer value to a variable.
   - Then, you can pass that variable into the range() function within a for loop.
   - In your code that displays a network message connection, incorporate a variable called connection_attempts.
   - Assign the positive integer of your choice as the value of that variable and fill in the missing variable in the iterative statement.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Test out the code with different values for connection_attempts and observe what happens.
   - [file example](./resources/code/lab_04/task_02.py)

- Task 3
   - This task can also be achieved with a while loop.
   - Complete the while loop with the correct code to instruct it to display "Connection could not be established." three times.
   - In this task, a for loop and a while loop will produce similar results, but each is based on a different approach.
   - In other words, the underlying logic is different in each.
   - A for loop terminates after a certain number of iterations have completed, whereas a while loop terminates once it reaches a certain condition.
   - In situations where you do not know how many times the specified action should be repeated, while loops are most appropriate.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_03.py)
   - What do you observe about the differences between the for loop and the while loop that you wrote?
   > The for loop iterates a specific number of times, while the while loop continues until a certain condition is met. In this case, both loops achieve the same result of printing the message three times, but they do so using different logic. The for loop is more concise when the number of iterations is known, while the while loop is more flexible for conditions that may change during execution.

- Task 4
   - Now, you'll move onto your next task.
   - You'll automate checking whether IP addresses are part of an allow list.
   - You will start with a list of IP addresses from which users have tried to log in, stored in a variable called ip_addresses.
   - Write a for loop that displays the elements of this list one at a time.
   - Use i as the loop variable in the for loop.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_04.py)

- Task 5
   - You are now given a list of IP addresses that are allowed to log in, stored in a variable called allow_list.
   - Write an if statement inside of the for loop.
   - For each IP address in the list of IP addresses from which users have tried to log in, display "IP address is allowed" if it is among the allowed addresses and display "IP address is not allowed" otherwise.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_05.py)

- Task 6
   - Imagine now that the information the users are trying to access is restricted, and if an IP address outside the list of allowed IP addresses attempts access, the loop should terminate because further investigation would be needed to assess whether this activity poses a threat.
   - To achieve this, use the break keyword and expand the message that is displayed to the user when their IP address is not in allow_list to provide more specifics.
   - Instead of "IP address is not allowed", display "IP address is not allowed.
   - Further investigation of login activity required".
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_06.py)

- Task 7
   - You'll now complete another task.
   - This involves automating the creation of new employee IDs.
   - You have been asked to create employee IDs for a Sales department, with the criteria that the employee IDs should all be numbers that are unique, divisible by 5, and falling between 5000 and 5150.
   - The employee IDs can include both 5000 and 5150.
   - Write a while loop that generates unique employee IDs for the Sales department by iterating through numbers and displays each ID created.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_07.py)

- Task 8
   - You would like to incorporate a message that displays Only 10 valid employee ids remaining as a helpful alert once the loop variable reaches 5100.
   - To do so, include an if statement in your code.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file example](./resources/code/lab_04/task_08.py)
   - Why do you think the statement print(i) is written before the conditional rather than inside the conditional?
   > The statement print(i) is written before the conditional to ensure that every valid employee ID generated by the loop is printed, regardless of whether it meets the condition for displaying the alert message. If print(i) were placed inside the conditional, only the IDs that trigger the alert (i.e., those greater than or equal to 5100) would be printed, and all other valid IDs would not be displayed. By placing print(i) before the conditional, all valid IDs are shown, while the alert message is only displayed when the specified condition is met.

- Conclusion
   - In this lab, you practiced writing iterative statements in Python.
   - You wrote code that displayed a message multiple times using both for and while loops.
   - You also wrote code that checked whether an IP address was on an allow list and terminated the loop if it was not.
   - Finally, you wrote code that generated unique employee IDs for a Sales department and displayed a helpful alert when the number of valid IDs remaining reached a certain threshold.

---

## Ejemplar: Crear bucles
- Mismo laboratorio que el anterior.

- Conclusion
   - Iterative statements play a major role in automating security-related processes that need to be repeated.
   - You can use for loops to repeat a process a specified number of times.
   - You can use while loops to repeat a process until a specified condition has been met. Comparison operators are often used in these conditions.
      - The < comparison operator allows you to check whether one value is less than another.
      - The <= comparison operator allows you to check whether one value is less than or equal to another.
      - The == comparison operator allows you to check whether one value is equal to another.

---

## Ponga a prueba sus Conocimientos: Sentencias condicionales e iterativas

1. ¿Qué mostrará el siguiente Código?
```python
ip_address = "192.168.183.51"
if ip_address == "192.168.183.51":
   print("You're logged in.")
else:
   print("Login failed, try again.")
```
   - [x] "You're logged in."
   - [ ] Nada
   - [ ] Tanto "You're logged in." como "Login failed, try again."
   - [ ] "Login failed, try again."
> El código mostrará "You're logged in." La condición en la sentencia if requiere que la variable ip_address contenga un valor de "192.168.183.51". Dado que esta condición se evalúa a True, Python ejecutará la acción especificada en el cuerpo de la sentencia if. En este caso, mostrará el mensaje "You're logged in." La acción especificada en el cuerpo de la sentencia else sólo se ejecutará cuando la condición en la sentencia if se evalúe a False, por lo que no imprimirá "Login failed, try again."

2. ¿Qué sentencia condicional imprime el mensaje "account locked" cuando el valor de failed_logins es 3 o superior? 
   - [ ] if failed_login_count == 3:
            print("account locked")
   - [ ] if failed_login_count != 3:
            print("account locked")
   - [x] if failed_logins >= 3:
            print("account locked")
   - [ ] if failed_login_count > 3:
            print("account locked")
> La siguiente sentencia condicional imprime el mensaje "account locked" cuando el valor de failed_logins es 3 o superior:
> if failed_logins >= 3:
>  print("account locked") 
> Esta condición comprueba si a failed_logins se le asigna un valor mayor o igual que 3. El Operador >= representa mayor o igual que. Cuando se cumple esta condición, el cuerpo imprime el mensaje "account locked".

3. ¿Qué código imprime todos los números de 3 a 7?
   - [ ] for i in range(3, 4, 5, 6, 7):
            print(i)
   - [ ] for i in range(3, 7):
            print(i)
   - [x] for i in range(3, 8):
            print(i)
   - [ ] for i in range(8):
            print(i)
> El siguiente código imprime todos los números desde 3 hasta 7:
> for i in range(3, 8):
>    print(i)
> La función range() genera una secuencia de números. Con range(3, 8), la secuencia comenzará en 3 y terminará en 7. Esto se debe a que el número de la primera posición, 3, se incluye en la secuencia, pero el número de la segunda posición, 8, se excluye. 

4. ¿Cuántas veces imprime el siguiente código el mensaje de "alerta de Seguridad"?
```python
count = 0
while count < 10:
   print("security alert")
   count = count + 1
```
   - [ ] 0
   - [ ] 9
   - [x] 10
   - [ ] 5
> Este código imprimirá "security alert" diez veces. Esto se debe a que a la variable count se le asigna un valor inicial de 0. Luego se incrementa en 1 con cada iteración del Bucle hasta que la condición le ordena detenerse en 10.