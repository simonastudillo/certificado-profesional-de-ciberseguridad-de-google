# Depuración de código Python

## Estrategias de depuración
- ​Como analista de Seguridad, ​es posible que deba leer o escribir código.
- ​Uno de los mayores desafíos ​es lograr que funcione correctamente.
- ​De hecho, corregir errores complejos en el ​código a veces puede llevar tanto ​tiempo, si no más, que escribir el código.
- ​Por eso es importante desarrollar esta habilidad.
- ​Ahora que has aprendido los conceptos básicos de la programación en Python, ​es importante que aprendas a gestionar los errores.
- ​Por ese motivo, nos centraremos en depurar tu código.
- ​Depuración es la práctica de ​identificar y corregir errores en el código.
- Exploraremos algunas técnicas para ello.
- ​Hay tres tipos de errores: errores de ​sintaxis, errores lógicos y excepciones.
- ​Los errores de sintaxis implican ​un uso no válido del lenguaje Python, como olvidar añadir dos puntos después del encabezado de una función.
- ​Exploremos este tipo de error.
- ​Cuando ejecutamos este código, ​recibimos un mensaje que indica que hay un error de sintaxis.
- ​Según el entorno de Python ​, también puede mostrar detalles adicionales.
- ​Por lo general, obtendremos información sobre ​el error, como su ubicación.
- ​Estos errores de sintaxis suelen ser fáciles de corregir, ​ya que puede encontrar exactamente dónde ocurrió el error.
- ​Son similares a corregir ​errores gramaticales simples en un correo electrónico.
- ​Como el mensaje de error nos dice que el problema está en ​la línea que define la función, vayamos allí.
- ​En este caso, podemos añadir ​dos puntos al encabezado y resolver nuestro error.
- ​Cuando lo ejecutamos de nuevo, ​ya no aparece ningún mensaje de error.
- ​Este es solo un ejemplo de error de sintaxis.
- [file](./resources/code/modulo-04_03-001.py)
- ​Otros ejemplos incluyen omitir ​un paréntesis después de una función, escribir ​mal una palabra clave de Python ​o no cerrar correctamente las comillas de una cadena.
- ​A continuación, centrémonos en los errores lógicos.
- ​Es posible que los errores lógicos no provoquen mensajes de error; ​en cambio, producen resultados no deseados.
- ​Un error lógico puede ser tan simple como escribir ​el texto incorrecto en una sentencia impresa, o ​puede implicar algo como escribir ​un símbolo menor que en lugar ​de un símbolo menor que o igual a.
- ​Este cambio en el operador excluiría ​un valor que era necesario para que el código funcionara según lo previsto.
- ​Por ejemplo, ​imagine que se pone en contacto con un equipo de respuesta cuando ​el nivel de prioridad de un problema es inferior a ​tres en lugar de inferior o igual a tres.
- ​Esto significa que todos los eventos clasificados como de ​nivel de prioridad 3 podrían pasar desapercibidos y quedar sin resolver.
- ​Para diagnosticar un error lógico difícil de encontrar, ​una estrategia consiste en utilizar sentencias impresas.
- ​Deberás insertar ​sentencias de impresión en todo el código.
- ​Las instrucciones de impresión deben ​describir la ubicación en el código; ​por ejemplo, «imprimir línea 20" ​o «imprimir línea 55: dentro del condicional».
- ​La idea es utilizar estas instrucciones impresas para ​identificar qué secciones ​del código funcionan correctamente.
- ​Cuando una sentencia de impresión ​no se imprime según lo esperado, ​esto ayuda a identificar ​las secciones del código con problemas.
- ​Otra opción para identificar ​errores lógicos es usar un depurador.
- ​Un depurador te permitirá ​insertar puntos de interrupción en tu código.
- ​Los puntos de interrupción te permiten segmentar el código en ​secciones y ejecutar solo una parte a la vez.
- ​Al igual que con las sentencias print, ​ejecutar estas secciones de forma independiente ​puede ayudar a aislar los problemas del código.
- ​Pasemos a nuestro último tipo de error: una excepción.
- ​Las excepciones se producen cuando el programa no sabe cómo ​ejecutar código aunque ​no haya problemas con la sintaxis.
- ​Las excepciones se producen por diversas razones.
- Por ejemplo, ​pueden ocurrir cuando algo es matemáticamente ​imposible, como pedirle ​al código que divida algo por 0.
- ​También pueden producirse excepciones cuando le ​pides a Python que acceda a valores de índice que no ​existen o cuando Python ​no reconoce los nombres de variables o funciones.
- ​También pueden producirse excepciones ​cuando se utiliza un tipo de datos incorrecto.
- ​Vamos a demostrar una excepción. ​Supongamos que tiene una variable llamada ​my_string que contiene la palabra «Seguridad».
- ​Como esta cadena tiene 8 caracteres, ​podemos imprimir correctamente cualquier índice inferior a 8.
- ​El índice 0 contiene «s».
- ​El Índice 1 contiene la letra «e».
- ​Y el índice 2 contiene «c».
- ​Sin embargo, si intentas acceder ​al personaje del índice 100, aparecerá un error.
- ​Analicemos esto y exploremos lo que sucede.
- ​Tras imprimir correctamente las tres primeras sentencias, ​aparece un mensaje de error: ​«índice de cadena fuera de rango».
- En ​el caso de los errores ​de excepción, también puede utilizar depuradores e ​imprimir sentencias para ​averiguar la posible fuente del error.
- [file](./resources/code/modulo-04_03-002.py)
- ​Se pueden esperar errores y excepciones al trabajar en Python.
- ​Lo importante es saber cómo tratar con ellos.

---

## Matt: Aprender de los errores
- ​Me llamo Matt.
- ​Soy un ingeniero de software que trabaja en ciberseguridad.
- Crecí viendo películas como La Matrix, ​y no es muy ​realista lo que realmente es el trabajo de ciberseguridad, ​pero es inspirador.
- ​Si profundizas ​en los detalles de lo que haces y das ​un paso atrás como si fueras ​ese tío guay con gafas de sol, eres un hacker.
- ​Cuando empecé a escribir código, ​veía los errores de programación ​como una señal de que me había ido mal.
- ​Pero a medida que crecí, ​un poco más madura, ​me di cuenta de que todo el mundo tiene errores de programación.
- ​Literalmente, el mejor ingeniero de software ​que conozco escribe código y tiene errores.
- ​Los errores representan un momento en el ​que puedes dar un paso atrás y decir: ¿qué hice mal?
- ​Es una oportunidad de aprendizaje.
- ​Ahora, veo momentos en los que ​puedo analizar algunos problemas que no ​entiendo y pensar: ¿por qué?
- ​Sumérjase en ello y amplíe ​mis conocimientos de informática, que es todo mi trabajo.
- ​Lo veo como un ​proceso de aprendizaje y es un poco divertido.
- ​Una de las áreas de programación más complicadas con las que me he topado ​durante mi estancia aquí en Google fue la toma de huellas dactilares ​cuando encontramos una vulnerabilidad.
- ​Si encontramos la misma vulnerabilidad más adelante, ​no queremos tener dos vulnerabilidades, ​no queremos molestar a alguien dos veces y decir: ​arregla esto si es exactamente lo mismo.
- ​Hacemos lo que se llama ​toma de huellas digitales, en la que decimos que esta vulnerabilidad tiene ​una huella digital específica y, si encontramos ​otra vulnerabilidad que tenga la misma huella digital, ​no la almacenaremos ​por separado ni la trataremos por separado.
- En efecto, ​son lo mismo.
- ​Me estaba encontrando con estos errores en los ​que las cosas no ​dejaban huellas dactilares de la manera que esperaba que lo hicieran.
- ​Estuve literalmente esforzándome durante semanas, ​intentando averiguar ​qué pasa con esta cosa.
- ​Pero cuando descubrí que era muy satisfactorio, ya está.
- ​Cuando estás en medio de este lío, ​todas esas dudas sobre ti mismo se apoderan de tu cerebro.
- ​Piensas que tal vez ​no soy tan bueno en esto como pensaba.
- ​Lo que volvería y ​me diría a mí mismo:
- A), no es interminable, ​mejora. Una vez que lo descubres, ​esa sensación de recompensa es increíble.
- ​Pero B), además, está bien engañar a la gente ​si tienes problemas con algo, ​siempre abogo por pedir ayuda.
- ​La mayoría de las personas están muy ​emocionadas de ayudarte con esto, ​especialmente cuando se trata de un problema complicado.
- ​Estoy muy emocionada de haber acabado en ciberseguridad.
- ​La ciberseguridad está teniendo su momento.
- ​Las personas se están dando cuenta, se están dando cuenta de la cantidad de datos ​que están publicando en ​el mundo y están empezando a preocuparse por ellos.
- ​Todos los días hay algo nuevo.
- ​Todos los días tengo algo ​emocionante que hacer y sí, ​dedicarme a ello.
- La ciberseguridad es el camino. 

---

## Aplicar estrategias de Depuración
- ​Supongamos que nuestros compañeros de trabajo ​necesitan ayuda para que su código funcione y ​nos hemos ofrecido a depurar su código para ​asegurarnos de que funciona sin problemas.
- ​En primer lugar, necesitamos conocer el propósito del código.
- ​En este caso, el propósito del código es ​analizar una sola línea de un archivo de registro y devolverla.
- ​El archivo de registro que utilizamos registra ​posibles problemas con las aplicaciones de software.
- ​Cada línea del registro contiene ​los códigos de estado de respuesta HTTP, ​la fecha, la hora ​y el nombre de la aplicación.
- ​Al escribir este código, ​nuestros compañeros de trabajo consideran si es ​necesario analizar todos estos códigos de estado.
- ​Dado que 200 indica un evento exitoso, ​llegaron a la conclusión de que las líneas con ​este código de estado no deberían analizarse.
- ​En su lugar, Python debería devolver un mensaje ​que indique que el análisis no era necesario.
- ​Para iniciar el proceso de depuración, ​ejecutemos primero el código para identificar los errores que aparecen.
- ​Nuestro primer error es un error de sintaxis.
- ​El mensaje de error también nos indica que ​el error de sintaxis se produce ​en una línea que define una función.
- ​Así que vamos a desplazarnos hasta esa parte del código.
- ​Como recordará, ​los encabezados de estas funciones deben terminar con dos puntos.
- ​Sigamos y agreguemos eso al código.
- ​Ahora, el error de sintaxis debería desaparecer.
- ​Vamos a ejecutar el código de nuevo.
- ​Ahora nuestro error de sintaxis ha desaparecido, ​lo cual es una buena noticia, pero ​tenemos otro error, un «error de nombre».
- ​El «error de nombre» es en realidad un tipo de excepción, ​lo que significa que hemos escrito una sintaxis válida, ​pero Python no puede procesar la sentencia.
- ​Según el error, ​el intérprete no entiende la ​variable application_name en el ​punto en el que se agregó a la lista parsed_line.
- ​Examinemos esa sección del código.
- ​Este error significa que no hemos ​asignado correctamente el nombre de la variable.
- ​Así que ahora volvamos al lugar donde se ​asignó por primera vez y determinemos qué pasó.
- ​Descubrimos que esta variable está mal escrita.
- ​Debe haber dos p en application_name, no una.
- ​Vamos a corregir la ortografía.
- ​Ahora que lo hemos arreglado, debería funcionar.
- ​Así que ejecutemos el código.
- ¡Genial! Hemos corregido ​un error y una excepción.
- ​Y ya no tenemos ningún mensaje de error.
- ​Pero esto no significa que nuestro trabajo de depuración haya terminado.
- ​Vamos a asegurarnos de que la lógica ​del programa funciona según lo previsto examinando el resultado.
- ​Nuestra salida es una línea analizada.
- ​En la mayoría de los casos, esto sería lo que queríamos.
- ​Pero como recordarás, ​si el código de estado es 200, ​nuestro código no debería analizar la línea.
- ​En su lugar, debería imprimir ​un mensaje que indique que no es necesario analizarlo.
- ​Y cuando lo llamamos con un código de estado 200, ​se produjo un error lógico ​porque este mensaje no se mostraba.
- ​Así que volvamos al condicional que usamos para ​manejar el código de estado 200 e investiguemos.
- ​Para encontrar el origen del problema, ​agreguemos declaraciones impresas.
- ​En nuestras declaraciones impresas, ​incluiremos el número de línea ​y la descripción de la ubicación.
- ​Agregaremos una sentencia de impresión antes de la línea de ​código que contiene «return parsed_list».
- ​Vamos a añadir otra encima de la sentencia if que comprueba ​el código de estado 200 para ​determinar si llega a la sentencia if.
- ​Añadiremos una sentencia print más dentro de ​la sentencia if para ​determinar si el programa la introduce siquiera.
- ​Ahora, ejecutemos el código y revisemos lo que se imprime.
- ​Solo la primera declaración impresa imprimió algo.
- ​Las otras dos declaraciones impresas después de estas no se imprimieron.
- ​Esto significa que el programa ​ni siquiera ingresó la sentencia if.
- ​El problema se produjo en algún lugar ​antes de la línea que devuelve la variable parsed_line.
- ​Vamos a investigar. ​Cuando Python encuentra la primera sentencia de retorno ​que devuelve la lista analizada, ​sale de la función.
- ​En otras palabras, devuelve la lista ​incluso antes de comprobar un valor de código de estado de 200.
- ​Para solucionar este problema, debemos mover la sentencia if y ​comprobar el código de estado ​en algún lugar antes de «devolver la línea analizada».
- ​Primero eliminemos nuestras declaraciones impresas.
- ​Esto hace que el programa ​sea más eficiente porque no ejecuta líneas de código innecesarias.
- ​Ahora, movamos la sentencia if.
- ​Lo colocaremos justo después de la línea de código ​que implica analizar el código de estado de la línea.
- ​Ejecutemos nuestro código y confirmemos que esto solucionó nuestro problema.
- ​¡Sí! Imprimió «Evento exitoso, no es necesario analizarlo».
- ​¡Gran trabajo! Hemos corregido este error lógico.
- ​He disfrutado depurando este código contigo.
- [file](./resources/code/modulo-04_03-003.py)

---

## Explore las técnicas de depuración
- Tipos de errores
   - Es una parte normal del desarrollo de código en Python recibir mensajes de error o descubrir que el código que estás ejecutando no está funcionando ASÍ.
   - Lo importante es que sepas cómo solucionar los errores cuando se producen.
   - Entender los tres tipos principales de errores puede ayudar.
   - Estos tipos incluyen errores de sintaxis, errores lógicos y excepciones.

- Errores de sintaxis
   - Un error de sintaxis es un error que implica un uso no válido de un lenguaje de programación.
   - Error de sintaxis ocurre cuando hay un error con la sintaxis de Python en sí.
   - Ejemplos comunes de errores de sintaxis incluyen olvidar un signo de puntuación, como un corchete de cierre para una lista o dos puntos después del encabezado de una función.
   - Cuando ejecutas código con errores de sintaxis, la salida identificará la localización del error con el número de línea y una porción del código afectado.
   - También describe el error.
   - Los errores de sintaxis suelen comenzar con la etiqueta"SyntaxError:".
   - A continuación, sigue una descripción del error.
   - La descripción puede ser simplemente "invalid syntax".
   - O si olvida un paréntesis de cierre en una función, la descripción podría ser "unexpected EOF while parsing".
   - "EOF" significa "fin de archivo".
   - El siguiente código contiene un error de sintaxis. Ejecútalo y examina su salida:
   - [file](./resources/code/modulo-04_03-004.py)
   - Aparece el mensaje "SyntaxError: EOL while scanning string literal".
   - "EOL" significa "fin de línea".
   - El mensaje de error también indica que el error se produce en la primera línea.
   - El error se produjo porque faltaba una comilla al final de la cadena de la primera línea.
   - Puede solucionarlo añadiendo esa comilla.
   - A veces encontrará la etiqueta de error "IndentationError" en lugar de "SyntaxError".
   - "IndentationError" es una subclase de "SyntaxError" que se produce cuando la sangría utilizada con una línea de código no es sintácticamente correcta. 

- Errores lógicos
   - Un Error lógico es un error que se produce cuando la lógica utilizada en el código produce resultados no deseados.
   - Los errores lógicos pueden no producir mensajes de error.
   - En otras palabras, el código no hará lo que se espera que haga, pero sigue siendo válido para el intérprete.
   - Por ejemplo, usar el operador lógico incorrecto, como un signo mayor o igual que (>=) en lugar del signo mayor que (>) puede resultar en un error lógico.
   - Python no evaluará una condición como usted pretendía.
   - Sin embargo, el código es válido, por lo que se ejecutará sin un mensaje de error.
   - El siguiente ejemplo muestra un mensaje relacionado con si un usuario ha alcanzado o no un número máximo de cinco intentos de inicio de sesión.
   - La condición en la sentencia if debería ser login_attempts < 5, pero está escrita como login_attempts >= 5.
   - Se ha asignado un valor de 5 a login_attempts para que pueda explorar lo que muestra en ese caso:
   - [file](./resources/code/modulo-04_03-005.py)
   - La salida muestra el mensaje "User has not reached maximum number of login attempts."
   - Sin embargo, esto no es cierto ya que el número máximo de intentos de inicio de sesión es cinco.
   - Esto es un Error lógico.
   - Los errores lógicos también pueden producirse cuando se asigna un valor incorrecto en una condición o cuando un error con la sangría hace que una línea de código se ejecute de una forma que no estaba prevista.

- Excepciones
   - Una excepción es un error que implica que el código no puede ejecutarse aunque sea sintácticamente correcto.
   - Esto ocurre por varias razones.
   - Una causa común de una excepción es cuando el código incluye una variable que no ha sido asignada o una función que no ha sido definida.
   - En este caso, su salida incluirá "NameError" para indicar que se trata de un error de nombre.
   - Después de ejecutar el siguiente código, utilice el mensaje de error para determinar qué variable no fue asignada:
   - [file](./resources/code/modulo-04_03-006.py)
   - La salida indica que hay un "NameError" que involucra la variable unusual_logins.
   - Puede solucionarlo asignando un valor a esta variable.
   - Además de los errores de nombre, se muestran los siguientes mensajes para otros tipos de excepciones:
      - "IndexError":
         - Un error de índice ocurre cuando se coloca un índice en notación entre corchetes que no existe en la secuencia referenciada.
         - Por ejemplo, en la lista usernames = ["bmoreno", "tshah", "elarson"], los índices son 0, 1, y 2.
         - Si se hace referencia a esta lista con la sentencia print(usernames[3]), se produciría un error de índice.
      - "TypeError":
         - Se produce un error de tipo al utilizar un tipo de datos incorrecto.
         - Por ejemplo, si intentara realizar un cálculo matemático sumando un valor de cadena a un entero, obtendría un error de tipo.
      - "FileNotFound":
         - Un error de archivo no encontrado se produce al intentar abrir un archivo que no existe en la ubicación especificada.

- Estrategias de depuración
   - Ten en cuenta que si tienes varios errores, el intérprete de Python mostrará mensajes de error de uno en uno, empezando por el primer error que encuentre.
   - Después de corregir ese error y ejecutar el código de nuevo, el intérprete mostrará otro mensaje para el siguiente error de sintaxis o excepción que encuentre.
   - Cuando se trata de errores de sintaxis, los mensajes de error que recibe en la salida generalmente le ayudarán a solucionar el error.
   - Sin embargo, en el caso de errores lógicos y excepciones, pueden ser necesarias estrategias adicionales.

- Depuradores
   - En este curso, has estado ejecutando código en un entorno de Notebook.
   - Sin embargo, puedes escribir código Python en un Entorno de desarrollo integrado (IDE).
   - Un IDE (entorno de desarrollo integrado) es una aplicación de software para escribir código que proporciona asistencia de edición y herramientas de corrección de errores.
   - Muchos IDE ofrecen herramientas de detección de errores en forma de depurador.
   - Un depurador es una herramienta de software que ayuda a localizar el origen de un error y a evaluar sus causas.
   - En los casos en que no se puede encontrar la línea de código que está causando el problema, los depuradores ayudan a reducir el origen del error en el programa.
   - Para ello, utilizan puntos de interrupción.
   - Los puntos de interrupción son marcadores colocados en determinadas líneas de código ejecutable que indican qué secciones de código deben ejecutarse al depurar.
   - Algunos depuradores también tienen una característica que le permite comprobar los valores almacenados en las variables a medida que cambian a lo largo de su código.
   - Esto es especialmente útil en el caso de errores lógicos, ya que permite localizar dónde han cambiado involuntariamente los valores de las variables.
   - Los recientes avances en IA han abierto muchas oportunidades para mejorar los IDE con una potente asistencia de codificación consciente del contexto.
   - Se trata de herramientas que se integran directamente en el IDE o en el entorno de codificación para proporcionar una experiencia de codificación más fluida.
   - Por ejemplo, Gemini Code Assist es una herramienta de IA gratuita que se integra en IDE populares como Visual Studio Code y JetBrains.
   - Funciona como un asistente que puede ayudar a analizar el código y encontrar errores, sugerir modificaciones y también interactuar de forma conversacional para responder a muchas otras preguntas, ya sean técnicas o más conceptuales. 
   - Estas herramientas se están convirtiendo rápidamente en indispensables para los programadores y los profesionales de la ciberseguridad, ya que facilitan y aceleran los flujos de trabajo, pero si decides utilizarlas, recuerda que esta tecnología aún está evolucionando.
   - Las sugerencias, el código o las explicaciones proporcionadas pueden no ser siempre perfectamente precisas, óptimas o seguras.
   - Revise y valide siempre cualquier resultado generado por IA antes de ejecutar programas o confiar en la información.
   - Trate la ayuda de la IA como un copiloto útil, pero mantenga la supervisión y la responsabilidad de su código final.

- Utilice instrucciones de impresión
   - Otra estrategia de depuración consiste en incorporar sentencias de impresión temporales diseñadas para identificar el origen del error.
   - Deberías incorporar estratégicamente estas sentencias de impresión para imprimir en varios puntos del código.
   - Puede especificar números de línea así como texto descriptivo sobre la ubicación.
   - Por ejemplo, puede tener un código destinado a añadir nuevos usuarios a una lista de aprobados y luego mostrar la lista de aprobados.
   - El código no debería añadir usuarios que ya están en la lista de aprobados.
   - Si analizas la salida de este código después de ejecutarlo, te darás cuenta de que hay un error lógico:
   - [file](./resources/code/modulo-04_03-007.py)
   - Aunque aparece el mensaje "bmoreno already in list", se añade una segunda instancia de "bmoreno" a la lista.
   - En el código siguiente, se han añadido sentencias print al código.
   - Al ejecutarlo, puede examinar lo que se imprime:
   - [file](./resources/code/modulo-04_03-008.py)
   - La sentencia print "line 5 - inside for loop" sale dos veces, indicando que Python ha entrado en el bucle for para cada nombre de usuario en new_users.
   - Esto es lo esperado.
   - Además, la sentencia print "line 7 - inside if statement" sólo imprime una vez, y esto también es lo esperado porque sólo uno de estos nombres de usuario ya estaba en approved_users.
   - Sin embargo, la sentencia print "line 9 - before .append method" sale dos veces.
   - Esto significa que el código llama al método .append() para ambos nombres de usuario aunque uno ya esté en approved_users.
   - Esto ayuda a aislar el Error lógico a esta área.
   - Esto puede ayudarte a darte cuenta de que la línea de código approved_users.append(user) debería ser el cuerpo de una sentencia else para que sólo se ejecute cuando user no esté en approved_users.

---

## Actividad: Depuración de código Python
- Introducción
   - En este laboratorio, abrirá un entorno de cuaderno para practicar habilidades de depuración en Python.
   - Se le presentará un escenario de seguridad para que lo explore a lo largo del laboratorio.
   - Utilizará las habilidades de depuración para identificar errores en el código y resolverlos para que el código logre el resultado deseado.

- Lo que hará
   - Aplicar estrategias de depuración para asegurarse de que el código funciona correctamente
   - Ajustar el código para resolver errores de sintaxis, excepciones y errores lógicos

- Scenario
   - In your work as a security analyst, you need to apply debugging strategies to ensure your code works properly.
   - Throughout this lab, you'll work with code that is similar to what you've written before, but now it has some errors that need to be fixed.
   - You'll need to read code cells, run them, identify the errors, and adjust the code to resolve the errors.

- Task 1
   - The following code cell contains a syntax error.
   - In this task, you'll run the code, identify why the error is occuring, and modify the code to resolve it.
   - (To ensure that it has been resolved, run the code again to check if it now functions properly.)
   - [file](./resources/code/lab_12/task_01.py)
   - What happens when you run the code before modifying it? How can you fix this?
   > The code will not run because the for loop is missing a colon at the end of the line. To fix this, add a colon at the end of the for loop line.

- Task 2
   - In the following code cell, you're provided a list of usernames.
   - There is an issue with the syntax.
   - In this task, you'll run the cell, observe what happens, and modify the code to fix the issue.
   - [file](./resources/code/lab_12/task_02.py)
   - What happens when you run the code before modifying it? How can you fix it?
   > The code will not run because there is a missing comma and a doble quote in the list of usernames. To fix this, add a comma and remove the double quote in the list of usernames.

- Task 3
   - In the following code cell, there is a syntax error.
   - Your task is to run the cell, identify what is causing the error, and fix it.
   - [file](./resources/code/lab_12/task_03.py)
   - What happens when you run the code before modifying it? What is causing the syntax error? How can you fix it?
   > The code will not run because there is missing a parenthesis. To fix this, add a parenthesis at the end of the print statement.

- Task 4
   - In the following code cell, you're provided a usernames_list, a username, and code that determines whether the username is approved.
   - There are two syntax errors and one exception.
   - Your task is to find them and fix the code.
   - A helpful debugging strategy is to focus on one error at a time and run the code after fixing each one.
   - [file](./resources/code/lab_12/task_04.py)
   - What happens when you run the code before modifying it? What is causing the errors? How can you fix it?
   > The code will not run because there is a misspelling in the username_list, the if statement was incorrect and if body need identation. To fix the code we need to correct the username_list to usernames_list, change the "=" to "==" in the if statement and add a identation in the body of if statement.

- Task 5
   - In this task, you'll examine the following code and identify the type of error that occurs.
   - Then, you'll adjust the code to fix the error.
   - [file](./resources/code/lab_12/task_05.py)
   - What happens when you run the code before modifying it? What type of error is this? How can you fix it?
   > The code will not run, there is an exception when trying to acces the 5 element of the list. We can fixed changed the 5 by -1. 

- Task 6
   - In this task, you'll examine the following code.
   - The code imports a text file into Python, reads its contents, and stores the contents as a list in a variable named ip_addresses.
   - It then removes elements from ip_addresses if they are in remove_list.
   - There are two errors in the code: first a syntax error and then an exception related to a string method.
   - Your goal is to find these errors and fix them.
   - [file](./resources/code/lab_12/task_06.py)
   - What happens when you run the code before modifying it? What is causing the errors? How can you fix them?
   > The code will not run because there is missing a colon at the end of the line 11, and there is a syntax error en line 16. To fix this, we need to add the colon at the end of the line 11, then, we need to fix de syntax error when trying to split.

- Task 7
   - In this final task, there are three operating systems: OS 1, OS 2, and OS 3.
   - Each operating system needs a security patch by a specific date.
   - The patch date for OS 1 is "March 1st", the patch date for OS 2 is "April 1st", and the patch date for OS 3 is "May 1st".
   - The following code stores one of these operating systems in a variable named system.
   - Then, it uses conditionals to output the patch date for this operating system.
   - However, this code has logic errors.
   - Your goal is to assign the system variable to different values, run the code to examine the output, identify the error, and fix it.
   - [file](./resources/code/lab_12/task_07.py)