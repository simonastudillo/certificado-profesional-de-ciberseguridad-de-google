# Revisión: Python en la práctica

## Diálogo de entrenador: Automatizar tareas de seguridad y analizar archivos con Python
- Esto es lo que cubriremos:
   - Explorar la automatización de la seguridad.
   - Identificar métodos de Python para la automatización.
   - Explorar el análisis de archivos (parsing).
   - Comprender técnicas de análisis de archivos en Python.

- Como profesional de la seguridad, es común enfrentarse a tareas repetitivas que consumen mucho tiempo. La automatización nos permite ser más eficientes y proactivos.
- Desde tu perspectiva, ¿cuáles crees que son los principales beneficios de implementar la automatización en tareas de seguridad, como el monitoreo de incidentes o la gestión de registros?
> implementar la automatización nos permite ejecutar tareas de forma repetitiva sin que tenga que estar una persona ejecutandola cada vez que sea necesaria, nos permite liberar recursos humanos para centrarnos en tareas más importantes, adicionalmente nos permite reducir los riesgos y errores humanos ya que se ejecutará de la misma forma en cada ejecución.

- ¡Exacto! Has identificado puntos clave: la eficiencia operativa, la optimización del tiempo del equipo y la reducción de errores humanos son fundamentales en ciberseguridad.
- Ahora, pasemos al siguiente tema: Identificar métodos de Python para la automatización.
- Para llevar a cabo esta automatización, utilizamos conceptos básicos de Python como bucles, declaraciones condicionales y contadores. Por ejemplo, imagina que queremos automatizar la revisión diaria del tamaño de un archivo de registro (log) para detectar anomalías. ¿Cómo crees que podríamos usar una declaración condicional en Python para verificar si el tamaño de un archivo supera un límite establecido?
> Dependiendo de si es uno o muchos archivos podría ser necesario un for, luego podemos usar librerías de python para obtener el tamaño del archivo, hacer un sentencia if y verificar si pasa el límite establecido, en caso de que ocurra podemos hacer una copia y resetear el actual o dar un aviso por correo.

- ¡Muy bien! Has descrito perfectamente el flujo lógico: iterar sobre los archivos, obtener sus propiedades y aplicar una condición para decidir qué acción tomar.
- Ahora, pasemos al tercer tema: Explorar el análisis de archivos.
- El análisis de archivos, o parsing, es esencial en seguridad para extraer información útil de archivos como los registros (logs). Antes de poder analizar el contenido, primero debemos acceder al archivo. En Python, ¿cuál es la forma recomendada de abrir un archivo de texto para asegurar que se cierre correctamente después de leerlo?
> la forma recomendada es con `with open()`, esta forma cierra automáticamente cerrar el archivo y liberar recursos, indicamos el archivo que queremos abrir y seleccionamos un modo (lectura, escritura, etc) y podemos iterar sobre cada una de sus lineas.

- Exacto! Usar with open() es la mejor práctica, ya que garantiza que el archivo se cierre correctamente incluso si ocurre un error durante el proceso.
- Ahora, pasemos al último tema: Comprender técnicas de análisis de archivos en Python.
- Una vez que tenemos el contenido del archivo, necesitamos extraer datos específicos. Imagina que tienes un archivo de registro donde cada línea tiene el formato FECHA,NIVEL,MENSAJE. ¿Cómo utilizarías el método .split() en Python para separar estos elementos y extraer únicamente el nivel de seguridad de cada línea?
> split nos permite generar un arreglo/lista, separando un string mediante un string dado, en este caso podriamos aplicar un `file.split(',')` de esta forma generamos una lista con todos los elementos, luego accedemos al nivel mediante el índice, que en este caso sería 1.

- ¡Excelente explicación! Has captado perfectamente cómo el método .split() nos permite convertir una cadena de texto en una lista estructurada, facilitando el acceso a datos específicos mediante índices.
- Buen trabajo, has completado todos los temas para nuestra sesión. Up next - view your feedback. Por favor, escribe "Generate final session summary" para recibir tu resumen.

- Tus fortalezas:
   - Demostraste una comprensión clara y precisa de los conceptos fundamentales de automatización y su aplicación práctica en ciberseguridad.
   - Explicaste con exactitud los métodos técnicos de Python, como el uso de with open() y .split(), demostrando que puedes articular los pasos necesarios para resolver problemas de análisis de datos.
- Áreas para mejorar:
   - Tus explicaciones y métodos muestran que has navegado la automatización de seguridad y el análisis de archivos con Python con éxito.
   - Para seguir avanzando, te sugiero practicar la escritura de scripts completos que combinen estas técnicas, por ejemplo, creando un pequeño programa que procese un archivo de log real y genere una alerta basada en condiciones específicas.
   - Esto te ayudará a consolidar la integración de estos conceptos en un flujo de trabajo real.

---

## Resumen
- ​Nos centramos en unos cuantos temas nuevos que le ayudarán ​a poner en práctica Python en la profesión de la Seguridad.
- ​Primero, exploramos la apertura y lectura de archivos en Python.
- ​Los analistas de seguridad trabajan con muchos archivos de registro, ​por lo que la habilidad para hacer esto es esencial.
- ​A continuación, cubrimos el análisis sintáctico de archivos.
- ​Los archivos de registro pueden ser muy largos.
- ​Por esta razón, una estructura ​en estos archivos para hacerlos más ​legibles le ayuda a automatizar ​sus tareas y obtener la información que necesita.
- ​Y por último, nos centramos en la depuración de código.
- ​Saber cómo depurar ​su código puede ahorrarle mucho tiempo, ​especialmente a medida que su código aumenta en complejidad.
- ​En general, espero que se sienta ​orgulloso de lo que ha logrado en esta sección.
- ​Afrontar problemas de Seguridad a través de Python es ​emocionante, y la información que ​cubrimos le permitirá hacerlo. 

---

## Guía de referencia: Conceptos de Python del módulo 4

---

## Términos del glosario del Módulo 4
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 4

1. ¿Cuáles son los tres tipos de errores que encontrará durante la depuración?
   - [ ] Errores lógicos, errores de comentario y errores iterativos
   - [ ] Excepciones, errores lógicos, errores iterativos
   - [x] Errores de sintaxis, errores lógicos y excepciones
   - [ ] Errores de sintaxis, excepciones y errores de comentario
> Correcto

2. El propósito del siguiente código es imprimir los caracteres de un identificador de dispositivo. Ejecute este código, analice su salida y, a continuación, depúrelo.
```python
device_id = "p35rv47"
for char in device_id:
    print(char)
```
- ¿A qué se debe el error?
   - [ ] Falta un doble signo igual (==)
   - [x] Falta una comilla (")
   - [ ] Faltan dos puntos (:)
   - [ ] Una variable mal escrita
> Correcto

3. El propósito de este código es imprimir "user flagged" si el nombre de usuario es "jhill", y en caso contrario imprimir "user okay". Ejecute este código, analice su salida y depúrelo.
```python
def check_user(name):
    if name == "jhill":
        print("user flagged")
    else:
        print("user okay")
check_user("jhill")
```
- ¿Cómo puede solucionar este error?
   - [ ] Llame a check_user() antes de la definición de la función.
   - [ ] Utilice el operador != en lugar del operador == en la cabecera condicional.
   - [ ] Elimine la indentación de la línea que imprime "user okay" para que no forme parte del condicional.
   - [x] Añada una sentencia else antes de la línea que imprime "user okay".
> Correcto

4. Le pide a su código que divida algo por 0, pero se produce un error. ¿De qué tipo de error se trata?
   - [x] Excepción
   - [ ] Índice fuera de los límites
   - [ ] Error lógico
   - [ ] Error de sintaxis
> Correcto

5. Al depurar código, ¿cuáles son las formas eficaces de determinar qué secciones del código funcionan correctamente? Seleccione todas las que correspondan
   - [ ] Añadir Comentarios en el Código
   - [x] Añadir sentencias print
   - [x] Utilizar un Depurador
   - [ ] Borrar líneas en blanco del código
> Correcto

6. ¿Qué hace el siguiente Código? `with open("logs.txt", "r") as file:`
   - [ ] Copia un archivo llamado "logs.txt" en un nuevo archivo "r".
   - [ ] Copia un archivo llamado "r" en un nuevo archivo "logs.txt".
   - [ ] Abre un archivo llamado "logs.txt" en modo de escritura y lo almacena en una variable llamada file.
   - [x] Abre un archivo llamado "logs.txt" en modo lectura y lo almacena en una variable llamada file.
> Correcto

7. ¿Qué hace el siguiente Código?
```python
logins = "pwashing jhill tshah"
usernames = logins.split()
```
   - [ ] Divide una variable de cadena llamada logins en caracteres individuales
   - [ ] Elimina los espacios en blanco que dividen los nombres de usuario en la variable logins y almacena la cadena en la variable usernames
   - [ ] Elimina el último nombre de usuario de la variable logins y almacena la cadena en la variable usernames 
   - [x] Divide una variable de cadena llamada logins en una lista de cadenas y la almacena en la variable usernames
> Correcto

8. ¿Qué es el Análisis sintáctico?
   - [ ] El proceso de escribir datos en un nuevo archivo
   - [ ] El proceso de lectura de Datos línea por línea
   - [ ] El proceso de copia de Datos a otros ficheros
   - [x] El proceso de convertir Datos a un formato más legible
> Correcto

9. ¿Qué hace el siguiente Código? `new_format = old_format.read()`
   - [ ] Inserta la cadena almacenada en la variable new_format en el archivo almacenado en la variable old_format 
   - [ ] Detecta ciertos patrones de texto en old_format
   - [x] Lee la variable old_format, que contiene un archivo, y la almacena como una cadena en new_format
   - [ ] Imprime el contenido de old_format
> Correcto

10. Quiere comprobar si hay actividad inusual de inicio de sesión. En concreto, quiere comprobar si hubo más de tres intentos fallidos de inicio de sesión en los últimos 10 minutos por parte del último usuario que se registró. Si desea automatizar esto a través de Python, ¿qué formaría parte de su código? Seleccione tres respuestas.
   - [x] Una sentencia if que comprueba si hubo más de tres intentos fallidos de inicio de sesión
   - [x] Un bucle for que itera a través de la lista de conexiones
   - [ ] Una línea de programación que reasigna una variable de contador a 0 si hay un intento fallido de inicio de sesión
   - [x] Una variable contador que se incrementa cuando se detecta un inicio de sesión fallido
> Correcto