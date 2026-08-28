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

---

## La importancia de las actualizaciones
- Es posible que en algún momento se haya preguntado: "¿Por qué necesitan actualizarse constantemente mis dispositivos?"
- Para los consumidores, las actualizaciones proporcionan mejoras en el rendimiento, la estabilidad e incluso ¡nuevas funciones!
- Pero desde el punto de vista de la Seguridad, sirven a un propósito específico.
- Las actualizaciones permiten a las organizaciones abordar las vulnerabilidades de seguridad que pueden poner en peligro a sus usuarios, dispositivos y redes.
- Suelen tener lugar después de una evaluación de vulnerabilidades, que es el proceso de revisión interna de los sistemas de Seguridad de una organización.
- En esta lectura, aprenderá qué hacen las actualizaciones, cómo se suministran y por qué son importantes para la ciberseguridad.

- Parchear las lagunas de seguridad
   - Una computadora anticuada se parece mucho a una casa con las puertas sin cerrar.
   - Los actores maliciosos utilizan estas brechas en la Seguridad de la misma manera, para obtener accesibilidad no autorizada.
   - Las actualizaciones de software son similares a cerrar las puertas para mantenerlos fuera.
   - Una actualización de parche es una actualización de software y del sistema operativo que aborda las vulnerabilidades de seguridad dentro de un programa o producto.
   - Los parches suelen contener correcciones de errores que abordan vulnerabilidades y exposiciones de seguridad comunes.
   - Idealmente, los parches abordan las vulnerabilidades y exposiciones comunes antes de que los hackers maliciosos las encuentren.
   - Sin embargo, los parches se desarrollan a veces como resultado de un Día cero, que es un exploit desconocido hasta entonces.

- Estrategias comunes de actualización
   - Cuando las actualizaciones de software están disponibles, los clientes y usuarios tienen dos opciones de instalación:
      - Actualizaciones manuales
      - Actualizaciones automáticas
   - Cada estrategia tiene tanto beneficios como desventajas.

- Actualizaciones manuales
   - Una estrategia de implementación manual depende de que los departamentos de TI o los usuarios obtengan las actualizaciones de los desarrolladores.
   - Los entornos de oficina en casa o de pequeña empresa pueden requerir que usted mismo busque, descargue e instale las actualizaciones.
   - En entornos empresariales, el proceso suele gestionarse con una herramienta de administración de configuraciones.
   - Estas Herramientas ofrecen una serie de opciones para la implementación de actualizaciones, como a todos los clientes de su red o a un grupo selecto de usuarios.

   - Ventaja: Una ventaja de las estrategias de implementación manual de actualizaciones es el control. Esto puede ser útil si los desarrolladores no prueban a fondo las actualizaciones de software, lo que puede dar lugar a problemas de inestabilidad.

   - Desventaja: Una desventaja de la implementación manual de actualizaciones es que las actualizaciones críticas pueden olvidarse o ignorarse por completo.

- Actualizaciones automáticas
   - Una estrategia de implementación automática adopta el enfoque opuesto.
   - Con esta opción, el sistema o la aplicación pueden encargarse de buscar, descargar e instalar las actualizaciones.
   - La Agencia de Ciberseguridad y Seguridad de las Infraestructuras (CISA) recomienda utilizar las opciones automáticas siempre que estén disponibles.
   - Es necesario que los usuarios o los grupos de TI habiliten ciertos permisos antes de que las actualizaciones puedan instalarse, o empujarse, cuando estén disponibles.
   - Depende de los desarrolladores probar adecuadamente sus parches antes de publicarlos.

   - Ventaja: Una ventaja de las actualizaciones automáticas es que el proceso de implementación se simplifica. También mantiene los sistemas y el software al día con los últimos parches críticos.

   - Desventaja: Un inconveniente de las actualizaciones automáticas es que pueden producirse problemas de inestabilidad si los parches no han sido probados a fondo por el proveedor. Esto puede provocar problemas de rendimiento y una mala experiencia del usuario.

- Software al final de su vida útil
   - A veces no hay actualizaciones disponibles para cierto tipo de software conocido como software de fin de vida útil (EOL).
   - Todo software tiene un ciclo de vida.
   - Comienza cuando se produce y termina cuando se publica una versión más reciente.
   - En ese momento, los desarrolladores deben asignar recursos a las versiones más recientes, lo que da lugar al software EOL.
   - Aunque el software más antiguo sigue siendo útil, el fabricante ya no le da soporte.
   - Los parches y las actualizaciones son muy diferentes de las mejoras.
   - Las actualizaciones se refieren a versiones completamente nuevas de hardware o software que pueden adquirirse.

- [CISA recomienda dejar de utilizar el software EOL](https://www.cisa.gov/news-events/news/understanding-patches-and-software-updates) porque supone un riesgo irreparable para los sistemas.
- Pero esta recomendación no siempre se sigue.
- La sustitución de la tecnología EOL puede resultar costosa para las empresas y los usuarios individuales.
- Los riesgos que presenta el software EOL siguen creciendo a medida que más dispositivos conectados entran en el mercado.
- Por ejemplo, hay miles de millones de dispositivos de Internet de las cosas (IoT), como bombillas inteligentes, conectados a redes domésticas y de trabajo.
- En algunos entornos empresariales, todo lo que necesita un atacante es un único dispositivo sin parchear para acceder a la red y causar problemas.

---

## Omad: Mi viaje de aprendizaje en la ciberseguridad
- Lo único que hago es resolver problemas.
- ​Los usuarios de Google tienen problemas, necesitan a alguien con quien hablar, por lo general hablan con nosotros.
- A ​todos los entrevistadores les gustó mi formación, les gustó que fuera autodidacta.
- ​Muchos entrevistadores pudieron identificarse conmigo. ​Dijeron: «Oye, yo hice lo mismo».
- ​Para quienes cambian de carrera, ​lo que tienen que otras personas no tienen es una mentalidad diferente.
- ​Viene de una experiencia fuera del espacio técnico que puede transferir ​al espacio técnico.
- ​No olvides que todos tenemos habilidades que pueden ayudarte en el campo.
- ​Eso es lo que buscan los empleadores, ​eso es lo que buscan los gerentes de contratación.
- ​Una cosa que aprendí como oficial de prisiones es cómo evaluar el riesgo.
- ​Cada situación es diferente, al igual que el espacio de Seguridad.
- Cada riesgo es ​diferente.
- Cada vulnerabilidad es diferente.
- Cada amenaza es diferente. 
- ​Puedes enseñarle tecnología a alguien, pero ​no puedes enseñarle una vida de habilidades fuera de la tecnología.

---

## Pruebas de penetración
- Un plan de Seguridad eficaz se basa en pruebas periódicas para encontrar los puntos débiles de una organización.

- Pruebas de penetración
   - Una prueba de penetración, o pen test, es un ataque simulado que ayuda a identificar vulnerabilidades en sistemas, redes, sitios web, aplicaciones y procesos.
   - El ataque simulado en una prueba de penetración implica el uso de las mismas herramientas y técnicas que los actores maliciosos con el fin de imitar un ataque en la vida real.
   - Dado que una prueba de penetración es un ataque autorizado, se considera una forma de hacking ético.
   - A diferencia de una evaluación de vulnerabilidades que encuentra puntos débiles en la Seguridad de un sistema, una prueba de penetración explota esos puntos débiles para determinar las consecuencias potenciales si el sistema se rompe o es penetrado por un agente de amenaza.
   - Por ejemplo, el Equipo de ciberseguridad de una empresa financiera podría simular un ataque a su aplicación bancaria para determinar si existen puntos débiles que permitirían a un atacante robar información de sus clientes o transferir fondos ilegalmente.
   - Si la prueba de penetración descubre errores de configuración, el Equipo puede abordarlos y mejorar la Seguridad general de la aplicación.
   - Las organizaciones reguladas por PCI DSS, HIPAA o GDPR deben realizar pruebas de penetración de forma rutinaria para mantener los Estándares de cumplimiento.

- Aprender de perspectivas variadas
   - Estos ataques autorizados son realizados por pen testers expertos en programación y arquitectura de redes.
   - Dependiendo de sus objetivos, las organizaciones pueden utilizar algunos enfoques diferentes para las pruebas de penetración:
      - Las pruebas del Equipo Rojo simulan ataques para identificar vulnerabilidades en sistemas, redes o aplicaciones.
      - Las pruebas del equipo azul se centran en la defensa y la Respuesta ante incidentes para validar los sistemas de Seguridad existentes en una organización.
      - Las pruebas del equipo púrpura son colaborativas y se centran en mejorar la postura de seguridad de la organización combinando elementos de los ejercicios de los equipos rojo y azul.
   - Las Pruebas de penetración de los equipos rojos suelen ser realizadas por "pen testers" independientes contratados para evaluar los sistemas internos.
   - Aunque los equipos de ciberseguridad también pueden contar con sus propios expertos en pruebas de penetración.
   - Independientemente del enfoque, los expertos en pruebas de penetración deben tomar una decisión importante antes de simular un ataque: ¿Cuánto acceso e Información necesito?

- Estrategias de pruebas de penetración
   - Existen tres estrategias comunes de pruebas de penetración:
      - Las pruebas de caja abierta son aquellas en las que el evaluador tiene el mismo acceso privilegiado que tendría un desarrollador interno a información como la arquitectura del sistema, el flujo de datos y los diagramas de red. Esta estrategia recibe varios nombres diferentes, como pruebas de penetración internas, de pleno conocimiento, de caja blanca y de caja clara.
      - Las pruebas de caja cerrada son aquellas en las que el probador tiene poco o ningún acceso a los sistemas internos, algo similar a lo que haría un hacker malintencionado. Esta estrategia se conoce a veces como pruebas de penetración externas, de caja negra o de conocimiento cero.
      - Las pruebas de conocimientos parciales se producen cuando la persona que realiza las pruebas tiene acceso y conocimientos limitados de un sistema interno; por ejemplo, un representante de atención al cliente. Esta estrategia también se conoce como pruebas de caja gris.
   - Las pruebas de caja cerrada tienden a producir las simulaciones más exactas de un ataque en el mundo real.
   - No obstante, cada estrategia produce resultados valiosos al demostrar cómo un atacante podría infiltrarse en un sistema y a qué información podría acceder.

- Convertirse en un probador de penetración
   - Los probadores de penetración están muy demandados en el campo de la ciberseguridad, en rápido crecimiento.
   - Todas las habilidades que está aprendiendo en este Programa pueden ayudarle a avanzar hacia una carrera en pruebas de penetración:
      - Seguridad de redes y aplicaciones
      - Experiencia con sistemas operativos, como Linux
      - Análisis de vulnerabilidad y modelado de amenazas
      - Herramientas de detección y respuesta
      - Lenguajes de programación, como Python y BASH
      - Habilidades de comunicación
   - Los conocimientos de programación son muy útiles en las pruebas de penetración porque a menudo se realizan en software y sistemas informáticos.
   - Con suficiente práctica y dedicación, los profesionales de la ciberseguridad de cualquier nivel pueden desarrollar las habilidades necesarias para ser un "pen tester".

- Programas de Recompensas por errores
   - Las organizaciones suelen llevar a cabo programas de recompensas por errores que ofrecen a los pen testers autónomos recompensas económicas por encontrar y notificar vulnerabilidades en sus productos.
   - Las Recompensas por errores son grandes oportunidades para que los profesionales de la Seguridad aficionados participen y hagan crecer sus habilidades.
   - [HackerOne](https://hackerone.com/bug-bounty-programs) es una comunidad de hackers éticos en la que puede encontrar Recompensas por errores activas en las que participar.

---

## Ponga a prueba sus Conocimientos: Identificar las vulnerabilidades del sistema

1. Rellene el espacio en blanco: Una vulnerabilidad ____ se refiere al proceso de revisión interna de los sistemas de Seguridad de una organización
- [x] evaluación
- [ ] escáner
- [ ] parche
- [ ] puntuación
> Una evaluación de vulnerabilidades es un proceso de revisión interna de los sistemas de Seguridad de una organización.

2. ¿Cuáles son los objetivos de una evaluación de vulnerabilidades? Seleccione dos respuestas
- [x] Para reducir la exposición global a las amenazas
- [ ] Detectar el tráfico de red
- [ ] Auditar el cumplimiento normativo
- [x] Identificar los puntos débiles existentes
> Los objetivos de una evaluación de vulnerabilidades son identificar las debilidades existentes y reducir la exposición general a las amenazas.

3. ¿Cuál de los siguientes ejemplos de remediación podría implementarse después de un escaneo de vulnerabilidad? Seleccione dos respuestas
- [x] Instalación de actualizaciones de software y parches
- [ ] Localización de vulnerabilidades en los puestos de trabajo
- [x] Entrenamiento de los empleados para que sigan los nuevos Procedimientos de Seguridad
- [ ] Identificar errores de configuración en una aplicación
> Entre los ejemplos de medidas correctoras que podrían llevarse a cabo tras un escaneado de vulnerabilidades se incluyen el Entrenamiento de los empleados en nuevos procedimientos y la instalación de actualizaciones y parches de software.

4. ¿Cuáles son los dos tipos de exploraciones de vulnerabilidad? Seleccione dos respuestas
- [ ] Parche o actualización
- [x] Limitado o completo
- [x] Autenticado o no autenticado
- [ ] Riesgo o Amenaza
> Autenticado o no autenticado y limitado o exhaustivo son dos tipos de escaneado de vulnerabilidades. Interna y externa es otro tipo común de exploración de vulnerabilidades.

---

## Actividad de Portfolio: Analizar un sistema vulnerable para una pequeña empresa
- Resumen de la actividad
   - En esta actividad, llevará a cabo una evaluación de vulnerabilidades para una pequeña empresa.
   - Una evaluación de la vulnerabilidad es el proceso de revisión interna de los sistemas de seguridad de una organización.
   - Evaluará los riesgos de un sistema de información vulnerable y esbozará un plan de corrección.
   - Como analista de ciberseguridad, podría ayudar con las evaluaciones de vulnerabilidad para prevenir ataques en una organización.

- Escenario
   - Usted es un analista de ciberseguridad recién contratado para una empresa de comercio electrónico.
   - La empresa almacena información en un servidor de base de datos remoto, ya que muchos de los empleados trabajan a distancia desde lugares de todo el mundo.
   - Los empleados de la empresa consultan, o solicitan, regularmente datos del servidor para encontrar clientes potenciales.
   - La base de datos ha estado abierta al público desde el lanzamiento de la empresa hace tres años.
   - Como profesional de la ciberseguridad, usted reconoce que mantener el servidor de la base de datos abierto al público es una vulnerabilidad grave.
   - Se le encomienda completar una evaluación de la vulnerabilidad de la situación para comunicar los riesgos potenciales a los responsables de la toma de decisiones en la empresa.
   - Debe crear un informe escrito que explique cómo el servidor vulnerable supone un riesgo para las operaciones de la empresa y cómo se puede asegurar.

- Instrucciones paso a paso

1. Abrir una plantilla de informe
   1. Abrir una plantilla de informe
   - [Vulnerability assessment report template](./resources/Vulnerability-assessment-report-template.docx)

   2. Acceda a los materiales de apoyo
   - [NIST SP 800-30 Rev. 1](./resources/NIST-SP-800-30-Rev.-1.docx)

   3. Revisar la información sobre el servidor vulnerable
   - En esta actividad, le hemos proporcionado la descripción del sistema y el Alcance del Informe de evaluación de vulnerabilidades en la plantilla proporcionada.
   - Las evaluaciones de vulnerabilidades incluyen una descripción del sistema que se está evaluando y el Alcance del proyecto.
   - Revise la Descripción del sistema y el Alcance del informe de Evaluación de vulnerabilidades.
   - La Descripción del sistema destaca los componentes relevantes, la arquitectura y las dependencias del sistema que se está evaluando.
   - Todas estas partes y conexiones conforman la superficie de ataque del sistema de Información vulnerable.
   - El Alcance especifica el enfoque y los límites de la evaluación.
   - Por ejemplo, puede especificar que el alcance de esta evaluación sólo se refiere a la confidencialidad, disponibilidad e integridad de los Datos en el servidor - no a la seguridad física del servidor o de sus sistemas informáticos relacionados.

2. Realizar la Evaluación de riesgos

   1. Explicar la finalidad del sistema de información
      - Una vez que haya revisado la descripción y el alcance del sistema, redactará una declaración de propósito.
      - La sección de propósito ayuda a las partes interesadas a comprender el objetivo subyacente y el resultado previsto de su análisis.
      - Una declaración de propósito también conecta los objetivos técnicos de su análisis con las metas de la organización.
      - Considere lo que sabe sobre el servidor:
         - ¿Qué valor tiene el servidor de base de datos para la empresa?
         - ¿Por qué es importante para la empresa proteger los datos del servidor?
         - ¿Cómo podría afectar al negocio la desactivación del servidor?
      - En la sección Propósito del informe, utilice las preguntas proporcionadas y escriba de 3 a 5 frases (de 60 a 100 palabras) que describan la(s) razón(es) para realizar este análisis de vulnerabilidad.
   2. Identificar las posibles fuentes de amenaza
      - Explore la sección Fuentes de amenazas del recurso NIST SP 800-30 Rev. 1.
      - Utilizando lo que sabe sobre el servidor de Base de datos vulnerable, fíjese en los tipos de amenazas y ejemplos descritos.
      - En la columna Fuente de amenazas de la tabla Evaluación de riesgos de su plantilla, identifique tres posibles amenazas.
      - Elija las amenazas basándose en la información que ha recopilado de la descripción del sistema, el Alcance, el Propósito y el recurso NIST SP 800-30 Rev. 1.
   3. Identificar posibles eventos de amenaza
      - NIST SP 800-30 Rev. 1 proporciona una lista exhaustiva de posibles eventos de seguridad que podrían comprometer un sistema de Información vulnerable - etiquetados como Eventos de Amenaza.
      - Esta Lista cubre lo que los atacantes de diferentes grupos suelen intentar conseguir y lo buenos que son en ello.
      - Por ejemplo, un competidor empresarial podría tener las capacidades técnicas necesarias para llevar a cabo un ataque de denegación de servicio.
      - Explore la sección de Eventos de Amenaza en el recurso.
      - A continuación, identifique tres eventos de amenaza que podrían iniciarse basándose en las fuentes de amenaza que haya identificado.
      - Escriba los tres eventos de amenaza en la columna Evento de amenaza de la tabla de Evaluación de riesgos de su plantilla.
   4. Calcular el riesgo de amenazas potenciales
      - Puede que recuerde de una lectura anterior sobre el cálculo de riesgos que las amenazas y vulnerabilidades potenciales son factores importantes en los que pensar a la hora de evaluar la Seguridad de un recurso.
      - Consulte las secciones de probabilidad y gravedad del recurso NIST SP 800-30 Rev. 1 y hágase las siguientes preguntas sobre cada una de las amenazas que identificó anteriormente:
         - ¿Con qué frecuencia podría ocurrir?
         - ¿Se verían afectadas las funciones críticas del negocio?
         - ¿Cómo podría afectar al negocio y a sus Clientes?
      - A continuación, calcule una puntuación de Probabilidad (1-3) y de Gravedad (1-3) para cada amenaza y añada sus puntuaciones a las columnas correspondientes de la tabla de Evaluación de riesgos de su plantilla.
      - Después, calcule una puntuación global de Riesgo (1-9) para cada amenaza utilizando la Fórmula (probabilidad x gravedad = riesgo).
      - El número de filas de una tabla de riesgos puede variar en función de la complejidad y el alcance de la evaluación.
      - En general, debe proporcionar a las partes interesadas una visión global de todos los riesgos importantes.

3. Proponer recomendaciones de Seguridad

   1. Explique su enfoque
      - Otra sección que suele incluirse en una evaluación de vulnerabilidad es una explicación de su enfoque.
      - Esto ayuda a las partes interesadas a comprender su proceso de reflexión para evaluar los riesgos que ha identificado, lo que añade un contexto valioso para las partes interesadas.
      - Usted está llevando a cabo una evaluación cualitativa de la vulnerabilidad, que se basa en el juicio subjetivo para evaluar la probabilidad y la gravedad de los riesgos.
      - Su tarea aquí es estimar lo malos que podrían ser los ataques juzgando sus posibilidades basándose en sus conocimientos de seguridad.
      - Las evaluaciones cualitativas de vulnerabilidad son útiles para identificar los riesgos de alto nivel a los que se enfrenta una organización.
      - Esta información ayuda a las organizaciones a tomar decisiones informadas sobre la asignación de recursos, la planificación de proyectos y otros aspectos de sus operaciones empresariales.
      - En la sección Enfoque de su plantilla, escriba de 3 a 5 frases (de 60 a 100 palabras) explicando por qué ha seleccionado las 3 fuentes/eventos de amenaza específicos que eligió y por qué cree que son riesgos empresariales significativos.
   2. Proponer una estrategia de reparación
      - Después de realizar una evaluación de vulnerabilidades, la creación de una estrategia de remediación bien definida es crucial para proteger sus sistemas y datos.
      - La estrategia de remediación debe proporcionar a las partes interesadas los pasos procesables que se pueden tomar para remediar, o arreglar, las vulnerabilidades para evitar amenazas.
      - Algunas amenazas no se pueden arreglar.
      - En esos casos, es igualmente importante considerar una estrategia de mitigación : un plan para reducir la gravedad de una amenaza.
      - Piense en los riesgos que podría remediar y/o mitigar utilizando controles de seguridad como:
         - Principio del menor privilegio
         - Defensa en profundidad
         - Autenticación multifactor (MFA)
         - Marco de autenticación, autorización y contabilidad (AAA)
      - En la sección Remediación de la plantilla, escriba de 3 a 5 frases (de 60 a 100 palabras) resumiendo los controles de seguridad específicos que podrían implementarse para remediar o mitigar los riesgos del sistema de información.
      - Alinee sus sugerencias con los riesgos que ha evaluado.
      - Por ejemplo, podría sugerir una Infraestructura de clave pública (PKI) para abordar la exfiltración de información sensible.

- Qué incluir en su respuesta
   - de 3 a 5 frases que describan las razones para realizar el análisis de seguridad en la sección Propósito 
   - Una sección de Evaluación de riesgos cumplimentada
   - 3-5 frases que expliquen su razonamiento sobre los riesgos identificados en la sección Enfoque 
   - 3-5 frases que resuman una estrategia de corrección y/o mitigación en la sección Corrección 

- Evaluación
   - Su Informe proporciona un propósito claro de por qué la evaluación de la vulnerabilidad del sistema es valiosa para la empresa
   - En la sección de Evaluación de riesgos de su Informe, ¿considera las posibles fuentes de amenazas de la base de datos vulnerable?
   - En la sección de Evaluación de Riesgos de su Informe, ¿puede cada Evento de Amenaza ser razonablemente iniciado por sus fuentes de amenaza relacionadas?
   - ¿Contiene la tabla de Evaluación de riesgos de su Informe puntuaciones de probabilidad, gravedad y riesgo para cada fuente potencial de amenaza?
   - Su Informe explica el enfoque que adoptó para analizar el Riesgo y proporciona una estrategia de remediación para asegurar el sistema vulnerable.

- Vulnerability Assessment Report

- Scope
   - El alcance de esta evaluación de vulnerabilidades se relaciona al actual control de acceso y seguridad de la base de datos de la empresa. La evaluación se centra en los últimos 6 meses de actividad, se considera de febrero a julio de 2026. Se utiliza cómo guía el NIST SP 800-30 Rev. 1 para la evaluación de riesgos y la identificación de vulnerabilidades.

- Risk Assessment

| Threat Source | Threat Event | Likelihood (1-3) | Severity (1-3) | Risk Score (1-9) |
|----------------|--------------|------------------|----------------|------------------|
| Competidor empresarial | Obtención de información confidencial de clientes | 3 | 3 | 9 |
| Hacker externo | Obtención de acceso no autorizado a la base de datos | 3 | 3 | 9 |
| Empleado | Eliminación accidental de datos de clientes | 2 | 2 | 4 |
| Cliente | Acceso no autorizado a información de otros clientes | 2 | 2 | 4 |

- Approach
   - Entre los riesgos evaluados están los procedimientos de acceso y almacenamiento y seguridad de la base de datos. Las fuentes de amenazas identificadas incluyen competidores empresariales, hackers externos, empleados y clientes. Los eventos se determinan en función de la probabilidad de que se produzcan y de la gravedad de sus consecuencias. Los incidentes encontrados superan el umbral de riesgo de 4, lo que indica que se requiere una acción inmediata para remediar o mitigar los riesgos. Esto significa modificar el funcionamiento operativo de la organización para reducir la probabilidad de que se produzcan estos eventos de amenaza y su gravedad.

- Remediation Strategy
   - Se deben implementar mecanismos de autenticación, autorización, auditoría, principios de menor privilegio y separación de funciones para mitigar los riesgos de amenazas identificados. Se recomienda el uso de cuentas individuales, con contraseñas que cumplan estándares de seguridad, para todos los empleados y clientes que accedan a la base de datos. Se recomienda que las cuentas generadas tengan un rol asignado, el cúal determine sus privilegios de acceso a la base de datos. Por último se recomienda bloquear accesos remotos a la base de datos y permitir únicamente conexiones desde la red interna de la empresa.