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

---

## Supervisión continua de CI/CD
- Monitorización continua de CI/CD: encontrar amenazas automáticamente
   - La supervisión de su canalización CI/CD ayuda a proteger su cadena de suministro de software y existen herramientas especiales que pueden encontrar automáticamente actividades inusuales y ayudarle a identificar Indicadores de Compromiso (IoC).

- Automatización para encontrar amenazas
   - Los procesos CI/CD le ayudan a liberar software más rápidamente, pero también pueden abrir nuevas vulnerabilidades para los atacantes.
   - Si alguien irrumpe en su canalización, podría añadir código, robar información privada o impedir que su software funcione.
   - Por lo tanto, la supervisión continua que detecta automáticamente la actividad inusual de la canalización es fundamental.
   - La supervisión eficaz de CI/CD utiliza la automatización para hacer algo más que recopilar registros.
   - Utiliza herramientas de supervisión para encontrar automáticamente cosas inusuales que ocurren en los procesos de construcción, código o pasos de despliegue que pueden indicar posibles amenazas a la seguridad.
   - Cuando se detectan estas amenazas, los equipos de seguridad pueden responder rápidamente y limitar los daños.
   - Esta detección automática de amenazas es uno de los principales objetivos de una seguridad CI/CD sólida.

- Indicadores comunes de compromiso (IoC) en los conductos de CI/CD
   - Comprender los IoC comunes de CI/CD le ayuda a supervisar de forma eficaz y a encontrar rápidamente incidentes de seguridad.
   - He aquí algunos ejemplos:
      - Cambios de código no autorizados:
         - Cambios de código realizados por personas que no deberían realizarlos.
         - Cambios de código realizados en momentos inusuales o desde lugares inesperados.
         - Cambios de código que parecen sospechosos, como código confuso, eliminaciones muy grandes sin una buena razón, o código que no sigue las reglas de codificación.
      - Patrones de despliegue sospechosos:
         - Despliegues en sistemas inusuales o no aprobados (por ejemplo, despliegues de producción iniciados directamente desde ramas de desarrollador).
         - Despliegues que se producen en momentos inesperados o con demasiada frecuencia (despliegues fuera de los plazos de lanzamiento previstos).
         - Despliegues iniciados por cuentas de usuario inusuales o cuentas automatizadas que no deberían estar liberando a producción.
      - Dependencias comprometidas:
         - Encontrar vulnerabilidades conocidas (CVEs) en dependencias durante comprobaciones automatizadas en la canalización CI/CD.
         - Adición repentina de dependencias nuevas e inesperadas a las configuraciones de compilación.
         - Intentos de descargar dependencias de fuentes no oficiales o no fiables.
      - Ejecución inusual de la canalización:
         - Pasos del pipeline que normalmente funcionan bien y de repente fallan.
         - Los pipelines tardan mucho más en ejecutarse sin una razón clara.
         - Cambios en el orden o la forma en que se ejecutan los pasos del pipeline sin que se hayan realizado cambios aprobados.
      - Intentos de exposición de secretos:
         - Registros que muestran intentos de acceder a secretos desde lugares no aprobados en el pipeline.
         - Descubrimiento de secretos privados codificados en cambios de código (lo ideal sería evitarlo antes, pero la supervisión puede detectar errores).

- Seguridad proactiva mediante la supervisión de IoC
   - La supervisión continua de los procesos CI/CD, centrada en la detección automatizada de anomalías y la búsqueda de IoC, refuerza la seguridad y la hace más proactiva.
   - Mediante el uso de herramientas de supervisión para comprobar continuamente la actividad de las canalizaciones en busca de estos indicadores antes de que se produzcan daños graves, puede:
      - Responder rápidamente a los incidentes:
         - Encontrar los IoC en una fase temprana ayuda a los equipos de seguridad a responder rápidamente a posibles ataques, deteniendo los problemas antes de que los atacantes alcancen sus objetivos.
         - Limitar los daños:
            - Responder rápidamente basándose en la detección de IoCs reduce el posible impacto de un problema de seguridad al limitar el tiempo que los atacantes están en la tubería.
      - Mejorar el conocimiento de las amenazas:
         - Comprobar los IoC proporciona información valiosa sobre cómo los atacantes están apuntando a su CI/CD, lo que ayuda a mejorar la seguridad y la caza de amenazas en el futuro.

- Uso de la automatización para encontrar anomalías e IoCs
   - Para supervisar las canalizaciones de CI/CD y encontrar amenazas automáticamente, puede utilizar estos métodos:
   - Registro y auditoría exhaustivos:
      - Los registros detallados son la base de la supervisión.
      - Los registros proporcionan los datos en bruto que las herramientas de supervisión comprueban en busca de actividad inusual y posibles indicadores de compromiso (IoC).
      - Los registros más comunes para encontrar anomalías incluyen:
         - Registros de ejecución de canalizaciones:
            - Para aprovechar eficazmente los registros de ejecución de canalizaciones para la supervisión de la seguridad, las herramientas especializadas emplean técnicas automatizadas de línea de base.
            - Estas herramientas analizan los registros de ejecuciones típicas y satisfactorias de canalizaciones CI/CD para establecer un perfil de funcionamiento normal.
            - Esta línea de base engloba indicadores clave de rendimiento, como la duración estándar de cada etapa del proceso y las tasas de éxito y fracaso esperadas.
            - Al supervisar continuamente los registros de ejecución y compararlos con esta línea de base establecida, las herramientas pueden detectar automáticamente actividades anómalas.
            - Las desviaciones de la norma, incluidos los pasos de la canalización que superan los tiempos de ejecución típicos, los errores inesperados o las alteraciones en el orden habitual de los pasos, se marcan como posibles indicadores de compromiso (IoC), lo que justifica un mayor escrutinio de seguridad.
         - Registros de confirmación de código:
            - Realiza un seguimiento de los cambios en el código de cada proceso.
            - Los cambios de código inusuales, como los cambios realizados por personas que no deberían estar realizando cambios, los cambios realizados a altas horas de la noche o los cambios con contenido sospechoso (como eliminaciones muy grandes o código confuso), son IoC importantes de supervisar.
         - Registros de acceso:
            - Las herramientas de monitorización pueden saber quién accede habitualmente a CI/CD.
            - Los inicios de sesión inusuales, como inicios de sesión desde diferentes países, intentos fallidos de inicio de sesión seguidos de un inicio de sesión exitoso, o intentos de inicio de sesión para cambiar configuraciones importantes de canalización, son fuertes indicadores de compromiso.
         - Registros de despliegue:
            - Las herramientas pueden saber con qué frecuencia se producen los despliegues y qué aspecto tienen.
            - Los despliegues inusuales, como los que se producen en momentos extraños o en lugares inesperados, pueden ser IoC.

- Integración de información de seguridad y gestión de eventos (SIEM)
   - Conectar sus registros de CI/CD a una herramienta SIEM puede ayudar a encontrar automáticamente anomalías a gran escala.
   - Las plataformas SIEM están hechas para:
      - Encontrar anomalías automáticamente:
         - Los SIEM utilizan el aprendizaje automático y el análisis para encontrar automáticamente patrones inusuales en los registros de CI/CD, que son posibles IoC para investigar.
      - Utilizar reglas para alertar sobre IoC conocidos:
         - Puede configurar reglas específicas en el SIEM para encontrar IoC de CI/CD conocidos.
         - Por ejemplo, las reglas pueden enviar alertas cuando:
            - Se detectan hashes de archivos maliciosos específicos (relacionados con ataques de CI/CD conocidos) en los resultados de la compilación.
            - Los servidores CI/CD se conectan a servidores de comando y control (C2) maliciosos conocidos (utilizando datos de inteligencia de amenazas).
            - Alguien intenta descargar o acceder a secretos privados fuera de los pasos aprobados del pipeline.

- Alertas y notificaciones en tiempo real
   - Las alertas automatizadas garantizan que los equipos de seguridad reciban notificaciones inmediatas sobre actividades inusuales y posibles IoC, para que puedan responder rápidamente.
   - Las alertas deben configurarse para:
      - Fallos de compilación inusuales:
         - Fallos repetidos en los pasos del proceso, especialmente después de cambios de código que no deberían causar fallos.
      - Cambios de código sospechosos (basados en anomalías):
         - Alertas enviadas por herramientas de análisis de código que encuentran cambios de código muy inusuales basados en el tamaño, autor o contenido confuso.
      - Intentos de exponer secretos:
         - Alertas enviadas por herramientas de seguridad cuando alguien intenta acceder o robar secretos de partes no aprobadas del pipeline.
      - Tráfico de red inusual:
         - Alertas de tráfico de red inusual desde servidores CI/CD, especialmente el tráfico que sale a ubicaciones desconocidas o sospechosas.

- Monitorización del rendimiento para encontrar IoAs y descubrir IoCs
   - La monitorización del rendimiento, aunque se utiliza principalmente para asegurarse de que las cosas están funcionando sin problemas, también puede ayudar indirectamente a encontrar IoCs.
   - Los problemas de rendimiento (Indicadores de Ataque - IoAs) como ralentizaciones repentinas o servidores CI/CD que se quedan sin recursos pueden llevar a comprobaciones más profundas que pueden descubrir IoCs.

- Exploración continua de vulnerabilidades
   - La comprobación periódica de la infraestructura de CI/CD en busca de puntos débiles puede detectar proactivamente partes vulnerables.
   - Esto incluye Vulnerabilidades y Exposiciones Comunes (CVEs) en herramientas CI/CD, plugins y contenedores.
   - Estos puntos débiles son IoC potenciales.
   - Destacan las áreas que necesitan ser parcheadas de inmediato para evitar ataques y un posible compromiso de la tubería.

- Recursos
   - [Optimización de registros para una canalización CI/CD más eficaz - Mejores prácticas](https://coralogix.com/blog/optimizing-logs-for-a-more-effective-ci-cd-pipeline/)
   - [Implementación de la IA en los procesos CI/CD: Una guía práctica](https://blog.axiomio.com/implementing-ai-in-ci-cd-pipelines-a-practical-guide-83466035e3c7)
   - [¿Qué es CI/CD? - Integración, entrega y despliegue continuos](https://www.threatintelligence.com/blog/continuous-integration-continuous-delivery)
   - [Canalizaciones CI/CD y DevOps: Una introducción](https://www.splunk.com/en_us/blog/learn/ci-cd-devops-pipeline.html)

---

## MK: Cambios en el sector de la ciberseguridad
- Hola, soy MK, Director de la Oficina del CISO para Google Nube.
- ​La función del Director de Seguridad de la Información es proteger Google Nube ​desde el punto de vista de la seguridad.
- ​Pero también garantizar que estamos proporcionando todas las herramientas y productos necesarios para ​que nuestros clientes puedan lograr sus resultados de seguridad también.
- ​Así que pasé varios años en el Gobierno de los EE.UU., 32 años de hecho, ​22 de los cuales los pasé como agente especial en la Oficina Federal de Investigación.
- ​Aproximadamente a mitad de mi carrera, ​tuve la oportunidad de cambiar a los carriles de la ciberseguridad, lo que inició, o ​debería decir, reinició mi interés por todo lo relacionado con las computadoras y la informática.
- ​Una de las cosas que le falta a la industria es un sentido de la agilidad, ​que el adversario tiene a raudales.
- ​Cuando identifican algo que les funciona, ​continúan machacándolo hasta que y a menos que haya un obstáculo.
- ​Y entonces, una vez que ese obstáculo se interpone en su camino, ​han demostrado una habilidad para pivotar fácilmente sus tácticas y técnicas de modo que ​puedan sortear el obstáculo en futuros intentos de acceder a entornos.
- ​Así que ninguno de nosotros puede predecir el futuro.
- ​No estamos en ningún tipo de fase final.
- ​Esta es una industria en continua evolución.
- ​Lo que sí se puede afirmar es que necesitamos estar preparados de diversas maneras ​para combatir lo que sin duda será un ataque persistente del adversario.
- ​Lo que eso requiere es un cierto sentido de la agilidad, ​hay que sentirse cómodo existiendo en lo desconocido.
- ​Pero también hay que tener la aptitud intelectual para poder digerir y ​formular nuevas soluciones sobre la marcha.
- ​Cero Confianza es una tendencia enorme en estos momentos porque ha sido tanto un deseo de ​la industria avanzar hacia la Cero Confianza, pero ​también un requisito en algunas zonas de todo el mundo.
- ​Confianza Cero es un movimiento que se aleja de la forma histórica en que hemos hecho la seguridad en ​el pasado.
- ​En términos de Layman, así que usted es un viajero de negocios, viaja ​con su portátil de negocios y se registra en su hotel al otro lado del mundo, ​y necesita prepararse y estar listo para una reunión de negocios que está a punto de ocurrir.
- ​Históricamente, usted querría ser capaz de atestiguar el hecho de que ese es ​un usuario previsto o cualificado dentro de la empresa que intenta acceder ​a esta información.
- ​Y sí, basándose en la información que usted tiene, la identidad y ​acoplando eso con la información del dispositivo, ese usuario y ese dispositivo deberían tener acceso a ​esta información y ser capaces de tomar una determinación al respecto.
- ​Creo que cuanto más invirtamos en el enfoque o ​arquitectura de Confianza Cero, llegaremos a un buen punto desde el que pivotar.
- ​Pero creo que mucho de lo que está por venir es desconocido, y ​eso significa aprendizaje continuo.
- ​Significa, exponerse continuamente a diferentes partes de la industria para ​que estemos preparados para lo que pueda ocurrir en el futuro. 