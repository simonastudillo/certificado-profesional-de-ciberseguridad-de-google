# Componentes principales de Python

## Tipos de datos en Python
- ​El siguiente tema se refiere a la categorización de datos en Python.
- ​En primer lugar, dediquemos un momento a ​considerar otro entorno en el que aplicamos categorías.
- ​Pensaremos en trabajar en la cocina.
- ​Al cocinar, podemos clasificar los ingredientes que ​utilizamos; por ejemplo, las zanahorias y los pimientos son verduras, y el ​pollo y la carne de res son carne.
- ​Estas categorías son importantes ​porque afectan a la forma en que manejamos estos ingredientes.
- ​Cuando se trabaja en Python, ​los tipos de datos tienen un propósito similar.
- ​Un tipo de datos es una categoría ​para un tipo concreto de elemento de datos.
- ​Python usa varios tipos de datos.
- ​Nos centraremos en los datos de cadenas, flotantes, enteros, booleanos y de listas.
- ​Cuando imprimimos el texto ​«¡Hola Python!» en nuestro vídeo anterior, ​este era un ejemplo de cadena.
- ​Datos de cadena son datos que ​consisten en una secuencia ordenada de caracteres.
- ​Estos caracteres pueden ser letras, ​símbolos, espacios e incluso números.
- ​Los números del tipo de datos de cadena ​no se pueden usar para los cálculos.
- ​Todos los caracteres de una cadena ​deben ir entre comillas.
- ​Por suerte, Python te lo dirá ​enviándote un mensaje de error ​si olvidas las comillas.
- ​Usemos nuestro código de antes y ​exploremos qué sucede cuando ​dejamos fuera de las comillas.
- ​Observe cómo ​falta una de nuestras comillas al final de la cadena.
- ​Cuando ejecutemos este código, ​recibiremos un mensaje de error.
- [File example](./resources/code/modulo-01_03-001.py)
- ​Python también admite tipos de datos numéricos.
- ​Cuando trabajamos con datos numéricos, ​no colocamos comillas alrededor de los datos.
- ​Datos numéricos incluyen números flotantes y enteros.
- ​Datos flotantes son ​datos que constan de un número con un punto decimal.
- ​Esto incluye fracciones como 2.1 o 10.5.
- ​También incluye números enteros con un ​punto decimal, como 2.0 o 10.0.
- ​Datos enteros son datos que constan de ​un número que no incluye un punto decimal.
- ​Los números como 0 ​, -9 y 5000 son números enteros válidos.
- ​Hasta ahora, hemos usado la función print para generar una cadena.
- ​Pero también se puede usar con ​tipos flotantes y enteros para los cálculos.
- ​Vamos a probar un ejemplo de esto.
- ​En primer lugar, ya que es una buena práctica, ​agreguemos un comentario para explicar el propósito de nuestro código.
- ​A continuación, le diremos a Python qué debe calcular.
- ​El resultado nos da la respuesta. ​1 más 1 es 2.
- ​Podemos usar la impresión con datos flotantes y enteros para ​realizar todo tipo de operaciones matemáticas como la suma, la ​resta, la multiplicación y la división.
- [File example](./resources/code/modulo-01_03-002.py)
- ​El tercer tipo de datos en Python se denomina Booleana.
- ​Datos booleanos son datos que solo pueden tener uno de dos valores: verdadero ​o falso.
- Los ​valores booleanos son útiles para la lógica de nuestros programas.
- ​Por ejemplo, comparemos números y ​determinemos los valores Booleanos de estas comparaciones.
- ​Primero, usaremos la función print para ​evaluar si 10 es menor que 5.
- ​Luego, también evaluaremos si 9 ​es menor que 12.
- Entonces, ¿qué opinas? ​10 no es menor que 5, ​pero 9 es menor que 12, ¿verdad?
- ​Veamos cómo Python maneja esto cuando lo ejecutamos.
- ​Python está de acuerdo. ​La primera línea de salida nos dice que es ​falso decir que 10 es menor que 5.
- ​La segunda nos dice que es cierto ​decir que 9 es menor que 12.
- ​Usaremos más la palabra Booleana cuando ​empecemos a incluir condiciones en nuestro código.
- [File example](./resources/code/modulo-01_03-003.py)
- ​Y el último tipo de datos que trataremos son las listas.
- ​Datos de lista son una estructura de datos que ​consiste en una colección de datos en forma secuencial.
- ​Crearemos e imprimiremos una lista que ​imprima todos los nombres de usuario de ​las tres personas que ​tienen acceso a un archivo confidencial.
- ​En primer lugar, agregaremos nuestro comentario ​sobre la intención de imprimir esta lista.
- ​Después de imprimir la palabra clave, ​agregaremos nuestra lista.
- ​Tenemos que poner la lista entre corchetes.
- ​Después de esto, colocamos los elementos individuales de ​la lista entre comillas ​y los separamos con comas.
- ​Ahora vamos a ejecutar esto.
- ​Como era de esperar, obtenemos la lista.
- ​Cuando se imprime, todavía tiene los corchetes.
- ​Esto es solo el principio de lo que puedes hacer con las listas.
- ​A medida que vaya adquiriendo conocimientos de Python, ​aprenderá cómo puede acceder a ​los elementos individuales de la lista y editarlos.
- [File example](./resources/code/modulo-01_03-004.py)
- Este ​fue un breve resumen de los ​cinco tipos de datos principales en Python: ​cadena, entero, flotante, ​booleana y lista.
- ​Estos tipos de datos son algunos de ​los más comunes ​con los que trabajarás a medida que avancemos en nuestras lecciones. 

---

## Más información sobre los tipos de datos
- Un tipo de datos es una categoría para un tipo particular de elemento de datos.
- Usted se centró en Cadena, Lista, Flotante, Entero y Datos booleanos.
- Estos son los tipos de datos con los que trabajará en este curso.
- Esta lectura ampliará estos tipos de datos.
- También introducirá tres tipos adicionales.
   
- Cadena
   - En Python, los Datos de cadena son datos formados por una secuencia ordenada de caracteres.
   - Los caracteres de una Cadena pueden incluir letras, números, símbolos y espacios.
   - Estos caracteres deben ir entre comillas. Todas estas son cadenas válidas:
      - "updates needed"
      - "20%"
      - "5.0"
      - "35"
      - "**/**/**" 
      - ""
   - El último elemento (""), que no contiene nada entre comillas, se denomina cadena vacía.
   - Puede utilizar la función print() para mostrar una cadena. Puede explorar esto ejecutando este código:
   - [File example](./resources/code/modulo-01_03-005.py)
   - El Código imprime "updates needed". 
   - Puede colocar cadenas entre comillas dobles ("") o simples ('').
   - El siguiente código demuestra que se imprime el mismo mensaje cuando la cadena está entre comillas simples:
   - [File example](./resources/code/modulo-01_03-006.py)
   - Elegir un tipo de comillas y utilizarlo de forma coherente facilita la lectura de su código.
   - Este curso utiliza comillas dobles.

- Lista
   - En Python, los datos de una lista son una estructura de datos que consiste en una colección de datos en forma secuencial.
   - Los elementos de una lista pueden ser de cualquier tipo de datos, como cadenas, enteros, booleanos o incluso otras listas.
   - Los elementos de una Lista se colocan entre corchetes, y cada elemento se separa por una coma.
   - Las listas siguientes contienen elementos de varios tipos de datos:
      - [12, 36, 54, 1, 7]
      - ["eraab", "arusso", "drosas"]
      - [True, False, True, True]
      - [15, "approved", True, 45.5, False]
      - []
   - El último elemento[], que no contiene nada entre corchetes, se denomina lista vacía.
   - También puede utilizar la función print() para mostrar una lista:
   - [File example](./resources/code/modulo-01_03-007.py)
   - Esto muestra una lista que contiene los enteros 12, 36, 54, 1, y 7.

- Entero
   - En Python, los datos enteros son datos formados por un número que no incluye punto decimal.
   - Todos estos son ejemplos de datos enteros:
      - -100 
      - -12
      - -1
      - 0
      - 1
      - 20
      - 500
   - Los enteros no se entrecomillan.
   - Puede utilizar la función print() para mostrar un número entero.
   - Cuando ejecute este código, aparecerá 5:
   - [File example](./resources/code/modulo-01_03-008.py)
   - También puede utilizar la función print() para realizar operaciones matemáticas con números enteros.
   - Por ejemplo, este código suma dos números enteros:
   - [File example](./resources/code/modulo-01_03-009.py)
   - El resultado es 7. También puede restar, multiplicar o dividir dos enteros.

- Flotante
   - Datos flotantes son aquellos que consisten en un número con un punto decimal.
   - Todos los siguientes son ejemplos de datos flotantes:
      - -2.2
      - -1.34
      - 0.0
      - 0.34
   - Al igual que los datos enteros, los datos flotantes no se entrecomillan.
   - Además, también puede utilizar la función print() para visualizar datos flotantes o para realizar cálculos matemáticos con datos flotantes.
   - Puede ejecutar el siguiente código para revisar el resultado de este cálculo:
   - [File example](./resources/code/modulo-01_03-010.py)
   - La salida es 4.0.
   - La división de dos valores enteros o dos valores flotantes da como resultado una salida flotante cuando se utiliza el símbolo /:
   - [File example](./resources/code/modulo-01_03-011.py)
   - La salida de ambos cálculos es el valor flotante de .25.
   - Si desea devolver un número entero de un cálculo, debe utilizar el símbolo // en su lugar:
   - [File example](./resources/code/modulo-01_03-012.py)
   - Redondeará hacia abajo al número entero más próximo.
   - En el caso de print(1//4), la salida es el valor entero de 0 porque el uso de este símbolo redondea hacia abajo el cálculo de .25 al número entero más cercano.
   - En el caso de print(1.0//4.0), la salida es el valor flotante de 0.0 porque mantiene el tipo de datos flotante de los valores en el cálculo a la vez que redondea hacia abajo al número entero más cercano.

- Booleana
   - Datos booleanos son datos que sólo pueden tener uno de dos valores: o True o False.
   - No debe entrecomillar los valores booleanos.
   - Al ejecutar el siguiente código, se muestra el valor booleano de True:
   - [File example](./resources/code/modulo-01_03-013.py)
   - También puede devolver un valor booleano comparando números.
   - Como 9 no es mayor que 10, este código evalúa a False:
   - [File example](./resources/code/modulo-01_03-014.py)

- Tipos de datos adicionales
   - En este curso, trabajará con los tipos de datos Cadena, Lista, Enteros, Flotantes y Booleanos, pero existen otros tipos de datos.
   - Estos tipos de datos adicionales incluyen los datos de tupla, los datos de diccionario y los Datos de conjunto.
   - Tupla
      - Los datos de tupla son una estructura de datos que consiste en una colección de datos que no pueden modificarse.
      - Al igual que las listas, las tuplas pueden contener elementos de distintos tipos de datos.
      - Una diferencia entre los datos de tupla y los datos de lista es que es posible cambiar los elementos de una lista, pero no es posible cambiar los elementos de una tupla.
      - Esto podría ser útil en un contexto de ciberseguridad.
      - Por ejemplo, si los identificadores de software se almacenan en una tupla para garantizar que no se alterarán, esto puede proporcionar la seguridad de que una lista de control de acceso sólo bloqueará el software previsto.
      - La sintaxis de una tupla también es diferente de la de una lista.
      - Una tupla se coloca entre paréntesis en lugar de entre corchetes.
      - Todos estos son ejemplos del tipo de datos de tupla:
         - ("wjaffrey", "arutley", "dkot")
         - (46, 2, 13, 2, 8, 0, 0)
         - (True, False, True, True)
         - ("wjaffrey", 13, True)
      - Las tuplas son más eficientes en memoria que las listas, por lo que resultan útiles cuando se trabaja con una gran cantidad de datos.
   - Diccionario
      - Los datos de diccionario son datos que constan de uno o más pares clave-valor.
      - Cada clave se asigna a un valor.
      - Entre la clave y el valor se colocan dos puntos (:).
      - Las comas separan los pares clave-valor de otros pares clave-valor, y el diccionario se coloca entre llaves ({}).
      - Los diccionarios son útiles cuando se desea almacenar y recuperar datos de forma predecible.
      - Por ejemplo, el siguiente diccionario asigna el nombre de un edificio a un número.
      - El nombre del edificio es el valor y el número es la clave.
      - Después de la clave se colocan dos puntos.
          - { 1: "East", 2: "West", 3: "North", 4: "South" }
   - Conjunto
      - En Python, los Datos de conjunto son datos que consisten en una colección desordenada de valores únicos.
      - Esto significa que no puede haber dos valores iguales en un conjunto.
      - Los elementos de un conjunto se colocan siempre entre llaves y se separan por una coma.
      - Estos elementos pueden ser de cualquier Tipo de datos.
      - Este ejemplo de conjunto contiene cadenas de nombres de usuario:
         - {"jlanksy", "drosas", "nmason"}

---

## Trabajar con variables en Python
- ​Anteriormente, hemos comparado los tipos de datos con ​las categorías que tenemos para ​los distintos ingredientes que utilizamos al cocinar, ​como las verduras o la carne.
- ​Algunas de estas categorías que utilizamos para ​los tipos de datos son la cadena, ​el flotante, el entero, ​el booleano y la lista.
- ​Ahora, hagamos ​otra comparación.
- Cuando trabajamos en la cocina, ​también utilizamos recipientes de almacenamiento.
- ​Estos recipientes pueden contener muchas cosas diferentes.
- ​Después de una comida, un recipiente podría contener arroz, ​y después de otra, podría ​contener algo diferente, como pasta.
- ​De forma similar, en Python, tenemos variables.
- ​Una variable es un recipiente que almacena Datos.
- ​Para crear una variable, ​necesita un nombre para ella.
- A continuación, se añade un signo igual ​y luego un objeto para almacenar en ella.
- ​Crear una variable se denomina a menudo asignación.
- ​La mejor práctica para nombrar variables es hacer que ​los nombres sean relevantes para lo que se están utilizando.
- ​Utilicemos una variable para almacenar el ID de un dispositivo.
- ​Nombraremos a nuestra variable ID_dispositivo, añadiremos ​el signo igual y, a continuación, le asignaremos un valor de h32rb17.
- ​Como el tipo de datos de esta variable es una cadena, ​colocaremos ese valor entre ​comillas.
- Vamos a ejecutar el código.
- ​Nuestra variable está ahora guardada en Python.
- [file example](./resources/code/modulo_01-03-015.py)
- ​El propósito de crear variables ​es utilizarlas más adelante en el código.
- ​Usar variables también puede denominarse "llamarlas".
- ​Para llamar a una variable, se escribe su nombre.
- ​Esto le dice a Python que utilice ​el objeto que contiene la variable.
- ​Añadamos al código que acabamos de ​escribir y llamamos a una variable.
- ​Hagamos que imprima la variable.
- ​Para ello, utilizamos la función print y ​le pedimos que imprima el valor ​almacenado en la variable ID del dispositivo.
- ​Cuando usamos una variable en nuestra función print, ​no usamos comillas.
- ​Esta vez, cuando la ejecutamos, ocurre algo.
- ​Python imprime h32rb17 en la pantalla.
- ​Añadamos una línea más de ​código para demostrar la diferencia ​entre imprimir una variable e imprimir una cadena.
- ​Le pediremos a Python que imprima ​una cadena que contenga otro ID de dispositivo: ​m50pi31.
- ​Debido a que se trata de datos de cadena y no de una variable, ​lo colocamos entre comillas.
- ​Ahora, ejecutemos el código y veamos los resultados.
- ​Ejecuta ambas sentencias print.
- ​La primera lee la variable e imprime ​el valor que contiene: h32rb17.
- ​Y la segunda lee la cadena especificada e imprime m50pi31.
- ​Pero si pudiéramos utilizar la cadena directamente, ​¿por qué necesitamos variables?
- ​Bueno, a menudo utilizamos ​variables para simplificar nuestro código o hacerlo ​más limpio y fácil de leer.
- ​O si necesitáramos una cadena o un número muy largos, ​almacenarlos en una variable nos permitiría utilizarlos ​en todo nuestro código sin tener que escribirlos todos.
- ​En el ejemplo anterior, ​la variable almacenaba datos de cadena, pero ​las variables pueden almacenar una gran variedad de tipos de datos.
- ​Las variables tienen el tipo de datos ​del objeto que las almacena en ese momento.
- ​Si no está seguro de ​el tipo de datos almacenado dentro de una variable, ​puede utilizar la función de tipo.
- ​La función de tipo es ​una función que devuelve el tipo de datos de su entrada.
- ​Utilicemos la función de tipo en Python.
- ​Empezaremos creando ​nuestra variable.
- Después, ​añadiremos una línea de código que incluya la función type.
- ​Esta línea pide a Python que nos diga el tipo de datos de ​la variable ID del dispositivo ​y que lo asigne a una nueva variable llamada data_type.
- ​Después de esto, podemos ​imprimir la variable data_type en la pantalla.
- ​¡Perfecto! Python nos dice ​que el valor que ID de dispositivo contiene una cadena.
- ​Cuando se trabaja con variables, ​es importante no perder de vista sus tipos de datos.
- [file example](./resources/code/modulo_01-03-016.py)
- ​Si no lo hace, podría obtener un error de tipo.
- ​Un error de tipo es ​un error que resulta de usar un tipo de datos incorrecto.
- ​Por ejemplo, si intenta sumar un número y una cadena, ​obtendrá un error de tipo ​porque Python no puede combinar ​esos dos tipos de datos juntos.
- ​Sólo puede sumar dos cadenas o dos números.
- ​Vamos a demostrar un error de tipo.
- ​Primero, reutilizaremos ​nuestra variable de ID de dispositivo que almacena un valor de cadena.
- ​Después, definiremos otra variable ​llamada número y le asignaremos un valor entero.
- ​Añadamos una sentencia print que muestre la suma de ​estas variables y, a continuación, ejecutamos esto.
- ​Acabamos con un error ​porque no podemos sumar una cadena a un número.
- [file example](./resources/code/modulo_01_03-017.py)
- ​Vamos a tratar un tema más relacionado con las variables.
- ​Antes hemos mencionado que las variables son como contenedores.
- ​Lo que contienen puede cambiar.
- ​Después de definir una variable, ​siempre podemos cambiar el objeto que contiene.
- ​Esto se llama reasignación.
- ​Reasignar una variable es muy ​similar a asignarla en primer lugar.
- ​Probemos esto y reasignemos una variable.
- ​Empezaremos asignando la misma cadena de ​h32rb17 a nuestra variable device_ID.
- ​Incluiremos también una línea ​de programación para imprimir esta variable.
- ​Ahora, probemos a reasignar la variable.
- ​Escribimos el nombre de esta variable, añadimos un signo igual, ​y, a continuación, añadimos el nuevo objeto.
- ​En este caso, utilizaremos la cadena ​n73ab07 como el nuevo ID del dispositivo.
- ​También pediremos a Python que imprima la variable de nuevo.
- ​Veamos qué ocurre cuando ejecutamos esto.
- ​Python imprime dos líneas de salida.
- ​La primera sentencia print vino antes de la reasignación, ​así que primero imprime la cadena de h32rb17.
- ​Pero la segunda sentencia print vino después de que cambiara.
- ​Por eso la segunda salida a la pantalla ​es la cadena n73ab07.
- ​Con este código, hemos reasignado una variable ​con un valor de cadena a otro valor de cadena, ​pero también es posible reasignar ​una variable a un valor de otro tipo de datos.
- Por ejemplo, podemos reasignar una variable ​con un valor de cadena a un valor entero.
- ​Las variables son una parte esencial de ​Python, y a medida que avancemos en este curso, ​nos iremos familiarizando con ellas.
- [file example](./resources/code/modulo_01_03-018.py)

---

## Asignar y reasignar variables en Python
- ¿Qué son las variables?
   - En un lenguaje de programación, una variable es un contenedor que almacena datos.
   - Es una ubicación de almacenamiento con nombre en la memoria de un ordenador que puede contener un valor.
   - Almacena los datos en un tipo de datos particular, como entero, cadena o booleano.
   - El valor que se almacena en una variable puede cambiar.
   - Puedes pensar en las variables como cajas con etiquetas.
   - Aunque cambie el contenido de una caja, la etiqueta de la caja no cambia.
   - Del mismo modo, cuando se cambia el valor almacenado en una variable, el nombre de la variable sigue siendo el mismo.
   - Los analistas de seguridad que trabajan en Python utilizarán una variedad de variables.
   - Algunos ejemplos incluyen variables para intentos de acceso, listas de permitidos y direcciones.

- Trabajar con variables
   - En Python, es importante saber cómo asignar variables y cómo reasignarlas.

- Asignación y reasignación de variables
   - Si quieres crear una variable llamada username y asignarle un valor de "nzhao", coloca la variable a la izquierda del signo igual y su valor a la derecha:
      - `# Assign 'username'`
      - `username = "nzhao"`
   - Si más tarde reasignas este nombre de usuario a "zhao2", seguirás refiriéndote a ese contenedor de variables como username.
      - `# Reassign 'username'`
      - `username = "zhao2"`
   - Aunque el contenido haya cambiado de "nzhao" a "zhao2", la variable username sigue siendo la misma. 
   - Debes poner "nzhao" y "zhao2" entre comillas porque son cadenas.
   - Python asigna automáticamente a una variable su tipo de datos cuando se ejecuta.
   - Por ejemplo, cuando la variable username contiene la cadena "nzhao", se le asigna un tipo de datos cadena.

- Asignación de variables a variables
   - Utilizando un proceso similar, también puedes asignar variables a otras variables.
   - En el siguiente ejemplo, la variable username se asigna a una nueva variable old_username:
      - `# Assign a variable to another variable`
      - `username = "nzhao"`
      - `old_username = username`
   - Como username contiene el valor de cadena de "nzhao" y old_username contiene el valor de username, old_username contiene ahora un valor de "nzhao".

- Montaje
   - El siguiente código demuestra cómo se puede actualizar un nombre de usuario.
   - A la variable username se le asigna un valor inicial, que se almacena en una segunda variable llamada old_username.
   - A continuación, se reasigna un nuevo valor a la variable username.
   - Puedes ejecutar este código para obtener un mensaje sobre el nombre de usuario anterior y el actual:
   - [File example](./resources/code/modulo_01_03-019.py)

- Mejores prácticas para nombrar variables
   - Puedes nombrar una variable casi como quieras, pero hay algunas pautas que debes seguir para asegurar una sintaxis correcta y prevenir errores:
      - Utilice sólo letras, números y guiones bajos en los nombres de las variables.
      - Ejemplos válidos: date_3, username, interval2
      - Recuerda que los nombres de variables en Python distinguen entre mayúsculas y minúsculas.
      - Estas son variables diferentes: time, Time, TIME, timE.
      - No uses palabras clave o funciones incorporadas en Python para nombres de variables.
      - Por ejemplo, las variables no deberían llamarse True, False, o if.
      - Además, debes seguir estas pautas de estilo para que tu código sea más fácil de leer y entender para ti y para otros analistas de seguridad:
         - Separe dos o más palabras con guiones bajos.
         - Ejemplos válidos: login_attempts, invalid_user, status_update
         - Evite variables con nombres similares.
         - Estas variables podrían confundirse fácilmente entre sí: start_time, starting_time, time_starting.
         - Evita nombres innecesariamente largos para las variables.
         - Por ejemplo, no dé a las variables nombres como variable_that_equals_3.
         - Los nombres deben describir los datos y no ser palabras al azar.
         - Ejemplos válidos: num_login_attempts, device_id, invalid_usernames
   - Se recomienda utilizar guiones bajos para separar varias palabras en las variables, pero otra convención que puede encontrarse es escribir en mayúscula la primera letra de cada palabra excepto la primera.
   - Ejemplo: loginAttempt
   
---

## Actividad: Asignar variables Python
- Introducción
   - En este laboratorio, abrirá un entorno de notebook para practicar la asignación de valores a variables en Python.
   - Se le presentará un escenario de seguridad para que lo explore a lo largo del laboratorio.
   - Creará variables para realizar un seguimiento de la información relevante para el proceso de inicio de sesión de los usuarios aprobados para iniciar sesión en un dispositivo específico.

- Lo que hará
   - Asignar variables de varios tipos de datos
   - Utilizar la función type() para devolver el tipo de datos de una variable

- Scenario
   - You are a security analyst who is responsible for writing code that will automate analysis of login attempts made to a specific device.
   - As the first step, you'll need to create variables to keep track of information relevant to the login process.
   - This information includes the device ID, list of approved usernames, maximum login attempts allowed per user, current login attempts made by a user, and login status.
   - Throughout this lab, you'll assign these variables and check the data types of the variables.

- Task 1
   - In your work as an analyst, imagine there is a device only users specified on an allow list can access, and its device ID is "72e08x0".
   - In the following code cell, assign this value to a variable named device_id.
   - Then, display the contents of the variable and observe the output.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_01.py)

- Task 2
   - Now that the variable device_id is defined, you can return its data type.
   - In this task, use a Python function to find the data type of the variable device_id.
   - Store the data type in another variable called device_id_type.
   - Then, display device_id_type to examine the output.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_02.py)
   - Based on the output above, what do you observe about the data type of device_id?
   > The data type of device_id is a string, as it contains a sequence of characters enclosed in quotes.

- Task 3
   - As you continue your work, you're provided a list of usernames of users who are allowed to access the device.
   - The usernames with this access are "madebowa", "jnguyen", "tbecker", "nhersh", and "redwards".
   - In this task, create a variable called username_list.
   - Assign a list with the approved usernames to this variable.
   - Then, display the value of the username_list variable.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_03.py)

- Task 4
   - In this task, find the data type of the username_list.
   - Store the type in a variable called username_list_type.
   - Then, display username_list_type to examine the output.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_04.py)
   - Based on the output above, what do you observe about the data type of username_list?
   > The data type of username_list is a list, as it contains a collection of values enclosed in square brackets.

- Task 5
   - Now, imagine that you've been informed that the previous list is not up-to-date and that there is another employee that now has access to the device.
   - You're given the updated list of usernames with access, including the new employee, as follows: "madebowa", "jnguyen", "tbecker", "nhersh", "redwards", and "lpope".
   - In this task, reassign the variable username_list to the new list. Run the code to display the list before and after it's been updated to observe the difference.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_05.py)
   - Based on the output above, what do you observe about the contents of username_list?
   > The contents of username_list have been updated to include the new employee "lpope", reflecting the current list of usernames with access to the device.

- Task 6
   - In this task, define a variable called max_logins that represents the maximum number of login attempts allowed per user.
   - Store the value 3 in this variable.
   - Then, store its data type in another variable called max_logins_type.
   - Display max_logins_type to examine the output.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_06.py)
   - Based on the output above, what do you observe about the data type of max_logins?
   > The data type of max_logins is an integer, as it contains a whole number without any decimal point.

- Task 7
   - In this task, define a variable called login_attempts that represents the current number of login attempts made by a user.
   - Store the value 2 in this variable.
   - Then, store its data type in a variable called login_attempts_type.
   - Display login_attempts_type to observe the output.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_07.py)
   - Based on the output above, what do you observe about the data type of login_attempts?
   > The data type of login_attempts is an integer, as it contains a whole number without any decimal point.

- Task 8
   - In this task, you'll determine the Boolean value that represents whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_08.py)
   - What is the output? What does this mean?
   > The output is True, which means that the current number of login attempts (2) is less than or equal to the maximum allowed login attempts (3). This indicates that the user has not exceeded the allowed number of login attempts.

- Task 9
   - This code continues to check for the Boolean value of whether max_logins is less than or equal to login_attempts.
   - In this task, reassign other values to login_attempts.
   - For example, you might choose a value that is higher than the maximum number of attempts allowed.
   - Observe how the output changes.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_09.py)
   - Based on the different values you assigned to login_attempts, what did you observe about the output?
   > When login_attempts is assigned a value greater than max_logins, the output changes to False. This indicates that the current number of login attempts has exceeded the maximum allowed, and the user would not be permitted to attempt another login.

- Task 10
   - Finally, you can also assign a Boolean value of True or False to a variable.
   - In this task, you'll create a variable called login_status, which is a Boolean that represents whether a user is logged in.
   - Assign False to this variable and store its data type in a variable called login_status_type and display it.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [File example](./resources/code/lab_02/task_10.py)
   - Based on the output above, what do you observe about the data type of login_status?
   > The data type of login_status is a Boolean, as it can only hold one of two values: True or False. In this case, it is assigned the value False, indicating that the user is not logged in.

---

## Ejemplar: Asignar variables Python
- Mismo laboratorio que el anterior

- Conclusion
   - There are many useful operators in Python that help you work with variables.
      - The = assignment operator allows you to assign or reassign a specific value to a variable.
      - The <= comparison operator allows you to compare the value of one variable to the value of another.
   - The type() function in Python helps you to determine the data type of an object.
      - If you pass in a variable to type(), it will output the data type of the value stored in the variable.
   - The print() function in Python allows you to display information.
      - It can take in a value directly, a variable that stores a value, or a comparison between variables that evaluates to a Boolean value.