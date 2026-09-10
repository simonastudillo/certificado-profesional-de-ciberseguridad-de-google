# Trabajar con funciones

## Utilizar parámetros en las funciones
- ​Anteriormente, definimos y llamamos a nuestra primera función.
- ​No requería ninguna información de fuera de la función, pero ​otras funciones podrían hacerlo.
- ​Esto significa que tenemos que hablar sobre el uso de parámetros en las funciones.
- ​En Python, un parámetro es un objeto que se incluye en la definición de una función para ​utilizarlo en esa función.
- ​Los parámetros se aceptan en una función a través de los paréntesis después de ​un nombre de función.
- ​La función que creamos en el último vídeo no acepta ningún parámetro.
- ​Ahora, volvamos a examinar otra función llamada range() que sí utiliza parámetros.
- ​Si lo recuerda, la función range() genera una secuencia de ​números desde un punto de inicio hasta el valor anterior al punto de parada.
- ​Por lo tanto, range() sí incluye parámetros para los índices de inicio y ​parada que aceptan cada uno un valor entero.
- ​Por ejemplo, podría aceptar los enteros 3 y 7.
- ​Esto significa que la secuencia que genera irá del 3 al 6.
- ​En nuestro ejemplo anterior, ​escribimos una función que mostraba un mensaje de bienvenida cuando alguien iniciaba sesión.
- ​Sería aún más acogedor si incluyéramos el nombre del empleado con ​el mensaje.
- ​¡Definamos una función con un parámetro para poder saludar a los empleados por su nombre!
- ​Cuando definamos nuestra función, ​incluiremos el nombre del parámetro del que depende nuestra función.
- ​Colocamos este parámetro, la variable de nombre, dentro del paréntesis.
- ​El resto de la sintaxis se mantiene igual.
- ​Ahora, pasemos a la siguiente línea y hagamos una sangría para ​poder decirle a Python lo que queremos que haga esta función.
- ​Queremos que imprima un mensaje que dé la bienvenida al empleado utilizando el nombre que se ​ha pasado a la función.
- ​Incorporar esta variable a nuestra sentencia print requiere algunas consideraciones.
- ​Al igual que antes, empezamos con el mensaje de bienvenida que queremos imprimir.
- ​En este caso, sin embargo, ​no vamos a detener nuestro mensaje después de decirles que han iniciado sesión.
- ​Queremos continuar y añadir el nombre del empleado al mensaje.
- ​Por eso estamos colocando una coma después de "Ha iniciado sesión" ​y luego añadimos la variable de nombre.
- ​Como se trata de una variable y no de una cadena específica, ​no la entrecomillamos.
- ​Ahora que nuestra función está configurada, ​estamos listos para llamarla con el argumento específico que queremos pasar.
- ​En Python, un argumento son los datos que se introducen en una función cuando se llama a ella.
- ​Por ejemplo, antes, cuando pasamos 3 y ​7 a la función range(), eran argumentos.
- ​En nuestro caso, imaginemos que queremos saludar a un empleado llamado Charley Patel.
- ​Llamamos a nuestra función greet_employee() con este argumento.
- ​¡Y cuando la ejecutamos, Charley Patel recibe un mensaje de bienvenida personalizado!
- ​En este ejemplo, sólo tenemos un parámetro en nuestra función.
- Pero ​podemos tener más.
- ​Exploremos un ejemplo de esto. ​Tal vez, en lugar de un único parámetro para el nombre, tengamos un parámetro para ​el nombre y un segundo parámetro para el apellido.
- ​Si es así, tendríamos que ajustar el código de la siguiente manera.
- ​Primero, cuando definimos la función, ​incluimos ambos parámetros y los separamos con una coma.
- ​Después, cuando la llamamos, también incluimos dos argumentos.
- Esta vez saludamos ​a alguien con el nombre de Kiara y con el apellido de Carter.
- ​También los separamos con una coma.
- ​¡Ejecutémosla y demos la bienvenida a Kiara Carter!
- ​Como acabamos de explorar, utilizar más de un parámetro ​sólo requiere unos pocos ajustes.
- [file](./resources/code/modulo-02_02-001.py)

---

## Sentencias de retorno
- ​Anteriormente aprendimos cómo pasar argumentos a una función.
- ​Podemos hacer más que pasar información a una función.
- ​¡También podemos enviar información fuera de una!
- ​Las sentencias de retorno nos permiten hacer esto.
- ​Una sentencia de retorno es una sentencia Python que se ejecuta dentro de una función y ​envía información de vuelta a la llamada a la función.
- ​Esta capacidad de enviar información de vuelta desde una función es útil para un ​analista de seguridad de varias maneras.
- ​Como ejemplo, un analista podría tener una función que comprueba ​si alguien tiene permiso para acceder a un archivo en particular y ​devolverá un valor booleano de "Verdadero" o "Falso" al programa más grande.
- ​Vamos a explorar otro ejemplo.
- ​Creemos una función relacionada con el análisis de los intentos de inicio de sesión.
- ​A partir de la información que toma, esta función calculará ​el porcentaje de intentos fallidos y devolverá este porcentaje.
- ​El programa podría utilizar esta información de diversas maneras.
- ​Por ejemplo, podría utilizarse para determinar si se debe bloquear o no una cuenta.
- ​Así que vamos a empezar y aprender cómo devolver información desde una función.
- ​Al igual que antes, empezamos definiendo nuestra función.
- La llamaremos calcular_intentos() ​y estableceremos dos parámetros relacionados con los intentos de inicio de sesión: ​uno para total_intentos y otro para intentos_fallidos.
- ​A continuación, le diremos a Python lo que queremos que haga esta función.
- ​Queremos que esta función almacene el porcentaje de intentos fallidos en ​una variable llamada fail_percentage.
- ​Necesitamos dividir failed_attempts entre total_attempts para obtener este porcentaje.
- ​Hasta ahora, esto es similar a lo que hemos aprendido anteriormente.
- Pero ahora, ​vamos a aprender cómo devolver el porcentaje de fallos.
- ​Para ello, necesitamos utilizar la palabra clave return.
- ​Return se utiliza para devolver información de una función.
- ​En nuestro caso, devolveremos el porcentaje que acabamos de calcular.
- ​Así que después de la palabra clave return, escribiremos fail_percentage.
- ​Esta es nuestra variable que contiene esta información.
- ​Ahora, estamos listos para llamar a esta función.
- Calcularemos el porcentaje para ​un usuario que se ha registrado 4 veces con 2 intentos fallidos.
- ​Entonces, nuestros argumentos son 4 y 2.
- ​Cuando ejecutamos esto, la función devuelve el porcentaje de ​intentos fallidos.
- Es .5, o el 50 por ciento, ​pero en algunos entornos Python, puede que esto no se imprima en pantalla.
- ​No podemos utilizar la variable específica llamada fail_percentage ​fuera de la función.
- ​Así que, para utilizar esta información en otra parte del Programa, ​tendríamos que devolver el valor de la función y asignarlo a una nueva variable.
- ​Vamos a comprobarlo.
- ​Esta vez, cuando se llama a la función, ​el valor que se devuelve se almacena en una variable llamada porcentaje.
- ​Entonces, podemos utilizar esta variable en código adicional.
- ​Por ejemplo, podemos escribir una condicional que compruebe si el porcentaje ​de intentos fallidos es mayor o igual al 50 por ciento.
- ​Cuando se cumpla esta condición, podemos decirle a Python que imprima un mensaje de "Cuenta bloqueada".
- ​Ejecutemos este código.
- ​Y esta vez, el porcentaje no se devuelve a la pantalla.
- ​En su lugar, obtenemos el mensaje "Cuenta bloqueada".

---

## Funciones y variables
- Trabajar con variables en funciones
   - Trabajar con variables en funciones requiere comprender tanto los parámetros como los argumentos.
   - Los términos parámetros y argumentos tienen usos distintos cuando se refieren a variables en una función.
   - Además, si desea que la función devuelva un resultado, debe estar familiarizado con las sentencias return.

- Parámetros
   - Un parámetro es un objeto que se incluye en la definición de una función para utilizarlo en ella.
   - Cuando define una función, crea variables en la cabecera de la función.
   - A continuación, pueden utilizarse en el cuerpo de la función.
   - En este contexto, estas variables se denominan parámetros.
   - Por ejemplo, considere la siguiente función:
   - [file](./resources/code/modulo-02_02-003.py)
   - Esta función toma dos variables, maximum_attempts y total_attempts y las utiliza para realizar un cálculo.
   - En este ejemplo, maximum_attempts y total_attempts son parámetros.

- Argumentos
   - En Python, un argumento son los datos que se introducen en una función cuando se llama a ella.
   - Al llamar a remaining_login_attempts en el siguiente ejemplo, los enteros 3 y 2 se consideran argumentos:
      - `remaining_login_attempts(3, 2)`
   - Estos enteros pasan a la función a través de los parámetros que se identificaron al definir la función.
   - En este caso, esos parámetros serían maximum_attempts y total_attempts.
   - 3 está en la primera posición, por lo que pasa a maximum_attempts.
   - Del mismo modo, 2 está en la segunda posición y pasa a total_attempts.

- Sentencias de retorno
   - Cuando se definen funciones en Python, se utilizan sentencias de retorno si se desea que la función devuelva una salida.
   - La palabra clave return se utiliza para devolver información de una función.
   - La palabra clave return aparece delante de la información que desea devolver.
   - En el siguiente ejemplo, está antes del cálculo de cuántos intentos de inicio de sesión quedan:
   - [file](./resources/code/modulo-02_02-004.py)
   - La palabra clave return no es una función, por lo que no debe colocar paréntesis después de ella.
   - Las sentencias de retorno son útiles cuando desea almacenar lo que devuelve una función dentro de una variable para utilizarlo en otra parte del código.
   - Por ejemplo, puede utilizar esta variable para cálculos o dentro de sentencias condicionales.
   - En el siguiente ejemplo, la información devuelta por la llamada a remaining_login_attempts se almacena en una variable llamada remaining_attempts.
   - A continuación, esta variable se utiliza en una condicional que imprime un mensaje "Your account is locked" cuando remaining_attempts es menor o igual que 0.
   - Puede ejecutar este código para explorar su resultado:
   - [file](./resources/code/modulo-02_02-005.py)
   - En este ejemplo, el mensaje se imprime porque el cálculo en la función da como resultado 0.
   - Cuando Python encuentra una sentencia return, ejecuta esta sentencia y luego sale de la función.
   - Si hay líneas de código que siguen a la sentencia return dentro de la función, no se ejecutarán.
   - El ejemplo anterior no contenía ninguna línea de código después de la sentencia return, pero esto podría aplicarse en otras funciones, como una que contenga una sentencia condicional.

- Variables globales y locales
   - Para entender mejor cómo interactúan las funciones con las variables, debe conocer la diferencia entre variables globales y locales.
   - Cuando define y llama a funciones, está trabajando con variables locales, que son diferentes de las variables que define fuera del ámbito de una función.

- Variables globales
   - Una variable global es una variable que está disponible en todo el programa.
   - Las variables globales se asignan fuera de la definición de una función.
   - Siempre que se llame a esa variable, ya sea dentro o fuera de una función, devolverá el valor que se le haya asignado.
   - Por ejemplo, puede asignar la siguiente variable al principio de su código:
      - `device_id = "7ad2130bd"`
   - A lo largo del resto de su código, podrá acceder a la variable device_id y modificarla en condicionales, bucles, funciones y otras sintaxis.

- Variables locales
   - Una variable local es una variable asignada dentro de una función.
   - No se puede llamar a estas variables ni acceder a ellas fuera del cuerpo de una función.
   - Las variables locales incluyen parámetros, así como otras variables asignadas dentro de la definición de una función.
   - En la siguiente definición de función, total_string y name son variables locales:
   - [file](./resources/code/modulo-02_02-006.py)
   - La variable total_string es una variable local porque está asignada dentro de la función.
   - El parámetro name es una variable local porque también se crea al definir la función. 
   - Cada vez que llama a una función, Python crea estas variables temporalmente mientras la función se está ejecutando y las borra de la memoria después de que la función deja de ejecutarse.
   - Esto significa que si llama a la función greet_employee() con un argumento y luego utiliza la variable total_string fuera de esta función, obtendrá un error.

- Mejores prácticas para variables globales y locales
   - Cuando trabaje con variables y funciones, es muy importante que se asegure de que sólo utiliza un determinado nombre de variable una vez, aunque una esté definida globalmente y la otra localmente.
   - Al utilizar variables globales dentro de las funciones, éstas pueden acceder a los valores de una variable global. Puede ejecutar el siguiente ejemplo para explorar esto:
   - [file](./resources/code/modulo-02_02-007.py)
   - El bloque de código devuelve "elarson" aunque ese nombre no esté definido localmente.
   - La función accede a la variable global.
   - Si quisiera que la función identify_user() diera cabida a otros nombres de usuario, tendría que reasignar la variable global de nombre de usuario fuera de la función.
   - Esto no es una buena práctica. Una forma mejor de pasar diferentes valores a una función es utilizar un parámetro en lugar de una variable global.
   - También hay algo más a tener en cuenta.
   - Si reutiliza el nombre de una variable global dentro de una función, se creará una nueva variable local con ese nombre.
   - En otras palabras, habrá tanto una variable global con ese nombre como una variable local con ese nombre, y tendrán valores diferentes.
   - Puede considerar el siguiente bloque de código:
   - [file](./resources/code/modulo-02_02-008.py)
   - La primera sentencia de impresión se produce antes de la función, y Python devuelve el valor de la variable global username, "elarson".
   - La segunda sentencia print está dentro de la función, y devuelve el valor de la variable local username, que es "bmoreno".
   - Pero esto no cambia el valor de la variable global, y cuando username se imprime por tercera vez después de la llamada a la función, sigue siendo "elarson".
   - Debido a esta complejidad, es mejor evitar combinar variables globales y locales dentro de las funciones. 

---

## Explorar las funciones integradas
- ​Ahora que sabemos cómo crear nuestras propias funciones, ​exploremos también algunas de las funciones integradas de Python.
- ​Como comentamos anteriormente, ​las funciones integradas son funciones que existen ​en Python y se pueden llamar directamente.
- ¡ ​Nuestro único trabajo es llamarlos por ​su nombre!
- Y ​ya hemos descrito algunas a lo largo del curso; ​por ejemplo, las funciones print () y type () de Python.
- ¡ ​Revisemos rápidamente esas dos funciones integradas ​antes de conocer otras nuevas!
- ​Primero, print () envía un objeto específico a la pantalla.
- ​Y luego, la función type () devuelve el tipo de datos de su entrada.
- ​Anteriormente, utilizábamos ​funciones de forma independiente unas de otras.
- ​Por ejemplo, le pedimos a Python que imprima ​algo o le pedimos ​a Python que devolviera el tipo de datos de algo.
- A ​medida que empecemos a explorar las funciones integradas, ​a menudo necesitaremos usar varias funciones juntas.
- ​Podemos hacerlo pasando ​una función a otra como argumento.
- ​Por ejemplo, en esta línea de código, ​Python devuelve primero el tipo de datos «Hello» en forma de cadena.
- ​Luego, este valor devuelto se pasa a la función print().
- ​Esto significa que el tipo de datos de la ​cadena se imprimirá en la pantalla.
- ​print() y type() ​no son las únicas funciones que ​verás que se usan juntas de esta manera.
- ​En todos los casos, la sintaxis general es la misma. ​La función interna se procesa primero y, a continuación, ​su valor devuelto se pasa a la función externa.
- ​Consideremos otro aspecto ​del trabajo con funciones integradas.
- ​Al trabajar con funciones, ​debe comprender cuáles son ​sus entradas y salidas esperadas.
- ​Algunas funciones solo esperan tipos de datos específicos ​y devolverán un error de tipo si utilizas uno incorrecto.
- ​Otras funciones necesitan una cantidad específica ​de parámetros o devuelven un tipo de datos diferente.
- ​La función print (), por ejemplo, ​puede tomar cualquier tipo de datos como entrada.
- ​También puede aceptar cualquier cantidad de parámetros, ​incluso aquellos con diferentes tipos de datos.
- ​Exploremos la entrada y la salida de la función print().
- ​Introduciremos tres argumentos.
- ​El primero contiene datos de cadenas.
- ​Luego, se usa una coma para ​separar esto del segundo argumento.
- ​Este segundo argumento es un número entero.
- ​Finalmente, después de otra coma, ​nuestro tercer argumento es otra cadena.
- ​Ahora, ejecutemos este código.
- ​¡Perfecto! ¡Esto se imprimió tal como se esperaba!
- [file](./resources/code/modulo-02_02-009.py)
- ​La función type() también acepta todos los tipos de datos, ​pero solo acepta un parámetro.
- ​Exploremos también esta entrada y salida.
- ​Nuestra primera línea de código ​determinará primero el tipo de datos de ​la palabra «Seguridad» y ​, a continuación, pasará lo que devuelve a una función print().
- ​Y la segunda línea de código hará ​lo mismo con el valor de 73.2.
- ​Ahora, ejecutemos esto y veamos qué pasa.
- ​Python primero devuelve un resultado que ​nos dice que la palabra «Seguridad» es una cadena de datos.
- [file](./resources/code/modulo-02_02-010.py)
- ​A continuación, devuelve otra línea de salida que ​nos dice que 73.2 son datos flotantes.
- ​Ahora, sabemos qué ​considerar antes de usar una función integrada.
- ​Tenemos que saber exactamente cuántos parámetros ​requiere y qué tipos de datos pueden ser.
- ​También necesitamos saber qué tipo de producto produce.
- ​Aprendamos un par de ​nuevas funciones integradas y pensemos en esto.
- ​Empezaremos con max().
- ​La función max () devuelve ​la entrada numérica más grande que se le haya pasado.
- ​No tiene un número definido de ​parámetros que acepte.
- ​Exploremos la función max().
- ​Pasaremos tres argumentos ​a max () en forma de variables.
- ​Así que primero definamos esas variables.
- ​Estableceremos el valor de a en 3, ​b en 9 ​y c en 6.
- ​Luego, pasaremos estas variables a ​la función max() y las imprimiremos.
- Vamos a ejecutar esto.
- ​Nos dice que el valor más alto entre ellos es 9.
- [file](./resources/code/modulo-02_02-011.py)
- Ahora, estudiemos ​otra función incorporada: la función sorted().
- ​La función sorted() ordena los componentes de una lista.
- ​Esta función puede resultar muy útil en un entorno de Seguridad.
- ​Cuando trabajamos con listas, ​a menudo tenemos que ordenarlas.
- Con las listas de números, ​los ordenamos de menor a ​mayor o viceversa.
- ​Con las listas de cadenas de datos, ​es posible que necesitemos ordenarlas alfabéticamente.
- ​Imagine que tiene una lista que contiene ​los nombres de usuario de su organización ​y desea ordenarlos alfabéticamente.
- ​Usemos la función sorted() de Python para esto.
- ​Especificaremos nuestra lista a través de una variable llamada usernames.
- ​En esta lista, incluiremos ​todos los nombres de usuario que queremos ordenar.
- ​Ahora, usaremos la función sorted() para ​ordenar estos nombres pasándole ​la variable usernames.
- ​Y luego pasaremos su resultado a ​la declaración de impresión para que pueda mostrarse en la pantalla.
- ​Cuando lo ejecutamos, ¡todo está en orden!
- [file](./resources/code/modulo-02_02-012.py)
- ​Estas son solo algunas de ​las funciones integradas disponibles para su uso.
- ​A medida que trabajes más en Python, ​te familiarizarás con ​otras personas que pueden ayudarte en tus programas. 

---

## Trabajar con funciones integradas
- Funciones integradas son funciones que existen dentro de Python y pueden ser llamadas directamente.

- print()
   - La función print() da salida a un objeto especificado en la pantalla.
   - La función print() es una de las más utilizadas en Python porque le permite dar salida a cualquier detalle de su código.
   - Para utilizar la función print(), debe pasar el objeto que desea imprimir como argumento a la función.
   - La función print() acepta cualquier número de argumentos, separados por una coma, e imprime todos ellos.
   - Por ejemplo, puede ejecutar el siguiente código que imprime una cadena, una variable, otra cadena y un número entero juntos:
   - [file](./resources/code/modulo-02_02-013.py)

- type()
   - La función type() devuelve el tipo de datos de su argumento.
   - La función type() le ayuda a realizar un seguimiento de los tipos de datos de las variables para evitar errores a lo largo de su código.
   - Para utilizarla, se pasa el objeto como argumento, y devuelve su tipo de datos.
   - Sólo acepta un argumento. Por ejemplo, puede especificar type("security") o type(7).

- Pasar una función a otra
   - Cuando trabaje con funciones, a menudo necesitará pasarlas a través de print() si desea que el tipo de datos aparezca en pantalla.
   - Este es el caso cuando se utiliza una función como type().
   - Considere el siguiente código:
   - [file](./resources/code/modulo-02_02-014.py)
   - Muestra str, lo que significa que el argumento pasado a la función type() es una cadena.
   - Esto sucede porque la función type() se procesa primero y su salida se pasa como argumento a la función print(). 

- max() y min()
   - La función max() devuelve la entrada numérica más grande que se le haya pasado.
   - La función min() devuelve la entrada numérica más pequeña que se le haya pasado.
   - Las funciones max() y min() aceptan argumentos de múltiples valores numéricos o de un iterable como una lista, y devuelven el mayor o el menor valor respectivamente.
   - En un contexto de ciberseguridad, podría utilizar estas funciones para identificar la Sesión más larga o más corta en la que se registró un usuario.
   - Si un usuario concreto se conectó siete veces durante una semana, y usted almacenó sus tiempos de acceso en minutos en una lista, puede utilizar las funciones max() y min() para encontrar e imprimir sus sesiones más larga y más corta:
   - [file](./resources/code/modulo-02_02-015.py)

- sorted()
   - La función sorted() ordena los componentes de una lista.
   - La función sorted() también funciona sobre cualquier iterable, como una cadena, y devuelve los elementos ordenados en una lista.
   - Por defecto, los ordena en orden ascendente.
   - Cuando se le da un iterable que contiene números, los ordena de menor a mayor; esto incluye iterables que contienen datos numéricos, así como iterables que contienen Datos de cadena que comienzan con números.
   - Un iterable que contenga cadenas que empiecen por caracteres alfabéticos se ordenará alfabéticamente.
   - La función sorted() toma como entrada un iterable, como una lista o una cadena.
   - Así, por ejemplo, puede utilizar el siguiente código para ordenar la lista de sesiones de inicio de sesión de la más corta a la más larga:
   - [file](./resources/code/modulo-02_02-016.py)
   - Esto muestra la lista ordenada.
   - La función sorted() no cambia el iterable que ordena. El código siguiente lo ilustra:
   - [file](./resources/code/modulo-02_02-017.py)
   - La primera función print() muestra la lista ordenada.
   - Sin embargo, la segunda función print(), que no incluye la función sorted(), muestra la lista tal y como se asignó a time_list en la primera línea de código.
   - Otro detalle importante sobre la función sorted() es que no puede tomar listas o cadenas que tengan elementos de más de un tipo de datos.
   - Por ejemplo, no puede utilizar la lista [1, 2, "hello"].

- Recursos
   - [Documentación de la Biblioteca estándar de Python](https://docs.python.org/3/library/functions.html)

---

## Actividad: Crear más funciones
- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para seguir practicando el trabajo con funciones en Python.
   - Se le presentará un escenario de Seguridad para que lo explore a lo largo del laboratorio.
   - Utilizará funciones integradas para trabajar con una Lista de intentos fallidos de inicio de sesión por mes.
   - También definirá una función que le ayudará a analizar los intentos de inicio de sesión.

- Lo que hará
   - Aplicar las funciones integradas max() y sorted() a una lista de intentos fallidos de inicio de sesión
   - Definir una función que compare los inicios de sesión del día actual con una media
   - Devolver información de la función que ha creado

- Scenario
   - In your work as a security analyst, you're responsible for working with a list that contains the number of failed attempts that occurred each month.
   - You'll identify any patterns that might indicate malicious activity.
   - You're also responsible for defining a function that compares the logins for the current day to an average and improving it by adding a return statement.

- Task 1
   - In your work as an analyst, imagine that you're provided a list of the number of failed login attempts per month, as follows:
   - 119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, and 223.
   - This list is organized in chronological order of months (January, February, March, April, May, June, July, August, September, October, November, and December).
   - This list is stored in a variable named failed_login_list.
   - In this task, use a built-in Python function to order the list.
   - You'll pass the call to the function that sorts the list directly into the print() function.
   - This will allow you to display and examine the result.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_01.py)
   - What do you observe from the output above? Do you notice any outlying numbers that indicate an increase in the failed number of login attempts?
   > From the output, it is evident that the numbers 264 and 223 are outliers, indicating a significant increase in the failed number of login attempts compared to the other months.

- Task 2
   - Now, you'll want to isolate the highest number of failed login attempts so you can later investigate information about the month when that highest value occurred.
   - You'll use the function that returns the largest numeric element from a list.
   - Then, you'll pass this function into the print() function to display the result.
   - This will allow you to determine which month to investigate further.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_02.py)
   - What do you observe from the output above?
   > From the output, it is evident that the highest number of failed login attempts occurred in the month corresponding to the value 264.

- Task 3
   - In your work as an analyst, you'll first define a function that displays a message about how many login attempts a user has made that day.
   - In this task, define a function named analyze_logins() that takes in two parameters, username and current_day_logins.
   - Every time this function is called, it should display a message about the number of login attempts the user has made that day.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - Note that the code cell will contain only a function definition, so running it will not produce an output.
   - [file](./resources/code/lab_06/task_03.py)

-  Task 4
   - Now that you've defined the analyze_logins() function, call it to test out how it behaves.
   - Call analyze_logins() with the arguments "ejones" and 9.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_04.py)
   - What does this function display? Would the output vary for different users?
   > The function displays a message indicating the current day's login total for the specified user. Yes, the output would vary for different users and different login totals.

- Task 5
   - Now, you'll need to expand this function so that it also provides the average number of login attempts made by the user on that day.
   - Doing this will require incorporating a third parameter into the function definition.
   - In this task, add a parameter called average_day_logins.
   - The code will use this parameter to display an additional message.
   - The additional message will convey the average login attemps made by the user on that day.
   - Then, call the function with the same first and second arguments as used in Task 4 and a third argument of 3.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_05.py)

- Task 6
   - In this task, you'll further expand the function.
   - Include a calculation to get the ratio of the logins made on the current day to the logins made on an average day.
   - Store this in a new variable named login_ratio.
   - The function displays an additional message that uses this variable.
   - Note that if average_day_logins is equal to 0, then dividing current_day_logins by average_day_logins will cause an error.
   - Due to the error, Python will display the following message: ZeroDivisionError: division by zero.
   - For this activity, assume that all users will have logged in at least once before.
   - This means that their average_day_logins will be greater than 0, and the function will not involve dividing by zero.
   - After defining the function, call the function with the same arguments that you used in the previous task.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_06.py)
   - What does this version of the analyze_logins() function display? Would the output vary for different users?
   > The function displays a message indicating the current day's login total, the average logins per day, and the ratio of the current day's logins to the average. Yes, the output would vary for different users and different login totals.

- Task 7
   - You'll continue working with the analyze_logins() function and add a return statement to it.
   - Return statements allow you to send information back to the function call.
   - In this task, use the return keyword to output the login_ratio from the function, so that it can be used later in your work.
   - You'll call the function with the same arguments used in the previous task and store the output from the function call in a variable named login_analysis.
   - You'll then use a print() statement to display the saved information.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_07.py)
   - How does this version of the analyze_logins() function compare to the previous versions?
   > This version of the analyze_logins() function not only displays the login information but also returns the login ratio, allowing the calling code to use this value for further analysis or display.

- Task 8
   - In this task, you'll use the value of login_analysis in a conditional statement.
   - When the value of login_analysis is greater than or equal to 3, then the login activity will require further investigation, and an alert will be displayed.
   - Incorporate this condition to complete the conditional statement in the code.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before you run the following cell.
   - [file](./resources/code/lab_06/task_08.py)

- Conclusion
   - This lab demonstrated how to define a function that analyzes login activity, how to return values from a function, and how to use those returned values in conditional statements to trigger alerts based on unusual login behavior.
   - By completing these tasks, you have practiced defining functions, returning values, and using conditional statements to analyze and respond to login activity.
   - This lab also emphasized the importance of monitoring login activity to detect potential security issues early.

---

## Ejemplar: Crear más funciones
- Mismo laboratorio que el anterior.

- Conclusion
   - There are a variety of ways a function can be written.
   - It can be written to display information to the screen, or return information that can then be saved in a variable.
   - Also it can be written to take in any number of parameters, use the parameters to execute a series of tasks, and then return a result.
   - The sorted() function in Python is a built-in function that helps you sort the components of a list.
   - For example, when you call sorted() with a list of numbers, it returns the list with the elements in numerical order.
   - The max() function in Python is a built-in function that helps you identify the element with the maximum value in a list.
   - For example, when you call max() with a list of numbers, it returns the largest number in the list.
   - The print() function in Python is a built-in function that helps display information. It can also be used to directly display the output from another function call.
   - To display the output from another function call, make sure to place it inside a print() statement.