# Revisar: Escribir código Python eficaz

## Resumen
- ​Gran trabajo por haber llegado tan lejos en el curso de Python!
- ​Ha puesto mucho trabajo y ​esfuerzo en aprender más sobre ​cómo puede utilizar Python de forma eficaz y eficiente.
- ​Recapitulemos rápidamente los conceptos ​que ha aprendido a lo largo de los vídeos.
- ​Primero, empezamos por ​comprender el papel de las funciones en Python.
- ​¡Pueden ahorrarle mucho tiempo! ​Aprendió cómo incorporar ​funciones incorporadas y cómo ​desarrollar su propia función para satisfacer sus necesidades.
- ​Después cambiamos nuestro enfoque hacia los módulos y bibliotecas, ​que nos dieron acceso a ​muchas más funciones que las incorporadas en Python.
- ​Por último, pasamos a aprender sobre ​la legibilidad del código y las mejores prácticas para ​escribir código limpio y comprensible.
- ​Con estos conocimientos, ​está preparado para aprender lo potente que puede ser realmente ​Python para la Automatización de tareas y ​cómo puede ayudarle a seguir adelante como analista de Seguridad.

---

## Guía de referencia: Conceptos de Python del Módulo 2

---

## Términos del glosario del Módulo 2
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 2

1. ¿Cuál de las siguientes opciones es un Encabezado válido en la definición de una Función?
   - [ ] def remove_user(username)
   - [x] def remove_user(username):
   - [ ] remove_user(username):
   - [ ] def (remove_user(username))
> Correcto

2. ¿Cuál de las siguientes llamadas a la función type() utiliza la sintaxis correcta?
   - [ ] type[(81, 17)]
   - [ ] type[81, 55, 17]
   - [ ] type([17, 81]):
   - [x] type([55, 81, 17])
> Correcto

2. ¿Cuáles de los siguientes componentes son necesarios para llamar a una Función integrada en Python? Seleccione tres respuestas
   - [x] Los argumentos requeridos por la función
   - [x] El nombre de la función
   - [x] ()
   - [ ] :
> Correcto

3. ¿Qué es un parámetro?
   - [ ] Una variable devuelta por una función
   - [ ] Los datos que se introducen en una función cuando se la llama
   - [x] Objeto que se incluye en la definición de una función para su uso en dicha función
   - [ ] El nombre de una función que se está definiendo
> Correcto

3. Revise el siguiente código. ¿Cuál de estas afirmaciones describe con exactitud name?
```python
def echo(name):
   return name * 3
```
   - [ ] Es un argumento porque se utiliza en una declaración return.
   - [x] Es un parámetro porque está incluido en la definición de la función. 
   - [ ] Es un argumento porque se incluye en la llamada a la función.
   - [ ] Es un parámetro porque se utiliza en una sentencia return.
> Correcto

3. Un argumento es un valor que se pasa a una función cuando ésta es llamada. En el siguiente código, ¿cuál es el argumento?
```python
def welcome_user(name):
   print("Welcome," name)
username="elarson"
welcome_user(username)
```
   - [ ] def 
   - [ ] welcome_user
   - [x] username
   - [ ] name
> Correcto

4. Cuando se trabaja en Python, ¿qué es una biblioteca?
   - [x] Una colección de módulos que proporcionan código al que los usuarios pueden acceder en sus programas
   - [ ] Un archivo Python que contiene funciones adicionales, variables, clases y cualquier tipo de código ejecutable
   - [ ] Módulo que le permite trabajar con un tipo concreto de archivo
   - [ ] Una colección de pautas de estilo para trabajar con Python
> Correcto

4. Rellene el espacio en blanco: Los módulos re, csv, glob, y time son todos _____
   - [ ] parte del PEP 8
   - [ ] palabras clave en el Encabezado de una Función
   - [ ] funciones integradas 
   - [x] parte de la Biblioteca estándar de Python
> Correcto

5. ¿Qué devuelve esta línea de código?
```python
print(sorted(["h32rb17", "p52jb81", "k11ry83"]))
```
   - [ ] ["p52jb81"]
   - [x] ["h32rb17", "k11ry83", "p52jb81"]
   - [ ] ["p52jb81", "k11ry83", "h32rb17"]
   - [ ] ["h32rb17"]
> Correcto

5. ¿Qué devuelve esta línea de código?
```python
print(type("h32rb17"))
```
   - [ ] h32rb17
   - [ ] "h32rb17"
   - [x] str
   - [ ] int
> Correcto

6. Qué devuelve la siguiente Función definida por el usuario si se le pasa el argumento de 2?
```python
def multiples(num):
   multiple = num * 3
   return multiple
multiples(2)
``` 
   - [ ] num
   - [ ] multiples
   - [x] 6
   - [ ] 2
> Correcto

7. ¿Qué contiene el PEP 8?
   - [ ] Sugerencias para facilitar el aprendizaje de Python
   - [ ] Una colección de módulos a los que los usuarios pueden acceder en sus programas
   - [x] Pautas estilísticas para programadores que trabajan en Python
   - [ ] Archivos con funciones adicionales que los usuarios pueden utilizar en su código
> Correcto

7. ¿En qué puede ayudarle una Guía de estilo cuando trabaja con Python? Seleccione dos respuestas
   - [ ] Cómo hacer que su código sea más complejo
   - [ ] Encontrar nuevos módulos que pueda incorporar a su código 
   - [x] Cómo hacer que su código sea más coherente 
   - [x] Facilitar a otros programadores la comprensión de su código
> Correcto

8. ¿Cuál es la ventaja de incluir este Comentario en el siguiente Código? Seleccione todo lo que corresponda:
```python
# For loop iterates to print an alert message 5 times
for i in range(5):
   print("alert")
```
   - [x] Puede ayudar a otros programadores a entender el propósito de este Bucle.
   - [ ] Aparece en la salida cuando se ejecuta el código en Python. 
   - [ ] Garantiza que el Bucle funcionará cuando se ejecute el código en Python.
   - [x] Puede ayudarle a entender el código si vuelve a consultarlo en el futuro.
> Correcto

8. ¿Qué debe hacer al escribir comentarios? Seleccione todo lo que corresponda
   - [ ] Colóquelas antes de cada línea de programación.
   - [x] Hágalos claros.
   - [x] Manténgalos al día.
   - [ ] Colóquelos sólo al principio de una programación.
> Correcto

9. ¿Qué es una función?
   - [ ] Un archivo Python que contiene código ejecutable
   - [ ] Un recurso descargable con instrucciones de codificación
   - [x] Una sección de código reutilizable
   - [ ] Un conjunto de directrices estilísticas para trabajar en Python
> Correcto

9. ¿Cuál de las siguientes afirmaciones describe con precisión las funciones? Seleccione todas las que correspondan
   - [ ] Las funciones no pueden utilizarse más de 10 veces desde un mismo programa.
   - [x] Las funciones pueden reutilizarse a lo largo de un programa.
   - [x] Cuando se actualizan las funciones, los cambios se aplican en todos los lugares en los que se utilizan.
   - [x] Las funciones son útiles para la Automatización.
> Correcto

10. Ha importado un Módulo de Python, ¿a qué tiene ahora accesibilidad en Python?
   - [x] Funciones adicionales, variables, clases y otros tipos de código ejecutable
   - [ ] Lista de comentarios que ha incluido en la programación anterior
   - [ ] Una Función que existe dentro de Python y puede ser llamada directamente
   - [ ] Un manual que informa sobre la redacción, el formato y el diseño de los documentos
> Correcto

10. Rellene el espacio en blanco: Los módulos de Python son archivos que _____
   - [x] contienen cualquier tipo de código ejecutable
   - [ ] sólo contienen nuevas variables
   - [ ] contención de bibliotecas
   - [ ] sólo contienen funciones integradas
> Correcto