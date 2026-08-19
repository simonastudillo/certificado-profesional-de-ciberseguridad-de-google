# Endurecimiento de la red

## Prácticas de endurecimiento de la red
- El endurecimiento de la red se centra ​en el endurecimiento de la seguridad relacionada con la red, ​como el filtrado de puertos, los privilegios de acceso a la red, ​y la encriptación a través de redes.
- ​Ciertas tareas de endurecimiento de la red se realizan regularmente, ​mientras que otras se realizan ​una vez y luego se actualizan según sea necesario.
- ​Algunas tareas que se ​realizan regularmente son el mantenimiento de las reglas del firewall, ​el análisis de registros de red, las actualizaciones de parches y las copias de seguridad de servidores. 
- Antes, aprendió que un registro es un registro de ​eventos que ocurren dentro de los sistemas de una organización.
- ​El análisis de registros de red es el proceso de ​examinar los registros de red para identificar eventos de interés.
- ​Los equipos de seguridad utilizan una herramienta de análisis de registros ​o una herramienta de gestión de eventos e información de seguridad, ​también conocida como SIEM, ​para llevar a cabo el análisis de registros de red.
- ​Una herramienta SIEM es una aplicación que recopila y analiza ​datos de registro para supervisar ​actividades críticas en una organización.
- ​Reúne datos de seguridad de una red y ​presenta esos datos en un único cuadro de mandos.
- ​La interfaz del cuadro de mandos se denomina a veces ​un único panel de cristal.
- ​Un SIEM ayuda a los analistas a inspeccionar, analizar, ​y reaccionar ante eventos de seguridad ​en toda la red en función de su prioridad.
- ​Los informes del SIEM proporcionan una lista de ​vulnerabilidades de red nuevas o en curso ​y las enumeran en una escala ​de prioridad de alta a ​baja, en la que las vulnerabilidades de alta prioridad ​tienen un plazo mucho más corto para su mitigación.
- ​Ahora que hemos cubierto las tareas ​que se realizan con regularidad, ​examinemos las tareas que se realizan una vez.
- ​Estas tareas incluyen el filtrado de puertos en cortafuegos, ​los privilegios de acceso a la red y ​la encriptación para la comunicación, entre otras muchas cosas.
- ​Comencemos con el filtrado de puertos.
   - ​El filtrado de puertos puede formarse a través de la Red.
   - ​El filtrado de puertos es una función del cortafuegos que bloquea o ​permite ciertos números de puerto ​para limitar la comunicación no deseada.
   - ​Un principio básico es que ​los únicos puertos que son ​necesarios son los que están permitidos.
   - ​Cualquier puerto que no esté siendo utilizado por ​las operaciones normales de la red debe ser desautorizado.
   - ​Esto protege contra las vulnerabilidades de los puertos.
- ​Las redes deberían configurarse con ​los protocolos inalámbricos más actualizados ​disponibles y ​los protocolos inalámbricos más antiguos deberían desactivarse.
- ​Los analistas de seguridad también utilizan ​la segmentación de red para crear ​subredes aisladas para ​diferentes departamentos de una organización.
- ​Por ejemplo, podrían hacer una para ​el departamento de marketing y ​una para el departamento financiero.
- ​Esto se hace para que los problemas de ​cada subred no se extiendan por toda la empresa y ​sólo los usuarios especificados tengan acceso a ​la parte de la red que necesitan para su función.
- ​La segmentación de red también puede utilizarse ​para separar diferentes zonas de seguridad.
- ​Cualquier zona restringida de una red que contenga ​datos altamente clasificados o confidenciales ​debería estar separada del resto de la red.
- ​Por último, todas las comunicaciones de red deberían ​cifrarse utilizando los últimos estándares de cifrado.
- ​Los Estándares de encriptación son reglas o métodos utilizados para ​ocultar los datos salientes y ​descubrir o desencriptar los datos entrantes.
- ​Los datos en zonas restringidas deben ​tener unos Estándares de encriptación mucho más altos, ​lo que hace que sea más difícil acceder a ellos.

---

## Aplicaciones de Seguridad de red
- Cada dispositivo, herramienta o estrategia de seguridad implementada por los analistas de seguridad protege -o refuerza- aún más la red hasta que el propietario de la red está satisfecho con el nivel de seguridad.
- Este enfoque de añadir capas de seguridad a una red se conoce como defensa en profundidad.
- Aprenderás sobre el papel de cuatro dispositivos utilizados para proteger una red: cortafuegos, sistemas de detección de intrusiones, sistemas de prevención de intrusiones y herramientas de gestión de eventos e información de seguridad.
- Los profesionales de la seguridad de redes tienen la opción de utilizar cualquiera o todos estos dispositivos y herramientas dependiendo del nivel de seguridad que esperan alcanzar. 
- Esta lectura discutirá los beneficios de la seguridad por capas.
- Cada herramienta mencionada es una capa adicional de defensa que puede reforzar gradualmente una red, empezando por el nivel mínimo de seguridad (proporcionado sólo por un cortafuegos), hasta el nivel más alto de seguridad (proporcionado por la combinación de un cortafuegos, un dispositivo de detección y prevención de intrusiones y la monitorización de eventos de seguridad).

<img src="./resources/image-16.png" alt="Imagen que muestra las diferencias entre un cortafuegos, un IPS y un IDS." width="700">

- Cada herramienta tiene su propio lugar en la arquitectura de la red.
- Los analistas de seguridad deben comprender las topologías de red que se muestran en los diagramas.
- Cortafuegos
   - Hasta ahora en este curso, has aprendido sobre firewalls sin estado, firewalls con estado, y firewalls de próxima generación (NGFWs), y las ventajas de seguridad de cada uno de ellos.
   - La mayoría de los cortafuegos son similares en sus funciones básicas.
   - Los cortafuegos permiten o bloquean el tráfico basándose en un conjunto de reglas.
   - Cuando los paquetes de datos entran en una red, se inspecciona la cabecera del paquete y se permite o deniega en función de su número de puerto.
   - Los NGFW también pueden inspeccionar la carga útil de los paquetes.
   - Cada sistema debe tener su propio cortafuegos, independientemente del cortafuegos de red.

<img src="./resources/image-17.png" alt="Un cortafuegos rodeado de guiones que protege la red interna del tráfico de Internet que entra por el modelo." width="700">

- Sistema de detección de intrusos 
   - Un sistema de detección de intrusiones (IDS) es una aplicación que supervisa la actividad del sistema y alerta sobre posibles intrusiones.
   - Un IDS alerta a los administradores basándose en la firma del tráfico malicioso.
   - El IDS está configurado para detectar ataques conocidos.
   - Los sistemas IDS suelen olfatear los paquetes de datos mientras se mueven por la red y los analizan en busca de las características de ataques conocidos.
   - Algunos sistemas IDS no sólo buscan firmas de ataques conocidos, sino también anomalías que podrían ser el signo de actividad maliciosa.
   - Cuando el IDS descubre una anomalía, envía una alerta al administrador de la red, que puede investigar más a fondo.
   - Las limitaciones de los sistemas IDS son que sólo pueden buscar ataques conocidos o anomalías obvias.
   - Los ataques nuevos y sofisticados pueden no ser detectados.
   - La otra limitación es que el IDS no detiene realmente el tráfico entrante si detecta algo raro.
   - Depende del administrador de la red detectar la actividad maliciosa antes de que cause algún daño a la red.
   - Cuando se combina con un cortafuegos, un IDS añade otra capa de defensa.
   - El IDS se coloca detrás del cortafuegos y antes de entrar en la LAN, lo que permite al IDS analizar flujos de datos después de que el tráfico de red no permitido por el cortafuegos haya sido filtrado.
   - Esto se hace para reducir el ruido en las alertas IDS, también conocidas como falsos positivos.

<img src="./resources/image-18.png" alt="Un IDS rodea con un círculo la imagen de un conmutador, que se sitúa entre un cortafuegos y la red." width="700">

- Sistema de prevención de intrusiones 
   - Un sistema de prevención de intrusiones (IPS) es una aplicación que monitoriza la actividad del sistema en busca de actividades intrusivas y toma medidas para detener la actividad.
   - Ofrece incluso más protección que un IDS porque detiene activamente las anomalías cuando las detecta, a diferencia del IDS que simplemente informa de la anomalía a un administrador de red.
   - Un IPS busca firmas de ataques conocidos y anomalías en los datos.
   - Un IPS informa de la anomalía a los analistas de seguridad y bloquea un remitente específico o elimina paquetes de red que parecen sospechosos.
   - El IPS (como un IDS) se sitúa detrás del cortafuegos en la arquitectura de red.
   - Esto ofrece un alto nivel de seguridad porque los flujos de datos de riesgo se interrumpen incluso antes de que lleguen a las partes sensibles de la red.
   - Sin embargo, una limitación potencial es que está en línea: Si se rompe, se rompe la conexión entre la red privada e Internet.
   - Otra limitación de los IPS es la posibilidad de que se produzcan falsos positivos, lo que puede provocar que se elimine tráfico legítimo.

<img src="./resources/image-19.png" alt="Un IPS se sitúa entre un cortafuegos y la red interna." width="700">

- Dispositivos de captura completa de paquetes
   - Los dispositivos de captura de paquetes completos pueden ser increíblemente útiles para los administradores de red y los profesionales de la seguridad.
   - Estos dispositivos permiten grabar y analizar todos los datos que se transmiten por la red.
   - También ayudan a investigar las alertas creadas por un IDS.

- Información de seguridad y gestión de eventos 
   - Un sistema de gestión de eventos e información de seguridad (SIEM ) es una aplicación que recopila y analiza datos de registro para supervisar actividades críticas en una organización.
   - Las herramientas SIEM trabajan en tiempo real para informar de actividades sospechosas en un panel centralizado.
   - Además, las herramientas SIEM analizan los datos de registro de red procedentes de IDS, IPS, cortafuegos, VPN, proxies y registros DNS.
   - Las herramientas SIEM son una forma de agregar datos de eventos de seguridad para que aparezcan en un solo lugar y puedan ser analizados por los analistas de seguridad.
   - Es lo que se conoce como un único panel de cristal. 
   - A continuación, puede ver un ejemplo de un panel de la herramienta SIEM de Google Cloud, Chronicle. Chronicle es una herramienta nativa de la nube diseñada para retener, analizar y buscar datos.

<img src="./resources/image-20.png" alt="Imagen del cuadro de mandos de la Crónica" width="700">

- Splunk es otra herramienta SIEM común.
   - Splunk ofrece diferentes opciones de herramientas SIEM: Splunk Enterprise y Splunk Cloud, ambas opciones incluyen paneles detallados que ayudan a los profesionales de la seguridad a revisar y analizar los datos de una organización.
- También hay otras herramientas SIEM similares disponibles, y es importante que los profesionales de la seguridad investiguen las diferentes herramientas para determinar cuál es la más beneficiosa para la organización.
- Una herramienta SIEM no sustituye a los conocimientos de los analistas de seguridad ni a las actividades de mantenimiento de redes y sistemas que se tratan en este curso, sino que se utilizan en combinación con otros métodos de seguridad.
- Los analistas de seguridad suelen trabajar en un Centro de Operaciones de Seguridad (SOC) donde pueden supervisar la actividad en toda la red.
- A continuación, pueden utilizar sus conocimientos y experiencia para determinar cómo responder a la información en el tablero de instrumentos y decidir cuándo los eventos cumplen los criterios para ser escalados a la supervisión.

| Dispositivos/herramientas | Ventajas | Desventajas |
| ---------------------------- | ------------------------- | ------------------------- |
| Cortafuegos | Un cortafuegos permite o bloquea el tráfico basándose en un conjunto de reglas. | Un cortafuegos sólo es capaz de filtrar paquetes basándose en la información proporcionada en la cabecera de los paquetes. |
| Sistema de detección de intrusiones (IDS) | Un IDS detecta y alerta a los administradores sobre posibles intrusiones, ataques y otro tráfico malicioso. | Un IDS sólo puede buscar ataques conocidos o anomalías obvias; es posible que no detecte ataques nuevos y sofisticados. En realidad, no detiene el tráfico entrante. |
| Sistema de prevención de intrusiones (IPS) | Un IPS supervisa la actividad del sistema en busca de intrusiones y anomalías y actúa para detenerlas. | Un IPS es un dispositivo en línea. Si falla, se interrumpe la conexión entre la red privada e Internet. Puede detectar falsos positivos y bloquear el tráfico legítimo. |
| Información de seguridad y gestión de eventos (SIEM) | Una herramienta SIEM recopila y analiza los datos de registro de varios equipos de la red. Agrega los eventos de seguridad para su supervisión en un panel central. | Una herramienta SIEM sólo informa sobre posibles problemas de seguridad. No realiza ninguna acción para detener o prevenir eventos sospechosos. |


- La compra, instalación y mantenimiento de cada uno de estos dispositivos o herramientas cuesta dinero.
- Una organización puede necesitar contratar personal adicional para supervisar las herramientas de seguridad, como en el caso de un SIEM.
- Los responsables de la toma de decisiones tienen la tarea de seleccionar el nivel apropiado de seguridad basándose en el coste y el riesgo para la organización.