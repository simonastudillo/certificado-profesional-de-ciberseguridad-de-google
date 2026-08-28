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