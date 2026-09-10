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