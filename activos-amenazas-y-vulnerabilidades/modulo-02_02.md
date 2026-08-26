# Métodos de encriptación

## Fundamentos de la criptografía
- ​Internet es un sistema abierto y público con una gran cantidad de datos que fluyen a través de él.
- ​Aunque todos enviamos y almacenamos información en línea, ​hay cierta información que decidimos mantener en privado.
- ​En materia de Seguridad, este tipo de datos se conoce como información de identificación personal.
- ​La información de identificación personal, o PII, ​es cualquier información que se puede usar para deducir la identidad de una persona.
- ​Esto puede incluir datos como el nombre de una persona, la ​información médica y financiera, las fotos, los correos electrónicos o las huellas dactilares.
- ​Mantener la privacidad de la PII en línea es difícil. Para ​ello se necesitan los controles de Seguridad adecuados.
- ​Uno de los principales controles de Seguridad que se utilizan para proteger la ​información en línea es la criptografía.
- ​La criptografía es el proceso de transformar la información en una forma que ​los lectores no deseados no puedan entender.
- ​Datos de cualquier tipo se mantienen en secreto mediante un proceso de dos pasos: ​encriptación para ocultar la información y desencriptación para mostrarla.
- ​Imagina enviar un correo electrónico a un amigo.
- ​El proceso comienza tomando los datos en su ​forma original y legible, conocida como texto plano.
- ​El cifrado toma esa información y la ​codifica en un formato ilegible, conocido como texto cifrado.
- ​Luego utilizamos la desencriptación para descifrar el texto cifrado y convertirlo en texto plano, haciéndolo legible nuevamente.
- ​Ocultar y mostrar información privada es una práctica que existe desde hace mucho tiempo.
- ​Uno de los primeros métodos criptográficos se conoce como el cifrado de César.
- ​Este método lleva el nombre de un general romano, Julio César, ​que gobernó el imperio romano cerca del final del siglo I a.C.
- La ​usó para mantener en privado los mensajes entre él y sus generales militares.
- ​El cifrado de César es un algoritmo bastante simple que funciona desplazando las letras ​del alfabeto romano hacia adelante en un número fijo de espacios.
- ​Un algoritmo es un conjunto de reglas que resuelven un problema.
- ​Específicamente en criptografía, un cifrado es un algoritmo que cifra la información.
- ​Por ejemplo, un mensaje codificado con el sistema de cifrado de César con un desplazamiento de 3 codificaría ​una A como una D, una B como una E, una C como una F, etc.
- ​En este ejemplo, puedes enviar a un amigo un mensaje que diga «hola» ​con un turno de 3 y que diga «khoor».
- ​Ahora, tal vez se pregunte cómo puede saber el cambio que ​utiliza un mensaje cifrado con el sistema de cifrado de César.
- La respuesta a eso es: ¡necesitas la clave!
- ​Una clave criptográfica es un mecanismo que descifra el texto cifrado.
- ​En nuestro ejemplo, la clave indicaría que mi mensaje está cifrado en 3 turnos.
- ¡ ​Con esa información, puedes desbloquear el mensaje oculto!
- Todas las formas de encriptación se basan tanto en un cifrado como en una ​clave para garantizar el intercambio de información.
- ​El cifrado de César no se usa ampliamente en la actualidad debido a un par de defectos importantes.
- ​Una se refiere al código en sí.
- La otra se refiere a la clave.
- ​Este sistema de cifrado en particular se basa completamente en los caracteres del alfabeto romano para ocultar la ​información.
- ​Por ejemplo, piense en un mensaje escrito con el alfabeto inglés, que solo tiene 26 ​caracteres.
- ​Incluso sin la clave, es bastante sencillo descifrar un mensaje protegido con el sistema de ​cifrado de César desplazando las letras de 26 maneras diferentes.
- ​En seguridad de la información, esta táctica se conoce como ataque de fuerza bruta, ​un proceso de prueba y error para descubrir información privada.
- ​El otro gran defecto del sistema de cifrado de César es que se basa en una sola clave.
- ​Si esa clave se perdió o fue robada, ​no hay nada que impida que alguien acceda a la información privada.
- ​Realizar un seguimiento adecuado de las claves criptográficas es una parte importante de la Seguridad.
- ​Para empezar, es importante asegurarse de que estas claves no se almacenen en lugares públicos ​y compartirlas por separado de la información que van a descifrar.
- ​El cifrado de César es solo uno de los muchos algoritmos que se utilizan para proteger la ​privacidad de las personas.

---

## Infraestructura de clave pública
- ​Las computadoras usan muchos ​algoritmos de encriptación para ​enviar y almacenar información en línea.
- ​Todas son útiles cuando se trata de ocultar ​información privada, pero solo ​mientras sus claves estén protegidas.
- ​¿Te imaginas tener que llevar ​un registro de las claves ​de encriptación que protegen toda tu información personal en línea?
- Yo tampoco puedo, ​y no tenemos que hacerlo, gracias a algo que se conoce ​como infraestructura de clave pública.
- ​Infraestructura de clave pública, o PKI, ​es un marco de encriptación ​que asegura el intercambio de información en línea.
- ​Es un sistema amplio que hace que el acceso a la ​información sea rápido, fácil y seguro.
- ​Entonces, ¿cómo funciona todo?
- ​La PKI es un proceso de dos pasos.
- Todo comienza con el intercambio de información cifrada.
- ​Esto implica la encriptación asimétrica, la ​encriptación simétrica o ambas.
- La ​encriptación asimétrica implica el uso de ​un par de claves públicas y privadas para la encriptación ​y desencriptación de datos.
- ​Imaginemos esto como una caja que ​se puede abrir con dos llaves.
- ​Una clave, la clave pública, ​solo se puede usar para acceder a ​la ranura y añadir objetos a la caja.
- ​Como la clave pública no se puede usar para eliminar elementos, ​se puede copiar y compartir con personas de ​todo el mundo para agregar elementos.
- ​Por otro lado, la segunda clave, la clave privada, ​abre la caja por completo, de modo que ​se pueden quitar los elementos que contiene.
- ​Solo el propietario de la caja tiene ​acceso a la clave privada que la desbloquea.
- El ​uso de una clave pública permite que ​las personas y los servidores con los que te estás comunicando ​vean y te envíen ​información cifrada que solo tú ​puedes descifrar con tu clave privada.
- ​Este sistema de dos claves convierte la ​criptografía asimétrica en una forma segura de ​intercambiar información en línea; ​sin embargo, también ralentiza el proceso.
- ​El Cifrado simétrico, por otro lado, ​es un enfoque más rápido y sencillo para la administración de claves.
- El ​cifrado simétrico implica el uso de ​una única clave secreta para intercambiar información.
- ​Imaginemos de nuevo la caja cerrada.
- ​En lugar de dos claves, la ​encriptación simétrica usa la misma clave.
- ​El propietario puede usarla para abrir la caja, añadir elementos ​y volver a cerrarla.
- Cuando quieren compartir el acceso, ​pueden dar la clave secreta a ​cualquier otra persona para que haga lo mismo.
- ​El intercambio de una única clave secreta ​puede hacer que las comunicaciones web sean más rápidas, ​pero también las hace menos seguras.
- ​La PKI utiliza tanto la encriptación asimétrica como la simétrica, ​a veces en conjunto.
- ​Todo depende de si la velocidad ​o la Seguridad son la prioridad.
- ​Por ejemplo, las aplicaciones de chat móvil ​utilizan criptografía asimétrica ​para establecer una conexión entre las personas ​al inicio de una conversación ​cuando la Seguridad es la prioridad.
- ​Posteriormente, cuando la velocidad de ​las comunicaciones de ida y vuelta es la prioridad, la ​encriptación simétrica toma el relevo.
- ​Si bien ambos tienen sus propias fortalezas y debilidades, ​comparten una vulnerabilidad común, que ​establece la confianza entre el remitente y el receptor.
- ​Ambos procesos se basan en compartir claves que ​pueden usarse indebidamente, perderse o robarse. 
- Esto no es un problema cuando ​intercambiamos información en persona porque ​podemos usar nuestros sentidos para diferenciar entre ​aquellos en quienes confiamos y aquellos en quienes no confiamos. 
- Las computadoras, por otro lado, ​no están naturalmente equipadas para hacer esta distinción.
- ​Ahí es donde se aplica el segundo paso de la PKI.
- ​La PKI aborda la vulnerabilidad del ​intercambio de claves al establecer la ​confianza mediante un sistema de ​certificados digitales entre ordenadores y redes.
- ​Un certificado digital es un archivo que ​verifica la identidad del titular de una clave pública.
- ​La mayor parte de la información en línea se ​intercambia mediante certificados digitales.
- ​Los usuarios, las empresas y ​las redes mantienen una y la intercambian ​cuando comunican información en línea ​como una forma de demostrar confianza.
- ​Veamos un ejemplo de cómo ​se crean los certificados digitales.
- ​Supongamos que una empresa en línea está a punto de lanzar ​su sitio web y quiere ​obtener un certificado digital.
- ​Cuando registran su dominio, ​la empresa de alojamiento envía cierta información ​a una autoridad certificadora (CA) de confianza.
- ​La información proporcionada suele ser básica, como ​el nombre de la empresa y el país ​donde se encuentra su sede.
- ​También se proporciona una clave pública para el sitio.
- A ​continuación, la autoridad certificadora ​utiliza estos datos para verificar la identidad de la empresa.
- ​Cuando se confirma, la CA ​cifra los datos con su propia clave privada.
- ​Por último, crean un certificado digital ​que contiene los datos cifrados de la empresa.
- ​También contiene la firma digital de CA ​para demostrar que es auténtica.
- ​Los certificados digitales se parecen mucho a una tarjeta de identificación digital ​que se usa en línea para restringir o ​conceder el acceso a la información.
- ​Así es como PKI resuelve el problema de la confianza.
- ​Combinado con la ​encriptación asimétrica y simétrica, ​este enfoque de dos pasos para intercambiar ​información segura entre fuentes confiables es lo ​que hace que la PKI sea un control de seguridad tan útil. 

---

## Cifrado simétrico y asimétrico
- Toda la información digital merece mantenerse privada, segura y protegida.
- El cifrado es una de las claves para conseguirlo.
- Sirve para transformar la información en una forma que los destinatarios no deseados no puedan entender.
- En esta lectura, compararás la criptografía simétrica y la asimétrica y conocerás algunos algoritmos conocidos de cada una de ellas.

- Tipos de cifrado
   - Existen dos tipos principales de cifrado:
      - Cifrado simétrico:
         - Consiste en utilizar una única clave secreta para intercambiar información.
         - Como utiliza una sola clave para cifrar y descifrar, el emisor y el receptor deben conocer la clave secreta para bloquear o desbloquear el cifrado.
      - Cifrado asimétrico:
         - Consiste en utilizar un par de claves pública y privada para cifrar y descifrar datos.
         - Utiliza dos claves distintas: una pública y otra privada.
         - La clave pública se utiliza para cifrar los datos y la privada para descifrarlos.
         - La clave privada sólo se entrega a los usuarios con acceso autorizado.

- La importancia de la longitud de la clave
   - Los cifradores son vulnerables a los ataques de fuerza bruta, que utilizan un proceso de ensayo y error para descubrir información privada.
   - Esta táctica es el equivalente digital de probar todos los números de una cerradura de combinación intentando dar con el correcto.
   - En el cifrado moderno, las longitudes de la clave más largas se consideran más seguras.
   - Una longitud de la clave más larga significa más posibilidades de que un atacante intente descifrar un cifrado.
   - Uno de los inconvenientes de tener claves de cifrado largas es que los tiempos de procesamiento son más lentos.
   - Aunque las longitudes de la clave cortas suelen ser menos seguras, su cálculo es mucho más rápido.
   - Proporcionar una comunicación de datos rápida en línea y, al mismo tiempo, mantener la seguridad de la información es un delicado ejercicio de equilibrio.

- Algoritmos aprobados
   - Muchas aplicaciones web utilizan una combinación de criptografía asimétrica y simétrica.
   - Así equilibran la experiencia del usuario con la salvaguarda de la información.
   - Como analista, debe conocer los algoritmos más utilizados.

- Algoritmos simétricos
   - Triple DES (3DES) se conoce como algoritmo de cifrado por bloques por la forma en que convierte el texto plano en texto cifrado en "bloques".
   - Sus orígenes se remontan al Data Encryption Standard (DES), desarrollado a principios de la década de 1970.
   - DES fue uno de los primeros algoritmos de encriptación simétrica que generaba claves de 64 bits, aunque sólo se utilizan 56 bits para la encriptación.
   - Un bit es la unidad más pequeña de medida de datos en un ordenador.
   - Como se puede imaginar, Triple DES genera claves tres veces más largas. Triple DES aplica el algoritmo DES tres veces, utilizando tres claves diferentes de 56 bits.
   - El resultado es una longitud de la clave efectiva de 168 bits.
   - A pesar de que las claves son más largas, muchas organizaciones están dejando de utilizar Triple DES debido a las limitaciones en la cantidad de datos que pueden cifrarse.
   - Sin embargo, es probable que Triple DES siga utilizándose por motivos de retrocompatibilidad.

- Estándar de encriptación avanzada (AES)
   - Es uno de los algoritmos simétricos más seguros de la actualidad.
   - AES genera claves de 128, 192 o 256 bits.
   - Se considera que las claves criptográficas de este tamaño están a salvo de ataques de fuerza bruta.
   - Se calcula que forzar una clave AES de 128 bits podría llevarle a un ordenador moderno miles de millones de años

- Algoritmos asimétricos
   - Rivest Shamir Adleman (RSA) debe su nombre a sus tres creadores, que lo desarrollaron en el Instituto Tecnológico de Massachusetts (MIT).
   - RSA es uno de los primeros algoritmos de criptografía asimétrica que produce un par de claves pública y privada.
   - Los algoritmos asimétricos como RSA producen longitudes de la clave aún más largas.
   - En parte, esto se debe al hecho de que estas funciones crean dos claves.
   - Los tamaños de la clave RSA son de 1.024, 2.048 o 4.096 bits.
   - RSA se utiliza principalmente para proteger datos muy sensibles.

- Algoritmo de firma digital (DSA)
   - Es un algoritmo asimétrico estándar que introdujo el NIST a principios de la década de 1990.
   - DSA también genera longitudes de la clave de 2.048 bits.
   - Este algoritmo se utiliza mucho hoy en día como complemento de RSA en infraestructuras de clave pública.

- Generación de claves
   - Estos algoritmos deben implementarse cuando una organización elige uno para proteger sus datos.
   - Una forma de hacerlo es utilizando OpenSSL, que es una herramienta de línea de comandos de código abierto que puede utilizarse para generar claves públicas y privadas.
   - OpenSSL se utiliza habitualmente en ordenadores para verificar certificados digitales que se intercambian como parte de la Infraestructura de clave pública.
   - OpenSSL es sólo una opción.
   - Hay varias otras disponibles que pueden generar claves con cualquiera de estos algoritmos comunes.
   - A principios de 2014, OpenSSL reveló una vulnerabilidad, conocida como el [bug Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), que exponía datos sensibles en la memoria de sitios web y aplicaciones.
   - Aunque todavía existen versiones no parcheadas de OpenSSL, el fallo Heartbleed fue parcheado a finales de ese mismo año (2014).
   - En la actualidad, muchas empresas utilizan las versiones seguras de OpenSSL para generar claves públicas y privadas, lo que demuestra la importancia de utilizar software actualizado.

- La oscuridad no es seguridad
   - En el mundo de la criptografía, hay que demostrar que un cifrado es indescifrable antes de afirmar que es seguro.
   - Según [el principio de Kerckhoffs](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle), la criptografía debe diseñarse de forma que todos los detalles de un algoritmo -excepto la clave privada- sean conocibles sin sacrificar su seguridad.
   - Por ejemplo, se puede acceder en línea a todos los detalles sobre el funcionamiento del cifrado AES y, sin embargo, sigue siendo indescifrable.
   - En ocasiones, las organizaciones implementan sus propios algoritmos de encriptación personalizados.
   - Ha habido casos en los que esos sistemas criptográficos secretos han sido rápidamente descifrados tras hacerse públicos.
   - Un sistema criptográfico no debe considerarse seguro si requiere que se mantenga en secreto su funcionamiento.

- El cifrado está en todas partes
   - Las empresas utilizan tanto la criptografía simétrica como la asimétrica.
   - A menudo trabajan en equipo, equilibrando la seguridad con la experiencia del usuario.
   - Por ejemplo, los sitios web tienden a utilizar la criptografía asimétrica para proteger pequeños bloques de datos que son importantes.
   - Los nombres de usuario y las contraseñas suelen protegerse con criptografía asimétrica mientras se procesan las solicitudes de acceso.
   - Una vez que el usuario obtiene acceso, el resto de su sesión web suele pasar a utilizar cifrado simétrico por su rapidez.
   - La ley exige cada vez más el uso de este tipo de cifrado de datos.
   - Reglamentos como el Federal Information Processing Standard (FIPS 140-3) y el Reglamento General de Protección de Datos (GDPR) describen cómo deben recopilarse, utilizarse y manejarse los datos.
   - Lograr el cumplimiento de cualquiera de estas normativas es fundamental para demostrar a los socios comerciales y a los gobiernos que los datos de los clientes se manejan de forma responsable.

---

## Recursos para completar los laboratorios
- Iniciar Qwiklabs
- Botón Start Lab
- El temporizador
- Botón Abrir Consola Linux
- Comprobar el progreso

---

## Consejos de laboratorio y pasos para la solución de problemas
- Requisito de edad de 18+ para utilizar la plataforma
- Compatibilidad del navegador: última versión de Google Chrome, Firefox o Microsoft Edge
- Conexión a Internet

---

## Actividad: Desencriptación de un mensaje encriptado
- Introducción
   - En este laboratorio, completará una serie de tareas para obtener instrucciones para la desencriptación de un archivo encriptado.
   - La encriptación de los Datos en uso, en reposo y en tránsito es fundamental para las funciones de Seguridad.
   - Utilizará las habilidades de Linux que ha aprendido para descubrir las pistas necesarias para descifrar un cifrado clásico, restaurar un archivo y revelar un mensaje oculto.
   
- Lo que hará
   - Listar el contenido de un Directorio
   - Leer el contenido de archivos
   - Usar comandos de Linux para revertir un cifrado clásico a texto plano
   - Desencriptar un archivo encriptado y restaurar el archivo a su estado original

- Resumen de actividad
   - Anteriormente, aprendiste sobre criptografía y cómo se pueden usar la encriptación y desencriptación para asegurar información en línea.
   - También conociste el algoritmo de cifrado Caesar, uno de los primeros algoritmos criptográficos utilizados para proteger la privacidad de las personas.
   - Como analista de seguridad, es importante que entiendas el rol de la encriptación para asegurar datos en línea y que conozcas los controles de seguridad adecuados para hacerlo.
   
- Situación
   - En esta situación, todos los archivos de tu directorio principal están encriptados.
   - Deberás usar comandos de Linux para romper el algoritmo de cifrado Caesar y desencriptar los archivos, de modo que puedas leer los mensajes ocultos que contienen.
   - Estos son los pasos que seguirás:
      1. Explorarás el contenido del directorio principal y leerás el contenido de un archivo.
      2. Encontrarás un archivo oculto y desencriptarás el algoritmo de cifrado Caesar que contiene.
      3. Desencriptarás el archivo de datos encriptado para recuperar los datos y revelar el mensaje oculto.

- Comienza el lab

1. Lee el contenido de un archivo
- Usa el comando ls para enumerar los archivos del directorio de trabajo actual.
```bash
ls -la
# -rw-r--r-- 1 root    root     260 Aug 26 02:59 Q1.encrypted
# -rw-r--r-- 1 root    root     165 Aug 26 02:59 README.txt
# drwxr-xr-x 2 root    root    4096 Aug 26 02:59 caesar
```
- Usa el comando cat para mostrar el contenido del archivo README.txt.
```bash
cat README.txt
# Hello,
# All of your data has been encrypted. To recover your data, you will need to solve a cipher. To get started look for a hidden file in the caesar subdirectory
```

2. Encuentra un archivo oculto
- Primero, usa el comando cd para cambiar al subdirectorio caesar de tu directorio principal.
```bash
cd caesar
```
- Usa el comando ls -a para enumerar todos los archivos, incluidos los ocultos, en tu directorio principal.
```bash
ls -la
# -rw-r--r-- 1 root    root     160 Aug 26 02:59 .leftShift3
```
- Usa el comando cat para mostrar el contenido del archivo .leftShift3
```bash
cat .leftShift3
# Lq rughu wr uhfryhu brxu ilohv brx zloo qhhg wr hqwhu wkh iroorzlqj frppdqg:
# rshqvvo dhv-256-fef -sengi2 -d -g -lq T1.hqfubswhg -rxw T1.uhfryhuhg -n hwwxeuxwh
```
- Al parecer, el mensaje del archivo .leftShift3 está desordenado. Esto se debe a que los datos se encriptaron mediante un algoritmo de cifrado Caesar. Este algoritmo de cifrado se puede resolver moviendo cada carácter del alfabeto hacia la izquierda o la derecha una cantidad específica de espacios. En este ejemplo, el cambio consiste en tres letras hacia la izquierda. Por lo tanto, "d" significa "a" y "e" significa "b".
- Puedes desencriptar el algoritmo de cifrado Caesar del archivo .leftshift3 usando el siguiente comando
```bash
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
# In order to recover your files you will need to enter the following command:
# openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```
- En este caso, el comando tr "d-za-cD-ZA-C" "a-zA-Z" traduce todas las letras en mayúsculas y minúsculas del alfabeto a su posición original. El grupo de caracteres, indicado como "d-za-cD-ZA-C", se traduce a un segundo grupo de caracteres, que es "a-zA-Z".

>[!NOTE] El comando tr traduce texto de un grupo de caracteres a otro, usando una asignación. El primer parámetro del comando tr representa el grupo de caracteres de entrada y el segundo representa el grupo de caracteres del resultado. Por lo tanto, si proporcionas parámetros "abcd" y "pqrs", y la cadena de entrada del comando tr es "ac", la cadena del resultado será "pr".

- Ahora, regresa a tu directorio principal antes de completar la siguiente tarea:
```bash
cd ~
```

3. Desencripta un archivo
- Usa el comando exacto que revelaste en la tarea anterior para desencriptar el archivo encriptado:
```bash
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```
- En este caso, el comando openssl revierte la encriptación del archivo con un algoritmo de cifrado simétrico seguro, como indica AES-256-CBC.
- La opción -pbkdf2 se usa para aumentar la seguridad a la clave y -a indica la codificación deseada para el resultado.
- El comando -d indica la desencriptación, mientras que -in especifica el archivo de entrada y -out especifica el archivo de salida.
- La opción -k especifica la contraseña, que en este ejemplo es ettubrute.
- Usa el comando ls para mostrar nuevamente el contenido de tu directorio principal actual.
```bash
ls -la
```
- Usa el comando cat para mostrar el contenido del archivo Q1.recovered.
```bash
cat Q1.recovered
# If you are able to read this, then you have successfully decrypted the classic cipher text. You recovered the encryption key that was used to encrypt this file. Great work!
```

---

## Ejemplo opcional: Desencriptación de un mensaje encriptado
- Mismo laboratorio que el anterior.

---

## Ejemplo: Descifrar un mensaje cifrado
- Se solicita listar el directorio del usuario analyst y leer el contenido del archivo README.txt. 
- El contenido de README.txt indica que todos los datos han sido encriptados y que para recuperarlos se debe resolver un cifrado dentro del subdirectorio `caesar`.
- Entramos al directorio y vemos un archivo oculto `.leftShift3`.
- Al leer el contenido de `.leftShift3`, se observa un mensaje encriptado con un cifrado César que indica cómo recuperar los archivos.
- Se utiliza el comando `tr` para descifrar el mensaje, revelando el comando necesario para desencriptar el archivo `Q1.encrypted`.
- Volvemos al home del usuario y ejecutamos el siguiente comando:
- `openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute`
   - `openssl`: Utiliza la herramienta OpenSSL para desencriptar el archivo.
   - `aes-256-cbc`: Especifica el algoritmo de cifrado simétrico AES con una longitud de clave de 256 bits y el modo CBC.
   - `-pbkdf2`: Indica que se debe usar la función de derivación de clave PBKDF2 para aumentar la seguridad.
   - `-a`: Indica que la entrada y salida están codificadas en base64.
   - `-d`: Indica que se debe realizar la desencriptación.
   - `-in Q1.encrypted`: Especifica el archivo de entrada que se desea desencriptar.
   - `-out Q1.recovered`: Especifica el archivo de salida donde se guardará el contenido desencriptado.
   - `-k ettubrute`: Proporciona la contraseña utilizada para desencriptar el archivo.
- Al ejecutar este comando, se desencripta el archivo `Q1.encrypted` y se guarda el contenido en `Q1.recovered`.
- Al revisar el contenido de `Q1.recovered`, se confirma que la desencriptación fue exitosa y se recuperó la clave de encriptación utilizada para cifrar el archivo.

---

## No repudio y hash
- ​Los profesionales de la seguridad siempre ​piensan en las vulnerabilidades.
- Es la forma de anticiparnos a las amenazas. 
- Hemos pasado algún tiempo juntos explorando un par de formas de encriptación.
- ​Los dos tipos que hemos analizado producen claves que se comparten ​al comunicar información.
- ​Las claves de cifrado son vulnerables a la pérdida o al robo, ​lo que puede poner en riesgo la información confidencial.
- ​Exploremos otro control de Seguridad que ayuda a las empresas a abordar esta ​debilidad.
- ​Una función hash es un algoritmo que produce un código que no se puede descifrar.
- ​A diferencia de los algoritmos asimétricos y simétricos, ​las funciones hash son procesos unidireccionales que no generan claves de desencriptación.
- ​En cambio, estos algoritmos producen un identificador único conocido como valor hash o ​resumen.
- ​He aquí un ejemplo para demostrarlo. ​Imagine que una empresa tiene una aplicación interna que utilizan los empleados y que ​se almacena en una unidad compartida. ​Tras pasar por una función de hash, el programa recibe su valor hash. ​Por ejemplo, ​creamos este valor de hash relativamente corto con la función de hash MD5. ​En general, se prefieren las funciones hash estándar que producen hashes más largos por ​ser más seguras. 
​A continuación, imaginemos que un atacante reemplaza el programa por ​una versión modificada que realiza acciones maliciosas. ​El programa malintencionado puede funcionar igual que el original. ​Sin embargo, si una línea de código es tan diferente de la original, ​generará un valor hash diferente. ​Al comparar los valores de hash, podemos validar que los programas son diferentes. ​Los atacantes utilizan este tipo de trucos con frecuencia porque es fácil pasarlos por alto. ​Afortunadamente, los valores hash nos ayudan a identificar cuándo ocurre algo así. ​En Seguridad, los hashes se utilizan principalmente como una forma de ​determinar la integridad de los archivos y las aplicaciones. 
​La integridad de los datos se refiere a la precisión y la coherencia de la información. ​Esto se conoce como no repudio, ​el concepto de que no se puede negar la autenticidad de la información. ​Las funciones hash son controles de Seguridad importantes que permiten demostrar la integridad de los datos ​. Los analistas las utilizan con frecuencia. ​Una forma de hacerlo es encontrar el valor hash de los archivos o ​aplicaciones y compararlos con los archivos maliciosos conocidos. ​Por ejemplo, podemos usar la línea de comandos de Linux para generar el valor hash de ​cualquier archivo de su computadora. ​Simplemente lanzamos una shell y escribimos el nombre del algoritmo de hash que queremos usar. 
​En este caso, estamos usando uno común conocido como sha256. ​A continuación, necesitamos introducir el nombre de cualquier archivo que queramos procesar. ​Vamos a analizar el contenido de newfile.txt. ​Ahora, presionaremos Entrar. ​La terminal genera este valor hash único para el archivo. ​Estas herramientas se pueden comparar con los valores de hash de los virus en línea conocidos. ​Una de esas bases de datos es VirusTotal. 
​Esta es una herramienta popular entre los profesionales de Seguridad que es útil para analizar ​archivos, dominios, IP y URL sospechosos. ​Como hemos explorado, incluso el más mínimo cambio en la entrada da como resultado un ​valor de hash totalmente diferente. ​Las funciones hash se diseñan intencionalmente de esta manera para ayudar en cuestiones de no repudio. ​Proporcionan a los ordenadores una forma rápida y sencilla de comparar los ​valores de entrada y salida y de validar la integridad de los datos. ​Bastante guay, ¿verdad? 