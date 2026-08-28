# Revisión: Vulnerabilidades en los sistemas

## Resumen
- ​Este entorno está lleno de brechas que los atacantes pueden ​utilizar para obtener acceso no autorizado a los recursos, ​lo que supone un reto para la defensa.
- ​Hemos explorado mucha información en esta ocasión, ​así que recapitulemos rápidamente lo que hemos cubierto.
- ​Aprendió sobre el proceso de Gestión de vulnerabilidades, ​empezando por el Modelo de defensa en profundidad.
- ​Aprendió sobre las capas de ​este framework de Seguridad y ​cómo cada una de ellas trabajan juntas ​para construir una defensa más fuerte.
- ​A continuación, conoció la Lista CVE ​que se utiliza para encontrar vulnerabilidades catalogadas.
- ​Es un gran complemento para ​su creciente caja de herramientas de seguridad.
- ​Después, conoció ​las superficies de ataque que protegen las empresas.
- ​Discutimos las superficies físicas y digitales ​y los retos de defender la Nube.
- ​Terminamos explorando los Vectores de ataque comunes, ​donde aprendió cómo los Equipos de Seguridad ​utilizan una mentalidad de atacante para ​identificar las brechas de seguridad ​que los ciberdelincuentes intentan explotar.
- ​Cada una de las vulnerabilidades que hemos discutido ​hasta ahora se enfrenta a una serie de amenazas.
- Vamos a ampliar nuestra mentalidad de atacantes ​aún más ​explorando el tipo específico de ataques ​que los ciberdelincuentes utilizan habitualmente.
- ​Veremos cosas como el software malicioso y las técnicas ​que los atacantes utilizan para comprometer los sistemas de defensa.
- Explorando cómo funcionan estas herramientas y tácticas, ​obtendrá una comprensión más clara ​de las amenazas que plantean.
- Concluiremos investigando cómo los Equipos de Seguridad ​evitan que estas amenazas ​dañen las operaciones de nuestras organizaciones, ​su Reputación y, lo que es más importante, ​sus Clientes y Empleados.

---

## Términos del glosario del Módulo 3
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del Módulo 3

1. Una cadena hotelera tiene routers WiFi obsoletos en las habitaciones de sus huéspedes. Un atacante pirateó los dispositivos y robó información confidencial de varios huéspedes. El router WiFi anticuado es un ejemplo de ¿qué?
- [ ] Un Control de acceso
- [ ] Una hazaña
- [ ] Una Amenaza
- [x] Una vulnerabilidad
> Correcto

1. Una aplicación ha roto los Controles de acceso que no restringen a ningún usuario la creación de nuevas cuentas. Esto permite que cualquiera pueda añadir nuevas cuentas con plenos privilegios de administrador. ¿Los Controles de acceso rotos de la aplicación son un ejemplo de qué?
- [ ] Una hazaña
- [ ] Una Amenaza
- [ ] Un control de seguridad
- [x] Una vulnerabilidad
> Correcto

2. Rellene el espacio en blanco: Las cinco capas del modelo de defensa en profundidad son: perímetro, red, punto final, aplicación y _____
- [ ] físico
- [ ] transporte
- [ ] sesión
- [x] datos
> Correcto

2. ¿Por qué las organizaciones utilizan el Modelo de defensa en profundidad para proteger la Información? Seleccione dos respuestas
- [x] Las defensas en capas reducen el Riesgo al abordar múltiples vulnerabilidades.
- [ ] Los Equipos de Seguridad pueden determinar fácilmente el "quién, qué, cuándo y cómo" de un ataque.
- [ ] Cada capa utiliza tecnologías únicas que se comunican entre sí.
- [x] Las amenazas que penetran en un nivel pueden ser contenidas en otro.
> Correcto

3. ¿Cuál es la diferencia entre las capas de aplicación y de datos del modelo de defensa en profundidad?
- [ ] La capa de Datos sólo permite a los empleados acceder a la Información. La capa de aplicación asegura la Información con controles que se programan en la propia aplicación.
- [ ] La capa de aplicación mantiene la integridad de la Información con controles como la encriptación y el hash. La capa de datos bloquea el tráfico de red procedente de sitios web no fiables.
- [x] La capa de aplicación asegura la información con controles que se programan en la propia aplicación. La capa de datos mantiene la integridad de la Información con controles como la encriptación y el hash.
- [ ] La capa de Datos incluye controles como la encriptación y el hash para asegurar los Datos en reposo. La capa de aplicación protege los dispositivos individuales que están conectados a una red.
> Correcto

3. ¿Qué capa del modelo de defensa en profundidad está relacionada con los dispositivos de los usuarios que han accedido a una red?
- [ ] Aplicación
- [ ] Perímetro
- [x] Punto de conexión
- [ ] Datos
> Correcto

3. El firewall de una organización está configurado para permitir el tráfico sólo desde direcciones IP autorizadas. ¿A qué capa del Modelo de defensa en profundidad está asociado el firewall?
- [ ] Aplicación
- [ ] Datos
- [ ] Punto de conexión
- [x] Red
> Correcto

4. ¿Cuál es el objetivo principal de la Lista de vulnerabilidades y exposiciones comunes (CVE®)?
- [ ] Proporcionar a las organizaciones un framework para gestionar los riesgos de ciberseguridad
- [ ] Crear un diccionario de las amenazas a los recursos de la organización que deben abordarse
- [x] Compartir una forma estándar de identificar y categorizar las vulnerabilidades y exposiciones conocidas
- [ ] Para llevar un registro de los errores de programación de los principales desarrolladores de software
> Correcto

4. Rellene el espacio en blanco: Según la Lista de vulnerabilidades y exposiciones comunes (CVE®), una vulnerabilidad con una puntuación de _____ o superior se considera un Riesgo crítico para los recursos de la empresa que debe abordarse de inmediato.
- [ ] 11
- [ ] 4
- [ ] 1
- [x] 9
> Correcto

5. ¿Cuál es el objetivo de la gestión de vulnerabilidades? Seleccione tres respuestas
- [x] Identificar las exposiciones a las amenazas internas y externas
- [x] Descubrir vulnerabilidades y reducir su exploit
- [x] Revisar los sistemas de Seguridad internos de una organización
- [ ] Seguimiento de los recursos y de los riesgos que les afectan (Incorrecto)
> Correcto

5. ¿Cuáles de las siguientes son características del proceso de gestión de vulnerabilidades? Seleccione dos respuestas.
- [ ] La Gestión de vulnerabilidades debería ser un proceso único.
- [ ] La Gestión de vulnerabilidades es una forma de descubrir nuevos recursos.
- [x] La Gestión de vulnerabilidades es una forma de limitar los Riesgos de Seguridad.
- [x] La Gestión de vulnerabilidades debe considerar varias perspectivas.
> Correcto

6. Un Equipo de Seguridad está llevando a cabo una evaluación periódica de la vulnerabilidad de sus Procedimientos de Seguridad. Su Objetivo es revisar las lagunas en sus Procedimientos actuales que podrían conducir a una violación de datos. Tras identificar y analizar los Procedimientos actuales, el Equipo lleva a cabo una Evaluación de riesgos. ¿Cuál es el objetivo de realizar una Evaluación de riesgos?
- [x] Para puntuar las vulnerabilidades en función de su gravedad e impacto
- [ ] Para simular los ataques que podrían realizarse contra cada vulnerabilidad
- [ ] Solucionar las vulnerabilidades que se hayan identificado
- [ ] Ajustar los actuales Procedimientos de Seguridad
> Correcto

6. Durante una evaluación de vulnerabilidades, un escáner identifica un servidor in situ vulnerable. Tras analizar el servidor, usted descubre que a su sistema operativo le faltan actualizaciones críticas. ¿Cuál es el siguiente paso que debe dar en el proceso de evaluación de vulnerabilidades?
- [ ] Escanee los millones de dispositivos que se conectan al servidor.
- [x] Realice una Evaluación de riesgos del antiguo sistema operativo.
- [ ] Desactive el servidor porque su sistema operativo está obsoleto.
- [ ] Descarte el sistema operativo obsoleto porque el aparato está operativo.
> Correcto

7. Rellene el espacio en blanco: Todas las vulnerabilidades potenciales que un agente de amenaza podría explotar se denomina ataque _____
- [ ] vector
- [x] superficie
- [ ] red
- [ ] base de datos
> Correcto

7. ¿Cuáles de los siguientes son tipos de superficies de ataque? Seleccione tres respuestas
- [x] Servidores en la Nube
- [ ] Software malicioso
- [x] Routers de red
- [x] Puestos de ordenador
> Correcto

8. Rellene el espacio en blanco: Un ataque _____ se refiere a las vías que utilizan los atacantes para penetrar las defensas de Seguridad.
- [ ] paisaje
- [x] vector
- [ ] superficie
- [ ] vulnerabilidad
> Correcto

8. Rellene el espacio en blanco: Un ataque _____ se refiere a las vías que utilizan los atacantes para penetrar las defensas de Seguridad
- [x] vector
- [ ] vulnerabilidad
- [ ] paisaje
- [ ] superficie
> Correcto

9. ¿Cuáles de las siguientes son razones por las que los equipos de Seguridad practican una mentalidad de ataque? Seleccione tres respuestas
- [x] Descubrir vulnerabilidades que deben ser monitorizadas
- [ ] Para explotar fallos en la base de código de una aplicación (Incorrecto)
- [x] Identificar vectores de ataque
- [ ] Para encontrar estadísticas sobre los mejores Controles de seguridad a utilizar
> Incorrecto

9. Un Equipo de Seguridad está realizando una evaluación de vulnerabilidades en una aplicación bancaria que está a punto de ser publicada. Su objetivo es identificar las herramientas y métodos que podría utilizar un atacante. ¿Qué pasos de la mentalidad de un atacante debería realizar el Equipo para averiguarlo? Seleccione tres respuestas
- [x] Identifique un objetivo.
- [x] Determine cómo se puede acceder al objetivo.
- [x] Evaluar los Vectores de ataque que pueden ser explotados.
- [ ] Considere los posibles agentes de amenaza.
> Correcto

9. ¿Qué fase viene después de identificar un objetivo cuando se practica una mentalidad de atacante?
- [ ] Determine cómo se puede acceder al objetivo.
- [ ] Encuentre las herramientas y los métodos de ataque.
- [ ] Preparar las defensas contra las amenazas.
- [ ] Evaluación de los vectores de ataque del objetivo. (Incorrecto)
> Incorrecto

10. ¿Qué no es un paso de la práctica de una mentalidad de ataque?
- [ ] Evaluar los Vectores de ataque que pueden ser explotados.
- [ ] Encuentre las herramientas y los métodos de ataque.
- [x] Identificar formas de solucionar las vulnerabilidades existentes.
- [ ] Determinar cómo se puede acceder a un objetivo.
> Correcto

10. Considere el siguiente escenario: Usted trabaja como profesional de la Seguridad para un distrito escolar. Un desarrollador de aplicaciones del distrito escolar ha creado una aplicación que conecta a los estudiantes con recursos educativos. Le han asignado la tarea de evaluar la Seguridad de la aplicación. Utilizando una mentalidad de atacante, ¿cuál de los siguientes pasos daría para evaluar la aplicación? Seleccione dos respuestas
- [x] Identifique los tipos de usuarios que interactuarán con la aplicación.
- [ ] Asegúrese de que el formulario de inicio de sesión de la aplicación funciona.
- [x] Evalúe cómo gestiona la aplicación los datos de los usuarios.
- [ ] Integrar la aplicación con los Recursos educativos existentes.
> Correcto