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