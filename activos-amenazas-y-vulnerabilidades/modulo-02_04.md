# Revisar: Proteger los recursos de la organización

## Resumen
- ​En esta sección nos centramos en un tema importante de Seguridad: la protección de los activos.
- ​Una gran parte de esto tiene que ver con la privacidad.
- ​Todos debemos disfrutar del derecho a decidir quién puede acceder a nuestra información.
- ​Como aprendimos, existen varios controles que ayudan a proteger los activos.
- ​Comenzamos la sección explorando los procesos efectivos de manejo de datos que ​se basan en el principio de privilegio mínimo.
- ​Luego exploramos el papel de la encriptación y el hash y la protección de la información.
- ​Exploramos cómo funciona la criptografía simétrica y asimétrica y ​cómo los hashes protegen aún más los datos de cualquier daño.
- ​Luego centramos nuestra atención en los controles de acceso estándar.
- ¡Autenticar ​y autorizar correctamente a los usuarios es de lo que se trata mantener la tríada CID de información de la CIA!
- ​Usamos el framework de Seguridad AAA para hacer un recorrido detallado por los ​sistemas de administración de identidades y accesos y los controles de acceso que validan si ​alguien es o no quien dice ser.
- ​Recuerde que sus antecedentes y experiencias son valiosos en este campo.
- ​Esto, combinado con los conceptos que estamos abordando, lo convertirá en ​un valioso colaborador para cualquier equipo de Seguridad.
- ​Hasta ahora, hemos estado explorando el lado defensivo de la seguridad, pero la ​seguridad no consiste solo en planificar con antelación y esperar a que suceda algo.
- ​En la siguiente parte de nuestro viaje, ​continuaremos desarrollando una mentalidad de seguridad mediante una ​visión más proactiva de la seguridad desde la perspectiva de los atacantes.

---

## Términos del glosario del Módulo 2
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del Módulo 2

1. ¿Cuáles de los siguientes ejemplos son categorías de Controles de seguridad? Seleccione tres respuestas
- [ ] Cumplimiento normativo
- [x] Técnico
- [x] Dirección
- [x] Operador
> Correcto

1. ¿Cuál es la finalidad de los Controles de seguridad?
- [ ] Crear políticas y procedimientos
- [ ] Establecer sistemas de respuesta ante incidentes
- [ ] Cifrar la información en aras de la privacidad
- [x] Reducir los riesgos específicos de Seguridad
> Correcto

2. Una gran cadena hotelera recopila las direcciones de correo electrónico de sus clientes como parte de un sorteo nacional. Como Custodios de datos, ¿cuáles son las responsabilidades de la cadena hotelera para proteger esta Información? Seleccione tres respuestas.
- [x] Manejar con seguridad los Datos cuando se accede a ellos
- [x] Proteger los Datos mientras están almacenados
- [x] Para transportar de forma segura los datos a través de las redes
- [ ] Para editar los Datos cuando sea necesario
> Correcto

2. Un empleado informa de que no puede registrarse en el sistema de nóminas con sus credenciales de acceso. El empleado no recuerda haber cambiado su nombre de usuario ni su contraseña. Como analista de Seguridad, se le pide que revise los registros de acceso para investigar si se ha producido una violación. ¿Qué información puede revisar como Custodio de datos en esta situación? Seleccione dos respuestas
- [ ] Información de contacto de algún compañero de trabajo
- [x] Hora de entrada y salida del usuario
- [ ] Cualquier credencial de acceso a la nómina que el usuario haya almacenado en el servidor
- [x] La dirección IP de la computadora utilizada para el registro
> Correcto

3. Usted envía un correo electrónico a un amigo. El proveedor de servicios de su bandeja de entrada encripta todos los mensajes que envía. ¿Qué ocurre con la información de su correo electrónico cuando está encriptada?
- [ ] Se convierte de texto cifrado a texto plano.
- [ ] Se convierte del cifrado César a texto plano.
- [x] Se convierte de texto plano a texto cifrado.
- [ ] Se convierte de un valor hash a texto cifrado.
> Correcto

3. ¿Qué utilizan los algoritmos de encriptación simétrica para encriptar y desencriptar la información?
- [ ] Un certificado digital
- [ ] Un par de claves pública y privada
- [ ] Un valor hash
- [x] Una única clave secreta
> Correcto

4. Un analista de Seguridad está investigando un archivo crítico del sistema que puede haber sido manipulado. ¿Cómo podría el analista verificar la integridad del archivo del sistema?
- [ ] Forzando bruscamente el archivo del sistema mediante una tabla rainbow.
- [x] Comparando el valor hash de los archivos del sistema con un valor hash conocido y de confianza.
- [ ] Abriendo el archivo del sistema en la aplicación de tratamiento de textos y comprobando su historial de versiones.
- [ ] Al desencriptar la clave secreta de los archivos del sistema utilizando el Estándar de encriptación avanzada (AES).
> Correcto

4. ¿Cómo utilizan principalmente el hash los profesionales de la Seguridad?
- [ ] Para que los Datos estén disponibles rápidamente
- [ ] Almacenar Datos en la Nube
- [ ] Para desencriptar Datos sensibles
- [x] Determinar la integridad de los datos
> Correcto

5. ¿Cuál de los siguientes pasos forma parte del proceso de Infraestructura de clave pública? Seleccione dos respuestas
- [ ] Establecer la confianza mediante certificados digitales
- [x] Intercambio de información encriptada
- [ ] Intercambio de claves públicas y privadas (Incorrecto)
- [ ] Transferencia de compendios hash
> Incorrecto

5. ¿Qué Controles de seguridad se utilizan en la Infraestructura de clave pública (PKI)? Seleccione tres respuestas
- [x] Certificados digitales
- [x] Criptografía asimétrica
- [ ] Autenticación de múltiples factores
- [x] Cifrado simétrico
> Correcto

6. ¿Cuáles son las dos formas de identificación más utilizadas por los sistemas de autenticación? Seleccione dos respuestas
- [ ] Huella dactilar
- [x] Nombre de usuario
- [x] Password (Contraseña)
- [ ] Escaneado facial
> Correcto

6. ¿Qué factores utilizan los sistemas de autenticación para verificar la identidad de un usuario? Seleccione tres respuestas
- [x] Conocimientos
- [x] Responsabilidad
- [ ] Contabilización
- [x] Característica
> Correcto

7. ¿Cuál es la ventaja de utilizar sistemas de inicio de sesión único (SSO) para autenticar a los usuarios?
- [x] Hace que el proceso de inicio de sesión sea más rápido.
- [ ] Evita los ataques de relleno de credenciales.
- [ ] Los usuarios deben establecer varias contraseñas.
- [ ] Los usuarios pierden el acceso a múltiples plataformas cuando el sistema está inactivo.
> Correcto

7. ¿Cuál es la desventaja de utilizar la tecnología de inicio de sesión único (SSO) para la autenticación de usuarios?
- [x] Las credenciales robadas pueden dar a los atacantes acceso a múltiples recursos.
- [ ] Los empleados son más vulnerables a los ataques.
- [ ] Clientes reciben una experiencia del usuario mejorada.
- [ ] Se agiliza la gestión de nombres de usuario y contraseñas.
> Correcto

8. En un negocio hay una persona que recibe el dinero de los Clientes en la caja registradora. Al final del día, otra persona cuenta ese dinero recibido con los artículos vendidos y lo deposita. ¿Qué principios de Seguridad se implementan en las operaciones de Negocio a negocio? Seleccione dos respuestas
- [ ] Autenticación de múltiples factores
- [x] Menor privilegio
- [x] Separación de funciones
- [ ] Inicio de sesión único
> Correcto

8. Una empresa de transporte importa y exporta Materiales por todo el mundo. Sus operaciones comerciales incluyen la compra de mercancías a proveedores, la recepción de envíos y la distribución de mercancías a minoristas. ¿Cómo debe proteger la naviera sus recursos según el principio de Separación de funciones? Seleccione dos respuestas
- [ ] Hacer que un empleado reciba los envíos y distribuya las mercancías
- [ ] Hacer que un empleado seleccione las mercancías y envíe los pagos
- [x] Hacer que un empleado apruebe los pedidos de compra
- [x] Hacer que un empleado archive los pedidos de compra
> Correcto

9. ¿Qué tipo de información sobre el usuario contiene un Token de API? Seleccione dos respuestas
- [x] Permisos del sitio de un usuario
- [ ] La contraseña de un usuario
- [x] La identidad de un usuario
- [ ] La clave secreta de un usuario
> Correcto

9. ¿Cuáles son las herramientas comunes de autorización diseñadas teniendo en cuenta el principio de privilegio mínimo y la separación de funciones? Seleccione tres respuestas
- [x] OAuth
- [x] Autenticación básica
- [x] Token de API
- [ ] SHA256
> Correcto

10. Un cliente de un minorista en línea se ha quejado de que su cuenta contiene una compra no autorizada. Usted investiga el incidente revisando los registros de acceso del minorista. ¿Qué componente de la Sesión del usuario podría revisar?
- [ ] Certificado de Sesión
- [ ] Algoritmo de Sesión
- [x] Cookie de sesión
- [ ] Clave de API de sesión
> Correcto

10. ¿En qué consiste la práctica de monitorizar los registros de acceso de un sistema?
- [ ] Contabilización (? Posible correcta)
- [ ] Auditoría (Incorrecto)
- [ ] Autenticación
- [ ] Autorización
> Incorrecto

10. Su Equipo de Seguridad recibe una alerta del servidor de inicio de sesión de la organización sobre múltiples intentos fallidos de inicio de sesión. La alerta indicaba que se habían producido 10 intentos fallidos de inicio de sesión en la base de datos de clientes de la empresa en la última hora. ¿Qué es lo primero que debe hacer para investigar este incidente?
- [x] Realice la contabilización en los registros de acceso del sistema.
- [ ] Ignore la alerta hasta que reciba más quejas de los usuarios.
- [ ] Desactive el servidor de la base de datos de clientes.
- [ ] Devuelva el sistema operativo de servidor a una versión anterior.
> Correcto