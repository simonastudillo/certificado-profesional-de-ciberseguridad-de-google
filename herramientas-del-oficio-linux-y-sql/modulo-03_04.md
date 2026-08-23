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

---

## Recursos Linux
- Linux tiene muchas opciones disponibles para dar a los usuarios la Información que necesitan.
- Comunidad Linux
   - Linux tiene una gran comunidad en línea, y este es un enorme recurso para los usuarios de Linux de todos los niveles.
   - Es probable que pueda encontrar las respuestas a sus preguntas con una simple búsqueda en línea.
   - La solución de problemas mediante la búsqueda y la lectura en línea es una manera eficaz de descubrir cómo otros abordaron su problema.
   - También es una forma estupenda para que los principiantes aprendan más sobre Linux.
   - La Pila de intercambio de UNIX y Linux es un recurso de confianza para la solución de problemas de Linux.
   - El Intercambio de Pila de Unix y Linux es un sitio web de preguntas y respuestas donde los miembros de la comunidad pueden hacer y responder preguntas sobre Linux.
   - Los miembros de la comunidad votan las respuestas, por lo que las de mayor calidad aparecen en la parte superior.
   - Muchas de las preguntas están relacionadas con temas específicos de usuarios avanzados, y los temas podrían ayudarle a solucionar problemas mientras sigue utilizando Linux.
- Soporte integrado de Linux
   - Linux también dispone de varios comandos que puede utilizar para obtener asistencia.
- man
   - El comando man muestra información sobre otros comandos y su funcionamiento.
   - Es la abreviatura de "manual"
   - Para buscar información sobre un comando, introduzca el comando después de man.
   - Por ejemplo, si introduce man chown obtendrá información detallada sobre chown, incluidas las distintas opciones que puede utilizar con él.
   - La salida del comando man también se denomina "página de manual"
- apropos
   - El comando apropos busca en las descripciones de las páginas de manual una cadena especificada.
   - Las páginas man pueden ser largas y difíciles de buscar si lo que busca es una palabra clave específica.
   - Para utilizar apropos, introduzca la palabra clave después de apropos.
   - También puede incluir la opción -a para buscar varias palabras.
   - Por ejemplo, si introduce apropos -a graph editor obtendrá las páginas de manual que contengan las palabras "gráfico" y "editor" en sus descripciones.
- whatis
   - El comando whatis muestra la descripción de un comando en una sola línea.
   - Por ejemplo, al introducir whatis nano se obtiene la descripción de nano.
   - Este comando es útil cuando no se necesita una descripción detallada, sino sólo una idea general del comando.
   - Puede ser como recordatorio.
   - O puede ser después de descubrir un nuevo comando a través de un colega o de un recurso en línea y querer saber más.

---

## Actividad: Obtener ayuda en la línea de comandos
- Introducción
   - En este laboratorio, utilizará los comandos man, whatis y apropos para practicar la búsqueda de respuestas a preguntas sobre Linux en la línea de comandos.
   - Estas habilidades son útiles para muchas tareas de Seguridad diferentes.
   - Utilizará comandos de Linux en el shell Bash para completar este laboratorio.
- Lo que hará
   - Explorar comandos que le ayudarán a aprender más sobre otros comandos
   - Encontrar opciones para un comando
   - Determinar las diferencias entre dos comandos
   - Identificar el comando necesario para crear un nuevo grupo
- Resumen de la actividad
   - Como analista de seguridad, no tendrás siempre todas las respuestas, pero puedes aprender a encontrarlas.
   - Uno de los mejores aspectos sobre Linux es que puedes obtener ayuda directamente en la línea de comandos.
   - En este lab, usarás los comandos man y whatis para obtener información sobre otros comandos y su funcionamiento.
   - También usarás el comando apropos para buscar un comando con una cadena específica en la página del manual.
   - Si trabajas como analista de seguridad, te resultará útil saber cómo descubrir qué comando usar o encontrar información sobre qué hace cada comando.
- Situación
   - En este caso, debes encontrar más información sobre comandos que necesitas usar.
   - También debes descubrir qué comando sirve para una tarea en particular.
   - Estos son los pasos que seguirás:
      1. Explorarás algunos comandos de la shell que te darán información sobre otros comandos.
      2. Buscarás una opción que debas agregar a un comando.
      3. Usarás un comando para obtener una descripción breve de los comandos, de modo que puedas identificar sus diferencias.
      4. Identificarás el comando que necesitas para realizar una tarea.

- Comienza el lab

1. Obtén más información sobre los comandos
- Ejecuta el comando whatis para obtener una descripción breve de cat.
- ¿Cuáles son las dos primeras palabras de la descripción breve de cat que devuelve whatis?
   - [x] concatenate files
   - [ ] cat is
   - [ ] file concatenator
   - [ ] the cat
- Usa el comando man para obtener más detalles sobre cat.
- ¿Qué opción puedes usar para enumerar las líneas del resultado del comando cat?
   - [ ] ninguna; es la opción predeterminada
   - [ ] -b, --number-nonblank
   - [x] -n, --number
   - [ ] -e, --enumerate
- Presiona Q para salir de esta página del manual.
- Usa apropos para encontrar un comando que muestre la primera parte de un archivo (part file).
- ¿Qué comando devuelve la primera parte de un archivo?
   - [x] head
   - [ ] tail
   - [ ] list
   - [ ] cat

2. Explora el comando useradd
- Usa el comando de Linux más adecuado para obtener ayuda con el comando useradd y explora todas sus opciones.
- ¿Qué opción se puede usar con el comando useradd para configurar la fecha de vencimiento de una cuenta de usuario temporal?
   - [ ] -x
   - [ ] -e
   - [ ] -f
   - [ ] -d
- Presiona Q para salir de esta página del manual.

3. Explora los comandos rm y rmdir
- Usa el comando de Linux más adecuado para recordar rápidamente qué hace cada comando.
- ¿Cuál de estos comandos quita solo los directorios vacíos?
   - [x] rmdir
   - [ ] rm

4. Determina qué comando usar
- Usa el comando de Linux más adecuado con estas palabras clave para identificar qué comando usar.
- ¿Qué comando puedes usar para crear un grupo nuevo?
   - [ ] newgroup
   - [ ] addnewgroup
   - [ ] setsid
   - [x] groupadd

- Listado de comandos utilizados en este laboratorio
```bash
whatis cat
man cat
apropos -a first part file
man useradd
whatis rm
whatis rmdir
apropos -a create new group
```

---

## Ejemplo opcional: Obtener ayuda en la línea de comandos
- Mismo laboratorio que el anterior.

---

## Ejemplo: Obtener ayuda en la línea de comandos
- Resumen de actividades
   - Como analista de seguridad, no tendrás todas las respuestas todo el tiempo, pero puedes aprender dónde encontrarlas.
   - Una de las mejores cosas de Linux es que puedes obtener ayuda a través de la línea de comandos.
   - En esta actividad de laboratorio, utilizarás los comandos man y whatis para obtener información sobre otros comandos y cómo funcionan.
   - También utilizarás el comando apropos para buscar en la página del manual un comando con una cadena especificada.
   - Cuando trabajes como analista de seguridad, es probable que te resulte útil saber cómo descubrir qué comando usar o información sobre lo que hacen los comandos.
   - Con eso en mente, exploremos tu escenario.

- Listado de comandos utilizados en este laboratorio
```bash
whatis cat
man cat
apropos -a first part file
man useradd
whatis rm
whatis rmdir
apropos -a create new group
```

- Conclusión
   - Ahora tienes experiencia práctica en el uso de comandos básicos del shell Bash de Linux para
      - obtener una breve descripción de un comando,
      - mostrar las páginas man para un comando, y
      - encontrar comandos basados en palabras clave sobre su función.