# Introducción a la programación Python en ciberseguridad

## Bienvenido al Módulo 1
- El proceso de aprender ​un nuevo lenguaje de programación es ​similar al de aprender un nuevo idioma.
- ​Por ejemplo, como cualquier lenguaje humano, ​la programación consiste en palabras ​organizadas juntas para formar líneas de código.
- ​Las líneas de código se utilizan para comunicarse con una computadora, ​similar a una frase, ​diciéndole cómo realizar una tarea.
- ​En esta sección, vamos a ​empezar a aprender el lenguaje necesario para ​comunicarnos con una computadora mientras ​exploramos algunos componentes clave de Python.
- ​Empezaremos introduciendo los fundamentos de la programación, ​empezando por por qué los analistas de seguridad utilizan Python.
- ​A continuación, empezaremos a construir los cimientos de Python.
- ​Hablaremos de los tipos de datos.
- ​Después, cubriremos las variables.
- ​Por último, aprenderemos sobre las ​afirmaciones específicas que podemos hacer en ​Python, como las afirmaciones condicionales.
- ​Las sentencias condicionales nos ayudan a ​incorporar lógica a nuestros programas.
- ​El segundo tipo de sentencia que aprenderemos ​es la sentencia iterativa.
- ​Las sentencias iterativas nos permiten repetir una línea de ​código varias veces sin tener que reescribirla.
- ​Aprender Python me ayudó ​a tener éxito en mi carrera porque usar ​Python me permite liberar ​tiempo de tareas repetitivas y, en su lugar, ​centrarme en tareas y problemas más desafiantes.
- ​Aplicar con éxito ​la automatización reduce mi carga de trabajo total, ​aumenta la productividad, ​y reduce el riesgo de errores humanos.
- ​El uso de la automatización también me permite ​centrarme en mis tareas de ingeniería, ​que requieren más creatividad, ​colaboración y resolución de problemas

---

## Python y la ciberseguridad
- ​Los profesionales de la Seguridad utilizan una gran variedad de herramientas.
- ​Una de esas herramientas es la Programación informática.
- ​La programación se utiliza para crear un conjunto específico de instrucciones para que ​una computadora ejecute tareas.
- ​Pongamos el ejemplo de una máquina expendedora.
- ​Piense en una máquina expendedora como una computadora que suministra alimentos o bebidas a los clientes.
- ​Para recibir un artículo, el cliente introduce el dinero en la máquina y ​a continuación selecciona el artículo que desea.
- ​Digamos que el cliente proporciona a la máquina un valor de 5 $.
- ​La máquina almacena este valor mientras usted realiza su selección.
- ​Si selecciona una chocolatina que cuesta 2 $, ​la máquina toma esta entrada, también conocida como instrucción, ​y entonces entiende que debe dar salida a su chocolatina por 2 $ ​y le proporciona el cambio de 3 $.
- ​Existen muchos lenguajes de programación.
- ​Aquí, nos centraremos en Python.
- ​Python se considera un lenguaje de propósito general.
- ​Esto significa que puede crear una gran variedad de programas diferentes, y ​no está especializado en ningún problema concreto en campos ​como el desarrollo web y la Inteligencia artificial.
- ​Python se utiliza normalmente para crear sitios web y realizar análisis de datos.
- ​En seguridad, la principal razón por la que utilizamos Python es para automatizar nuestras tareas.
- ​La automatización es el uso de la tecnología para reducir el esfuerzo humano y ​manual para realizar tareas comunes y repetitivas.
- ​Python es generalmente mejor para automatizar tareas cortas y sencillas.
- ​Por ejemplo, un analista de seguridad que está tratando un incidente de ​seguridad puede tener un registro con la información necesaria.
- ​Leerlos manualmente llevaría demasiado tiempo, pero ​Python puede ayudar a ordenarlos para que los analistas puedan encontrar lo que necesitan.
- ​Como otro ejemplo, un analista podría utilizar Python para gestionar una Lista de control de acceso, ​la lista que controla quién puede acceder al sistema y a sus recursos.
- ​Sería potencialmente menos coherente si los analistas tuvieran ​que eliminar manualmente el acceso de un empleado cada vez que abandona la empresa.
- ​Sin embargo, un programa Python puede monitorizar periódicamente esto en su lugar.
- O bien, ​Python también podría realizar algunas tareas automatizadas, como analizar el Tráfico de red.
- ​Aunque estas tareas pueden realizarse a través de aplicaciones externas, ​también son posibles a través de Python.
- ​Además de automatizar tareas individuales, ​Python puede combinar tareas separadas en un flujo de trabajo.
- ​Por ejemplo, imagine que un Manual de estrategias indica que un analista necesita resolver ​una determinada situación mediante la entrega de un archivo y la posterior notificación a las personas adecuadas.
- ​Python puede conectar estos procesos entre sí.
- ​Entonces, ¿por qué exactamente podría un profesional de la Seguridad elegir Python para estas tareas?
- ​Existen varias ventajas que Python tiene como lenguaje de programación.
- ​Para empezar, Python es fácil de usar porque se asemeja al lenguaje humano, ​requiere menos código y es fácil de leer.
- ​Los programadores de Python también tienen la ventaja de seguir unas directrices estándar ​para garantizar la coherencia con el diseño y la legibilidad del código.
- ​Otra gran razón para ​aprender Python es que hay una gran cantidad de soporte en línea.
- ​Python también tiene una amplia colección de código incorporado que podemos importar y ​utilizar para realizar muchas tareas diferentes.
- ​Estas son sólo algunas de las razones por las que Python sigue teniendo una gran demanda ​en diferentes industrias de todo el mundo.
- ​Es muy probable que lo utilice en su carrera de Seguridad.

---

## Conozca Python
- Cómo funciona la programación
   - La programación es un proceso que puede utilizarse para crear un conjunto específico de instrucciones para que una computadora ejecute tareas.
   - Los programas de ordenador existen en todas partes.
   - Las computadoras, los teléfonos móviles y muchos otros dispositivos electrónicos reciben instrucciones de programas informáticos.
   - Existen múltiples lenguajes de programación utilizados para crear programas de ordenador.
   - Python es uno de ellos.
   - Los lenguajes de programación se convierten a números binarios, que son una serie de 0 y 1 que representan las operaciones que debe realizar la unidad central de procesamiento (CPU) de la computadora.
   - Cada instrucción corresponde a una operación específica, como sumar dos números o cargar un valor de la memoria.
   - A los humanos nos llevaría mucho tiempo comunicarnos de esta manera.
   - Los lenguajes de programación como Python facilitan la escritura de código porque se puede utilizar menos sintaxis a la hora de dar instrucciones a las computadoras para que realicen procesos complejos.

- Uso de Python para programar
   - Python es un lenguaje de programación de propósito general que puede utilizarse para resolver una gran variedad de problemas.
   - Por ejemplo, puede utilizarse para crear sitios web, realizar análisis de datos y automatizar tareas.
   - El código Python debe convertirse a través de un intérprete antes de que la computadora pueda procesarlo.
   - Un intérprete es un programa de computadora que traduce el código Python en instrucciones ejecutables línea por línea. 

- Versiones de Python
   - Existen múltiples versiones de Python.
   - En este curso, usted está utilizando Python 3.
   - Mientras utilice Python, es importante que lleve un registro de la versión que está utilizando.
   - Existen diferencias en la sintaxis de cada versión.
   - Sintaxis se refiere a las reglas que determinan lo que está correctamente estructurado en un lenguaje informático.

- Python en la ciberseguridad
   - En ciberseguridad, Python se utiliza especialmente para la Automatización.
   - La Automatización es el uso de la tecnología para reducir el esfuerzo humano y manual para realizar tareas comunes y repetitivas.
   - Estas son algunas áreas específicas de la ciberseguridad en las que Python podría utilizarse para automatizar tareas específicas:
      - Análisis de registros
      - Análisis de software malicioso
      - Gestión de listas de control de acceso
      - Detección de intrusiones
      - Cumplimiento normativo
      - Escaneado de redes

---

## Crear una secuencia de comandos de Python básica
- ​​Cuando trabajamos en Python, ​nos referimos a lo que escribimos como un "script" o un "programa".
- ​Existen sutiles diferencias entre ambos.
- ​Comparemos un programa de ordenador ​con una representación teatral.
- ​Casi todas las representaciones teatrales ​incluyen un script escrito.
- ​Los actores estudian y memorizan ​un script para decirlo en voz alta al público.
- ​Sin embargo, ése no es el único componente.
- ​También está la representación en su conjunto.
- ​Los directores toman decisiones sobre qué iluminación ​utilizar, o el vestuario, o el aspecto del escenario.
- ​La representación en su conjunto ​implica muchas decisiones de diseño, ​como la escenografía, la iluminación y el vestuario.
- ​El proceso de creación de esta producción es ​similar al proceso de programación en Python.
- ​La programación implica muchas decisiones de diseño.
- ​Pero el proceso de escritura de secuencias de comandos en Python es más parecido a ​escribir las palabras concretas que dirán los actores.
- ​En Python, es una buena práctica empezar con un comentario.
- ​Un comentario es una nota que los programadores ​hacen sobre la intención que hay detrás de su código.
- ​Añadamos uno ahora.
- ​Empezamos con el símbolo hash para indicar que esto es ​un comentario.
- Y luego añadiremos detalles sobre nuestra intención.
- ​Aquí vamos a imprimir ​"Hola Python" en la pantalla.
- ​Bien, ahora vamos a escribir nuestra primera línea de código Python.
- ​Este código utiliza print. ​Print da salida a un objeto especificado en la pantalla.
- ​Después de print, ponemos lo que ​queremos dar salida entre paréntesis.
- ​En este caso, queremos dar salida a la cadena "¡Hola Python!"
- ​Debemos colocar los datos de la cadena entre comillas.
- ​Estas comillas son ​sólo un ejemplo de ​sintaxis que encontrará en Python.
- ​La Sintaxis se refiere a las reglas que determinan ​qué está correctamente estructurado en un lenguaje de programación.
- ​Y ahora, ejecutaremos este código ​para que la computadora pueda dar salida a la cadena.
- ​Acaba de ejecutar su primera línea de código.
- ​Como nuestra sintaxis es correcta, ​la cadena se muestra ahora.
- ​Ahora que ya tiene experiencia ​escribiendo y ejecutando código en Python, ​estamos listos para discutir ​sus componentes básicos.
- [Ver código de ejemplo](./resources/code/modulo_01_02-001.py)

---

## Entornos Python
- Puede ejecutar Python a través de una gran variedad de entornos.
- Estos entornos incluyen notebooks, entornos de desarrollo integrados (IDE) y la línea de comandos.
- Esta lectura le presentará estos entornos.
- Se centrará principalmente en los notebooks porque así es como interactuará con Python en este curso.

- Notebooks
   - Una forma de escribir código Python es a través de un notebook.
   - En este curso, interactuará con Python a través de notebook.
   - Un notebook es una interfaz en línea para escribir, almacenar y ejecutar código.
   - También le permiten documentar información sobre el código.
   - El contenido del Notebook aparece en una celda de Código o en una celda de Markdown.

- Celdas de código
   - Las celdas de Código están pensadas para escribir y ejecutar código.
   - Un notebook proporciona un mecanismo para ejecutar estas celdas de código.
   - A menudo, se trata de un botón de reproducción situado dentro de la celda.
   - Al ejecutar el código, su salida aparece después del código.

- Celdas Markdown
   - Las celdas Markdown están pensadas para describir el código.
   - Le permiten dar formato al texto en el lenguaje markdown.
   - El lenguaje Markdown se utiliza para dar formato a texto sin formato en editores de texto y editores de código.
   - Por ejemplo, puede indicar que el texto debe tener un determinado estilo de encabezado.

- Entornos de notebook habituales
   - Dos entornos de notebook comunes son:
     - [Notebook de Jupyter](https://jupyter.org/about)
     - [Google Colaboratory (o Google Colab).](https://colab.sandbox.google.com/)
   - Le permiten ejecutar varios lenguajes de programación, incluido Python.

- Entornos de desarrollo integrados (IDE)
   - Otra opción para escribir código Python es a través de un entorno de desarrollo integrado (IDE), o una aplicación de software para escribir código que proporciona asistencia de edición y herramientas de corrección de errores.
   - Los entornos de desarrollo integrados incluyen una interfaz gráfica de usuario (GUI) que proporciona a los programadores una gran variedad de opciones para personalizar y construir sus programas.

- Línea de comandos
   - La línea de comandos es otro entorno que le permite ejecutar programas Python.
   - Anteriormente, aprendió que una interfaz de línea de comandos (CLI) es una interfaz de usuario basada en texto que utiliza comandos para interactuar con la computadora.
   - Introduciendo comandos en la línea de comandos, puede acceder a todos los archivos y directorios guardados en su disco duro, incluidos los archivos que contienen el código Python que desea ejecutar.
   - También puede utilizar la línea de comandos para abrir un editor de archivos y crear un nuevo archivo Python.

---

## Consejos de laboratorio y pasos para la solución de problemas
- Requisito de edad de 18+ para utilizar la plataforma
- Compatibilidad del navegador: última versión de Google Chrome, Firefox o Microsoft Edge
- Conexión a Internet

---

## Actividad: Practicar la escritura de código Python
- Introducción
   - En este laboratorio, abrirá un entorno de notebooks para practicar la escritura de código Python.
   - Se le presentará un escenario de seguridad para que lo explore a lo largo del laboratorio.
   - Se familiarizará con el trabajo en un entorno de notebooks, la escritura de comentarios de código en Python y la visualización de cadenas con la función print().
- Lo que hará
   - Conocer las capacidades de un entorno de cuaderno
   - Escribir comentarios de código en Python
   - Visualizar cadenas con la función print()

- Scenario
   - As a security analyst, you'll often use notebook environments and notebooks to write and run code.
   - This lab will help you get familiar with working in a notebook environment, writing code comments in Python, and displaying strings with the print() function.
   - In this lab, you'll complete a series of tasks that involve observing and running some pre-written cells of text and code, as well as filling in cells with your own text, Python code, and code comments.

- Task 1
   - The lab environment you're working in is a notebook-based coding environment.
   - Notebooks, such as this one, consist of two types of cells: (1) text cells, also known as markdown cells, and (2) code cells.
   - Markdown cells allow you to write plain text and format it in the markdown language.
   - Markdown language is used for formatting plain text in text editors and code editors.
   - For example, you can use markdown to make headers, bold or italicize words, format text as code, add hyperlinks, and more.
   - For this task, write something into the following markdown cell.
   - Be sure to replace the "[Double-click to edit this markdown cell and write something here.]" with your own text.
   - When you have finished editing, press the Shift and Enter keys (or on some keyboards, the Shift and Return keys) to display your text.

- Task 2
   - In Python notebooks, code cells allow you to write code comments and code in Python.
   - To run a code cell, first place your cursor on the cell.
   - Then, you can either click on the play icon, or press the Shift and Enter keys (or on some keyboards, the Shift and Return keys).
   - For this task, run the following code cell as is and observe the output.
   - [file](./resources/code/lab_01/task_2.py)
   - What do you observe about the output after you ran the code cell?
      > Hello world!

- Task 3
   - Writing code comments is a way to document the intention behind code.
   - It's a standard that analysts commonly use in their workflow.
   - Writing comments that accompany code allows you to keep track of the technical decisions you've made in your project.
   - This makes it easier for you and your team to read and revisit your code in order to understand what it does and why you took certain approaches.
   - For this task, run the following code cell as is and observe the output.
   - [file](./resources/code/lab_01/task_3.py)
   - What do you observe about the output after you ran the cell above?
      > Nothing, the comments are not executed as code, so they do not produce any output.

- Task 4
   - To type in a code cell, first click into the cell.
   - Then you can write comments and code inside the cell.
   - For this task, add a comment at the beginning of the following code cell, describing what the code is doing.
   - Write the comment to say # This cell displays "I am using Python.".
   - Be sure to replace the # YOUR COMMENT HERE with your own comment before running the following cell.
   - [file](./resources/code/lab_01/task_4.py)
   - What do you observe about the output after you ran the cell above?
      > The output displays the string "I am using Python."

- Task 5
   - In Python, print() helps you to display information to the screen.
   - For this task, use print() to display the message "I am a security analyst." by placing that message within the parentheses.
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before running the following code cell.
   - [file](./resources/code/lab_01/task_5.py)
   - What do you observe about the output after you ran the cell above?
      > The output displays the string "I am a security analyst."

- Task 6
   - For this task, write a print() statement to display the string "Python is useful for security!"
   - Be sure to replace the ### YOUR CODE HERE ### with your own code before running the following code cell.
   - [file](./resources/code/lab_01/task_6.py)
   - What do you observe about the output after you ran the cell above?
      > The output displays the string "Python is useful for security!"

- Task 7
   - For your final task, you'll combine all the print() statements you've encountered and written in this lab up to this point, into one code cell.
   - Complete the following code with the remaining messages.
   - Be sure to replace each ### YOUR CODE HERE ### with your own code before running the following cell.
   - [file](./resources/code/lab_01/task_7.py)
   - What do you observe about the output after you ran the cell above?
      > The output displays the following strings:
      > Hello world!
      > I am using Python.
      > I am a security analyst.
      > Python is useful for security!

- What are your key takeaways from this lab?
   > This lab helped me get familiar with working in a notebook environment, writing code comments in Python, and displaying strings with the print() function.

---

## Ejemplar: Practicar la escritura de código Python
- Mismo laboratorio que el anterior.
- Conclusion
   - It's helpful to use code comments to document the decisions you make as you code.
   - Code comments are ignored by computers; they're read by you and your team to understand the intentions behind the code.
   - You can write comments in Python using the hash symbol (#).
   - You can use print() in Python to display information to the screen.
      - When you use print() to display a string, the quotes around the string do not appear in the output on the screen.

---

## Akash: Python y el profesional de la ciberseguridad
- Mi nombre es Akash, y trabajo como Ingeniero de Seguridad en Google.
- ​Como ingeniero de Ciberseguridad, acabarías usando Python la mayor parte de tu carrera.
- ​Es muy importante que aprendas Python.
- ​Cuando te dediques a la ciberseguridad, ​estarás tratando con millones de Datos y cosas por el estilo, ​lo que te resultará muy difícil de hacer manualmente.
- ​Entonces, es cuando Python entra en juego para automatizar y escribir secuencias de comandos y ​pequeños programas que serán capaces de hacer lo mismo en una fracción de segundo.
- ​Aprender Python es súper divertido.
- Cuando ves cómo diez líneas de código hacen cosas ​como analizar megabytes de datos en cuestión de segundos, puede ser muy satisfactorio.
- ​Hay un montón de recursos para Python, y un montón de comunidades de código abierto, y ​la gente es muy servicial.
- ​Mantén la curiosidad y acepta pequeños problemas y ​luego ensúciate las manos haciéndolo y ​no tengas miedo de buscar sintaxis y aprender recursos en línea.
- ​Mi trabajo como ingeniero de seguridad en Google Chrome consiste en proteger a nuestros Clientes ​de gobiernos extranjeros y de amenazas muy persistentes en todo el mundo.
- ​Las amenazas son ilimitadas, no tienen límite, y ​eso es lo que hace que la Ciberseguridad sea muy emocionante.
- ​Así que, siga con ello, es una habilidad esencial que al principio le llevará algún tiempo ​desarrollar pero que le servirá a lo largo de su carrera. 

---

## Ponga a prueba sus Conocimientos: Introducción a la programación Python en ciberseguridad

1. ¿Qué tareas es más probable que automatice un analista de Seguridad con Python? Seleccione tres respuestas
   - [ ] Abordar un problema inusual de ciberseguridad
   - [x] Gestionar una Lista de control de acceso
   - [x] Análisis del Tráfico de red
   - [x] Ordenación de un archivo de registro
> Lo más probable es que un analista de seguridad automatice las siguientes tareas con Python: Ordenación de un archivo de registro, Gestionar una Lista de control de acceso y Analizar el Tráfico de red. Python se utiliza más comúnmente en ciberseguridad para automatizar tareas comunes y repetitivas.

2. ¿Cuáles son algunos de los Beneficios de utilizar Python en Seguridad? Seleccione todas las que corresponda
   - [x] Python puede combinar tareas separadas en un flujo de trabajo.
   - [x] Python ayuda a automatizar tareas cortas y sencillas.
   - [x] Python reduce el esfuerzo manual.
   - [ ] Python es el único lenguaje que crea un conjunto específico de instrucciones para ejecutar tareas.
> Python reduce el esfuerzo manual necesario para realizar tareas comunes y repetitivas. Ayuda a automatizar tareas cortas y sencillas y puede combinar tareas separadas en un flujo de trabajo. 

3. ¿Cuál de los siguientes bloques de código contiene un comentario de Python válido?
   - [x] # This prints a "Try again" message
         print("Try again")
   - [ ] This prints a "Try again" message
         print("Try again")
   - [ ] : This prints a "Try again" message
         print("Try again")
   - [ ] comment: This prints a "Try again" message
         print("Try again")
> El siguiente bloque de código contiene un Comentario de Python válido:
> # This prints a "Try again" message
> print("Try again")
> Un Comentario es una nota que los programadores hacen sobre la intención detrás de su código. Los comentarios comienzan con el símbolo hash (#).

4. ¿Qué línea de programación muestra en pantalla la cadena "invalid username"?
   - [x] print("invalid username")
   - [ ] # print("invalid username")
   - [ ] print(#invalid username#)
   - [ ] print(invalid username)
> El Código print("invalid username") muestra en pantalla la cadena "invalid username". La función print() muestra en pantalla el objeto especificado entre paréntesis. Para dar salida a una cadena, ésta debe ir entre comillas. 