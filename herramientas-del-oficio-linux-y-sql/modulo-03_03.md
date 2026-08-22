# Autenticación y autorización de usuarios

## Permisos de archivo y responsabilidad
- ​Aprenderemos cómo Linux representa los permisos ​y cómo puede comprobar los permisos ​asociados a archivos y directorios.
- ​Los permisos son el tipo de ​acceso concedido para un archivo o directorio.
- Los permisos están relacionados con la autorización.
- ​La autorización es el concepto de conceder ​acceso a recursos específicos en un sistema.
- ​La autorización le permite limitar ​el acceso a archivos o directorios especificados.
- ​Una buena regla a seguir es que ​el acceso a los datos es en la medida en que sea necesario.
- ​Puede imaginarse el riesgo que supondría para la seguridad ​que cualquiera ​pudiera acceder o modificar ​todo lo que quisiera en un sistema.
- ​En ​Linux existen tres tipos de permisos que puede tener un usuario autorizado.
- ​El primer tipo de permiso es el de lectura.
   - ​En un archivo, los permisos de lectura ​significan que se puede leer el contenido del archivo.
   - En un directorio, ​este permiso significa que se pueden leer ​todos los archivos de ese directorio.
- ​Los siguientes son los permisos de escritura.
   - ​Los permisos de escritura en un archivo permiten ​modificar el contenido del archivo.
   - ​En un directorio, los permisos de escritura indican que ​se pueden crear nuevos archivos en ese directorio.
- ​Por último, también existen los permisos de ejecución.
   - ​Los permisos de ejecución sobre archivos significan que ​el archivo puede ejecutarse si se trata de un archivo ejecutable.
   - ​Los permisos de ejecución sobre directorios permiten a los usuarios ​entrar en un directorio y acceder a sus archivos.
- ​Se conceden permisos para ​tres tipos diferentes de propietarios.
   - ​El primer tipo es el usuario.
      - ​El usuario es el propietario del archivo.
      - ​Cuando crea un archivo, ​se convierte en el propietario del archivo, ​pero la propiedad puede cambiarse.
   - ​El grupo es el siguiente tipo.
      - ​Cada usuario forma parte de un determinado grupo.
      - ​Un grupo está formado por varios usuarios, ​y ésta es una forma de gestionar un entorno multiusuario.
   - ​Por último, está other.
      - ​Other puede considerarse todos los demás usuarios del sistema.
      - ​Básicamente, cualquier otra persona con acceso ​al sistema pertenece a este grupo.
      - ​En Linux, los permisos de archivo se ​representan con una cadena de 10 caracteres.
- ​Para un directorio con permisos completos para el grupo de usuarios, ​esta cadena sería: drwxrwxrwx.
- ​Examinemos lo que esto significa más detenidamente.
   - ​El primer carácter indica el tipo de archivo.
      - ​Como se muestra en este ejemplo, `​d` se utiliza para indicar que se trata de un directorio.
      - ​Si este carácter contuviera un guión `-` en su lugar, ​se trataría de un archivo normal.
   - ​El segundo, tercer y ​cuarto carácter indican los permisos del usuario.
      - ​En este ejemplo, `r` ​indica que el usuario tiene permisos de lectura, `​w` indica que el usuario tiene permisos de escritura, ​y `x` indica que el usuario tiene permisos de ejecución.
      - ​Si faltara uno de estos permisos, ​habría un guión en lugar de la letra.
      - ​Del mismo modo, los caracteres quinto, sexto, ​y séptimo indican ​permisos para el siguiente grupo tipo propietario.
      - ​Como se muestra aquí, ​el grupo tipo también tiene permisos de lectura, ​escritura y ejecución.
      - ​No hay guiones para indicar que ​no se ha concedido alguno de estos permisos.
   - ​Por último, los caracteres octavo a décimo ​indican permisos para el último tipo de propietario: otro.
      - ​También tienen permisos de lectura, escritura, ​y ejecución en este ejemplo.
      - ​Asegurarse de que los archivos y directorios están configurados ​con sus permisos de acceso adecuados es ​crítico para proteger los archivos confidenciales y ​mantener la seguridad general de un sistema.
      - ​Por ejemplo, los departamentos de nóminas ​manejan información sensible.
      - ​Si alguien ajeno ​al grupo de nóminas pudiera leer este archivo, ​esto supondría un problema de privacidad.
      - ​Otro ejemplo es cuando el usuario, ​el grupo y otros pueden todos escribir en un archivo.
- ​Este tipo de archivo se considera un archivo escribible por todos.
- ​Los archivos escribibles por todos pueden plantear importantes Riesgos de Seguridad.
- Entonces, ¿cómo comprobamos los permisos?
   - ​Primero, necesitamos entender qué son las opciones.
      - ​Las opciones modifican el comportamiento del comando.
      - ​Las opciones de un comando ​pueden ser una sola letra o una palabra completa.
      - ​Comprobar los permisos implica añadir ​opciones al comando ls.
      - ​En primer lugar, `ls -l` muestra ​permisos de archivos y directorios.
   - También es posible que desee mostrar ​archivos ocultos e identificar sus permisos.
      - ​Los archivos ocultos, que empiezan por ​un punto antes de su nombre, no ​aparecen normalmente cuando utiliza ls para mostrar el contenido de los archivos.
      - Introduciendo `ls -a` muestra los archivos ocultos.
      - ​Entonces puede combinar estas dos opciones para hacer ambas cosas.
- ​Introduciendo `ls -la` muestra los permisos ​para archivos y directorios, incluyendo los archivos ocultos.
- ​Vamos a entrar en Bash y probar estas opciones.
- ​En este momento, estamos en el subdirectorio del proyecto.
- ​Primero, vamos a utilizar el comando `ls` para mostrar su contenido.
- ​La salida muestra los archivos en este directorio, ​pero no sabemos nada acerca de sus permisos.
- ​Al utilizar `ls -l` en su lugar, ​obtenemos información ampliada sobre ​estos archivos.
- ​Los nombres de los ficheros están ahora a la derecha de cada fila.
- ​La primera pieza de información en cada fila ​muestra los permisos en ​el formato que discutimos antes.
- ​Dado que todos estos son ficheros y no directorios, ​fíjese cómo el primer carácter es un guión.
- ​Centrémonos en un archivo concreto: proyecto1.txt.
- ​Los caracteres segundo a cuarto de sus ​permisos nos muestran que el usuario ​tiene permisos de lectura y escritura ​pero carece de permisos de ejecución.
- ​Tanto en los caracteres quinto a ​séptimo como en los caracteres octavo a décimo, ​la secuencia es r--.
- Esto significa que el grupo y otros sólo tienen privilegios de lectura.
- Después de los permisos, `ls -l` muestra primero el nombre de usuario.
- ​Aquí, somos nosotros, analista.
- Luego viene el nombre del grupo; ​en nuestro caso, el grupo de Seguridad.
- ​Ahora utilicemos `ls -a` ​La salida incluye dos archivos más-archivos ocultos ​con los nombres: .hidden1.txt ​y .hidden2.txt
- ​Por último, también podemos utilizar `​ls -la` para mostrar los permisos de todos los archivos, ​incluidos estos archivos ocultos.

---

## Cambiar permisos
- ​​Cuando se trabaja como analista de seguridad, ​puede haber muchas razones para ​cambiar los permisos de un usuario.
- ​Un usuario puede haber cambiado de departamento ​o haber sido asignado a un grupo de trabajo diferente.
- ​Un usuario puede simplemente dejar de trabajar en ​un proyecto que requiere ciertos permisos.
- ​Estos cambios son necesarios para proteger ​los archivos del sistema de ser ​accidental o deliberadamente alterados o borrados.
- ​Exploremos un comando relacionado ​que ayuda a controlar este acceso.
- ​chmod cambia los permisos en archivos y directorios.
- ​El comando chmod significa modo de cambio.
- ​Hay dos modos para cambiar los permisos, ​pero nos centraremos en el simbólico.
- La mejor manera de ​aprender cómo funciona chmod es a través de un ejemplo.
- ​Sé que esto tiene muchos detalles, ​pero lo desglosaremos.
- ​Tenga en cuenta también que, como muchos comandos de Linux, ​no tiene que memorizar ​la información y siempre puede encontrar una referencia.
- ​Con chmod, necesita identificar para qué ​archivo o directorio desea ajustar los permisos.
- ​Este es el argumento final, ​en este caso, un archivo llamado: access.txt.
- ​El primer argumento, añadido directamente después de ​el comando chmod, indica cómo cambiar los permisos.
- ​Ahora mismo, esto puede parecer difícil de interpretar, ​pero pronto entenderemos por qué ​esto se llama modo simbólico.
- ​Previamente, aprendimos sobre los tres tipos ​de propietarios: usuario, grupo y otro.
- ​Para identificarlos con chmod, ​usamos u para representar al usuario, ​g para representar al grupo, ​y o para representar a otro.
- ​En este ejemplo concreto, ​`g` indica que haremos ​algunos cambios en los permisos de grupo, ​y `o` en los permisos para otros.
- Estos tipos de propietarios están separados ​por una coma en este argumento.
- ​¿Pero queremos añadir o quitar permisos?
- Pues bien, para ello, utilizamos operadores matemáticos.
- ​Así, el signo más después de `g` ​significa que queremos añadir permisos para grupo.
- ​El signo menos después de `o` ​significa que queremos quitárselos a otros.
- ​Y la última pregunta es: ¿qué tipo de cambios?
- ​Ya hemos aprendido que `r` representa permisos de lectura, ​`w` representa permisos de escritura, ​y `x` representa permisos de ejecución.
- Así que en este caso, la `w` indica ​que estamos añadiendo permisos de escritura al grupo, ​y la `r` indica que estamos quitando ​permisos de lectura a otros.
- ​Pero ahora que lo hemos desglosado, ​quizá ya no parezca ​tanto un idioma extranjero.
- ​​Empezaremos en el subdirectorio logs.
- ​Si utilizamos el comando `ls -l`, ​nos mostrará los permisos del archivo.
- ​Muestra los permisos del único archivo ​de este directorio: access.txt.
- ​Los caracteres segundo a cuarto ​indican que el usuario tiene permisos de lectura y escritura.
- ​Los caracteres quinto a séptimo ​muestran que el grupo sólo tiene permisos de lectura.
- ​Y los caracteres octavo a décimo muestran ​que otros sólo tienen permisos de lectura.
- ​Necesitamos ajustar estos permisos.
- ​Queremos asegurarnos de que los analistas en ​el grupo de seguridad tienen permiso de escritura, ​pero quitamos los permisos de lectura del propietario-tipo otro, ​así que añadimos permisos de escritura para ​el grupo y quitamos los permisos de lectura para otro.
- ​Volvamos a ejecutar `ls -l`.
- ​Esto muestra un cambio en los permisos para access.txt.
- ​Note cómo en el segmento medio ​de los permisos para el grupo, ​`w` se ha añadido para dar permisos de escritura.
- ​Y otro cambio es que ​se ha eliminado la `r` en el último segmento, ​indicando que se han eliminado los permisos de lectura ​para `other`.
- ​Como se mencionó anteriormente, estos guiones ​indican una falta de permisos.
- Ahora, `other` carece de todos los permisos.

---

## Comandos de permiso
- Permisos de lectura
   - En Linux, los permisos se representan con una cadena de 10 caracteres.
   - Los permisos incluyen:
      - leer: para archivos, esta es la capacidad de leer el contenido del archivo; para directorios, esta es la capacidad de leer todo el contenido en el directorio incluyendo tanto archivos como subdirectorios
      - escribir: para archivos, esta es la capacidad de hacer modificaciones en el contenido del archivo; para directorios, esta es la capacidad de crear nuevos archivos en el directorio
      - ejecutar: para los archivos, es la capacidad de ejecutar el archivo si se trata de un programa; para los directorios, es la capacidad de entrar en el directorio y acceder a sus archivos
   - Estos permisos se otorgan a estos tipos de propietarios:
      - usuario: el propietario del archivo
      - grupo: un grupo mayor del que forma parte el propietario
      - otro: todos los demás usuarios del sistema
   - Cada carácter de la cadena de 10 caracteres transmite información diferente sobre estos permisos.
   - La siguiente tabla describe el propósito de cada carácter:

| Carácter | Ejemplo | Significado |
| --- | --- | --- |
| 1° | drwxrwxrwx | tipo de archivo: `d` para un directorio `-` para un archivo regular |
| 2º | drwxrwxrwx | permisos de lectura para el usuario `r` si el usuario tiene permisos de lectura `-` si el usuario carece de permisos de lectura |
| 3º | drwxrwxrwx | permisos de escritura para el usuario `w` si el usuario tiene permisos de escritura `-` si el usuario carece de permisos de escritura |
| 4º | drwxrwxrwx | permisos de ejecución para el usuario `x` si el usuario tiene permisos de ejecución `-` si el usuario carece de permisos de ejecución |
| 5º | drwxrwxrwx | permisos de lectura para el grupo `r` si el grupo tiene permisos de lectura `-` si el grupo carece de permisos de lectura |
| 6º | drwxrwxrwx | permisos de escritura para el grupo `w` si el grupo tiene permisos de escritura `-` si el grupo carece de permisos de escritura |
| 7º | drwxrwxrwx | permisos de ejecución para el grupo `x` si el grupo tiene permisos de ejecución `-` si el grupo carece de permisos de ejecución |
| 8º | drwxrwxrwx | permisos de lectura para otros `r` si el otro tipo de propietario tiene permisos de lectura `-` si el otro tipo de propietario carece de permisos de lectura |
| 9º | drwxrwxrwx | permisos de escritura para otro `w` si el otro tipo de propietario tiene permisos de escritura `-` si el otro tipo de propietario carece de permisos de escritura |
| 10º | drwxrwxrwx | permisos de ejecución para otro `x` si el otro tipo de propietario tiene permisos de ejecución `-` si el otro tipo de propietario carece de permisos de ejecución |

- Exploración de los permisos existentes
   - Puede utilizar el comando `ls` para investigar quién tiene permisos sobre archivos y directorios.
   - Existen opciones adicionales que puede añadir al comando `ls` para que su comando sea más específico.
   - Algunas de estas opciones proporcionan detalles sobre los permisos.
   - He aquí algunas opciones de `ls` importantes para los analistas de Seguridad:
      - `ls -a`: Muestra los archivos ocultos. Los archivos ocultos comienzan con un punto (.) al principio.
      - `ls -l`: Muestra los permisos de archivos y directorios. También muestra otra información adicional, como el nombre del propietario, el grupo, el tamaño del archivo y la hora de la última modificación.
      - `ls -la`: Muestra los permisos de archivos y directorios, incluidos los archivos ocultos. Es una combinación de las otras dos opciones.
   
- Cambio de permisos
   - El principio de privilegio mínimo es el concepto de conceder sólo el acceso y la autorización mínimos necesarios para completar una tarea o función.
   - En otras palabras, los usuarios no deben tener privilegios que vayan más allá de lo necesario.
   - No seguir el principio de privilegio mínimo puede crear riesgos de Seguridad.
   - El comando chmod puede ayudarle a gestionar esta autorización.
   - El comando chmod cambia los permisos de archivos y directorios.

- Uso de chmod
   - El comando chmod requiere dos argumentos.
   - El primer argumento indica cómo cambiar los permisos, y el segundo argumento indica el archivo o directorio para el que desea cambiar los permisos.
   - Por ejemplo, el siguiente comando añadiría todos los permisos a login_sessions.txt:
   - `chmod u+rwx,g+rwx,o+rwx login_sessions.txt`
   - Si quisiera quitar todos los permisos, podría utilizar:
   - `chmod u-rwx,g-rwx,o-rwx login_sessions.txt`
   - Otra forma de asignar estos permisos es utilizar el signo igual (=) en este primer argumento.
   - El uso de `=` con chmod establece, o asigna, los permisos exactamente como se especifican.
   - Por ejemplo, el siguiente comando establecería permisos de lectura para login_sessions.txt para usuario, grupo y otros:
      - `chmod u=r,g=r,o=r login_sessions.txt`
   - Este comando sobrescribe los permisos existentes.
   - Por ejemplo, si el usuario tenía previamente permisos de escritura, estos permisos de escritura se eliminan después de que usted especifique sólo permisos de lectura con `=`
   - La siguiente tabla repasa cómo se utiliza cada carácter dentro del primer argumento de chmod:

| Carácter | Descripción |
| --- | --- |
| u | indica que se realizarán cambios en los permisos de usuario |
| g | indica que se realizarán cambios en los permisos de grupo |
| o | indica que se realizarán cambios en otros permisos |
| + | añade permisos al usuario, grupo u otro |
| - | elimina permisos del usuario, grupo u otro |
| = | asigna permisos al usuario, grupo u otro |

- Cuando hay cambios de permisos a más de un tipo de propietario, se necesitan comas para separar los cambios para cada tipo de propietario.
- No debe añadir espacios después de esas comas.

- El principio de privilegio mínimo en acción
- Como analista de Seguridad, puede encontrarse con una situación como la siguiente:
   - Hay un archivo llamado `bonuses.txt` dentro de un directorio de `compensación`.
   - El propietario de este archivo es un miembro del departamento de Recursos Humanos con el nombre de usuario hrrep1.
   - Se ha decidido que hrrep1 necesita acceder a este archivo.
   - Pero, como este archivo contiene información confidencial, nadie más del grupo hr necesita acceso.
- Usted ejecuta `ls -l` para comprobar los permisos de los archivos en el directorio de compensación y descubre que los permisos para `bonuses.txt` son `-rw-rw----`.
- El tipo de propietario del grupo tiene permisos de lectura y escritura que no se ajustan al principio de privilegio mínimo.
- Para remediar la situación, usted introduce `chmod g-rw bonuses.txt`.
- Ahora, sólo el usuario que necesita acceder a este archivo para llevar a cabo sus responsabilidades laborales puede acceder a este archivo.

---

## Actividad: Gestionar la autorización
- Introducción
   - En este laboratorio, aprenderá a examinar y gestionar los permisos de archivos.
   - Estas habilidades pueden utilizarse al configurar la autorización de usuarios.
   - Utilizará comandos Linux en el Shell Bash para completar este laboratorio.
   - Mientras completa este laboratorio por favor tome capturas de pantalla o anote los comandos que utiliza en el Shell Bash.
- Lo que hará
   - Comprobar los permisos de los archivos de un directorio
   - Comprobar si hay permisos de archivos incorrectos y cambiar los permisos según sea necesario
   - Eliminar el acceso no autorizado a un directorio
- Resumen de la actividad
   - En este lab, usarás comandos de Linux para configurar autorizaciones.
   - La autorización implica dar acceso a recursos específicos de un sistema.
   - Es un concepto importante porque, sin la autorización, cualquier usuario podría acceder a todos los archivos que pertenecen a otros usuarios o a archivos del sistema y modificarlos.
   - Sin dudas, se correrían riesgos de seguridad.
   - En Linux, se usan permisos de archivos y de directorios para especificar quién tiene acceso a archivos y directorios específicos.
   - Explorarás los permisos de archivos y de directorios, y cambiarás la propiedad de un archivo y un directorio para limitar quién puede acceder a ellos.
   - Como analista de seguridad, configurar permisos de acceso adecuados es fundamental para proteger información sensible y mantener la seguridad general de un sistema.
- Situación
   - En este caso, debes examinar y administrar los permisos de los archivos del directorio /home/researcher2/projects para el usuario researcher2.
   - El usuario researcher2 es parte del grupo research_team.
   - Debes verificar los permisos para todos los archivos del directorio, incluidos los archivos ocultos, para asegurarte de que coincidan con el grado de autorización que debería otorgarse.
   - De no ser así, debes cambiar los permisos.
   - Estos son los pasos que seguirás:
      1. Verificarás los permisos del usuario y el grupo para todos los archivos del directorio projects.
      2. Verificarás si algún archivo tiene permisos incorrectos y los modificarás según sea necesario.
      3. Verificarás los permisos del directorio /home/researcher2/drafts y los modificarás para quitar los accesos no autorizados.

- Comienza el lab

1. Verifica los detalles de archivos y directorios
- Navega hasta el directorio projects
- Obtén una lista del contenido y los permisos del directorio projects
- ¿Cómo se llama el grupo propietario de los archivos en el directorio projects?
   - [ ] other_users
   - [ ] security_team
   - [x] research_team
   - [ ] researcher2
- Verifica si existen archivos ocultos en el directorio projects
- ¿Cuál de estos archivos está oculto en el directorio projects?
   - [x] .project_x.txt
   - [ ] .project_r.txt
   - [ ] No hay archivos ocultos
   - [ ] .project_m.txt

2. Cambia los permisos de archivos
- Verifica si algún archivo del directorio projects tiene permisos de escritura para el tipo de propietario 'otro'
- ¿Qué archivo les otorga permisos de escritura a otros usuarios?
   - [ ] project_t.txt
   - [ ] project_m.txt
   - [x] project_k.txt
- Cambia los permisos del archivo que hayas identificado en el paso anterior, de modo que otros usuarios no tengan permisos de escritura.
- El archivo project_m.txt es restringido y nadie debería poder leerlo ni escribirlo, ni siquiera el grupo.
- Obtén una lista del contenido y los permisos del directorio actual y verifica si el grupo tiene permisos de lectura o escritura
- ¿Cuáles son los permisos grupales del archivo project_m.txt?
   - [ ] Lectura, escritura y ejecución
   - [ ] Lectura y escritura
   - [x] Solo lectura
- Usa el comando chmod para cambiar los permisos del archivo project_m.txt, de modo que el grupo no tenga permisos de escritura ni de lectura

3. Cambia los permisos de un archivo oculto
- Verifica los permisos del archivo oculto .project_x.txt y responde la siguiente pregunta
- ¿Qué tipo de propietario tiene permisos de escritura incorrectos?
   - [x] El usuario y el grupo
   - [ ] Solo el grupo
   - [ ] Solo el usuario
- Cambia los permisos del archivo .project_x.txt, de modo que tanto el usuario como el grupo puedan leerlo, pero no escribirlo

4. Cambia los permisos de un directorio
- Verifica los permisos del directorio drafts y responde la siguiente pregunta
- ¿El grupo tiene acceso al directorio drafts?
   - [x] Sí
   - [ ] No
- Quita el permiso de ejecución del grupo correspondiente al directorio drafts


- Listado de comandos utilizados en este laboratorio
```bash
pwd
ls -la projects/
chmod o-w projects/project_k.txt
ls -la projects/
ls -la projects/project_m.txt
chmod g-r projects/project_m.txt
ls -la projects/.project_x.txt
chmod u-w,g-w projects/.project_x.txt
chmod u+r,g+r projects/.project_x.txt
ls -la projects/.project_x.txt
chmod g-x drafts/
ls -la projects/drafts/
```

---

## Ejemplo opcional: Gestionar la autorización
- Mismo laboratorio que el anterior.