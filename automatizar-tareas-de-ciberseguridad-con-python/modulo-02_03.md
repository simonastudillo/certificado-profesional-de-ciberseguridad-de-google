# Aprenda de la comunidad Python

## Módulos y bibliotecas
- ​​Las funciones integradas vienen de serie en todas las versiones ​de Python y constan de funciones como print(), type(), max() y muchas más.
- ​Para acceder a funciones adicionales prediseñadas, puede importar una biblioteca.
- ​Una biblioteca es una colección de módulos que proporcionan código al que los usuarios pueden ​acceder en sus programas.
- ​Todas las bibliotecas se componen generalmente de varios módulos.
- ​Un módulo es un archivo de Python que contiene funciones, ​variables, clases y cualquier tipo de código ejecutable adicionales.
- ​Piense en ellos como archivos de Python guardados que contienen funciones útiles.
- ​Los módulos pueden estar compuestos de líneas de código pequeñas y simples o ​ser complejos y de gran tamaño.
- ​De cualquier manera, ayudan a ahorrar tiempo a los programadores y hacen que el código sea más legible.
- ​Ahora, centrémonos específicamente en la Biblioteca estándar de Python.
- ​La Biblioteca estándar de Python es una colección extensa de ​código Python utilizable que a menudo viene empaquetado con Python.
- ​Un ejemplo de módulo de la Biblioteca estándar de Python es el módulo re.
- ​Este es un módulo útil para ​un analista de Seguridad cuando tiene la tarea de buscar patrones en los archivos de registro.
- ​Otro módulo es el módulo csv. ​Le permite trabajar de manera eficiente con archivos CSV.
- ​La Biblioteca estándar de Python también contiene módulos glob y os para ​interactuar con la línea de comandos, así como la hora y la ​fecha y hora para trabajar con marcas de tiempo.
- ​Estos son solo algunos de los módulos de la Biblioteca estándar de Python.
- ​Además de lo que siempre está disponible en la Biblioteca estándar de Python, ​también puedes descargar bibliotecas externas.
- ​Un par de ejemplos son Beautiful Soup para analizar archivos HTML de sitios web y ​NumPy para matrices y cálculos matemáticos.
- ​Estas bibliotecas lo ayudarán como analista de Seguridad en el ​análisis del tráfico de red, el análisis de archivos de registro y las matemáticas complejas.
- ​En general, las bibliotecas y ​los módulos de Python son útiles porque proporcionan funciones y variables preprogramadas.
- ​Esto ahorra tiempo al usuario. ​Te animo a explorar algunas de las bibliotecas y módulos que hemos discutido aquí y ​las formas en que pueden serte útiles mientras trabajas en Python. 

---

## Importar módulos y bibliotecas en Python
- También aprendió que una biblioteca es una colección de módulos que proporcionan código al que los usuarios pueden acceder en sus programas.
- Se le presentaron algunos módulos de la Biblioteca estándar de Python y un par de bibliotecas externas.
- En esta lectura, aprenderá a importar un Módulo que existe en la Biblioteca estándar de Python y a utilizar sus funciones.
- También ampliará sus conocimientos sobre las bibliotecas externas.

- La Biblioteca estándar de Python
   - La Biblioteca estándar de Python es una extensa colección de código Python que a menudo viene empaquetada con Python.
   - Incluye una variedad de Módulos, cada uno con código pre-construido centrado en un tipo particular de tarea.
   - Por ejemplo, anteriormente se le presentaron los siguientes módulos de la Biblioteca estándar de Python:
      - El módulo re, que proporciona funciones utilizadas para la búsqueda de patrones en archivos de registro
      - El módulo csv, que proporciona funciones utilizadas al trabajar con archivos .csv 
      - Los módulos glob y os, que proporcionan funciones utilizadas al interactuar con la línea de comandos
      - Los módulos time y datetime, que proporcionan funciones utilizadas al trabajar con marcas de tiempo
   - Otro módulo de la Biblioteca estándar de Python es statistics.
   - El módulo statistics incluye funciones utilizadas al calcular estadísticas relacionadas con datos numéricos.
   - Por ejemplo, mean() es una función del módulo statistics que toma datos numéricos como entrada y calcula su media (o promedio).
   - Además, median() es una función del módulo statistics que toma datos numéricos como entrada y calcula su mediana (o valor medio).

- Cómo importar módulos desde la Biblioteca estándar de Python
   - Para acceder a los módulos de la Biblioteca estándar de Python, debe importarlos.
   - Puede elegir entre importar un módulo completo o sólo importar funciones específicas de un módulo.

- Importar un módulo completo
   - Para importar un módulo completo de la Biblioteca estándar de Python, utilice la palabra clave import.
   - La palabra clave import busca un módulo o biblioteca en un sistema y lo añade al entorno local de Python.
   - Después de import, especifique el nombre del módulo a importar.
   - Por ejemplo, puede especificar import statistics para importar el módulo statistics.
   - Esto importará todas las funciones dentro del módulo statistics para su uso posterior en su código.
   - A modo de ejemplo, puede que desee utilizar la función mean() del módulo statistics para calcular el número medio de intentos fallidos de inicio de sesión al mes de un usuario concreto.
   - En el siguiente bloque de código, el número total de intentos fallidos de inicio de sesión para cada uno de los doce meses se almacena en una Lista llamada monthly_failed_attempts.
   - Ejecute este código y analice cómo puede utilizarse mean() para calcular la media de estos totales mensuales de inicios de sesión fallidos y almacenarla en mean_failed_attempts:
   - [file](./resources/code/modulo-02_03-001.py)
   - La salida devuelve una media de 35.25.
   - Puede que note el valor periférico de 178 y quiera encontrar también el valor medio.
   - Para hacerlo a través de la función median(), puede utilizar el siguiente código:
   - [file](./resources/code/modulo-02_03-002.py)
   - Esto le da el valor de 20.5, que también podría ser útil para analizar las estadísticas de intentos fallidos de inicio de sesión del usuario.
   - Cuando importe un módulo completo de la Biblioteca estándar de Python, deberá identificar el nombre del módulo con la función al llamarlo.
   - Puede hacerlo colocando el nombre del Módulo seguido de un punto (.) antes del nombre de la función.
   - Por ejemplo, los bloques de código anteriores utilizan statistics.mean() y statistics.median() para llamar a esas funciones.

- Importar funciones específicas de un módulo
   - Para importar una función específica de la Biblioteca estándar de Python, puede utilizar la palabra clave from.
   - Por ejemplo, si desea importar sólo la función median() del módulo statistics, puede escribir from statistics import median.
   - Para importar varias funciones de un módulo, puede separar las funciones que desee importar con una coma.
   - Por ejemplo, from statistics import mean, median importa tanto la función mean() como la median() del módulo statistics.
   - Un detalle importante a tener en cuenta es que si importa funciones específicas de un módulo, ya no tendrá que especificar el nombre del módulo antes de dichas funciones.
   - Puede examinar esto en el código siguiente, que importa específicamente sólo las funciones median() y mean() del módulo statistics y realiza los mismos cálculos que los ejemplos anteriores:
   - [file](./resources/code/modulo-02_03-003.py)
   - Ya no es necesario especificar statistics.mean() o statistics.median() y en su lugar el código incorpora estas funciones como mean() y median().

- Bibliotecas externas
   - Además de la Biblioteca estándar de Python, también puede descargar bibliotecas externas e incorporarlas a su código Python.
   - Por ejemplo, anteriormente conoció Beautiful Soup (bs4) para analizar archivos HTML y NumPy (numpy) para matrices y cálculos matemáticos.
   - Antes de utilizarlas en un Notebook de Jupyter o en un entorno Google Colab, deberá instalarlas.
   - Para instalar una biblioteca, como numpy, en cualquiera de los dos entornos, puede ejecutar la siguiente línea antes de importar la biblioteca:
      - `pip install numpy`
   - Esto instala la biblioteca para que pueda utilizarla en su bloc de notas.
   - Una vez instalada una biblioteca, puede importarla directamente a Python utilizando la palabra clave import de forma similar a como la utilizó para importar módulos de la Biblioteca estándar de Python.
   - Por ejemplo, tras la instalación de numpy, puede utilizar este código para importarla:
      - `import numpy`

---

## Legibilidad del Código
- ​Una de las ventajas de programar en Python es que ​es un lenguaje muy legible.
- ​También ayuda que la comunidad Python comparta un conjunto de directrices que ​promueven un código limpio y ordenado.
- Se denominan guías de estilo. ​Una guía de estilo es un manual que informa sobre la escritura, ​el formato y el diseño de los documentos.
- ​En lo que respecta a la programación, ​las guías de estilo pretenden ayudar a los programadores a seguir convenciones similares.
- ​La Guía de estilo PEP 8 es un recurso que proporciona directrices de estilo para ​programadores que trabajan en Python.
- ​PEP es la abreviatura de Python Enhancement Proposals (Propuestas de mejora de Python).
- ​PEP 8 proporciona a los programadores sugerencias relacionadas con la sintaxis.
- ​No son obligatorias, pero ayudan a crear coherencia ​entre los programadores para asegurarnos de que los demás puedan entender fácilmente nuestro código.
- ​Se basa esencialmente en el principio de que el código ​se lee mucho más a menudo de lo que se escribe.
- ​Es un gran recurso para cualquiera que quiera aprender a dar estilo y ​formato a su código Python de una manera coherente con otros programadores.
- ​Por ejemplo, la PEP 8 habla de los comentarios.
- ​Un comentario es una nota que los programadores hacen sobre la intención que hay detrás de su código.
- ​Se insertan en los programas de ordenador para indicar qué está haciendo el código y por qué.
- ​PEP 8 da recomendaciones específicas, como hacer que sus comentarios sean claros ​y mantenerlos actualizados cuando cambie el código.
- ​He aquí un ejemplo de código sin comentario.
- ​Puede que la persona que lo escribió sepa lo que está pasando, pero ​¿qué pasa con otras personas que necesiten leerlo?
- ​Puede que no entiendan el contexto detrás de la variable de intentos fallidos y ​por qué imprime "Cuenta bloqueada" si es mayor de 5.
- ​Y puede que el escritor original necesite volver a visitar este código en el futuro, por ​ejemplo, para depurar el programa más grande.
- ​Sin el comentario, también serían menos eficientes.
- ​Pero en este ejemplo hemos añadido un comentario.
- ​Todos los lectores pueden entender rápidamente lo que están haciendo nuestro Programa y ​sus variables.
- ​Los comentarios deben ser breves y directos al grano.
- ​A continuación, hablemos de otro aspecto importante de la legibilidad del código: la indentación.
- ​La indentación es un espacio que se añade al principio de una línea de código.
- ​Esto mejora la legibilidad y garantiza que el código se ejecute correctamente.
- ​Hay casos en los que debe indentar líneas de código para ​establecer conexiones con otras líneas de código.
- ​Esto agrupa las líneas de código sangradas y ​establece una conexión con una línea de código anterior que no está sangrada.
- ​El cuerpo de una sentencia condicional es un ejemplo de ello.
- ​Necesitamos asegurarnos de que esta sentencia impresa se ejecuta sólo cuando se cumple la condición.
- La indentación aquí proporciona esta instrucción a Python.
- ​Si la sentencia impresa no estuviera indentada, Python ejecutaría esta sentencia ​impresa fuera de la condicional y siempre imprimiría.
- ​Esto sería problemático porque recibiría un mensaje de que se necesitan actualizaciones​, ​aunque no sea así.
- Para aplicar una sangría, ​debe añadir al menos un espacio antes de una línea de código.
- ​Típicamente, los programadores utilizan de dos a cuatro espacios para una mayor claridad visual.
- ​La Guía de estilo PEP 8 recomienda cuatro espacios.
- ​En mi primer trabajo de ingeniería, escribí una secuencia de comandos para ayudar a validar y ​lanzar reglas de firewall.
- ​Inicialmente, mi secuencia de comandos funcionaba bien, pero ​se volvió difícil de leer un año después, cuando intentábamos ampliar su funcionalidad.
- ​Mis conocimientos de programación y ​estilo de codificación habían evolucionado durante ese año, al igual que las prácticas de codificación de mis compañeros de equipo.
- ​Nuestra organización no utilizaba una guía de estilo de codificación en ese momento, por lo que ​nuestros códigos eran muy diferentes, difíciles de leer y no escalaban bien.
- ​Esto causó muchos problemas y requirió trabajo adicional para solucionarlo.
- ​Asegurarse de que el código es legible y puede modificarse con el tiempo es la razón por la que ​es importante que los profesionales de la Seguridad se adhieran a las guías de estilo de codificación ​y por qué las guías de estilo son tan importantes para que las organizaciones las utilicen.
- ​La capacidad de escribir código legible es clave cuando se trabaja en Python.
- ​A medida que nos adentremos en la siguiente parte de nuestro curso, ​continuaremos desarrollando prácticas de código eficaces para una mejor legibilidad. 

---

## Garantizar una sintaxis y legibilidad adecuadas en Python
- Comentarios
   - Un comentario es una nota que hacen los programadores sobre las intenciones que hay detrás de su código.
   - Los Comentarios le facilitan a usted y a otros programadores la lectura y comprensión de su código.
   - Es importante comenzar su código con un comentario que explique lo que hace el programa.
   - Después, a lo largo del código, debería añadir comentarios adicionales sobre sus intenciones detrás de secciones específicas.
   - Cuando añada comentarios, puede añadir tanto comentarios de una sola línea como comentarios de varias líneas.

- Comentarios de una sola línea
   - Los comentarios de una sola línea en Python comienzan con el símbolo (#).
   - De acuerdo con la Guía de estilo PEP 8, es una buena práctica mantener todas las líneas en Python por debajo de 79 caracteres para mantener la legibilidad, y esto incluye los comentarios.
   - Los comentarios de una sola línea se utilizan a menudo a lo largo de su programa para explicar la intención detrás de secciones específicas de código.
   - Por ejemplo, esto podría ser cuando usted está explicando los componentes más simples de su programa, como el siguiente for bucle:
   - [file](./resources/code/modulo-02_03-004.py)
   - Los comentarios son importantes cuando se escribe código más complejo, como funciones, o bucles múltiples o sentencias condicionales.
   - Sin embargo, son opcionales cuando se escribe código menos complejo, como la reasignación de una variable.

- Comentarios multilínea
   - Los comentarios multilínea se utilizan cuando se necesitan más de 79 caracteres en un solo comentario.
   - Por ejemplo, esto puede ocurrir al definir una función si el comentario describe sus entradas y sus tipos de datos, así como su salida.
   - Hay dos formas habituales de escribir comentarios multilínea en Python.
   - La primera es utilizando el símbolo Hashtag (#) sobre varias líneas:
   - [file](./resources/code/modulo-02_03-005.py)
   - Otra forma de escribir comentarios multilínea es utilizando cadenas de documentación y no asignándolas a una variable.
   - Las cadenas de documentación, también llamadas docstrings, son cadenas que se escriben sobre varias líneas y se utilizan para documentar código.
   - Para crear una cadena de documentación, utilice comillas triples (""" """).
   - También podría añadir de este modo el comentario a la función del ejemplo anterior:
   - [file](./resources/code/modulo-02_03-006.py)

- Indentación correcta
   - La indentación es el espacio que se añade al principio de una línea de código.
   - En Python, debe sangrar el cuerpo de las sentencias condicionales, las sentencias iterativas y las definiciones de funciones.
   - La indentación no sólo es necesaria para que Python interprete correctamente esta sintaxis, sino que también puede facilitarle a usted y a otros programadores la lectura de su código.
   - La Guía de estilo PEP 8 recomienda que las indentaciones sean de cuatro espacios.
   - Por ejemplo, si tuviera una sentencia condicional dentro de un bucle while, el cuerpo del bucle tendría una sangría de cuatro espacios y el cuerpo de la condicional tendría una sangría de cuatro espacios más allá.
   - Esto significa que la condicional tendría una sangría de ocho espacios en total.
   - [file](./resources/code/modulo-02_03-007.py)

- Mantener una sintaxis correcta
   - Los errores de sintaxis implican un uso no válido del lenguaje Python.
   - Son increíblemente comunes con Python, por lo que centrarse en la sintaxis correcta es esencial para garantizar que su código funcione.
   - Ser consciente de los errores comunes le ayudará a solucionarlos más fácilmente.
   - Los errores de sintaxis suelen producirse por equivocaciones con los tipos de datos o en los encabezados de las sentencias iterativas o condicionales o de las definiciones de funciones.

- Tipos de datos
   - La sintaxis correcta varía en función del tipo de datos:
      - Coloque los Datos de cadena entre comillas.
         - Ejemplo: username = "bmoreno"
      - No entrecomille los tipos de datos enteros, flotantes o booleanos.
         - Ejemplos: login_attempts = 5, percentage_successful = .8, login_status = True
      - Coloque las listas entre corchetes y separe los elementos de una lista con comas.
         - Ejemplo: username_list = ["bmoreno", "tshah"]

- Dos puntos en las cabeceras
   - El encabezado de una Sentencia iterativa o condicional o de una definición de función debe terminar con dos puntos.
   - Por ejemplo, aparecen dos puntos al final de la cabecera en la siguiente definición de función:
   - [file](./resources/code/modulo-02_03-008.py)

- Recursos
   - PEP 8 - [Guía de estilo para código Python](https://peps.python.org/pep-0008/): La Guía de estilo PEP 8 contiene todos los Estándares del Código Python. Cuando lea esta guía, es útil utilizar la tabla de contenidos para navegar por los conceptos que aún no ha aprendido.

---

## Dorsa: Utilizar Python de forma eficaz en un equipo de ciberseguridad
- ​Hola, me llamo Dorsa y soy ingeniera de seguridad.
- ​Lo que más me gusta de mi trabajo ​es que puedo ver ​diferentes diseños de infraestructuras y sistemas ​a diario.
- ​Un consejo para las personas que están ​empezando en su profesión de ciberseguridad es que ​es muy importante trabajar de ​forma colaborativa en Python y uno de ​los aspectos clave es ​escuchar los comentarios que proporcionan los miembros de su equipo.
- ​Python permite muchas formas diferentes ​de acceder a información diferente.
- ​Cuando compartes ​fragmentos de código de Python entre los miembros de tu equipo, ​el código es más uniforme ​y el proceso de codificación es más eficiente.
- ​Hace que la base del código sea mucho más ​legible y permite que ​otros ingenieros trabajen en tu código después de ti.
- ​He visto muchos ejemplos en los que el ​código Python escrito de forma colaborativa ​ha sido útil en la industria.
- ​Uno de los ejemplos es cuando en Google escribimos ​una base de código escrita de forma colaborativa que permitió ​reducir el proceso de incorporación ​de seis o siete horas a un par de minutos.
- ​La colaboración fue una parte clave de este proceso porque, de ​lo contrario, ​una sola persona habría tardado muchos años en escribirla.
- ​Una sola persona no es capaz de ​entender todos los detalles de ​cada sistema y, si ​no tuviéramos varios ingenieros trabajando en ​él, este proceso habría sido mucho más difícil.
- ​La comunicación es muy importante cuando trabajas en ​equipo y, especialmente ​si estás desarrollando código en Python, ​debes expresar ​si necesitas ayuda durante todo el proceso, ​ya que los miembros de tu equipo están ahí para ​garantizar que tengas éxito.
- ​Al final del día, tu éxito ​significa que tu equipo también tiene éxito.
- A ​medida que avances en tu carrera ​como persona que escribe código en Python, ​te darás cuenta de ​que hay un montón de funciones y métodos que siguen ​existiendo en Internet y ​podrás encontrarlos con una búsqueda rápida ​y esos métodos te ​resultarán útiles y podrás reutilizarlos para tus fragmentos de código.
- ​Un recurso realmente bueno para que ​aprendas nuevas habilidades y amplíes ​tus habilidades de codificación en Python es ​hablar con tus colegas, asistir ​a reuniones y hablar con diferentes ​profesionales de seguridad que no trabajan en ​tu empresa, porque todos saben ​cómo ​mejorar tus habilidades de codificación, especialmente en ciberseguridad. 