# Introducción a las funciones

## Bienvenido al Módulo 2
- ​Empezamos desde el principio ​entendiendo cómo utilizan Python los analistas de seguridad.
- ​Aprendimos varios bloques de construcción de Python.
- ​Entramos en detalle aprendiendo sobre tipos de datos, ​variables y sentencias básicas.
- ​Ahora, añadiremos a esto y aprenderemos ​más sobre cómo escribir secuencias de comandos de Python eficaces.
- ​Descubriremos formas en las que podemos hacer ​nuestros esfuerzos más eficientes.
- ​Los próximos vídeos van a comenzar introduciendo ​las funciones, que son muy importantes en Python. ​Las funciones nos permiten reunir un conjunto ​de instrucciones que podemos usar ​una y otra vez en nuestro código.
- ​Después, vamos a aprender ​sobre los módulos y bibliotecas de Python, ​que incluyen colecciones de ​funciones y tipos de datos que podemos usar con Python.
- ​Nos ayudan a tener acceso a ​funciones sin tener que crearlas nosotros mismos.
- ​Por último, vamos a hablar de ​una de las reglas más importantes de la programación, ​y es la legibilidad del código.
- ​Aprenderemos todas las formas de ​asegurarnos de que todo el mundo pueda entender y trabajar con su código.

---

## Introducción a las funciones
- ​A medida que aumenta la complejidad de nuestros programas, ​también es probable que reutilicemos las mismas líneas de código.
- ​Escribir este código varias veces ​nos llevaría mucho tiempo, pero por suerte ​tenemos una forma de gestionarlo.
- ​Podemos utilizar funciones. ​Una función es una sección ​de código que puede reutilizarse en un programa.
- ​Ya aprendimos una función cuando trabajamos con ​print y la utilizamos para mostrar en pantalla los datos especificados.
- ​Por ejemplo, imprimimos "Hola Python".
- ​Existen muchas otras funciones.
- ​A veces, necesitamos automatizar una tarea que ​de otro modo podría ser repetitiva si la hiciéramos manualmente.
- ​Previamente, comparamos ​otros componentes clave de Python con los elementos de una cocina.
- ​Comparamos los tipos de datos con las categorías de alimentos.
- ​Existen diferencias en cómo manejamos ​las verduras y la carne, y del mismo modo, ​existen diferencias en cómo ​manejamos los distintos tipos de datos.
- ​Después hablamos de cómo las variables son ​como los recipientes en los que se pone la comida después de comer; ​lo que contienen puede cambiar.
- ​En cuanto a las funciones, ​podemos pensar en ellas como en un lavavajillas.
- ​Si no utiliza un lavavajillas, ​pasará mucho tiempo lavando cada plato por separado.
- ​Pero un lavavajillas automatiza ​esto y le permite lavarlo todo de una vez.
- ​De forma similar, las funciones mejoran la eficiencia.
- ​Realizan actividades repetitivas ​dentro de un programa y le permiten trabajar con eficacia.
- ​Las funciones están hechas para ser reutilizadas en nuestros programas.
- ​Consisten en pequeñas instrucciones y pueden ser llamadas ​cualquier número de ​veces y desde cualquier parte de nuestros programas.
- ​Otro beneficio de las funciones es ​que si alguna vez tuviéramos que hacer cambios en ellas, ​podemos hacer esos cambios directamente en la función, ​y se aplicarán en todas partes donde las usemos.
- ​Esto es mucho mejor que hacer ​los mismos cambios en ​muchos lugares diferentes dentro de un programa.
- ​La función print() es un ejemplo de función integrada.
- ​Las funciones integradas son funciones que ​existen dentro de Python y que se pueden llamar directamente.
- ​Están a nuestra disposición por defecto.
- ​También podemos crear nuestras propias funciones.
- ​Las funciones definidas por el usuario son funciones que ​los programadores diseñan para sus necesidades específicas.
- ​Ambos tipos de funciones son ​como miniprogramas dentro de un programa más grande.
- ​Hacen que trabajar en Python sea mucho ​más efectivo y eficiente. 

---

## Crear una función básica
- Comencemos nuestra exploración de ​las funciones definidas por el usuario creando ​y luego ejecutando una función muy simple.
- ​Lo primero que tenemos que hacer ​es definir nuestra función.
- ​Cuando definimos una función, ​básicamente le decimos a Python que existe.
- ​Para ello se necesita la palabra clave def.
- ​def se coloca antes del ​nombre de una función para definir una función.
- ​Vamos a crear una función que ​salude a los empleados después de iniciar sesión.
- ​En primer lugar, ​comentaremos lo que queremos hacer con este código.
- ​Queremos definir una función.
- ​Ahora, iremos a una nueva línea y ​usaremos la palabra clave def para asignar un nombre a nuestra función.
- Lo ​llamaremos greet_employee.
- ​Veamos esta sintaxis un poco más de cerca.
- ​Después de nuestra palabra clave def y ​el nombre de la función, colocamos paréntesis.
- ​Más adelante, exploraremos cómo agregar ​información entre paréntesis, ​pero para esta sencilla función, ​no necesitamos agregar nada.
- ​Además, al igual que hicimos con ​las sentencias condicionales e iterativas, ​agregamos dos puntos al final de este encabezado.
- ​Después de los dos puntos, ​indicaremos lo que hará la función.
- ​En nuestro caso, queremos que la función ​genere un mensaje una vez que el empleado inicie sesión.
- ​Así que sigamos creando nuestra función ​y dígale a Python que imprima esta cadena.
- ​Esta línea está indentada porque forma parte de esta función.
- ​Entonces, ¿qué pasa si ejecutamos este código?
- ​¿Imprime nuestro mensaje? Probemos esto. ​No lo hace.
- ​Esto se debe a que también tienes que llamar a tu función.
- ​Puede que no te des cuenta, ​pero ya tienes experiencia en llamar a funciones.
- ​La impresión es una función integrada a la ​que hemos llamado muchas veces.
- ​Así que para llamar a greet_employee, haremos algo similar.
- ​Vamos con una nueva línea.
- ​Vamos a añadir otro comentario ​porque ahora nuestro propósito es llamar a nuestra función.
- ​Y luego, llamaremos a la función greet_employee.
- ​Lo volveremos a ejecutar.
- ​Esta vez imprimió nuestro mensaje de bienvenida.
- ​¡Gran trabajo! Ahora hemos definido y llamado a una función.
- [file example](./resources/code/modulo-02_01-001.py)

---

## Funciones de Python en ciberseguridad
- Funciones en ciberseguridad
   - Una función es una sección de código que puede ser reutilizada en un programa.
   - Las funciones son importantes en Python porque te permiten automatizar partes repetitivas de tu código.
   - En ciberseguridad, es probable que adoptes algunos procesos que repetirás a menudo.
   - Cuando trabajes con registros de seguridad, a menudo te encontrarás con tareas que necesitan ser repetidas.
   - Por ejemplo, si fueras responsable de encontrar actividad de inicio de sesión maliciosa basada en intentos de inicio de sesión fallidos, podrías tener que repetir el proceso para múltiples registros.
   - Para evitarlo, puedes definir una función que tome un registro como entrada y devuelva todos los inicios de sesión potencialmente maliciosos.
   - Sería fácil aplicar esta función a diferentes registros.

- Definir una función
   - En Python, trabajarás con funciones integradas y funciones definidas por el usuario.
   - Funciones integradas son funciones que existen dentro de Python y pueden ser llamadas directamente.
   - La función print() es un ejemplo de función integrada.
   - Funciones definidas por el usuario son funciones que los programadores diseñan para sus necesidades específicas.
   - Para definir una función, necesitas incluir una cabecera de función y el cuerpo de tu función.

- Cabecera de la función
   - La cabecera de la función es lo que indica a Python que estás empezando a definir una función.
   - Por ejemplo, si quieres definir una función que muestre un mensaje "investigate activity", puedes incluir esta cabecera de función:
      - `def display_investigation_message():`
   - La palabra clave def se coloca antes del nombre de una función para definirla.
   - En este caso, el nombre de esa función es display_investigation_message.
   - Los paréntesis que siguen al nombre de la función y los dos puntos (:) al final de la cabecera de la función son también partes esenciales de la sintaxis.
   - Cuando nombres una función, dale un nombre que indique lo que hace.
   - Esto hará que sea más fácil de recordar cuando la llame más tarde.

- Cuerpo de la función
   - El cuerpo de la función es un bloque de código con sangría que aparece después de la cabecera de la función y que define lo que hace la función.
   - La sangría es muy importante cuando se escribe una función porque separa la definición de una función del resto del código.
   - Para añadir un cuerpo a su definición de la función display_investigation_message(), añada una línea sangrada con la función print().
   - Su definición de función se convierte en lo siguiente:
   - [file](resources/code/modulo-02_01-002.py)

- Llamada a una función
   - Después de definir una función, puedes utilizarla tantas veces como necesites en tu código.
   - El uso de una función después de definirla se denomina llamada a una función.
   - Para llamar a una función, escriba su nombre seguido de un paréntesis.
   - Así, para la función que definiste previamente, puedes usar el siguiente código para llamarla:
      - `display_investigation_message()`
   - Aunque utilizarás funciones de formas más complejas a medida que amplíes tus conocimientos, el siguiente código proporciona una introducción a cómo la función display_investigation_message() puede formar parte de una sección de código mayor.
   - Puedes ejecutarla y analizar su resultado:
   - [file](resources/code/modulo-02_01-003.py)
   - La función display_investigation_message() se utiliza dos veces en el código.
   - Imprimirá mensajes "investigate activity" sobre dos registros diferentes cuando las condiciones especificadas se evalúen a True.
   - En este ejemplo, sólo la primera sentencia condicional se evalúa a True, por lo que el mensaje se imprime una vez.
   - Este código llama a la función desde dentro de las condicionales, pero usted podría llamar a una función desde una variedad de lugares dentro del código.
   - Llamar a una función dentro del cuerpo de su definición de función puede crear un bucle infinito.
   - Esto ocurre cuando no se combina con lógica que detiene la llamada a la función cuando se cumplen ciertas condiciones.
   - Por ejemplo, en la siguiente definición de función, después de llamar por primera vez a func1(), continuará llamándose a sí misma y creará un bucle infinito:
   - [file](resources/code/modulo-02_01-004.py)