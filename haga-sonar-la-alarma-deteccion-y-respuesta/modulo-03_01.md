# Detección y verificación de incidentes

## Bienvenido al Módulo 3
- Las habilidades que está aprendiendo crearán una base sólida a medida que comience su ​carrera en seguridad.
- ​En la sección anterior, aplicó sus conocimientos sobre redes para profundizar ​en su comprensión del tráfico de red.
- ​Practicó algunas habilidades que los analistas de seguridad utilizan en el trabajo como ​captar el tráfico de red y diseccionar paquetes.
- ​A continuación, examinaremos el ciclo de vida de un incidente de seguridad de principio a fin.
- ​Se centrará en cómo detectar, responder y recuperarse de un incidente.
- ​A continuación, aprenderá a investigar y ​verificar un incidente una vez detectado.
- ​Explorará los planes y procesos que hay detrás de la respuesta ante incidentes.
- ​Por último, aprenderá sobre las acciones posteriores al incidente que las organizaciones ​toman para aprender y mejorar de la experiencia.
- ​Al final de esta sección, ​obtendrá una comprensión global del ciclo de vida de un incidente.

---

## La fase de detección y análisis del ciclo de vida
- ​Los incidentes ocurren y, como analista de seguridad, es probable que en algún momento de su carrera se le encargue ​investigar y responder a incidentes de seguridad.
- ​Examinemos la fase de Detección y Análisis del ciclo de vida de la respuesta ante incidentes.
- ​Aquí es donde los equipos de respuesta ante incidentes verifican y analizan los incidentes.
- ​La Detección permite el rápido descubrimiento de incidentes de Seguridad.
- ​Recuerde que no todos los incidentes son incidentes, pero todos los incidentes son eventos.
- ​Los eventos son sucesos regulares en las operaciones de negocio, como las visitas a un sitio web o ​las solicitudes de restablecimiento de contraseña.
- ​Las herramientas IDS y SIEM recopilan y ​analizan datos de incidentes de distintas fuentes para identificar posibles actividades inusuales.
- ​Si se detecta un incidente, como que un actor malicioso haya conseguido ​acceder sin autorización a una cuenta, entonces se envía una alerta.
- ​Los equipos de seguridad comienzan entonces la fase de Análisis.
- ​El análisis implica la investigación y validación de alertas.
- ​Durante el proceso de análisis, los analistas deben aplicar su pensamiento crítico y ​sus habilidades de análisis de incidentes para investigar y validar las alertas.
- ​Examinarán los indicadores de compromiso para determinar si se ha producido un incidente.
- ​Esto puede suponer un reto por un par de razones.
- ​El reto de la Detección es que es imposible detectarlo todo.
- ​Incluso las grandes herramientas de detección tienen limitaciones en su funcionamiento, y las herramientas automatizadas ​pueden no estar totalmente implementadas en toda una organización debido a la limitación de recursos.
- ​Algunos incidentes son inevitables, por lo que es importante que las ​organizaciones cuenten con un Plan de respuesta a incidentes.
- ​Los analistas suelen recibir un alto volumen de alertas por turno, ​a veces incluso miles.
- ​La mayoría de las veces, los altos volúmenes de alertas están causados por una configuración de alertas incorrecta.
- ​Por ejemplo, las reglas de alerta que son demasiado amplias y ​no están ajustadas al entorno de una organización crean falsos positivos.
- ​Otras veces, los altos volúmenes de alertas pueden ser alertas legítimas causadas ​por actores maliciosos que se aprovechan de una vulnerabilidad recién descubierta.
- ​Como analista de Seguridad, es importante que esté equipado para analizar ​alertas de forma eficaz.

---

## Métodos de detección de incidentes de ciberseguridad
- Los analistas de Seguridad utilizan herramientas de Detección para ayudarles a descubrir amenazas, pero existen métodos adicionales de Detección que también pueden ser utilizados.

- Métodos de Detección
   - Durante la fase de Detección y Análisis del ciclo de vida de la respuesta a incidentes, los Equipos de Seguridad reciben la notificación de un posible incidente y trabajan para investigarlo y verificarlo mediante la recopilación y el análisis de datos.
   - Como recordatorio, la Detección se refiere al descubrimiento prompt de los Eventos de Seguridad y el Análisis implica la investigación y validación de las alertas.
   - Como ha aprendido, un Sistema de detección de intrusiones (IDS) puede detectar posibles intrusiones y enviar alertas a los analistas de seguridad para que investiguen la actividad sospechosa.
   - Los analistas de seguridad también pueden utilizar herramientas de administración de información y eventos de seguridad (SIEM) para detectar, recopilar y analizar los datos de seguridad.
   - También ha aprendido que la Detección plantea retos.
   - Incluso los mejores Equipos de Seguridad pueden fallar en la detección de amenazas reales por una gran variedad de razones.
   - Por ejemplo, las herramientas de Detección sólo pueden detectar lo que los Equipos de Seguridad configuran para Monitorear.
   - Si no están bien configuradas, pueden no detectar actividades sospechosas, dejando los sistemas vulnerables a los ataques.
   - Es importante que los equipos de Seguridad utilicen métodos adicionales de Detección para aumentar su cobertura y precisión.

- Caza de amenazas
   - Las amenazas evolucionan y los atacantes avanzan en sus tácticas y técnicas.
   - La Detección automatizada e impulsada por la tecnología puede ser limitada a la hora de mantenerse al día con el panorama cambiante de las amenazas.
   - La detección impulsada por el hombre, como la caza de amenazas, combina el poder de la tecnología con un elemento humano para descubrir amenazas ocultas que las herramientas de detección no detectan.
   - La caza de amenazas es la búsqueda proactiva de amenazas en una red.
   - Los profesionales de la Seguridad utilizan la caza de amenazas para descubrir actividades maliciosas que no fueron identificadas por las herramientas de Detección y como una forma de realizar análisis adicionales sobre las detecciones.
   - La caza de amenazas también se utiliza para detectar amenazas antes de que causen daños.
   - Por ejemplo, el software malicioso sin archivos es difícil de identificar para las herramientas de Detección.
   - Es una forma de software malicioso que utiliza sofisticadas técnicas de evasión, como ocultarse en la memoria en lugar de utilizar archivos o aplicaciones, lo que le permite eludir los métodos tradicionales de Detección, como el Análisis de firmas.
   - Con la caza de amenazas, se utiliza la combinación del análisis humano activo y la tecnología para identificar amenazas como el software malicioso sin archivos.
   - Los especialistas en caza de amenazas se conocen como cazadores de amenazas.
   - Los cazadores de amenazas realizan investigaciones sobre amenazas y ataques emergentes y luego determinan la probabilidad de que una organización sea vulnerable a un ataque concreto.
   - Los cazadores de amenazas utilizan una combinación de Inteligencia sobre amenazas, Indicadores de compromiso, Indicadores de ataque y Aprendizaje automático para buscar amenazas en una organización.

- Inteligencia sobre amenazas
   - Las organizaciones pueden mejorar su capacidad de Detección manteniéndose al día sobre la evolución del panorama de las amenazas y comprendiendo la relación entre su entorno y los actores maliciosos.
   - Una forma de comprender las amenazas es utilizar la inteligencia sobre amenazas, que es información sobre amenazas basada en pruebas que proporciona contexto sobre las amenazas existentes o emergentes.
   - La inteligencia sobre amenazas puede proceder de fuentes privadas o públicas como:
      - Informes de la industria:
         - A menudo incluyen detalles sobre las Tácticas, Técnicas y Procedimientos (TTP) de los atacantes.
      - Avisos del Gobierno:
         - Al igual que los informes de la industria, los avisos gubernamentales incluyen detalles sobre la TTP de los atacantes.
      - Fuentes de datos sobre amenazas:
         - Los feeds de datos sobre amenazas proporcionan un flujo de datos relacionados con las amenazas que pueden utilizarse para ayudar a protegerse contra atacantes sofisticados como las amenazas persistentes avanzadas (APT).
         - Las APT son instancias en las que un actor de amenaza mantiene un acceso no autorizado a un sistema durante un largo periodo de tiempo.
         - Los Datos suelen ser una lista de indicadores como direcciones IP, dominios y hashes de archivos.
   - Puede resultar difícil para las organizaciones gestionar eficazmente grandes volúmenes de inteligencia sobre amenazas.
   - Las organizaciones pueden aprovechar una plataforma de inteligencia sobre amenazas (TIP), que es una aplicación que recopila, centraliza y analiza la inteligencia sobre amenazas procedente de distintas fuentes.
   - Las TIP proporcionan una plataforma centralizada para que las organizaciones identifiquen y prioricen las amenazas relevantes y mejoren su postura de Seguridad.
   - Las fuentes de datos de Inteligencia sobre amenazas se utilizan mejor para añadir contexto a las detecciones.
   - No deben dirigir las detecciones por completo y deben evaluarse antes de aplicarse a una organización.

- Ciberengaño
   - El engaño cibernético implica técnicas que engañan deliberadamente a los actores maliciosos con el objetivo de aumentar la Detección y mejorar las estrategias defensivas.
   - Los Honeypots son un ejemplo de mecanismo activo de ciberdefensa que utiliza la tecnología del engaño.
   - Los Honeypots son sistemas o Recursos que se crean como señuelos vulnerables a los ataques con el propósito de atraer a posibles intrusos.
   - Por ejemplo, tener un archivo falso con la etiqueta Información de la tarjeta de crédito del cliente - 2022 puede utilizarse para captar la actividad de actores maliciosos engañándoles para que accedan al archivo porque parece legítimo.
   - Una vez que un actor malicioso intenta acceder a este archivo, se alerta a los equipos de Seguridad.

- Recursos
   - [Un repositorio de información sobre la caza de amenazas de The ThreatHunting Project](https://www.threathunting.net/)
   - [Investigación sobre hackers patrocinados por el estado del Grupo de Análisis de Amenazas (TAG)](https://blog.google/threat-analysis-group/)