# Autenticación, autorización y contabilidad

## Controles de acceso y sistemas de autenticación
- ​Proteger los datos es una característica fundamental de los controles de seguridad.
- ​Cuando se trata de mantener la información a salvo y segura, el hash y el cifrado ​son herramientas poderosas, aunque limitadas.
- ​Gestionar quién o ​qué tiene acceso a la información también es clave para salvaguardar la información.
- ​La siguiente serie de controles que exploraremos son los Controles de acceso, ​los controles de seguridad que gestionan el acceso, la autorización y la ​rendición de cuentas de la información.
- ​Cuando se hacen bien, los Controles de acceso mantienen la confidencialidad de los datos, ​integridad y disponibilidad.
- ​También consiguen que los usuarios obtengan rápidamente la información que necesitan. 
- Estos sistemas suelen dividirse en tres funciones ​separadas, aunque relacionadas, conocidas como el marco de autenticación, autorización y contabilidad.
- ​Cada control tiene su propio protocolo y sistemas que los hacen funcionar.
- ​Los sistemas de autenticación son controles de acceso que sirven a un propósito muy básico.
- Le hacen a cualquier persona que intente acceder a la Información ​esta sencilla pregunta: ¿quién es usted?
- ​Las organizaciones recogen las respuestas a estas preguntas de forma diferente, ​dependiendo de los objetivos de su política de Seguridad.
- ​Algunas son más minuciosas que otras, pero en general, ​las respuestas a esta pregunta pueden basarse en tres factores de autenticación.
- ​El primero es el conocimiento.
   - La autenticación por conocimiento se refiere a algo que el usuario ​conoce, como una contraseña o ​la respuesta a una pregunta de seguridad que haya proporcionado previamente.
- ​Otro factor es la propiedad, que se refiere a algo que el usuario posee.
   - ​Un tipo de autenticación por propiedad muy utilizado es un código de acceso de un solo uso, u OTP.
   - ​Probablemente haya experimentado esto alguna vez.
   - ​Se trata de una secuencia de números aleatorios que una aplicación o sitio web ​le enviará por mensaje de texto o correo electrónico y le pedirá que proporcione.
- ​El último es la característica.
   - La autenticación mediante este factor es algo que el usuario es.
   - ​Los datos biométricos, como el escaneado de huellas dactilares en su smartphone, son un ejemplo de este tipo de ​autenticación.
   - ​Aunque no se utiliza en todas partes, esta forma de autenticación es cada vez más común ​porque es mucho más difícil para los delincuentes hacerse pasar por alguien ​si tienen que imitar una huella dactilar o un escaneado facial en lugar de una contraseña.
- ​La información proporcionada durante la autenticación tiene que coincidir ​con la información archivada para que estos Controles de acceso funcionen.
- ​Cuando las credenciales no coinciden, la autenticación falla y se deniega el acceso.
- Cuando coinciden, se concede el acceso.
- ​Denegar incorrectamente el acceso puede ser frustrante para cualquiera.
- ​Para que los sistemas de acceso sean más cómodos, ​muchas organizaciones confían hoy en día en el inicio de sesión único. 
- El inicio de sesión único, o ​SSO, es una tecnología que combina varios inicios de sesión diferentes en uno solo.
- ​¿Se imagina tener que volver a presentarse cada vez que queda con ​un amigo?
- ​Ese es exactamente el tipo de problema que resuelve el SSO.
- ​En lugar de exigir a los usuarios que se autentiquen una y otra vez, el SSO establece ​su identidad una vez, lo que les permite acceder a los Recursos de la empresa más rápidamente.
- ​Aunque los sistemas SSO son útiles cuando se trata de acelerar el proceso de autenticación, ​presentan una vulnerabilidad importante cuando se utilizan solos.
- ​Denegar el acceso a los usuarios autorizados puede ser frustrante, ​pero ¿sabe qué es aún peor?
- Conceder incorrectamente el acceso al usuario equivocado.
- ​La tecnología SSO es estupenda, pero no si se basa en un único factor de ​autenticación.
- Añadir más factores de autenticación refuerza estos sistemas.
- ​La autenticación de múltiples factores, o MFA, es una medida de seguridad que requiere que ​un usuario verifique su identidad de dos o más formas para acceder a un sistema o red.
- ​MFA combina dos o más credenciales independientes, como los conocimientos y la ​propiedad, para demostrar que alguien es quien dice ser.
- ​SSO y MFA se utilizan a menudo conjuntamente ​para aumentar las capacidades de defensa de los sistemas de autenticación.
- ​Cuando se utilizan ambos, las organizaciones pueden garantizar un acceso cómodo ​que también es seguro.

---

## El auge de SSO y MFA
- La mayoría de las empresas ayudan a mantener sus Datos a buen recaudo tras sistemas de autenticación.
- Los nombres de usuario y las contraseñas son las claves que desbloquean la Información para la mayoría de las organizaciones.
- Pero, ¿son suficientes esas credenciales?
- La Seguridad de la información a menudo se centra en gestionar el acceso y la autorización de un usuario a la información.
- Anteriormente, usted aprendió acerca de los tres factores de autenticación: Conocimientos, Responsabilidad y Característica.
- El inicio de sesión único (SSO) y la autenticación de múltiples factores (MFA) son dos tecnologías que se han hecho populares para implementar estos factores de autenticación.

- Un mejor enfoque de la autenticación
   - El inicio de sesión único (SSO) es una tecnología que combina varios inicios de sesión diferentes en uno solo.
   - Cada vez más empresas recurren al SSO como solución a sus necesidades de autenticación por tres razones:
      - El SSO mejora la experiencia del usuario al eliminar el número de nombres de usuario y contraseñas que la gente tiene que recordar.
      - Las empresas pueden reducir costes racionalizando la forma en que gestionan los servicios conectados.
      - El SSO mejora la Seguridad general al reducir el número de puntos de acceso a los que pueden dirigirse los atacantes.
   - Esta tecnología empezó a estar disponible a mediados de la década de 1990 como una forma de combatir la fatiga de contraseñas, que se refiere a la tendencia de la gente a reutilizar contraseñas en todos los servicios.
   - Recordar muchas contraseñas diferentes puede ser un reto, pero utilizar la misma contraseña repetidamente supone un importante riesgo para la Seguridad.
   - El SSO resuelve este dilema desplazando la carga de la autenticación lejos del usuario.

- Cómo funciona el SSO
   - El SSO funciona automatizando el modo en que se establece la confianza entre un usuario y un proveedor de servicios.
   - En lugar de hacer recaer la responsabilidad en un empleado o cliente, las soluciones SSO recurren a terceros de confianza para demostrar que un usuario es quien dice ser.
   - Esto se hace mediante el intercambio de tokens de acceso encriptados entre el proveedor de identidad y el proveedor de servicios.
   - Al igual que otros tipos de información digital, estos tokens de acceso se intercambian utilizando protocolos específicos.
   - Las implementaciones de SSO suelen basarse en dos protocolos de autenticación diferentes: LDAP y SAML.
   - LDAP, que significa Protocolo ligero de acceso a directorios, se utiliza sobre todo para transmitir información dentro de las instalaciones;
   - SAML, que significa Lenguaje de marcado de aserción de seguridad, se utiliza sobre todo para transmitir información fuera de las instalaciones, como en la nube.
   - Los protocolos LDAP y SAML suelen utilizarse juntos.
   - He aquí un ejemplo de cómo el SSO puede conectar a un usuario a varias aplicaciones con un token de acceso:

<img src="./resources/image-05.png" alt="Un usuario se conecta a varias aplicaciones con un token de acceso" width="600"/>

- Limitaciones del SSO
   - Los nombres de usuario y las contraseñas por sí solos no siempre son la forma más segura de proteger la información confidencial.
   - El SSO proporciona beneficios útiles, pero sigue existiendo el riesgo asociado al uso de una sola forma de autenticación.
   - Por ejemplo, una contraseña perdida o robada podría exponer información a través de múltiples servicios.
   - Afortunadamente, existe una solución a este problema.

- MFA al rescate
   - La autenticación de múltiples factores (MFA) requiere que un usuario verifique su identidad de dos o más formas para acceder a un sistema o red.
   - En cierto sentido, la MFA es similar a utilizar un cajero automático para retirar dinero de su cuenta bancaria.
   - En primer lugar, usted introduce una tarjeta de débito en la máquina como una forma de identificación.
   - Después, introduce su número PIN como segunda forma de identificación.
   - Combinados, ambos pasos, o factores, se utilizan para verificar su identidad antes de autorizarle a acceder a la cuenta.
   
- Refuerzo de la autenticación
   - La MFA se basa en los beneficios de la SSO.
   - Funciona haciendo que los usuarios demuestren que son quienes dicen ser.
   - El usuario debe proporcionar dos factores (2FA) o tres factores (3FA) para autenticar su identificación.
   - El proceso MFA pide a los usuarios que proporcionen estas pruebas, como por ejemplo:
      - Algo que un usuario sabe: normalmente un nombre de usuario y una contraseña
      - Algo que un usuario tiene: normalmente recibido de un proveedor de servicios, como un código de acceso de un solo uso (OTP) enviado por SMS
      - Algo que un usuario es: se refiere a las características físicas de un usuario, como sus huellas dactilares o escáneres faciales
   - Exigir múltiples formas de identificación es una medida de seguridad eficaz, especialmente en los entornos de nube.
   - Puede ser difícil para las empresas en la Nube asegurarse de que los usuarios que acceden remotamente a sus sistemas no son actores de amenazas.
   - La MFA puede reducir el riesgo de autenticar a los usuarios equivocados exigiendo formas de identificación difíciles de imitar o de someter a fuerza bruta.

---

## Los mecanismos de autorización
- El acceso tiene que ver tanto con la autorización ​como con la autenticación.
- ​Una de las funciones más importantes de ​los controles de acceso es la forma en que ​asignan la responsabilidad de ciertos sistemas y procesos.
- ​El siguiente paso en nuestra exploración de los ​sistemas de control de acceso son ​los mecanismos de autorización.
- ​De hecho, estos protocolos funcionan en estrecha colaboración con ​las tecnologías de autenticación.
- Mientras uno ​valida quién es el usuario, ​el otro determina lo que se le permite hacer.
- ​Veamos la siguiente parte del ​framework de autenticación, autorización y contabilización que protege la información privada.
- ​Anteriormente, aprendimos sobre ​el principio de privilegio mínimo.
- ​La autorización está vinculada a la idea de que el ​acceso a la información solo dura el tiempo que sea necesario.
- ​Los sistemas de autorización también están ​muy influenciados por esta idea​, además de otro importante principio de Seguridad, ​la separación de funciones.
- ​La separación de funciones es ​el principio según el cual los usuarios no deben recibir ​niveles de autorización que ​les permitan hacer un mal uso de un sistema.
- La ​separación de tareas reduce el riesgo de ​fallos del sistema y de comportamientos inapropiados por parte de los usuarios.
- ​Por ejemplo, una persona ​responsable de prestar el servicio de atención al cliente ​tampoco debería estar autorizada a evaluar ​su propio desempeño.
- En esta posición, ​podrían fácilmente descuidar sus deberes y ​continuar otorgándose ​altas calificaciones sin supervisión.
- ​Del mismo modo, si una persona fue ​autorizada a desarrollar y probar un sistema de Seguridad, es ​mucho más probable ​que desconozca sus puntos débiles.
- ​Tanto el principio de privilegio mínimo como el concepto de ​separación de funciones se aplican a algo más que a las personas.
- ​Se aplican a todos los sistemas, incluidas las redes, las ​bases de datos, los procesos y ​cualquier otro aspecto de una organización.
- ​En última instancia, la autorización ​depende del rol del usuario o del sistema.
- ​Cuando se trata de proteger los datos en una red, ​hay un par de ​controles de acceso de uso frecuente con los que debería estar familiarizado: ​HTTP basic auth y OAuth.
- ​¿Alguna vez te has preguntado qué ​significa HTTP en las direcciones web?
- ​Son las siglas de protocolo de transferencia de hipertexto, que ​es la forma en que se establecen las comunicaciones a través de la red.
- ​HTTP usa lo que se conoce como autenticación básica, ​la tecnología utilizada para establecer la ​solicitud de un usuario para acceder a un servidor.
- ​La autenticación básica funciona enviando ​un identificador cada vez que ​un usuario se comunica con una página web.
- ​Algunos sitios web siguen utilizando la autenticación básica para saber si ​alguien está autorizado o no a ​acceder a la información de ese sitio.
- ​Sin embargo, su protocolo ​se considera vulnerable a los ataques ​porque transmite nombres de usuario y ​contraseñas abiertamente a través de la red.
- ​La mayoría de los sitios web actuales utilizan HTTPS en su lugar, ​que significa protocolo seguro de transferencia de hipertexto.
- Este protocolo no expone información confidencial, ​como las credenciales de acceso, cuando se ​comunica a través de la red.
- ​Otra tecnología de autenticación segura que ​se utiliza hoy en día es OAuth.
- ​OAuth es un ​protocolo de autorización de estándar abierto que comparte el acceso designado entre aplicaciones.
- ​Por ejemplo, puedes decirle a Google que está ​bien que otro sitio web acceda a tu perfil ​para crear una cuenta.
- ​En lugar de solicitar y enviar ​nombres de usuario y contraseñas confidenciales a través de la red, ​OAuth usa tokens de API ​para verificar el acceso entre tú y un proveedor de servicios.
- ​Un Token de API es un pequeño bloque de ​código cifrado que contiene información sobre un usuario.
- ​Estos tokens contienen datos como tu identidad, los permisos del sitio y mucho más.
- ​OAuth envía y recibe solicitudes de acceso mediante ​tokens de API pasándolas de ​un servidor al dispositivo de un usuario.
- ​Exploremos lo que sucede entre bastidores.
- ​Cuando autorizas a un sitio a crear ​una cuenta con tu perfil de Google, ​todos los protocolos de inicio de sesión habituales de Google siguen activos.
- ​Si tienes ​habilitada la autenticación multifactor en tu cuenta, y deberías hacerlo, ​seguirás disfrutando de las ventajas de Seguridad que ofrece.
- ​Los tokens de API minimizan los riesgos de manera importante.
- ​Estos tokens de API sirven como ​una capa adicional de encriptación que ayuda ​a mantener segura tu contraseña de Google ​en caso de que se produzca una violación en otra plataforma.
- ​Autenticación básica y OAuth ​son solo un par de ejemplos de ​herramientas de autorización diseñadas teniendo en cuenta los principios ​de mínimo privilegio y separación de funciones.
- ​Hay muchos otros controles que ayudan a limitar ​el riesgo de acceso no autorizado a la información.
- ​Además de controlar el acceso, ​también es importante supervisarlo.
- ​En nuestro siguiente vídeo, nos centraremos en ​la tercera y última parte del ​framework de autenticación, autorización y contabilización. 

---

## Por qué auditamos la actividad de los usuarios
- ​¿Alguna vez se ha preguntado si su empleador lleva ​un registro de cuándo inicia sesión en los sistemas de la empresa?
- ​Bueno, lo son, si están implementando ​la tercera y última función del ​framework de autenticación, autorización y contabilización.
- La ​contabilidad es la práctica de ​supervisar los registros de acceso de un sistema.
- ​Estos registros contienen información como quién ​accedió al sistema, cuándo lo hizo ​y qué recursos utilizó.
- ​Los analistas de seguridad utilizan mucho los registros de acceso.
- ​Los datos que contienen son una forma útil de ​identificar tendencias, como los intentos fallidos de inicio de sesión.
- ​También se utilizan para descubrir a ​los piratas informáticos que han accedido a ​un sistema y para ​detectar un incidente, como una violación de datos.
- ​En este campo, los registros de acceso son esenciales.
- ​Con frecuencia, analizarlos es ​el primer procedimiento que ​se sigue al investigar un evento de Seguridad.
- ​Entonces, ¿cómo recopilan los registros de acceso toda esta información útil?
- ​​Cada vez que un usuario accede a un sistema, ​inicia lo que se denomina una sesión.
- ​Una sesión es una secuencia de ​solicitudes y ​respuestas de autenticación HTTP básica de red asociadas al mismo usuario, ​como cuando visita un sitio web.
- ​Los registros de acceso son esencialmente registros de sesiones que ​capturan el momento en que un usuario entra en ​un sistema hasta el momento en que lo abandona.
- ​Cuando comienza la sesión, se activan dos acciones.
- ​La primera es la creación de un identificador de sesión.
- ​Un identificador de sesión es un token único que identifica a ​un usuario y su dispositivo al acceder al sistema.
- ​Los ID de sesión se adjuntan al usuario hasta ​que cierre el navegador o se agote el tiempo de espera de la sesión.
- ​La segunda acción que tiene ​lugar al inicio de una sesión es el ​intercambio de cookies de sesión ​entre un servidor y el dispositivo del usuario.
- ​Una cookie de sesión es un token que los sitios web utilizan para ​validar una sesión y determinar ​cuánto tiempo debe durar esa sesión.
- ​Cuando se intercambian cookies ​entre su computadora y un servidor, ​se lee su ID de sesión para determinar ​qué información debe mostrarle el sitio web.
- ​Las cookies hacen que las sesiones web sean más seguras y eficientes.
- ​El intercambio de tokens significa que ​no se ​comparte información confidencial, como nombres de usuario y contraseñas.
- ​Las cookies de sesión evitan que ​los atacantes obtengan datos confidenciales.
- ​Sin embargo, hay otros daños que pueden causar.
- ​Con una cookie robada, ​un atacante puede hacerse pasar por un ​usuario utilizando su token de sesión.
- ​Este tipo de ataque se conoce como secuestro de sesión (session hijacking).
- ​El secuestro de sesión es un evento en el que los ​atacantes obtienen el ID de sesión de un usuario legítimo.
- ​Durante este tipo de ataques, los ​ciberdelincuentes se hacen pasar por el usuario y ​causan todo tipo de daños.
- ​Se puede robar dinero o datos privados.
- Si, por ejemplo, ​los secuestradores obtienen una ​credencial de inicio de sesión único a partir de cookies robadas, ​pueden incluso acceder a ​sistemas adicionales que, de otro modo, parecen seguros.
- ​Esta es una de las razones por las que la contabilización ​y la supervisión de los registros de sesión son tan importantes.
- ​La actividad inusual en los registros de acceso puede indicar que se ​ha accedido indebidamente a la información o que se la ha robado.
- ​Al fin y al cabo, la contabilización es la forma en que ​obtenemos estadísticas valiosas que hacen que la información sea más segura. 

---

## Tim: Encontrar un propósito en la protección de los recursos
- Trabajo en el Equipo de Detección y Respuesta de Google.
- ​Puede pensar que somos los detectores de humo y los bomberos de Google.
- ​Así que nuestro trabajo consiste en detectar actividades dañinas que puedan ​afectar a Google y a sus usuarios.
- ​Lo que está en juego aquí es muy, muy importante.
- ​Imagínese lo que tiene en Google, ya sean Docs, ​fotos, su información financiera, algunos de sus secretos.
- ​Los profesionales de la ciberseguridad ​están ahí para proteger los recursos más valiosos de la empresa.
- ​Estarás ahí para proteger eso, y ​esa línea directa desde lo que estás haciendo hasta lo que la empresa considera más importante, ​más valioso, y proteger eso, creo que proporciona mucho propósito a la gente.
- ​Y proporciona mucha motivación y proporciona la base y ​los cimientos para una carrera muy, muy satisfactoria.
- ​La ciberseguridad es una carrera profundamente gratificante.
- ​Es una función que es crítica en muchas, muchas empresas y ​es una carrera que está muy solicitada, y ​hay una escasez absoluta de mano de obra con talento ahí fuera.

---

## Gestión de identidad y acceso
- Seguridad es más que simplemente combinar procesos y tecnologías para proteger los recursos.
- En su lugar, la Seguridad consiste en garantizar que estos procesos y tecnologías están creando un entorno seguro que respalda una estrategia de defensa.
- Una clave para lograrlo es implementar dos principios fundamentales de Seguridad que limitan el acceso a los recursos de la organización:
   - El principio de privilegio mínimo en el que a un usuario sólo se le concede el nivel mínimo de acceso y autorización requerido para completar una tarea o función.
   - Separación de funciones, que es el principio según el cual no se debe conceder a los usuarios niveles de autorización que les permitan hacer un uso indebido de un sistema.
- Ambos principios suelen apoyarse mutuamente.
- Por ejemplo, según el de menor privilegio, una persona que necesita permiso para aprobar las compras del departamento de informática no debería tenerlo para aprobar las compras de todos los departamentos.
- Del mismo modo, según la separación de funciones, la persona que puede aprobar las compras del departamento de TI debe ser diferente de la persona que puede introducir nuevas compras.
- En otras palabras, el privilegio mínimo limita el acceso que recibe un individuo, mientras que la separación de funciones divide las responsabilidades entre varias personas para evitar que una sola tenga demasiado control.
- La separación de funciones se denomina a veces segregación de funciones.
- Anteriormente, usted aprendió sobre el framework de autenticación, autorización y contabilidad (AAA).
- Muchas empresas utilizaron este Modelo para implementar estos dos principios de Seguridad y gestionar el acceso de los usuarios.
- Conocerá las similitudes entre AAA e IAM y cómo se implementan habitualmente.

- Gestión de identidad y acceso (IAM)
   - Así como las organizaciones dependen cada vez más de la tecnología, las agencias reguladoras han puesto más presión sobre ellas para que demuestren que están haciendo todo lo posible para prevenir las amenazas.
   - La gestión de identidad y acceso (IAM) es un conjunto de procesos y tecnologías que ayuda a las organizaciones a gestionar las identidades digitales en su entorno.
   - Tanto los sistemas AAA como los IAM están diseñados para autenticar a los usuarios, determinar sus privilegios de acceso y realizar un seguimiento de sus actividades dentro de un sistema.
   - Cualquiera de los dos Modelos utilizados por su organización es más que un sistema único y claramente definido.
   - Cada uno de ellos consiste en una colección de Controles de seguridad que garantizan al usuario adecuado el acceso a los Recursos adecuados en el momento adecuado y por las razones adecuadas.
   - Cada uno de esos cuatro factores está determinado por las políticas y los procesos de su organización.
   - Un usuario puede ser una persona, un dispositivo o un software.

- Autenticación de usuarios
   - Para garantizar que el usuario correcto está intentando acceder a un recurso se requiere alguna forma de prueba de que el usuario es quien dice ser.
   - Hay unos cuantos factores que se pueden utilizar para autenticar a un usuario:
      - Conocimientos, o algo que el usuario sabe
      - Responsabilidad, o algo que el usuario posee
      - Característica, o algo que el usuario es
   - La autenticación se verifica principalmente con las credenciales de inicio de sesión.
   - El inicio de sesión único (SSO), una tecnología que combina varios inicios de sesión diferentes en uno, y la autenticación de múltiples factores (MFA), una medida de seguridad que requiere que un usuario verifique su identidad de dos o más formas para acceder a un sistema o red, son otras herramientas que las organizaciones utilizan para autenticar a las personas y los sistemas.
   - Otra forma de recordar este Modelo de autenticación es: algo que sabe, algo que tiene y algo que es.

- Aprovisionamiento de usuarios
   - Los sistemas back-end deben ser capaces de verificar si la información facilitada por un usuario es correcta.
   - Para lograrlo, los usuarios deben estar correctamente aprovisionados.
   - El Aprovisionamiento de usuarios es el proceso de creación y mantenimiento de la identidad digital de un usuario.
   - Por ejemplo, una universidad puede crear una nueva cuenta de usuario cuando se contrata a un nuevo instructor.
   - La nueva cuenta se configurará para proporcionar acceso a los recursos exclusivos del instructor mientras esté impartiendo clase.
   - Los analistas de seguridad participan habitualmente en el aprovisionamiento de usuarios y sus privilegios de acceso.
   - Otra función que tienen los analistas en IAM es la de desaprovisionar usuarios.
   - Se trata de una práctica importante que elimina los derechos de acceso de un usuario cuando ya no debería tenerlos.

- Conceder autorización
   - Si se ha autenticado al usuario correcto, la red debe garantizar que se ponen a su disposición los recursos adecuados.
   - Hay tres frameworks comunes que las organizaciones utilizan para manejar este paso de IAM:
      - Control de acceso obligatorio (MAC)
      - Control de acceso discrecional (DAC)
      - Control de acceso basado en roles (RBAC)

<img src="./resources/image-06.png" alt="Un administrador del sistema que decide conceder a los usuarios y a un sistema operativo acceso a los datos." width="600"/>

- Control de acceso obligatorio (MAC)
   - MAC es el más estricto de los tres framework.
   - La autorización en este Modelo se basa en una estricta necesidad de conocer.
   - El acceso a la información debe ser concedido manualmente por una autoridad central o por el administrador del sistema.
   - Por ejemplo, MAC se aplica comúnmente en las fuerzas del orden, el ejército y otros organismos gubernamentales en los que los usuarios deben solicitar el acceso a través de una cadena de mando.
   - El MAC también se conoce como control no discrecional porque el acceso no se concede a discreción del Propietario de los datos.

<img src="./resources/image-07.png" alt="Un propietario de datos que decide conceder a determinados usuarios acceso a sus datos." width="600"/>

- Control de acceso discrecional (DAC)
   - El DAC se aplica normalmente cuando el Propietario de los datos decide los niveles apropiados de accesibilidad.
   - Un ejemplo de DAC es cuando el propietario de una carpeta de Google Drive comparte el acceso de editor, visualizador o comentarista con otra persona.

<img src="./resources/image-08.png" alt="Un administrador del sistema que asigna a los usuarios funciones específicas con niveles de acceso predefinidos." width="600"/>

- Control de acceso basado en roles (RBAC)
   - El RBAC se utiliza cuando la autorización viene determinada por la función de un usuario dentro de una organización.
   - Por ejemplo, un usuario del departamento de marketing puede tener acceso a los análisis de datos de los usuarios pero no a la administración de redes.

- Tecnologías de Control de acceso
   - Los usuarios suelen experimentar la autenticación y la autorización como una experiencia única y sin fisuras.
   - En gran parte, eso se debe a las tecnologías de Control de acceso que están configuradas para trabajar juntas.
   - Estas herramientas ofrecen la Velocidad y la Automatización que necesitan los administradores para monitorizar y modificar los derechos de acceso.
   - También disminuyen los errores y los riesgos potenciales.
   - A veces, el departamento de TI de una organización desarrolla y mantiene por su cuenta tecnologías de control de acceso personalizadas.
   - Un sistema IAM o AAA típico consta de un directorio de usuarios, un conjunto de herramientas para gestionar los datos de ese directorio, un sistema de autorización y un sistema de auditoría.
   - Algunas organizaciones crean sistemas a medida para adaptarlos a sus necesidades de Seguridad.
   - Sin embargo, crear una solución interna tiene un coste elevado de tiempo y otros recursos.
   - En su lugar, muchas organizaciones optan por adquirir licencias de soluciones de terceros que ofrecen un conjunto de herramientas que les permiten asegurar rápidamente sus sistemas de Información.
   - Tenga en cuenta que la Seguridad es algo más que combinar un puñado de herramientas. Siempre es importante configurar estas tecnologías para que contribuyan a proporcionar un entorno seguro.

- [IDPro©](https://www.idpro.org/) es una organización profesional dedicada a compartir los conocimientos esenciales del sector IAM

---

## Actividad: Mejorar la autenticación, autorización y contabilidad de una pequeña empresa (Business to Business)
- Resumen de la actividad
   - En esta actividad, evaluará los controles de acceso utilizados por una empresa.
   - Analizará su proceso actual, identificará los problemas y hará recomendaciones para mejorar sus prácticas de seguridad.
   - Anteriormente, aprendió que los controles de acceso son controles de seguridad que gestionan el acceso, la autorización y la responsabilidad de la información.
   - Los controles de autenticación se utilizan para verificar quién es alguien, mientras que los controles de autorización se utilizan para conceder permisos a un usuario y establecer límites sobre las cosas que se le permite hacer.
   - Cuando se hacen bien, los controles de acceso son la clave para disminuir la probabilidad de un riesgo para la seguridad.
   
- Escenario
   - Revise el escenario que aparece a continuación.
   - A continuación, complete las instrucciones paso a paso.
   - Usted es el primer profesional de la ciberseguridad contratado por una empresa en expansión.
   - Recientemente, se ha realizado un ingreso desde la empresa a una cuenta bancaria desconocida.
   - El director financiero dice que no cometieron ningún error.
   - Afortunadamente, pudieron detener el pago.
   - El propietario le ha pedido que investigue lo sucedido para evitar futuros incidentes.
   - Para ello, tendrá que hacer un poco de contabilidad sobre el incidente para comprender mejor lo sucedido.
   - En primer lugar, revisará el registro de accesos del incidente.
   - A continuación, tomará notas que puedan ayudarle a identificar a un posible actor de la amenaza.
   - Después, detectará los problemas con los controles de acceso que fueron aprovechados por el usuario.
   - Por último, recomendará mitigaciones que puedan mejorar los controles de acceso de la empresa y reducir la probabilidad de que este incidente vuelva a producirse.

- Instrucciones paso a paso

1. Acceder a la plantilla
- [Hoja de trabajo de control de acceso](./resources/Activity-Template_-Access-control-worksheet.docx)

2. Acceda a los materiales de apoyo
- Los siguientes materiales de apoyo le ayudarán a completar esta actividad. Manténgalos abiertos mientras continúa con los siguientes pasos.
- [Ejercicio de contabilidad](./resources/Accounting-exercise.xlsx)

3. Revisar el registro de incidentes de este incidente de nómina
- Los registros de eventos contienen información relacionada con el funcionamiento y el uso de un sistema.
- Pueden utilizarse para Identificar actividades sospechosas, Detectar vulnerabilidades y Rastrear usuarios.
- Busque la pestaña Registro de eventos de la hoja de cálculo del ejercicio de contabilización.
- Revise cuidadosamente el registro de eventos de este Incidente para comenzar su investigación.
- Fíjese en el tipo de Evento, la fecha, la hora y la dirección IP del usuario en los detalles del registro.
- Tome 1-2 notas de la información que ha aprendido sobre el usuario al revisar los detalles del registro de eventos.
- Añada sus notas a la columna Notas de la hoja de trabajo Control de accesibilidad.

4. Identificar los problemas de Control de acceso que provocaron el Incidente
- Los detalles del registro le dicen mucho sobre un momento concreto.
- Puede encontrar otros detalles útiles sobre un Evento cruzando esa información con otras fuentes.
- En esta empresa trabajan diferentes empleados.
- Actualmente, todos ellos gestionan los Recursos de la empresa mediante una unidad de disco compartida en la nube.
- Busque la pestaña Directorio de empleados de la hoja de cálculo Ejercicio de contabilización.
- Compare la Información encontrada en la pestaña Directorio de empleados con la Información de la pestaña Registro de eventos.
- Observe cualquier similitud entre los detalles del registro de Eventos y los detalles del Directorio de empleados.
- A continuación, enumere 1 ó 2 problemas que descubra con la forma en que la empresa gestiona el acceso de los empleados en la columna Problemas de la hoja de cálculo Control de acceso.

5. Recomendar mitigaciones que puedan evitar una futura violación
- Ha finalizado la contabilización del pago extraño y ha descubierto fallos en la forma en que la empresa gestiona su Información.
- Busque la columna Recomendación(es) de la hoja de trabajo Control de acceso.
- Haga al menos 2 recomendaciones de mitigaciones que la empresa pueda implementar para prevenir incidentes como éste en el futuro.
- Por ejemplo, una recomendación podría ser disponer de procedimientos para revocar el acceso a los archivos cuando un empleado ya no trabaje en la empresa.

- Qué incluir en su respuesta
   - 1-2 notas sobre el usuario
   - 1-2 problemas de control de acceso
   - 2 recomendaciones para mitigar el control de acceso

- Access controls worksheet
   - Authorization/Authentication
      1. Notes
         - Según lo detectado, la transacción se hizo desde la IP 152.207.255.255, la cual corresponde con el acceso del empleado Robert Taylor.
         - La cuenta de Robert está marcada con fecha de termino para el 27/12/2019, pero el registro de eventos muestra que la transacción se realizó el 10/03/2023.
         - Robert es un contratista que trabaja en la empresa y tiene el rol de Administrador.
      2. Problems
         - El problema principal detectado es que no se detecta el principio de privilegio mínimo, ya que Robert y todos los usuarios tienen permiso de administrador, lo que les permite hacer cambios en la información de la empresa sin importar si son Part Time, Full Time o Contratistas.
         - Otro problema es que no se detecta la separación de funciones, ya que Robert tiene acceso a la información de nómina y puede hacer cambios en ella, lo que le permite realizar transacciones sin supervisión.
         - Un problema importante es que las cuentas no se están desactivando automáticamente cuando un empleado deja de trabajar en la empresa, lo que permite que los usuarios sigan teniendo acceso a la información de la empresa después de su fecha de terminación.
      3. Recommendations
         - Asignar perfiles y permisos de acceso según el principio de privilegio mínimo, asegurando que los usuarios solo tengan acceso a la información necesaria para realizar sus funciones.
         - Implementar la separación de funciones, asegurando que los usuarios no tengan acceso a información que les permita realizar transacciones sin supervisión, especialmente en áreas críticas como la nómina.
         - Implementar un proceso de desactivación automática de cuentas cuando un empleado deja de trabajar en la empresa, o en su defecto marcar alguna alerta en calendario para que el administrador de la empresa pueda desactivar la cuenta del empleado a tiempo.

---

## Ejemplo de actividad: Mejorar la autenticación y autorización de una pequeña empresa
- Ejemplar completado
   - Revisa el ejemplo de actividad completado a continuación para ver cómo se puede abordar la actividad.
   - [Control de acceso de ejemplo completado](./resources/Access-control-worksheet-exemplar.docx)

- Nota(s) sobre el usuario:
   - El Evento tuvo lugar el 10/03/23.
   - El usuario es Legal/Administrador.
   - La dirección IP de la computadora utilizada para iniciar sesión es 152.207.255.255.
> Los registros de eventos pueden ayudarle a menudo a identificar el quién, el qué y el porqué de un Incidente de Seguridad.

- Problema(s) de Control de acceso:
   - Robert Taylor, Jr. es un contratista con acceso de administrador.
   - Su contrato finalizó en 2019, pero su cuenta accedió a los sistemas de nómina en 2023.
> A menudo, este tipo de incidentes se producen porque los sistemas están mal configurados o se utilizan de forma inadecuada.
> Ese es el caso de cómo esta empresa está compartiendo Información entre sus empleados.

- Recomendaciones:
   - Las cuentas de usuario deberían caducar a los 30 días.
   - Los contratistas deberían tener un acceso limitado a los Recursos de la empresa.
   - Habilite la autenticación de múltiples factores (MFA).

- Parece que un antiguo empleado es potencialmente el Agente de amenaza.
- Sin embargo, es posible que no fuera la persona responsable de este Incidente de Seguridad.
- Es habitual que la gente reutilice las credenciales de inicio de sesión en muchos servicios.
- Y si esas credenciales se ven comprometidas en una plataforma, un atacante puede utilizarlas para acceder a otras.
- En este caso, Implementar Controles de acceso, como políticas de contraseñas, permisos de archivo limitados y MFA puede proteger a la empresa de incidentes como este.

