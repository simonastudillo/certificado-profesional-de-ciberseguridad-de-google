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