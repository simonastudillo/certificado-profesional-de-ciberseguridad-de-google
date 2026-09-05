# Visión general de los sistemas de detección de intrusos (IDS)

## Vigilancia de la seguridad con herramientas de detección
- ​La detección requiere datos, y ​estos datos pueden provenir de varias fuentes de datos.
- ​Ya ha explorado cómo ​diferentes dispositivos producen registros.
- ​Ahora examinaremos cómo diferentes tecnologías de detección ​vigilan dispositivos y ​registran diferentes tipos de actividad del sistema, ​como la telemetría de red y de punto final.
- ​La telemetría es la recopilación y ​transmisión de datos para su análisis.
- ​Mientras que los registros registran los eventos que ocurren en los sistemas, ​la telemetría describe los datos en sí.
- ​Por ejemplo, las capturas de paquetes ​se consideran telemetría de red.
- ​Para los profesionales de la Seguridad, ​los registros y la telemetría son fuentes de ​evidencias que pueden utilizarse para ​responder preguntas durante las investigaciones.
- ​Previamente, usted aprendió sobre ​un sistema de detección de intrusiones, o IDS.
- ​Recuerde que IDS es una aplicación que ​monitorea la actividad y alerta sobre posibles intrusiones.
- ​Esto incluye monitorear diferentes partes de ​un sistema o red como un punto final.
- ​Un punto final es cualquier dispositivo ​conectado a una red, como un ordenador portátil, ​una tableta, un ordenador de sobremesa o un smartphone.
- ​Los puntos finales son puntos de entrada a ​una red, lo que los convierte en objetivos ​clave para los actores maliciosos que buscan obtener ​acceso no autorizado a un sistema.
- ​Para monitorizar los puntos finales en busca de amenazas o ataques, ​se puede utilizar un sistema de detección de intrusiones basado en el anfitrión.
- ​Se trata de una aplicación que monitoriza ​la actividad del anfitrión en el que está instalada.
- ​Para aclarar, un host es cualquier dispositivo que ​se comunica con otros dispositivos de una red, ​similar a un punto final.
- ​Los sistemas de detección de intrusiones basados en host ​se instalan como un agente en un único host, ​como un ordenador portátil o un servidor.
- ​Dependiendo de su configuración, ​los sistemas de detección de intrusiones basados en host ​monitorearán el host ​en el que está instalado para detectar actividades sospechosas.
- ​Una vez que se ha detectado algo, ​registra la salida en forma de registros y se genera una alerta.
- ​¿Y si quisiéramos supervisar una red?
- ​Un sistema de detección de intrusiones basado en red recopila ​y analiza el tráfico y los datos de red.
- ​Los sistemas de detección de intrusiones basados en red ​funcionan de forma similar a los rastreadores de paquetes ​porque analizan el tráfico de red y ​los datos de red en un punto específico de la red.
- ​Es habitual implementar varios sensores IDS en ​diferentes puntos de la red ​para lograr una visibilidad adecuada.
- ​Cuando se detecta actividad sospechosa o inusual en la red, ​el Sistema de detección de intrusiones basado en la red ​la registra y genera una alerta.
- ​En este ejemplo, el ​sistema de detección de intrusiones basado en redes está ​vigilando el tráfico que proviene ​de Internet y que se dirige a Internet.
- ​Los sistemas de detección de intrusiones utilizan ​diferentes tipos de métodos de detección.
- ​Uno de los métodos más comunes es el Análisis de firmas.
- ​El Análisis de firmas es un Método de detección ​utilizado para encontrar Eventos de Interés.
- ​Una firma especifica un conjunto de reglas a las que un ​IDS hace referencia cuando monitorea la actividad.
- ​Si la actividad coincide con las reglas de la firma, ​el IDS la registra y envía una alerta.
- ​Por ejemplo, una firma puede ​escribirse para generar una alerta si ​un inicio de sesión fallido en un sistema se produce tres veces seguidas, ​lo que sugiere un posible ataque de descifrado de contraseña.
- ​Antes de que se generen las alertas, ​la actividad debe registrarse.
- ​Las tecnologías IDS registran la información de los dispositivos, ​sistemas y redes que monitorizan como registros IDS.
- ​Los registros IDS pueden enviarse, almacenarse, ​y analizarse en un repositorio de registros centralizado como un SIEM.

---

## Herramientas y técnicas de detección
- También explorará las dos técnicas de Detección más comunes utilizadas por los sistemas de detección.
- Comprender las capacidades y limitaciones de las tecnologías IDS y sus técnicas de detección le ayudará a interpretar la información de seguridad para identificar, analizar y responder a los eventos de seguridad.
- Un Sistema de detección de intrusiones (IDS) es una aplicación que monitoriza la actividad del sistema y alerta sobre posibles intrusiones.
- Las tecnologías IDS ayudan a las organizaciones a supervisar la actividad que se produce en sus sistemas y redes para identificar indicios de actividad maliciosa.
- Dependiendo del lugar que elija para instalar un IDS, éste puede estar basado en el host o en la red.

- Sistema de detección de intrusiones basado en el anfitrión
   - Un Sistema de detección de intrusiones basado en el anfitrión (HIDS) es una aplicación que monitoriza la actividad del anfitrión en el que está instalado.
   - Un HIDS se instala como un agente en un host.
   - Un host también se conoce como punto final, que es cualquier dispositivo conectado a una red como una computadora o un servidor.
   - Normalmente, los agentes HIDS se instalan en todos los puntos finales y se utilizan para Monitorear y Detectar Amenazas a la Seguridad.
   - Un HIDS monitoriza la actividad interna que tiene lugar en el host para identificar cualquier comportamiento no autorizado o anómalo.
   - Si se detecta algo inusual, como la instalación de una aplicación no autorizada, el HIDS lo registra y envía una alerta.
   - Además de monitorizar los flujos de tráfico entrante y saliente, HIDS puede tener capacidades adicionales, como monitorizar los sistemas de archivos, el uso de recursos del sistema, la actividad de los usuarios, etc.
   
- Sistema de detección de intrusiones basado en la red
   - Un Sistema de detección de intrusiones basado en la red (NIDS) es una aplicación que recoge y monitoriza el Tráfico de red y los Datos de red.
   - El software NIDS se instala en dispositivos situados en partes específicas de la red que se desea supervisar.
   - La aplicación NIDS inspecciona el tráfico de red procedente de distintos dispositivos de la red.
   - Si se detecta algún tráfico de red malicioso, el NIDS lo registra y genera una alerta.
   - El uso de una combinación de HIDS y NIDS para monitorizar un entorno puede proporcionar un enfoque multicapa para la detección de intrusiones y la respuesta a las mismas.
   - Las herramientas HIDS y NIDS proporcionan una perspectiva diferente de la actividad que se produce en una red y en los hosts individuales que están conectados a ella.
   - Esto ayuda a proporcionar una visión completa de la actividad que se produce en un entorno.

- Técnicas de Detección
   - Los sistemas de Detección pueden utilizar diferentes técnicas para detectar amenazas y ataques.
   - Los dos tipos de técnicas de detección que suelen utilizar las tecnologías IDS son el Análisis basado en firmas y el Análisis basado en anomalías.
 
- Análisis basado en firmas
   - El análisis de firmas, o Análisis basado en firmas, es un Método de Detección que se utiliza para encontrar Eventos de Interés.
   - Una Firma es un Patrón que se asocia con una actividad maliciosa.
   - Las Firmas pueden contener patrones específicos como una secuencia de números binarios, bytes, o incluso datos específicos como una dirección IP.
   - Anteriormente, usted exploró la Pirámide del Dolor, que es un concepto que prioriza los diferentes tipos de Indicadores de compromiso (IoC) asociados con un ataque o amenaza, como direcciones IP, Herramientas, Tácticas, Técnicas y más.
   - Los IoC y otros Indicadores de ataque pueden ser útiles para crear firmas específicas para detectar y bloquear ataques.
   - Se pueden utilizar distintos tipos de firmas en función del tipo de amenaza o ataque que se desee detectar.
   - Por ejemplo, una firma antimalware contiene patrones asociados al software malicioso.
   - Esto puede incluir secuencias de comandos maliciosas que utiliza el software malicioso.
   - Las Herramientas IDS monitorizarán un entorno en busca de eventos que coincidan con los patrones definidos en esta Firma de software malicioso.
   - Si un evento coincide con la firma, el evento se registra y se genera una alerta.

- Ventajas
   - Baja tasa de falsos positivos:
      - El análisis basado en firmas es muy eficaz a la hora de detectar amenazas conocidas, ya que se limita a comparar la actividad con las firmas.
      - Esto conduce a un menor número de falsos positivos.
      - Recuerde que un falso positivo es una alerta que detecta incorrectamente la presencia de una amenaza.
- Desventajas
   - Las Firmas pueden ser evadidas:
      - Las firmas son únicas y los atacantes pueden modificar sus comportamientos de ataque para eludirlas.
      - Por ejemplo, los atacantes pueden realizar ligeras modificaciones en el código del software malicioso para alterar su firma y evitar la Detección.
   - Las firmas requieren actualizaciones:
      - El Análisis basado en firmas se basa en una Base de datos de firmas para Detectar amenazas.
      - Cada vez que se descubre un nuevo exploit o ataque, deben crearse nuevas firmas y añadirse a la base de datos de firmas.
   - Incapacidad para detectar amenazas desconocidas:
      - El análisis basado en firmas se basa en la detección de amenazas conocidas mediante firmas.
      - No se pueden detectar las amenazas desconocidas, como las nuevas familias de software malicioso o los ataques de Día cero, que son exploits hasta ahora desconocidos. 

- Análisis basado en anomalías
   - El análisis basado en anomalías es un Método de Detección que identifica comportamientos anómalos.
   - El Análisis basado en anomalías consta de dos fases: una fase de Entrenamiento y una fase de Detección.
   - En la fase de Entrenamiento, debe establecerse una línea de base del comportamiento normal o esperado.
   - Las líneas de base se desarrollan recopilando datos que corresponden al comportamiento normal del sistema.
   - En la fase de Detección, la actividad actual del sistema se compara con esta línea de base.
   - La actividad que se produce fuera de la línea de base se registra y se genera una alerta.
      - Ventajas
         - Capacidad para detectar amenazas nuevas y en evolución:
            - A diferencia del análisis basado en firmas, que utiliza patrones conocidos para detectar amenazas, el análisis basado en anomalías puede detectar amenazas desconocidas.
      - Desventajas
         - Alto índice de falsos positivos:
            - Cualquier comportamiento que se desvíe de la línea de base puede ser marcado como anómalo, incluidos los comportamientos no maliciosos.
            - Esto conduce a una alta tasa de falsos positivos.
         - Compromiso pre existente:
            - La existencia de un atacante durante la fase de Entrenamiento incluirá comportamientos maliciosos en la línea de base.
            - Esto puede llevar a pasar por alto a un atacante preexistente.

---

## Gracia: Mentalidad de seguridad en la detección y respuesta
- Hola, soy Grace, y trabajo en Detección y Respuesta en Google.
- ​Cuando le cuento a la gente lo que hago, piensan que es increíble, ​Me encanta poder decir, mi trabajo es detectar hackers que intentan hackear Google.
- ​Hay gente que nos confía sus datos y que desempeña funciones críticas en la sociedad, ​como periodistas y activistas, por ejemplo.
- ​Así que necesitan poder tener sus datos con nosotros y ​confiar en que van a estar seguros.
- ​La mentalidad de seguridad tiene que ver con la curiosidad.
- ​Hay un solapamiento realmente agradable entre la ciberseguridad y la informática y ​tener esa salida creativa y lógica y un interés por los grandes asuntos del mundo.
- ​Lo que piensan los hackers, lo que piensan los defensores.
- ​Siento empatía por la gente que busca cómo se puede ​obtener información, quizás a veces de fuentes inusuales.
- ​Un ejemplo de una de las cosas más locas de las que me he enterado sería cómo ​la gente puede obtener información de una CPU.
- ​Algunas tareas para una CPU son más difíciles que otras, ​requieren más energía para hacer multiplicar números como ejemplo de ello, ​lo que significa que la CPU va a trabajar más, ​se va a calentar más, va a estar ejecutando más funciones.
- ​Así que puedes usar esa información para saber cosas sobre lo que está haciendo esa CPU.
- ​A partir de ahí, puedes empezar a deducir lo que está pasando en un momento dado.
- ​Lo que recomiendo a la gente que esté interesada en desarrollar una ​mentalidad de seguridad es escuchar historias.
- ​Hay Pódcast que tienen grandes entrevistas con hackers.
- ​Recomiendo seguir las noticias y leer artículos sobre las distintas ​amenazas cibernéticas que están sucediendo en el mundo.
- ​Recomiendo ir a conferencias, ir a meetups, ​encontrar gente con la que puedas estudiar y practicar.
- ​Incluso los hackers se enseñan unos a otros cómo hackear cosas en foros y salas de chat.
- ​No es hacer trampas pedir ayuda.
- ​Otro consejo que tengo para ​la gente sería que no se rindan cuando se encuentren con obstáculos.
- ​Estudiar el certificado es una muy buena idea, y ​realmente merece la pena perseverar hasta el final.
- ​Incluso cuando se ponga difícil y empiece a sentirse abrumado, no pasa nada, ​son términos nuevos.
- ​Puedo garantizarle que si vuelve a retomarlo más adelante, le resultará más familiar.
- ​Le resultará más fácil.
- ​Ser realmente amable consigo mismo y comprensivo y ​paciente le ayudará mucho cuando se enfrente a estos retos.

---

## Componentes de una firma de detección
- Como analista de Seguridad, ​puede que se le encargue escribir, ​personalizar o probar firmas.
- ​Para ello, utilizará herramientas de IDS.
- ​Una firma especifica las reglas de detección.
- ​Estas reglas describen los tipos de ​intrusiones en la red que desea que detecte un IDS.
- ​Por ejemplo, una firma puede ​escribirse para detectar y alertar ​sobre el tráfico sospechoso que intenta conectarse a un puerto.
- ​El lenguaje de las reglas difiere según los ​diferentes sistemas de detección de intrusiones en la red.
- ​El término Sistema de detección de intrusiones en la red ​se abrevia a menudo ​como el acrónimo N-I-D-S y se pronuncia NIDS.
- ​Generalmente, las reglas NIDS constan de tres componentes: ​una acción, un encabezado y las opciones de la regla.
- ​Ahora, examinemos cada uno de ​estos tres componentes con más detalle.
- ​Típicamente, la acción es ​el primer elemento especificado en una Firma.
- ​Determina la acción que se llevará a cabo si se cumplen ​los criterios de la regla.
- ​Las acciones difieren según el lenguaje de las reglas NIDS, ​pero algunas acciones comunes son: alertar, pasar o rechazar.
- ​Usando nuestro ejemplo, si una regla especifica alertar sobre ​tráfico de red sospechoso que ​establece una conexión inusual a un puerto, ​el IDS inspeccionará ​los paquetes de tráfico y enviará una alerta.
- ​El Encabezado define el Tráfico de red de la firma.
- ​Incluye información como ​direcciones IP de origen y destino, ​puertos de origen y destino, ​protocolos y dirección del tráfico.
- ​Si queremos detectar una alerta sobre ​tráfico sospechoso que se conecta a un puerto, ​tenemos que definir primero el origen ​del tráfico sospechoso en la cabecera.
- ​El tráfico sospechoso puede originarse desde ​direcciones IP externas a la red local.
- ​También puede utilizar protocolos específicos o inusuales.
- ​Podemos especificar direcciones IP externas ​y estos protocolos en la cabecera.
- ​Aquí tiene un ejemplo de cómo ​puede aparecer la información de la cabecera en una regla básica.
```snort
tcp 10.120.170.17 any -> 133.113.202.181 80
```
- ​En primer lugar, podemos observar que el protocolo, ​TCP, es el primer elemento de la lista de la Firma.
- ​A continuación, se especifica que la dirección IP de origen ​10.120.170.17 y el número de puerto de origen ​son cualquiera.
- ​La flecha en el centro de la firma ​indica la dirección del Tráfico de red.
- ​Así que sabemos que se origina en la IP de origen ​10.120.170.17 desde cualquier puerto ​y va al siguiente destino ​Dirección IP 133.113.202.181 y puerto de destino 80.
- ​Las opciones de la regla le permiten personalizar ​las firmas con parámetros adicionales.
- ​Hay muchas opciones diferentes disponibles para utilizar.
- ​Por ejemplo, puede establecer opciones para que coincidan ​con el contenido de un paquete de red ​para detectar cargas útiles maliciosas.
- ​Las cargas útiles maliciosas residen en los datos de un paquete y realizan ​actividades maliciosas como borrar o encriptar datos.
- ​Configurar las opciones de las reglas ayuda ​a delimitar el tráfico de red, ​para que pueda encontrar exactamente lo que busca.
- ​Típicamente, las opciones de regla están separadas por ​semicolones y encerradas entre paréntesis.
- ​En este ejemplo, podemos examinar ​que las opciones de regla están encerradas entre ​un par de paréntesis y están ​también separadas con semicolones.
- ​La primera opción de regla, msg, ​que significa mensaje, ​proporciona el texto de la alerta.
- ​En este caso, la alerta imprimirá el texto: ​"Esto es un mensaje."
- ​También está la opción sid, ​que significa ID de firma.
- ​Así se asigna un identificador único a cada Firma.
- ​La opción rev significa revisión.
- ​Cada vez que se actualiza o cambia una Firma, ​el número de revisión cambia.
- ​Aquí, el número 1 significa ​que es la primera versión de la Firma.

---

## Examinar firmas con Suricata
- ​​Muchas tecnologías NIDS vienen con firmas pre-escritas.
- ​Puede pensar en estas firmas como plantillas personalizables.
- ​Es algo así como las diferentes plantillas disponibles en un procesador de textos.
- ​Estas plantillas de firmas le proporcionan un punto de partida para escribir y ​definir sus reglas.
- También puede escribir y añadir sus propias reglas.
- ​Examinemos una firma preescrita a través de Suricata.
- ​En este equipo Linux con Ubuntu, Suricata ya está instalado.
- ​Examinemos algunos de sus archivos cambiando de directorio al directorio etc ​y al directorio suricata.
- ​Aquí es donde se encuentran todos los archivos de configuración de Suricata.
- ​A continuación, utilizaremos el comando ls para listar el contenido del directorio suricata.
- ​Aquí hay un par de archivos diferentes, pero nos centraremos en la carpeta rules.
- ​Aquí es donde están las firmas preescritas.
- ​También puede añadir firmas personalizadas aquí.
- ​Utilizaremos el comando cd seguido del nombre de la carpeta para navegar hasta esa ​carpeta.
- ​Usando el comando ls, podemos observar que la carpeta contiene algunas plantillas de reglas ​para diferentes protocolos y servicios.
- ​Examinemos las personalizadas.rules utilizando el comando less.
- ​A modo de recordatorio rápido, el comando less devuelve el contenido de un archivo ​una página cada vez, lo que facilita avanzar y retroceder por el contenido.
- ​Utilizaremos la clave de flecha para desplazarnos hacia arriba.
- ​Las líneas que comienzan con un signo de almohadilla (#) son comentarios destinados a proporcionar contexto a ​quienes los lean y son ignorados por Suricata.
- ​La primera línea dice Ejemplo de reglas personalizadas para conexión HTTP.
- ​Esto nos indica que este archivo contiene reglas personalizadas para conexiones HTTP.
- ​Podemos observar que hay una firma.
- ​La primera palabra especifica la ACCIÓN de la firma.
- ​Para esta firma, la acción es alerta.
- ​Esto significa que la firma genera una alerta cuando se cumplen todas las condiciones.
- ​La siguiente parte de la firma es el ENCABEZADO.
- ​Especifica el protocolo http. La dirección IP de origen es HOME_NET y ​el puerto de origen se define como ANY.
- ​La flecha indica la dirección del tráfico que procede de la red doméstica y ​se dirige a la dirección IP de destino EXTERNAL_NET y al puerto de destino ANY.
- ​Hasta ahora, sabemos que esta firma activa una alerta cuando detecta cualquier tráfico HTTP ​que salga de la red doméstica y se dirija a la red externa.
- ​Examinemos el resto de la firma para identificar si hay alguna ​condición adicional que la firma busque.
- ​La última parte de la firma incluye las OPCIONES DE LA REGLA.
- ​Están encerradas entre paréntesis y separadas por punto y coma.
- ​Hay muchas opciones enumeradas aquí, pero nos centraremos en las opciones de mensaje, flujo y ​contenido.
- ​La opción de mensaje mostrará el mensaje "GET on wire" una vez que se active la alerta.
- ​La opción de flujo se utiliza para coincidir en la dirección del flujo de tráfico de red.
- ​Aquí se establece.
- ​Esto significa que se ha establecido con éxito una conexión.
- ​La opción de contenido inspecciona el contenido de un paquete.
- ​Aquí, entre las comillas, se especifica el texto GET.
- ​GET es una petición HTTP que se utiliza para recuperar y solicitar datos a un servidor.
- ​Esto significa que la Firma coincidirá si un paquete de red contiene el texto GET, ​indicando una petición.
- ​En resumen, esta Firma alerta cada vez que Suricata observa el texto GET en ​una conexión HTTP desde la red doméstica, que va a la red externa.
- ​Cada entorno es diferente y para que ​un IDS sea eficaz, las firmas deben probarse y adaptarse.
- ​Como analista de Seguridad, puede probar, modificar o ​crear firmas IDS para mejorar la detección de amenazas en un entorno y ​reducir la probabilidad de falsos positivos.