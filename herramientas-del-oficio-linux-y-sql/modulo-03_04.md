# Obtener ayuda en Linux

## Damar: Mi viaje a los comandos de Linux
- ​Mi consejo para las personas que intentan entrar en la ciberseguridad es que puede ser mucho ​más fácil de lo que creen.
- Definitivamente fue mucho más fácil de lo que pensaba.
- ​Algo que aprendí por mí mismo es que no vas a poder ​aprender todo de una vez, y ​no vas a necesitar saberlo todo de una vez.
- ​Linux es muy importante porque ​se usa ampliamente en casi todas las empresas.
- ​Puede usar Linux para conservar los registros.
- ​Es una práctica muy común que también puede usar para configurar ​trabajos por lotes que le ayudarán con las tareas rutinarias en Linux.
- ​El mejor consejo que puedo dar a alguien que está intentando aprender Linux y ​los comandos de Linux es que no se desanime por ningún pequeño contratiempo que surja.
- ​Sigue con ello. ​Quédate con eso. ​Piensa en ello como cuando aprendiste a nadar por primera vez, ​¿verdad? Probablemente no eras muy bueno en eso.
- Hay una gran cantidad de recursos de apoyo cuando se aprende Linux.
- ​Otra forma de apoyo para aprender Linux es simplemente buscar respuestas en Google usando ​Stack Overflow, tal vez incluso haciendo una publicación en Reddit.

---

## La comunidad Linux
- La popularidad y facilidad de uso de Linux ​ha creado una gran comunidad en línea ​que publica constantemente información para ​ayudar a los usuarios a aprender a manejar Linux.
- ​Dado que Linux es de código abierto, ​se ha convertido en una comunidad global de ​usuarios que contribuyen con frecuencia.
- ​Esta comunidad global es un enorme recurso para ​todos los usuarios de Linux porque los usuarios ​pueden encontrar respuestas para las tareas cotidianas.
- ​Sólo con buscar en Internet obtendrá muchas respuestas.
- ​La forma más fácil de solucionar problemas en una tarea es buscar y ​leer sobre cómo lo ha hecho otra persona.
- ​Buscar recursos sobre cómo ejecutar ​una tarea es una buena forma de que los principiantes sigan aprendiendo.
- ​Hasta ahora, ha aprendido a añadir usuarios, ​pero imagine que más adelante desea añadir un nuevo grupo. 
- Una forma de aprender cómo hacerlo es buscar en Internet.
- ​Intentémoslo a través de una búsqueda en Google.
- ​Los resultados de la búsqueda nos dan ​muchas opciones para añadir un grupo en Linux.
- ​Otra fuente de buena reputación es un ​Unix & Linux Pila Exchange.
- ​Sus respuestas están clasificadas con ​puntos para mostrar respuestas de alta calidad.
- ​Muchas preguntas están relacionadas con ​usuarios más avanzados y ​están orientadas a la solución de problemas.
- ​Bueno, ahora ya sabe dónde obtener algo de soporte extra ​siempre que tenga dudas sobre temas en Linux.
- ​Hay mucho soporte a sólo un clic de distancia.

---

## Páginas man dentro del shell
- ​El primer comando que puede ayudarle de esta manera es: `man`.
- ​man muestra información sobre ​otros comandos y cómo funcionan.
- El nombre de este comando proviene de la palabra manual.
- ​Examinemos esto más de cerca utilizando ​man para obtener información sobre el comando usermod.
- ​Después de man, escribimos el nombre de este comando.
- ​La información que devuelve man ​incluye una descripción general.
- ​También contiene información ​sobre cada una de las opciones de usermod.
- ​Por ejemplo, la opción -d puede ​añadirse a usermod para cambiar el directorio personal de un usuario.
- ​man proporciona mucha información, ​pero a veces sólo necesitamos ​una referencia rápida sobre lo que hace un comando.
- ​En ese caso, se utiliza `whatis`.
- ​whatis muestra una descripción ​de un comando en una sola línea.
- ​Digamos que ha oído a un compañero de trabajo ​mencionar un comando como tail.
- ​Nunca había oído hablar de este comando, ​pero puede averiguar lo que hace.
- ​Simplemente utilice el comando, ​whatis tail, y aprenda que ​expresa la última parte de los archivos.
- ​A veces puede que ni siquiera sepamos qué comando buscar.
- ​Aquí es donde `apropos` puede ayudarnos.
- ​`apropos` busca en las descripciones de las páginas del manual ​una cadena especificada.
- ​Digamos que tiene una tarea que ​requiere que cambie una contraseña, ​pero no está muy seguro de cómo hacerlo.
- ​Si utilizamos el comando `apropos` con la cadena contraseña, ​se mostrará un gran número ​de comandos con esa palabra.
- ​Esto ayuda un poco, ​pero aún puede ser difícil encontrar lo que necesitamos.
- ​Pero podemos filtrar esto añadiendo ​la opción -a y una cadena adicional.
- ​Esta opción devolverá ​sólo los comandos que contengan ambas cadenas.
- ​En nuestro caso, ya que queremos cambiar la contraseña, ​busquemos comandos con ambas: cambio y contraseña.
- ​Ahora, la salida se ha ​limitado a los comandos más relevantes.