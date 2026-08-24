# Revisión: Bases de datos y SQL

## Diálogo con el entrenador: Explorar las aplicaciones de SQL en la seguridad
- Esto es lo que cubriremos:
   - Identificar el almacenamiento de datos de seguridad: Discutiremos dónde una empresa como SecureCorp almacenaría sus datos relacionados con la seguridad.
   - Conectar SQL con tareas de seguridad: Veremos por qué SQL es una habilidad valiosa para un profesional de seguridad y qué tareas se pueden realizar con él.
   - Aplicar SQL a escenarios de seguridad: Analizaremos cómo SQL puede usarse en situaciones de seguridad específicas.
   - Explorar usos más amplios de SQL: Pensaremos en otras formas en que los profesionales de seguridad utilizan SQL en su trabajo diario.

- Conversación con el entrenador: 

- ¡Genial! Para empezar, en una empresa hipotética como SecureCorp, ¿dónde crees que se almacenarían los datos relacionados con la seguridad, como registros de actividad o información de usuarios? Me refiero a los diferentes tipos de repositorios de datos que podrían usar.
> Dependiendo de la configuración que tenga la empresa, estos registros pueden quedan en los registros logs del servidor o en una base de datos relacional.

- ¡Muy bien! Has mencionado dos lugares clave: los registros del servidor (logs) y las bases de datos relacionales. Ambos son fundamentales para almacenar información de seguridad.
- Ahora, pensando en esos lugares donde se guarda la información, ¿por qué crees que la habilidad de usar SQL es tan valiosa para un profesional de seguridad en SecureCorp? ¿Cómo se conecta SQL con la interacción con esos datos?
> SQL nos permite buscar, filtrar y unir información de forma eficiente, rápida además de mantener un histórico

- ¡Exacto! Has dado en el clavo con la eficiencia y la capacidad de buscar, filtrar y unir información. Esas son ventajas clave de SQL. Ahora, pensando en tareas de seguridad específicas en SecureCorp, ¿qué tipo de actividades o investigaciones crees que un profesional de seguridad podría realizar de manera eficiente utilizando consultas SQL?
> En SQL podemos almacenar que usuarios se conectaron, a qué hora se conectaron, desde que IP lo hicieron y en algunos casos la ubicación geográfica, esto nos dan indicios de problemas de seguridad, intentos de fuerza bruta para entrar al sistema. Por ejemplo, podríamos ver los intentos de inicio de sesión fuera de horario laboral, intentos con IP que no son las habituales para los usuarios, etc.

- ¡Excelente ejemplo! Has identificado cómo SQL puede ser crucial para detectar actividades sospechosas como intentos de fuerza bruta o inicios de sesión anómalos. La capacidad de registrar y consultar datos como la hora de conexión, la IP y el usuario es fundamental para la seguridad.
- Ahora, pasemos a un escenario más específico. Imagina que en SecureCorp se ha detectado un aumento inusual de intentos de inicio de sesión fallidos para un usuario en particular. ¿Cómo usaría un analista de seguridad SQL para investigar este incidente y obtener la información relevante?
> Lo primero sería bloquear la cuenta de forma temporal mientras se analiza, luego se puede investigar los horarios, las IPs, de esta forma detectar si se trata de un intento legítimo o un intento de hackeo. Luego podemos solicitar al usuario el cambio de contraseña por una con mayor seguridad, bloquear las IPs al tener más de x intentos seguidos fallidos.

- ¡Muy bien! Has descrito pasos importantes para la gestión de un incidente de seguridad, como bloquear la cuenta y analizar los patrones de los intentos fallidos. Ahora, centrándonos en la parte de la investigación con SQL, ¿qué tipo de consulta SQL específica podrías usar para obtener la información sobre los horarios y las IPs de esos intentos de inicio de sesión fallidos para un usuario en particular? ¿Qué elementos de una tabla de registros de seguridad serían importantes para tu consulta?
> Podría hacer varias consultas al respecto, se me ocurre una consulta agrupando la cantidad de fallos por cuenta usando un count y group by. También podría hacer un select a la tabla de inicio de sesión y usar un where con el usuario con más intentos fallidos, ordenar por hora y/o IP para detectar patrones

- ¡Perfecto! Esas son excelentes ideas para usar SQL en este escenario. La combinación de COUNT y GROUP BY es muy útil para identificar la magnitud del problema por usuario, y el SELECT con WHERE y ORDER BY te permitiría examinar los detalles de cada intento fallido, buscando patrones en horarios e IPs.
- Ahora, pensemos en otro escenario. En SecureCorp, necesitan identificar sistemas que no tienen un parche de seguridad crítico instalado. ¿Cómo podría un analista de seguridad usar SQL para encontrar rápidamente todos los sistemas que están perdiendo este parche específico, asumiendo que tienen una base de datos con información de los sistemas y sus parches?
> Para ese caso podría hacer un SELECT a la tabla de machines donde patch_version no sea 'x' (WHERE NOT patch_version = 'x'), de esta forma sabremos que maquinas no tienen el último parche importante

- ¡Excelente! Esa es una forma muy efectiva de identificar los sistemas sin el parche. Asumiendo que tienes una tabla machines con una columna patch_version, tu consulta SELECT * FROM machines WHERE NOT patch_version = 'x' (o WHERE patch_version != 'x') te daría exactamente lo que necesitas. También podrías usar WHERE patch_version IS NULL si los sistemas sin parche no tienen ningún valor en esa columna.
- Ahora, ampliemos un poco más. ¿Se te ocurre alguna otra forma en que los profesionales de seguridad en SecureCorp podrían usar SQL en su trabajo diario, más allá de los escenarios específicos que hemos discutido, como para informes, verificaciones de cumplimiento o análisis de inteligencia de amenazas?
> Absolutamente, SQL nos permite guardar la información de nuestros sistemas, podemos guardar logs de quien, cómo y cuándo realizaron cambios. Esto nos permitiría realizar informes sobre cambios realizados, acciones realizadas o intentos de realizar acción sin permiso, acceso a información sensible entre otras cosas.

- ¡Fantástico! Has captado la esencia de cómo SQL va más allá de la investigación de incidentes. La capacidad de registrar y consultar quién, cómo y cuándo se realizaron cambios es fundamental para la auditoría, la generación de informes de cumplimiento y la detección de accesos no autorizados o intentos de manipulación de datos. Esto es clave para la inteligencia de amenazas y para mantener la integridad de los sistemas.
- ¡Buen trabajo, has completado todos los temas de nuestra sesión! A continuación, puedes ver tus comentarios.

- Tus fortalezas:
   - Demostraste una comprensión clara de cómo SQL puede ser utilizado para la detección de anomalías y la investigación de incidentes de seguridad, como los intentos de inicio de sesión fallidos.
   - Pudiste aplicar tus conocimientos de SQL para proponer soluciones prácticas en escenarios de seguridad, como la identificación de sistemas sin parches críticos y la auditoría de cambios en los sistemas.
- Áreas de mejora:
   - Aunque tus respuestas fueron muy buenas, podrías profundizar un poco más en la sintaxis específica de SQL para cada escenario, lo que te permitiría tener un control aún mayor sobre las consultas.

---

## Resumen
- Empezamos aprendiendo sobre ​la estructura de las bases de datos relacionales ​y cómo podemos acceder a ellas ​utilizando el lenguaje de consulta SQL.
- ​Después practicamos ​con la escritura de nuestras propias consultas SQL.
- ​Utilizamos SQL para obtener información que podría ​necesitar en el trabajo cuando trabaje como analista.
- ​Después nos centramos en los filtros SQL.
- ​Empezamos con condiciones sencillas con cadenas, ​y al final, aprendimos a utilizar ​múltiples filtros en una consulta.
- ​Concluimos la unidad con SQL ​joins y aprendimos a unir múltiples tablas, ​dándonos aún más información de una vez.