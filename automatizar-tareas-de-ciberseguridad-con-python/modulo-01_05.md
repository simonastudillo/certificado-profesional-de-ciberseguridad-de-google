# Revisión: Introducción a Python

## Resumen
- Has aprendido por qué los analistas de Seguridad usan Python y ​la estructura básica de un programa.
- ​Incluso has escrito algunas líneas de código en Python. ​Repasemos lo que has aprendido hasta ahora.
- ​Primero aprendió los conceptos básicos de la programación y ​por qué es una herramienta muy importante para los analistas de Seguridad.
- ​También aprendió algunos de los conceptos básicos de cómo ​funcionan los lenguajes de programación.
- ​Luego aprendió a reconocer los tipos de datos en Python.
- ​Nos centramos en datos de cadenas, enteros, flotantes, booleanos y de listas.
- ​A continuación, nos centramos en trabajar con variables.
- ​A continuación, aprendió todo sobre las sentencias condicionales y cómo comprobar ​las condiciones lógicas mediante sentencias de Python.
- ​Por último, trabajamos con sentencias iterativas y ​analizamos los dos tipos de bucles: bucles for y while.
- ​Utilizará este conocimiento a medida que avance en este curso y ​en su carrera como analista de Seguridad.
- ​En la siguiente sección, exploraremos otros componentes importantes de Python, ​incluidas las funciones.

---

## Guía de referencia: Conceptos de Python del Módulo 1

---

## Términos del glosario del Módulo 1
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 1

1. Rellene el espacio en blanco: Automatización es _____
   - [ ] la combinación de tecnología y esfuerzo manual para completar una tarea
   - [ ] la sustitución de la tecnología existente
   - [x] el uso de la tecnología para reducir el esfuerzo humano y manual en la realización de tareas comunes y repetitivas
   - [ ] la utilización del esfuerzo humano y manual para reducir el consumo de energía tecnológica
> Correcto

2. ¿Qué ocurre con el siguiente Código?
```python
for username in failed_login:
print(username)
```
   - [ ] La primera línea debe dividirse en dos, y in failed_login: debe sangrarse en la nueva línea.
   - [ ] La línea con for username in failed_login: no tiene sangría.
   - [x] La línea con print(username) no tiene sangría.
   - [ ] Ambas líneas no tienen sangría.
> Correcto

3. ¿Qué tipo de datos requiere comillas (" ")?
   - [ ] Booleana
   - [ ] Entero
   - [x] Cadena
   - [ ] Flotante
> Correcto

4. ¿Cuáles son los valores posibles para el tipo de datos booleanos? Seleccione todos los que correspondan
   - [ ] !=
   - [ ] >
   - [x] True
   - [x] False
> Correcto

5. ¿Cómo se asigna el valor de cadena "rtp3426" a una variable llamada device_id?
   - [ ] device_id(rtp3426)
   - [x] device_id = "rtp3426"
   - [ ] device_id = rtp3426
   - [ ] device_id("rtp3426")
> Correcto

6. ¿Qué hará este código cuando lo ejecute?
```python
var2 = ["a","b","c"]

var2_type = type(var2)

print(var2_type)
```
   - [ ] Muestra en pantalla los caracteres "a", "b", y "c" 
   - [ ] Imprime la cadena "var2_type" en la pantalla
   - [x] Indique que var2 contiene datos de lista 
   - [ ] Cambiar el Tipo de datos de var2
> Correcto

7. Está implementando medidas de Seguridad en un servidor. Si un usuario tiene más de 3 intentos de inicio de sesión fallidos, el programa debe imprimir "locked out". El número de intentos fallidos de inicio de sesión se almacena en una variable llamada failed_attempts. ¿Qué sentencia condicional tiene la sintaxis correcta necesaria para hacer esto?
   - [ ] if failed_attempts < 3
            print("locked out")
   - [ ] if failed_attempts <= 3:
            print("locked out")
   - [x] if failed_attempts > 3:
            print("locked out")
   - [ ] if failed_attempts >= 3
            print("locked out")
> Correcto

8. Usted ha escrito el siguiente código:
```python
if operating_system == "OS 3":
   print("Updates needed")
```
- Quiere añadirlo para que imprima un mensaje "No updates needed" siempre que el valor de operating_system no sea "OS 3". ¿Qué líneas de código tienen la sintaxis correcta para hacerlo?
   - [ ] elif operating_system == "OS 3":
            print("No updates needed")
   - [ ] else operating_system != "OS 3":
            print("No updates needed")
   - [ ] else
            print("No updates needed")
   - [x] else:
            print("No updates needed")
> Correcto

9. ¿Qué Sentencia iterativa debe utilizar si desea imprimir los números 1, 2, y 3?
   - [x] for i in range(1, 4):
            print(i)
   - [ ] for i in range(1, 3):
            print(i)
   - [ ] for i in [1, 3]:
            print(i)
   - [ ] for i in range(0, 3):
            print(i)
> Correcto

10. Si desea ejecutar un bucle que se repita si una variable de recuento es menor que 50, ¿qué código debe contener la cabecera del bucle?
   - [x] while count < 50:
   - [ ] while count == 50:
   - [ ] print(50)
   - [ ] count = count + 50
> Correcto