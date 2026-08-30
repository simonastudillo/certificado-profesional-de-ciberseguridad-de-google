# Explotaciones basadas en web

## Secuencias de comandos en sitios cruzados (XSS)
- ​Anteriormente, exploramos algunos tipos de software malicioso.
- ​Ya sea que esté instalado en una ​computadora individual o en un servidor de red, todo el software malintencionado debe ​entregarse al objetivo antes de que pueda funcionar.
- ​El Phishing y otras ​técnicas de ingeniería social son formas habituales de distribución de software malicioso.
- ​Otra forma de propagación es mediante el uso de una amplia ​clase de amenazas conocidas como exploits basados en la web.
- ​Explotaciones basadas en web son códigos o comportamientos malintencionados que ​se utilizan para aprovechar las fallas de programación en una aplicación web.
- ​Los ciberdelincuentes se centran en las vulnerabilidades basadas en la web para obtener información personal confidencial.
- ​Los ataques se producen porque las aplicaciones web ​interactúan con varios usuarios en varias redes.
- ​Los piratas informáticos malintencionados suelen explotar este ​alto nivel de interacción mediante ataques de inyección.
- ​Un ataque de inyección es un código malintencionado que se inserta en una aplicación vulnerable.
- La aplicación infectada a menudo parece funcionar con normalidad.
- Esto se ​debe a que el código inyectado se ejecuta en segundo plano, sin que el usuario lo sepa.
- ​Las aplicaciones son vulnerables a ​los ataques de inyección porque están programadas para recibir entradas de datos.
- ​Puede ser algo que el usuario escribe​, hace clic o algo que un programa comparte con otro.
- ​Cuando se codifican correctamente, ​las aplicaciones deben poder interpretar y gestionar las entradas de los usuarios.
- ​Por ejemplo, supongamos que una aplicación ​espera que el usuario introduzca un número de teléfono.
- ​Esta aplicación debe validar la entrada ​del usuario para asegurarse de que todos los datos son números y no más de diez dígitos.
- ​Si la entrada del usuario no cumple con ​estos requisitos, la aplicación debe saber cómo manejarla.
- ​Las aplicaciones web interactúan con varios usuarios en muchas plataformas.
- ​También tienen muchos objetos interactivos como imágenes y botones.
- ​Esto hace que ​a los desarrolladores les resulte difícil pensar en todas las formas en las que deberían desinfectar sus entradas.
- ​Un tipo de ​ataque por inyección común y peligroso que representa una amenaza para las aplicaciones web es la secuencia de comandos entre sitios.
- ​La escritura de secuencias de comandos entre sitios, o XSS, es un ataque de inyección que ​inserta código en un sitio web o una aplicación web vulnerable.
- ​Estos ataques suelen lanzarse ​mediante la explotación de los dos lenguajes utilizados por la mayoría de los sitios web, HTML y JavaScript.
- ​Ambos pueden dar acceso a los ciberdelincuentes ​a todo lo que se carga en la página web infectada.
- ​Esto puede incluir cookies de sesión, ​geolocalización e incluso cámaras web y micrófonos.
- ​Hay tres tipos principales de ​ataques de secuencia de comandos entre sitios reflejados, almacenados y basados en DOM.
- ​Un ataque XSS reflejado es una instancia en la que se envía una secuencia de comandos ​malintencionada al servidor y se activa durante la respuesta del servidor.
- ​Un ejemplo común de esto es la barra de búsqueda de un sitio web.
- ​En un ataque XSS reflejado, ​los delincuentes envían a su objetivo un enlace web que parece ir a un sitio confiable.
- ​Cuando hacen clic en el enlace, envía una solicitud HTTP al servidor del sitio vulnerable.
- A ​continuación, la secuencia de comandos del atacante se devuelve o ​se refleja en el navegador del usuario inocente.
- ​Aquí, el navegador carga la secuencia de ​comandos maliciosa porque confía en la respuesta del servidor.
- ​Con la secuencia de comandos cargada, ​la información, como las cookies de sesión, se devuelve al atacante. 
- En un ataque XSS almacenado, ​la secuencia de comandos maliciosa no está oculta en un enlace que deba enviarse al servidor.
- ​En cambio, un ataque XSS almacenado es una instancia en la que ​se inyecta una secuencia de comandos maliciosa directamente en el servidor.
- ​Aquí, los atacantes atacan los elementos de un sitio que se ofrecen al usuario.
- ​Pueden ser cosas como imágenes ​y botones que se cargan cuando se visita el sitio.
- Los elementos infectados activan el código malicioso cuando un usuario simplemente visita el sitio.
- ​Los ataques XSS almacenados pueden ser perjudiciales porque el ​usuario no tiene forma de saber de antemano que el sitio está infectado.
- ​Por último, está el XSS basado en DOM.
- DOM son ​las siglas de Modelo de objetos de documentos, que es básicamente el código fuente de un sitio web.
- ​Un Ataque XSS basado en DOM es una ​instancia en la que existe una secuencia de comandos maliciosa en la página web que carga ​un navegador.
- A diferencia del XSS reflejado, ​no es necesario enviar estos ataques al servidor para activarse.
- ​En un ataque basado en DOM, se puede ver una secuencia de comandos maliciosa en la URL.
- ​En este ejemplo, la URL del sitio web contiene valores de parámetros.
- ​Los valores de los parámetros reflejan la entrada del usuario.
- ​Aquí, el sitio permite a los usuarios seleccionar temas de color.
- ​Cuando el usuario hace una selección, aparece como parte de la URL.
- ​En un ataque basado en DOM, los delincuentes cambian el parámetro que espera una entrada.
- ​Por ejemplo, podrían ocultar JavaScript malintencionado en las etiquetas HTML.
- ​El navegador procesaría el HTML y ejecutaría el JavaScript.
- ​Los piratas informáticos utilizan estos métodos de secuencia de comandos entre sitios para robar información confidencial.
- ​Los analistas de seguridad deben estar familiarizados con este grupo de ataques por inyección.

---

## Lagunas explotables en las bases de datos
- ​Sigamos explorando la inyección y los ​ataques investigando otro tipo común de exploit basado en web.
- ​El siguiente que vamos a discutir explota la forma en que los sitios web acceden a la ​información de las bases de datos.
- Al principio del Programa, puede que haya aprendido sobre SQL.
- ​Puede que recuerde, SQL es un lenguaje de programación utilizado para crear, ​interactuar con, y solicitar información de una base de datos.
- ​SQL es utilizado por la mayoría de las aplicaciones web.
- Por ejemplo, los sitios web de compras lo utilizan mucho.
- ​Imagínese las bases de datos de una tienda de ropa en línea
- Es probable que contenga un inventario completo de todos los artículos que vende la empresa.
- ​Los sitios web no suelen hacer que los usuarios introduzcan las consultas SQL manualmente.
- ​En su lugar, utilizan elementos como menús, imágenes y ​botones para mostrar a los usuarios información de forma significativa.
- ​Por ejemplo, cuando un comprador en línea hace clic en un botón para añadir un jersey a su cesta, ​se desencadena una consulta SQL.
- La consulta se ejecuta en segundo plano, donde nadie puede verla.
- ​Nunca lo sabría al utilizar los menús y botones de un sitio web, pero ​a veces esas consultas de backend son vulnerables a ataques de inyección.
- ​Una inyección de SQL es un ataque que ejecuta consultas inesperadas en una base de datos.
- ​Al igual que la secuencia de comandos entre sitios, la inyección de SQL se produce debido a una falta de entrada desinfectada.
- ​Las inyecciones tienen lugar en el área del sitio web que están diseñadas para ​aceptar la entrada del usuario.
- Un ejemplo común es el formulario de inicio de sesión para acceder a un sitio.
- ​Uno de estos formularios puede activar una sentencia SQL backend ​como ésta cuando un usuario introduce sus credenciales.
- ​Los formularios web, como éste, están diseñados para copiar la entrada del usuario en la sentencia ​exactamente como están escritos.
- ​La sentencia envía entonces una petición al servidor, que ejecuta la consulta.
- ​Los sitios web vulnerables a la inyección de SQL insertan la entrada del usuario exactamente ​como se introduce antes de ejecutar el código.
- ​Desgraciadamente, se trata de un grave fallo de diseño.
- ​Sucede habitualmente porque los desarrolladores web esperan que la gente utilice estas entradas ​correctamente.
- ​No prevén que los atacantes las exploten.
- Por ejemplo, ​un atacante podría insertar código SQL adicional.
- ​Esto podría hacer que el servidor ejecute una consulta de código dañino que no ​esperaba.
- ​Los hackers maliciosos pueden apuntar a estos vectores de ataque para obtener información sensible, ​modificar tablas e incluso obtener derechos administrativos sobre la base de datos.
- ​La mejor forma de defenderse contra la inyección de SQL es un código que sanee ​la entrada.
- ​Los desarrolladores pueden escribir código para buscar caracteres SQL específicos.
- ​Esto da al servidor una idea más clara de qué entradas esperar.
- ​Una forma de hacerlo es con sentencias preparadas.
- ​Una sentencia preparada es una técnica de programación que ejecuta ​sentencias SQL antes de pasarlas a la base de datos.
- ​Cuando se desconoce la entrada del usuario, ​la mejor práctica es utilizar estas sentencias preparadas.
- ​Con sólo unas pocas líneas de código adicionales, ​una sentencia preparada ejecuta el código antes de pasarlo al servidor.
- ​Esto significa que el código puede validarse antes de realizar la consulta.
- ​Tener un código bien escrito es una de las claves para prevenir la inyección de SQL.
- ​Los equipos de seguridad trabajan con los desarrolladores de programas para probar las aplicaciones en busca de ​este tipo de vulnerabilidades.
- ​Al igual que muchas tareas de seguridad, se trata de un trabajo en equipo.
- ​Los ataques de inyección son sólo uno de los muchos tipos de exploits basados en web a los que se enfrentan los equipos de ​seguridad.

---

## Evitar los ataques por inyección
- Anteriormente, aprendió que el Lenguaje de Consulta Estructurado (SQL) es un lenguaje de programación utilizado para crear, interactuar y solicitar información a una base de datos.
- SQL es uno de los lenguajes de programación más utilizados para interactuar con bases de datos porque está ampliamente soportado por una amplia gama de productos de bases de datos.
- Como recordará, la inyección de SQL maliciosa es un tipo de ataque que ejecuta consultas inesperadas en una base de datos.
- Agentes de amenaza realizan inyecciones de SQL para modificar, borrar o robar información de las bases de datos.
- Una inyección de SQL es un vector de ataque común que se utiliza para obtener acceso no autorizado a las aplicaciones web.
- Debido a la popularidad de este lenguaje entre los desarrolladores, las inyecciones de SQL aparecen regularmente en la Lista OWASP® Top 10 porque los desarrolladores tienden a centrarse en hacer que sus aplicaciones funcionen correctamente en lugar de proteger sus productos de las inyecciones.

- Consultas SQL
   - Cada bit de información al que se accede en línea se almacena en una base de datos.
   - Una base de datos es una colección organizada de información o datos en un solo lugar.
   - Una base de datos puede incluir datos como el Directorio de empleados de una organización o los métodos de pago de los clientes.
   - En SQL, la información de la base de datos se organiza en tablas.
   - SQL se utiliza habitualmente para recuperar, insertar, actualizar o eliminar información de las tablas mediante consultas.
   - Una consulta SQL es una solicitud de datos de una base de datos.
   - Por ejemplo, una consulta SQL puede solicitar datos del directorio de empleados de una organización, como ID, nombres y cargos de los empleados.
   - Una aplicación de recursos humanos puede aceptar una entrada que consulte una tabla SQL para filtrar los datos y localizar a una persona concreta.
   - Las inyecciones de SQL pueden producirse en cualquier lugar dentro de una aplicación vulnerable que pueda aceptar una consulta SQL.
   - Las consultas suelen iniciarse en lugares donde los usuarios pueden introducir información en una aplicación o un sitio web a través de un campo de entrada.
   - Los campos de entrada incluyen elementos que aceptan la introducción de texto, como formularios de inicio de sesión, barras de búsqueda o cuadros de envío de comentarios.
   - Una inyección de SQL se produce cuando un atacante explota campos de entrada que no están programados para filtrar el texto no deseado.
   - Las inyecciones de SQL pueden utilizarse para manipular bases de datos, robar datos confidenciales o incluso tomar el control de aplicaciones vulnerables.

- Categorías de inyección de SQL
   - Existen tres categorías principales de inyección de SQL:
      - Dentro de banda
      - Fuera de banda
      - Inferencial

- Inyección de SQL en banda
   - La inyección de SQL en banda, o clásica, es el tipo más común.
   - Una inyección en banda es aquella que utiliza el mismo canal de comunicación para lanzar el ataque y recoger los resultados.
   - Por ejemplo, esto podría ocurrir en el cuadro de búsqueda de la página web de un minorista que permite a los clientes encontrar productos para comprar.
   - Si el cuadro de búsqueda es vulnerable a la inyección, un atacante podría introducir una consulta maliciosa que se ejecutaría en la base de datos, haciendo que ésta devolviera información sensible como las contraseñas de los usuarios.
   - Los Datos devueltos se muestran de nuevo en el cuadro de búsqueda donde se inició el ataque.

- Inyección de SQL fuera de banda
   - Una inyección fuera de banda es aquella que utiliza un canal de comunicación diferente  para lanzar el ataque y recoger los resultados.
   - Por ejemplo, un atacante podría utilizar una consulta maliciosa para crear una conexión entre un sitio web vulnerable y una base de datos que controle.
   - Este canal independiente les permitiría eludir cualquier control de seguridad existente en el servidor del sitio web, lo que les permitiría robar datos sensibles
   - Los ataques de inyección fuera de banda son muy poco comunes porque sólo funcionarán cuando ciertas características estén habilitadas en el servidor objetivo.

- Inyección de SQL inferencial
   - La inyección de SQL inferencial se produce cuando un atacante no puede ver directamente los resultados de su ataque.
   - En su lugar, pueden interpretar los resultados analizando el comportamiento del sistema.
   - Por ejemplo, un atacante puede realizar un ataque de inyección de SQL en el formulario de inicio de sesión de un sitio web que haga que el sistema responda con un mensaje de error.
   - Aunque no se devuelven datos sensibles, el atacante puede averiguar la estructura de la base de datos basándose en el error.
   - A continuación, puede utilizar esta información para elaborar ataques que le den acceso a datos sensibles o para hacerse con el control del sistema.

- Prevención de la inyección
   - Las consultas SQL se programan a menudo dando por sentado que los usuarios sólo introducirán información relevante.
   - Por ejemplo, un formulario de acceso que espera que los usuarios introduzcan su dirección de correo electrónico asume que la entrada tendrá un formato determinado, como jdoe@domain.com.
   - Por desgracia, no siempre es así.
   - Una clave para prevenir los ataques de inyección de SQL es escapar de las entradas del usuario, impidiendoque alguien inserte cualquier código que un programa no esté esperando.
   - Existen varias formas de escapar a las entradas del usuario:
      - Sentencias preparadas: una técnica de programación que ejecuta sentencias SQL antes de pasarlas a una base de datos
      - Saneamiento de entradas: programación que elimina las entradas del usuario que podrían interpretarse como código.
      - Validación de entrada: programación que garantiza que la entrada del usuario cumple las expectativas de un sistema.
   - El uso de una combinación de estas técnicas puede ayudar a prevenir los ataques de inyección de SQL.
   - En el campo de la Seguridad, es posible que tenga que colaborar estrechamente con los desarrolladores de aplicaciones para abordar las vulnerabilidades que pueden dar lugar a inyecciones de SQL.
   - [Las técnicas de detección de inyección de SQL de OWASP](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection) son un recurso útil si está interesado en investigar por su cuenta las vulnerabilidades de inyección de SQL.

---

## Pon a prueba tus conocimientos: Exploits basados en la Web

1. Rellene el espacio en blanco: _____ son códigos o comportamientos maliciosos que se utilizan para aprovecharse de los fallos de programación de una aplicación web
- [ ] Ataque de phishing dirigido
- [ ] Ingeniería social
- [x] Explotaciones basadas en web
- [ ] Interfaz de línea de comandos
> Las explotaciones basadas en web son códigos o comportamientos maliciosos que se utilizan para aprovecharse de fallos de programación en una aplicación web.

2. Los ataques de secuencia de comandos entre sitios (XSS) se realizan a menudo explotando ¿cuál de los siguientes lenguajes? Seleccione dos respuestas
- [x] HTML
- [x] JavaScript
- [ ] SQL
- [ ] Python
> Los ataques XSS se realizan explotando los dos lenguajes utilizados por la mayoría de los sitios web, HTML y JavaScript.

3. Rellene el espacio en blanco: Un _____ es una técnica de programación que ejecuta sentencias SQL antes de pasarlas a la base de datos
- [ ] botnet
- [x] sentencia preparada
- [ ] inyección de SQL
- [ ] kit de phishing
> Una sentencia preparada es una técnica de programación que ejecuta sentencias SQL antes de pasarlas a la base de datos. Las sentencias preparadas se utilizan para defenderse de los ataques de inyección de SQL mediante la validación del código antes de realizar una consulta.

4. ¿Cuáles son dos ejemplos de cuándo pueden producirse inyecciones de SQL?
- [x] Al utilizar el formulario de inicio de sesión para acceder a un sitio
- [ ] Cuando existe una secuencia de comandos maliciosa en la página web que carga un navegador
- [x] Cuando un usuario introduce sus credenciales
- [ ] Cuando se inyecta una secuencia de comandos maliciosa directamente en el servidor
> Dos ejemplos de cuándo pueden producirse inyecciones de SQL son cuando se utiliza el formulario de inicio de sesión para acceder a un sitio y cuando un usuario introduce sus credenciales. La inyección de SQL puede tener lugar en áreas del sitio web que están diseñadas para aceptar la entrada del usuario. 

5. En un ataque de inyección de SQL, los hackers malintencionados intentan obtener ¿cuál de las siguientes cosas? Seleccione dos respuestas
- [x] Información sensible
- [ ] Contraseñas almacenadas de forma segura
- [x] Derechos administrativos
- [ ] Sistema operativo
> En un ataque de inyección de SQL, los hackers malintencionados intentan obtener información confidencial y obtener derechos administrativos.