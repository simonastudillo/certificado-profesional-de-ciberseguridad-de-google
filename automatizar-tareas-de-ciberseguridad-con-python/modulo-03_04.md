# Repasar: Trabajar con cadenas y listas

## Resumen
- ​Empezamos este curso centrándonos en ​trabajar con cadenas y listas.
- ​Aprendimos métodos que trabajan ​específicamente con estos tipos de datos.
- ​También aprendimos a trabajar con ​índices y a extraer la información que necesitamos.
- ​A continuación, nos centramos en la escritura de algoritmos.
- ​Escribimos un algoritmo sencillo que troceaba ​el ID de red a partir de una lista de direcciones IP.
- ​Por último, cubrimos el uso de expresiones regulares.
- ​Las expresiones regulares le permiten buscar patrones, ​y esto proporciona formas ampliadas de ​localizar lo que necesita en registros y otros archivos.
- ​Estos son conceptos complejos, y siempre ​será bienvenido a volver a visitar los vídeos cuando lo desee.
- ​Con estos conceptos, ha dado ​un gran paso para poder ​trabajar con datos y escribir ​los algoritmos que necesitan los profesionales de la seguridad.
- ​A lo largo del resto de este curso, ​va a adquirir más práctica con ​Python y lo que puede ofrecer a los analistas de seguridad.

---

## Guía de referencia: Conceptos de Python del Módulo 3

---

## Términos del glosario del Módulo 3
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 3

1. ¿Qué línea de código devuelve el número de caracteres de la cadena asignada a la variable username?
   - [x] print(len(username))
   - [ ] print(username.len())
   - [ ] print(username.str())
   - [ ] print(str(username))
> Correcto

2. ¿Cuál es el resultado cuando se aplica .upper() a una cadena?
   - [x] Se devuelve una copia de la cadena con todas las letras mayúsculas.
   - [ ] El valor de la cadena se reasigna al valor de la cadena de la línea que la precede.
   - [ ] El valor de la cadena se reasigna para contener todas las letras mayúsculas.
   - [ ] Se extrae de la cadena el carácter que aparece con más frecuencia en ella y se devuelve
> Correcto

3. ¿Cuál es el índice del carácter "c" en la cadena "encryption"?
   - [ ] 4
   - [ ] 3
   - [ ] 1
   - [x] 2
> Correcto

4. Debe extraer una porción de un ID de red. En concreto, debe extraer los caracteres con índices de 6 a 10. Complete el código Python para tomar esta rebanada y mostrarla.
```python
network_id = "l693m585n528"
print(network_id[6:11])
```
   - [ ] "5n528"
   - [x] "85n52"
   - [ ] "585n5"
   - [ ] "m585n"
> Correcto

5. ¿Cuál es el resultado del siguiente código?
```python
username_list  = ["elarson", "bmoreno", "tshah"] 
device_id_list = ["us2c0R5", "2R78TBR", "bt3MIEz"]
print(username_list + device_id_list)
```
   - [ ] Un mensaje de error
   - [x] ["elarson", "bmoreno", "tshah", "us2c0R5", "2R78TBR", "bt3MIEz"]
   - [ ] ["us2c0R5", "2R78TBR", "bt3MIEz", "elarson", "bmoreno", "tshah"]
   - [ ] ["elarson", "us2c0R5", "bmoreno", "2R78TBR", "tshah", "bt3MIEz"]
> Correcto

6. ¿Cuál es el resultado del siguiente código?
```python
approved_users = ["bmoreno", "elarson", "tshah", "eraab"]
print(approved_users[1])
```
   - [ ] [1, "bmoreno", "elarson", "tshah", "eraab"]
   - [ ] ["bmoreno", "elarson", "tshah", "eraab", 1]
   - [x] "elarson"
   - [ ] "bmoreno"
> Correcto

7. Rellene el espacio en blanco: Determinar que necesita utilizar el corte de cadenas y un bucle for para extraer información de los elementos de una lista forma parte de la creación de a(n) _____
   - [x] algoritmo
   - [ ] índice
   - [ ] adjuntar
   - [ ] expresión regular
> Correcto

8. ¿A qué corresponde el símbolo \w en una expresión regular?
   - [ ] Cualquier número
   - [ ] Cualquier letra
   - [ ] Cualquier carácter y símbolo
   - [x] Cualquier carácter alfanumérico
> Correcto

9. ¿Qué devuelve la función re.findall()?
   - [ ] Todas las apariciones del patrón "re" en una cadena dada
   - [ ] La primera coincidencia con una expresión regular en una cadena dada
   - [x] Lista de todas las coincidencias con una expresión regular en una cadena determinada
   - [ ] Todas las expresiones regulares posibles que coinciden con una cadena dada
> Correcto

10. ¿Qué hace el código device_ids.append("h32rb17")?
   - [ ] Inserta "h32rb17" al principio de la lista device_ids 
   - [x] Añade "h32rb17" al final de la lista device_ids 
   - [ ] Devuelve todas las coincidencias con el patrón "h32rb17" en la lista device_ids 
   - [ ] Actualiza a mayúsculas todas las instancias de "h32rb17" en la lista device_ids 
> Correcto