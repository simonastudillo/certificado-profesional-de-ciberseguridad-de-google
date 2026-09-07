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
   - La línea de comandos es otro entorno que le permite ejecutar programas Python. Anteriormente, aprendió que una interfaz de línea de comandos (CLI) es una interfaz de usuario basada en texto que utiliza comandos para interactuar con la computadora.
   - Introduciendo comandos en la línea de comandos, puede acceder a todos los archivos y directorios guardados en su disco duro, incluidos los archivos que contienen el código Python que desea ejecutar.
   - También puede utilizar la línea de comandos para abrir un editor de archivos y crear un nuevo archivo Python.