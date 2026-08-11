# Herramientas importantes de ciberseguridad

## Bienvenido al Módulo 4
- aprenderás sobre la información de Seguridad y las herramientas de ​gestión de eventos (SIEM, por sus siglas en inglés)
- También conocerá otras herramientas, como los manuales de ​estrategias y los analizadores de protocolos de red
- Luego, aprenderá sobre el sistema operativo Linux y ​las tareas relacionadas con la seguridad que se inician mediante ​lenguajes de programación, como SQL y Python. 
- SQL permite explorar ​las diferentes fuentes de datos que recopilamos ​y permite a mi equipo analizar los datos en busca de tendencias

---

## Herramientas comunes de ciberseguridad
- Si identificas una fuga, ​no importa el color o la forma del balde que utilices para recoger el agua
- Lo importante es mitigar los riesgos y ​amenazas a su hogar mediante el uso de las herramientas que tiene a su disposición
- analizaremos ​los principales propósitos y funciones ​de algunas herramientas de Seguridad de uso común
- Logs (registros)
   - Un registro es un registro de los eventos que ​se producen en los sistemas de una organización
   - Entre los ejemplos de registros relacionados con la seguridad se incluyen los registros de ​empleados que inician sesión en sus ordenadores ​o acceden a servicios basados en la web
   - Los registros ayudan a los profesionales de la seguridad a identificar ​las vulnerabilidades y posibles infracciones de seguridad
- Las primeras herramientas que analizaremos son las herramientas de ​administración de información y eventos de seguridad, ​o herramientas SIEM
- ​Una herramienta SIEM es una aplicación que recopila y analiza los ​datos de registro para monitorear ​las actividades críticas de una organización
- Las herramientas SIEM recopilan información en tiempo real o instantánea ​y permiten a los analistas de Seguridad ​identificar posibles infracciones a medida que ocurren. 
- ​Imagine tener que leer páginas y páginas de ​registros para determinar si hay alguna amenaza de Seguridad. ​Según la cantidad de datos, ​puede tardar horas o días
- ​Las herramientas de SIEM reducen la cantidad de datos que un analista debe ​revisar al proporcionar alertas para ​tipos específicos de riesgos y amenazas
- ejemplos de herramientas SIEM de uso común: ​Splunk y Chronicle
   - Splunk
      - Splunk es una plataforma de análisis de datos ​y Splunk Enterprise ofrece soluciones SIEM.
      - ​Splunk Enterprise es una herramienta autohospedada que se utiliza para retener ​, analizar y buscar los datos de registro de una organización
   - Chronicle
      - ​Chronicle es una herramienta SIEM nativa de la nube que ​almacena datos de Seguridad para su búsqueda y análisis
      - Nativo en la nube significa que ​Chronicle permite la entrega rápida de nuevas funciones
- Ambas herramientas de SIEM, y los SIEM en general, ​recopilan datos de varios lugares y ​luego los analizan y filtran ​para permitir a los equipos de seguridad prevenir y ​reaccionar rápidamente ante posibles amenazas de seguridad
- Según la configuración del SIEM y el enfoque de riesgo de su organización, ​las herramientas y su funcionamiento pueden diferir, ​pero en última instancia, todas se utilizan para mitigar el riesgo
- Otras herramientas clave que utilizará en ​su función de analista de Seguridad, ​y que tendrá la ​oportunidad práctica de utilizar más adelante en el ​programa, son los manuales de estrategias (Playbooks) y los analizadores de protocolos de red
   - Playbooks
      - es un manual que ​proporciona detalles sobre cualquier acción operativa, ​como la forma de responder a un incidente. 
      - Varían de una organización a otra, ​guían a los analistas sobre cómo ​gestionar un incidente de Seguridad antes ​, durante y después de que se produzca
      - pueden referirse a las ​revisiones de Seguridad o cumplimiento, la administración del acceso ​y muchas otras tareas organizativas que ​requieren un proceso documentado de principio a fin
   - Analizadores de protocolos de red (Packet sniffer)
      - Un rastreador de paquetes es una herramienta diseñada para ​capturar y analizar el tráfico de datos dentro de una red
      - Entre los ​analizadores de protocolos de red más comunes se ​incluyen tcpdump y Wireshark

---

## Herramientas para proteger las operaciones de Negocio a negocio (Business-to-Business)
- El kit de herramientas de un analista de nivel básico
   - Herramientas de administración de información y eventos de seguridad (SIEM)
      - Una herramienta SIEM es una aplicación que recopila y analiza datos de registro para monitorizar las actividades críticas de una organización
      - Un registro A es un registro de los eventos que se producen en los sistemas de una organización
      - Las herramientas SIEM reducen la cantidad de datos que un analista debe revisar proporcionando alertas para tipos específicos de amenazas, riesgos y vulnerabilidades
      - Las distintas herramientas SIEM tienen diferentes tipos de paneles que muestran la información a la que se tiene acceso.
      - Las herramientas SIEM también vienen con diferentes opciones de alojamiento, incluyendo on-premise y en la nube
      - Las organizaciones pueden elegir una opción de alojamiento sobre otra basándose en la experiencia de un miembro del equipo de Seguridad
      - Por ejemplo, debido a que una versión alojada en la nube tiende a ser más fácil de configurar, utilizar y mantener que una versión in situ, un Equipo de seguridad con menos experiencia puede elegir esta opción para su organización.
   - Analizadores de protocolos de red (packet sniffers)
      - Un analizador de protocolos de red, también conocido como rastreador de paquetes, es una herramienta diseñada para capturar y analizar el tráfico de datos en una red
      - Esto significa que la herramienta mantiene un registro de todos los datos que encuentra una computadora dentro de la red de una organización
   - Manuales de estrategias (Playbooks)
      - Es un manual que proporciona detalles sobre cualquier acción operativa, como por ejemplo cómo responder a un incidente de seguridad
      - Las organizaciones suelen tener varios manuales de estrategias que documentan los procesos y procedimientos que deben seguir sus equipos
      - Los manuales de estrategias varían de una organización a otra, pero todos tienen un propósito similar: guiar a los analistas a través de una serie de pasos para completar tareas específicas relacionadas con la Seguridad.
      - ejemplo
         - Usted trabaja como analista de Seguridad para una empresa de Respuesta ante incidentes
         - Se le asigna un caso relacionado con una pequeña consulta médica que ha sufrido una brecha de Seguridad
         - Su trabajo consiste en ayudar en la investigación forense y proporcionar pruebas a una compañía de seguros de ciberseguridad
         - A continuación, utilizarán sus conclusiones de la investigación para determinar si la práctica médica recibirá el pago de su seguro.
         - En este escenario, los manuales de estrategias describirían las acciones específicas que debe llevar a cabo para realizar la investigación
         - Los manuales de estrategias también le ayudarán a asegurarse de que sigue los protocolos y procedimientos adecuados
         - Tipos de manuales
            - Playbook de la cadena de custodia (Playbook chain of custody)
               - La cadena de custodia es el proceso de documentación de la posesión y el control de las pruebas durante el ciclo de vida de un incidente
               - Como analista de seguridad que participa en un análisis forense, trabajará con los datos informáticos que fueron violados
               - Usted y el equipo forense también tendrán que documentar quién, qué, dónde y por qué tiene las pruebas recogidas.
               - Las pruebas son su responsabilidad mientras estén en su posesión.
               - Las pruebas deben mantenerse seguras y rastreadas
               - Cada vez que se trasladen las pruebas, deberá informarse de ello
               - Esto permite que todas las partes implicadas sepan exactamente dónde están las pruebas en todo momento.
            - Manual de protección y preservación de evidencias (Playbook evidence protection and preservation)
               - Proteger y preservar evidencias es el proceso de trabajar adecuadamente con evidencias digitales frágiles y volátiles
               - ASÍ, como analista de Seguridad, es fundamental comprender qué son las pruebas digitales frágiles y volátiles y por qué existe un procedimiento
               - A medida que siga este Manual de estrategias, consultará el Orden de volatilidad, que es una secuencia que describe el orden de los datos que deben conservarse del primero al último
               - Da prioridad a los Datos volátiles, que son aquellos que pueden perderse si el dispositivo en cuestión se apaga, independientemente del motivo
               - Mientras se lleva a cabo una investigación, una gestión inadecuada de las pruebas digitales puede comprometer y alterar dichas pruebas
               - Cuando las pruebas se gestionan de forma inadecuada durante una investigación, ya no pueden utilizarse
               - Por esta razón, la primera prioridad en cualquier investigación es preservar adecuadamente los datos.
               - Puede preservar los Datos haciendo copias y llevando a cabo su investigación utilizando esas copias.