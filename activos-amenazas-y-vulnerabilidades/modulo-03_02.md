# Identificar las vulnerabilidades del sistema

## Evaluaciones de vulnerabilidades
- ​Hemos hablado de cómo las vulnerabilidades ​influyen en el diseño de las defensas.
- ​También hemos hablado de cómo ​se comparten las vulnerabilidades comunes.
- ​Un tema que nos queda por cubrir es ​cómo se encuentran las vulnerabilidades en primer lugar.
- Las debilidades y los defectos generalmente ​se encuentran durante una evaluación de vulnerabilidades.
- ​Una evaluación de vulnerabilidades es ​el proceso de revisión interna de ​los sistemas de seguridad de una organización.
- Estas evaluaciones funcionan de forma similar al proceso de ​identificación y categorización de vulnerabilidades ​en la Lista de CVE.
- ​La principal diferencia es ​que el Equipo de Seguridad de la organización las realiza, ​evalúa, puntúa y corrige por su cuenta.
- ​Los analistas de seguridad desempeñan ​una función clave en todo este proceso.
- ​En general, el objetivo de ​una evaluación de vulnerabilidades es ​identificar puntos débiles y prevenir ataques.
- ​También son el modo en que los equipos de seguridad determinan si ​sus controles de seguridad cumplen los Estándares normativos.
- ​Las organizaciones realizan evaluaciones de vulnerabilidades con mucha frecuencia.
- ​Dado que las empresas tienen tantos recursos ​que proteger, los Equipos de seguridad ​a veces tienen que seleccionar en qué área ​centrarse a través de las evaluaciones de vulnerabilidades.
- ​Una vez que deciden en qué centrarse, ​las evaluaciones de vulnerabilidades suelen seguir ​un proceso de cuatro pasos.
- ​El primer paso es la identificación.
   - ​Aquí se utilizan herramientas de exploración y ​pruebas manuales para encontrar vulnerabilidades.
   - ​Durante el paso de identificación, ​el objetivo es comprender ​el estado actual de un sistema de seguridad, ​como si se tomara una fotografía del mismo.
   - ​Una gran cantidad de hallazgos ​suelen aparecer tras la identificación.
- ​El siguiente paso del proceso es el Análisis de vulnerabilidades.
   - ​Durante este paso, se comprueba cada una de ​las vulnerabilidades que se identificaron.
   - ​Al ser un detective digital, el objetivo del ​análisis de vulnerabilidades es ​encontrar el origen del problema.
- ​El tercer paso del proceso es la Evaluación de riesgos.
   - ​Durante este paso del proceso, ​se asigna una puntuación a cada vulnerabilidad.
   - ​Esta puntuación se asigna en función de dos factores: ​la gravedad del impacto que tendría si se ​explotara la vulnerabilidad y la probabilidad de que esto ocurra.
   - ​Las vulnerabilidades descubiertas durante ​los dos primeros pasos de este proceso ​a menudo superan en número a las personas disponibles para solucionarlas.
   - ​Las evaluaciones de riesgos son una forma de priorizar los recursos para ​manejar las vulnerabilidades que deben ​atenderse en función de su puntuación.
- ​El cuarto y último paso de ​la evaluación de vulnerabilidades es la reparación.
   - ​Durante este paso se abordan las vulnerabilidades ​que pueden afectar a la organización.
   - ​La reparación se produce en función ​de la puntuación de gravedad asignada ​durante el paso de Evaluación de riesgos.
   - ​Esta parte del proceso suele ser ​un esfuerzo conjunto entre el personal de Seguridad y los equipos de ​informática para idear el mejor enfoque para ​corregir las vulnerabilidades que se descubrieron anteriormente.
   - ​Ejemplos de pasos de reparación pueden incluir ​cosas como hacer cumplir nuevos procedimientos de seguridad, ​actualizar sistemas operativos, ​o implementar parches del sistema.
   - ​Las evaluaciones de vulnerabilidades son estupendas ​para identificar los fallos de un sistema.
- ​La mayoría de las organizaciones las utilizan para ​buscar problemas antes de que se produzcan.

---

## Enfoques para la exploración de vulnerabilidades
- Una organización realiza evaluaciones de vulnerabilidad para identificar debilidades y prevenir ataques.
- Las herramientas de exploración de vulnerabilidades se utilizan habitualmente para simular amenazas encontrando vulnerabilidades en una superficie de ataque.
- También ayudan a los Equipos de Seguridad a tomar medidas proactivas para implementar su estrategia de remediación.
- Los escáneres de vulnerabilidades son herramientas importantes que probablemente utilizará sobre el terreno.
- En esta lectura, explorará cómo funcionan los escáneres de vulnerabilidades y los tipos de escaneos que pueden realizar.

- ¿Qué es un escáner de vulnerabilidades?
   - Un escáner de vulnerabilidades es un software que compara automáticamente las vulnerabilidades y exposiciones conocidas con las tecnologías de la red.
   - En general, estas herramientas escanean los sistemas para encontrar errores de configuración o de programación.
   - Las herramientas de escaneado se utilizan para analizar cada una de las cinco superficies de ataque:
      1. Capa de perímetro, como los sistemas de autenticación que validan la accesibilidad de los usuarios
      2. Capa de red, que se compone de tecnologías como firewalls de red y otras
      3. Capa de punto final, que describe los dispositivos de una red, como ordenadores portátiles, de sobremesa o servidores
      4. Capa de aplicación, que implica el software con el que interactúan los usuarios
      5. Capa de datos, que incluye cualquier información almacenada, en tránsito o en uso
   - Cuando comienza un escaneado de cualquier capa, la herramienta de escaneado compara los hallazgos con las bases de datos de amenazas a la seguridad.
   - Al final de la exploración, la herramienta marca cualquier vulnerabilidad que encuentre y la añade a su base de datos de referencia.
   - Cada exploración añade más información a la base de datos, lo que ayuda a la herramienta a ser más precisa en su análisis.
   - Las bases de datos de vulnerabilidades también son actualizadas rutinariamente por la empresa que diseñó el software de exploración.

- Realización de exploraciones
   - Los escáneres de vulnerabilidades están pensados para no ser intrusivos.
   - Es decir, no rompen ni se aprovechan de un sistema como lo haría un atacante.
   - En su lugar, simplemente escanean una superficie y le alertan de cualquier puerta potencialmente desbloqueada en sus sistemas.
   - Aunque los escáneres de vulnerabilidades no son intrusivos, hay casos en los que un escáner puede causar problemas inadvertidamente, como bloquear un sistema.
   - Estas herramientas se utilizan de varias maneras para escanear una superficie.
   - Cada enfoque corresponde a la vía que podría seguir un Agente de amenaza.
   - A continuación, puede explorar cada tipo de escaneado para tener una idea más clara al respecto.

- Externo frente a interno
   - Los escaneos externos e internos simulan el enfoque de un atacante.
   - Los escaneos externos prueban la capa perimetral fuera de la red interna.
   - Analizan sistemas orientados al exterior, como sitios web y firewalls.
   - Este tipo de exploraciones pueden descubrir puntos vulnerables, como puertos de red o servidores vulnerables.
   - Los escaneos internos parten del extremo opuesto, examinando los sistemas internos de una organización.
   - Por ejemplo, este tipo de escaneado podría analizar el software de aplicación en busca de puntos débiles en la forma en que gestiona la entrada de datos de los usuarios.

- Autenticación frente a no autenticación
   - Los escaneos autenticados y no autenticados simulan si un usuario tiene o no acceso a un sistema.
   - Los escaneos autenticados pueden probar un sistema registrándose con una cuenta de usuario real o incluso con una cuenta de administrador.
   - Estas cuentas de servicio se utilizan para comprobar vulnerabilidades, como controles de acceso rotos.
   - Los escaneos no autenticados simulan agentes de amenaza externos que no tienen acceso a los recursos de su empresa.
   - Por ejemplo, un escaneado podría analizar los recursos compartidos de archivos dentro de la organización que se utilizan para albergar documentos exclusivamente internos.
   - Los usuarios no autentificados deberían recibir resultados de "acceso denegado" si intentaran abrir estos archivos.
   - Sin embargo, se identificaría una vulnerabilidad si pudieran acceder a un archivo.

- Limitado frente a exhaustivo
   - Los escaneos limitados y exhaustivos se centran en dispositivos concretos a los que acceden usuarios internos y externos.
   - Los escaneos limitados analizan dispositivos concretos de una red, como la búsqueda de errores de configuración en un firewall.
   - Los escaneos exhaustivos analizan todos los dispositivos conectados a una red.
   - Esto incluye sistemas operativos, bases de datos de usuarios, etc.
   - La exploración de descubrimiento debe realizarse antes de las exploraciones limitadas o exhaustivas.
   - La exploración de descubrimiento se utiliza para hacerse una idea de las computadoras, dispositivos y puertos abiertos que hay en una red.