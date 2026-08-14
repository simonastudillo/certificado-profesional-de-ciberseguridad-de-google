# Principios OWASP y auditorías de seguridad

## Principios de Seguridad OWASP
- ​Es importante comprender cómo proteger ​los datos y recursos de una organización ​porque eso formará parte de ​su papel como analista de seguridad
- Afortunadamente, existen principios y ​directrices que pueden utilizarse, junto con ​los marcos del NIST y la tríada CID, para ​ayudar a los equipos de seguridad a minimizar las amenazas y los riesgos
- En este vídeo, exploraremos algunos principios de seguridad del Proyecto abierto de seguridad de las aplicaciones web (Open ​Web Application Security Proyecto, u OWASP) ​que es ​útil conocer como analista principiante
- El primer principio del OWASP es ​minimizar la superficie de ataque
   - Una superficie de ataque se refiere a ​todas las vulnerabilidades potenciales ​que un agente de amenaza podría explotar, ​como los vectores de ataque, que son vías ​que los atacantes utilizan para penetrar en las defensas de seguridad
   - Ejemplos de vectores de ataque comunes son ​los correos electrónicos de phishing y las contraseñas débiles
   - Para minimizar la superficie de ataque ​y evitar incidentes por este tipo de ​vectores, los Equipos de seguridad podrían desactivar características del software, ​restringir quién puede acceder a ciertos recursos o ​establecer requisitos más complejos para las contraseñas.
   - El principio de privilegio mínimo ​significa asegurarse de que los usuarios tienen ​la menor cantidad de acceso ​necesario para realizar sus tareas cotidianas
   - La razón principal para limitar el acceso ​a la Información y ​los Recursos de la organización es reducir la cantidad de ​daños que podría causar una brecha de seguridad
   - ​Por ejemplo, como analista de nivel básico, ​puede que tenga acceso a los datos de registro, ​pero puede que no tenga acceso para cambiar los permisos de usuario
   - Por lo tanto, si ​un agente de amenaza compromete sus credenciales, ​sólo podrá obtener un acceso ​limitado a los recursos digitales o físicos, ​lo que puede no ser suficiente para que ​despliegue su ataque previsto
- El siguiente principio que trataremos es la defensa en profundidad
   - Defensa en profundidad significa que una organización debe tener ​múltiples controles de seguridad que ​abordenen los riesgos y amenazas de diferentes maneras
   - Un ejemplo de control de seguridad es la ​autenticación de múltiples factores, o MFA, ​que requiere que los usuarios den ​un paso adicional más allá de simplemente ​introducir su nombre de usuario y ​contraseña para acceder a una aplicación
   - Otros controles incluyen firewalls, ​sistemas de detección de intrusos, ​y configuraciones de permisos que pueden ​utilizarse para crear múltiples puntos de defensa, ​que un agente de Amenaza debe atravesar ​para vulnerar una organización
- Otro principio es la separación de funciones, ​que puede utilizarse para evitar que los individuos ​realicen actividades fraudulentas o ilegales
   - Este principio significa que a nadie se le deben dar ​tantos privilegios que pueda hacer un mal uso del sistema
   - Por ejemplo, la persona de una empresa que firma ​las nóminas no debería ser también ​la persona que las prepara
- Mantener la Seguridad simple es ​el siguiente principio
   - Como su nombre indica, ​al implementar controles de seguridad, ​se deben ​evitar las soluciones innecesariamente complicadas porque pueden llegar a ser inmanejables. 
   - Cuanto más complejos sean los controles de seguridad, ​más difícil será que la gente trabaje en colaboración
- El último principio es solucionar los problemas de seguridad correctamente
   - La tecnología es una gran herramienta, ​pero también puede presentar desafíos
   - Cuando se produce un incidente de seguridad, ​se espera que los profesionales de la seguridad ​identifiquen la causa raíz rápidamente
   - ​A partir de ahí, es importante corregir ​cualquier vulnerabilidad identificada y ​realizar pruebas para garantizar que las reparaciones tienen éxito
   - Un ejemplo de problema es una contraseña débil para ​acceder al wifi de una organización ​porque podría dar lugar a una brecha
   - ​Para solucionar este tipo de Problema de Seguridad, ​se podrían establecer políticas de contraseñas más estrictas. 

---

## Más información sobre los principios de Seguridad OWASP
- Principios de seguridad
   - En el lugar de trabajo, los principios de seguridad están integrados en las tareas diarias
   - Ya sea analizando registros, supervisando un panel de administración de información y eventos de seguridad (SIEM) o utilizando un escáner de vulnerabilidades, utilizará estos principios de alguna manera.
- principios de seguridad OWASP:
   - Minimizar la superficie de ataque: La superficie de ataque se refiere a todas las vulnerabilidades potenciales que un Agente de amenaza podría explotar.
   - Principio de privilegio mínimo: Los usuarios tienen la menor cantidad de acceso necesario para realizar sus tareas cotidianas.
   - Defensa en profundidad: Las organizaciones deben disponer de diversos controles de seguridad que mitiguen los riesgos y amenazas.
   - Separación de funciones: Las acciones críticas deben depender de varias personas, cada una de las cuales debe seguir el principio de privilegio mínimo.
   - Seguridad sencilla: Evite las soluciones innecesariamente complicadas. La complejidad dificulta la seguridad.
   - Solucione correctamente los problemas de seguridad: Cuando se produzcan incidentes de seguridad, identifique la causa raíz, contenga el impacto, identifique las vulnerabilidades y lleve a cabo pruebas para garantizar que la corrección se realiza correctamente.
- Principios de seguridad OWASP adicionales
   - cuatro principios de seguridad OWASP adicionales que los analistas de ciberseguridad y sus equipos utilizan para mantener las operaciones de la organización y las personas a salvo.
   - Establecer valores predeterminados seguros
      - Este principio significa que el estado de seguridad óptimo de una aplicación es también su estado por defecto para los usuarios; debería costar un trabajo extra hacer que la aplicación sea insegura.
   - Fallar con seguridad
      - Fallar de forma segura significa que cuando un control falla o se detiene, debe hacerlo pasando por defecto a su opción más segura
      - Por ejemplo, cuando un cortafuegos falla, debería simplemente cerrar todas las conexiones y bloquear todas las nuevas, en lugar de empezar a aceptarlo todo.
   - No confíes en los servicios
      - Muchas organizaciones trabajan con socios externos
      - Estos socios externos suelen tener políticas de seguridad diferentes a las de la organización
      - Y la organización no debe confiar explícitamente en que los sistemas de sus socios sean seguros
      - Por ejemplo, si un proveedor externo realiza el seguimiento de los puntos de recompensa de los clientes de una aerolínea, ésta debería asegurarse de que el saldo es exacto antes de compartir esa información con sus clientes.
   - Evitar la seguridad por oscuridad
      - La seguridad de los sistemas clave no debe basarse en mantener ocultos los detalles. Considere el siguiente ejemplo FROM OWASP (2016)
- La seguridad de una aplicación no debería basarse en mantener en secreto el código fuente.
- Su seguridad debe basarse en muchos otros factores, incluidas políticas de contraseñas razonables, defensa en profundidad, límites de transacciones comerciales, arquitectura de red sólida y controles de fraude y auditoría.

---

## Wajih Manténgase al día sobre las últimas amenazas a la ciberseguridad
- Algunas de las estrategias que he utilizado para mantenerme al día sobre las últimas ​tendencias de ciberseguridad son las de recurrir a foros en línea como Medium para ​investigar diferentes tendencias y temas de seguridad
- Personalmente, uso mucho Medium, ya que podría filtrar por la etiqueta de ​«me gusta», «quiero encontrar artículos relacionados con la ciberseguridad» ​o «quiero encontrar artículos relacionados con la seguridad en la nube»
- Si lo que estás deseando es más bien una red de redes, te ​recomiendo encarecidamente que asistas a esas, como conferencias
- Mi consejo para las personas que desean dedicarse a la ciberseguridad es que no se sientan abrumadas ​al tratar de entender cada una de las especializaciones dentro de la ciberseguridad
- Están sucediendo muchas cosas en el campo de la ciberseguridad en términos de tendencias y ​es bueno estar al día con todas ellas, pero a ​veces es necesario dar un paso atrás y priorizar los temas de ​ciberseguridad en los que te mantienes más actualizado

---

## Planificación de una Auditoría de Seguridad
- Una auditoría de seguridad es una revisión de los ​controles ​, políticas y procedimientos de seguridad de una organización en comparación con un conjunto de expectativas
- Hay dos tipos principales de ​auditorías de Seguridad: externas e internas
- Por lo general, una auditoría de seguridad interna la lleva a cabo un equipo de ​personas que puede incluir al ​oficial de cumplimiento, al ​gerente de seguridad y a otros miembros del equipo de seguridad de la organización
- ​Las auditorías de seguridad internas se utilizan para ayudar a mejorar la ​postura de seguridad de una organización y ayudar a las organizaciones a ​evitar multas de ​las agencias gubernamentales debido a la falta de cumplimiento. 
- Las auditorías de seguridad internas ayudan a ​los equipos de seguridad a identificar el riesgo organizacional ​, evaluar los controles y corregir los problemas de cumplimiento
- Ahora que hemos analizado los propósitos de las auditorías internas, ​abordemos algunos elementos comunes de las auditorías internas
- Estos incluyen establecer el alcance ​y los objetivos de la auditoría, ​realizar una evaluación ​de riesgos de los activos de la organización, ​completar una evaluación de controles, ​evaluar el cumplimiento ​y comunicar los resultados a la parte interesada
- El ​alcance se refiere a los criterios específicos ​de una auditoría de Seguridad interna
- El alcance exige que las organizaciones identifiquen a las personas, los activos ​, las políticas, los procedimientos ​y las tecnologías que podrían ​afectar a la postura de Seguridad de una organización
- ​Las metas son un resumen de ​los objetivos de seguridad de la organización ​o lo que quieren lograr ​para mejorar su postura de seguridad. 
- ​Si bien los miembros del equipo de Seguridad de más alto ​nivel y otra parte interesada suelen establecer el alcance y los objetivos de la auditoría, es posible que se ​pida a los analistas principiantes que revisen y comprendan ​el alcance y los objetivos para ​completar otros elementos de la auditoría
- [Ejemplo](./example_1.txt)
- Usando el ejemplo anterior
- el alcance de ​esta auditoría implica la evaluación de los permisos de los usuarios; la ​identificación de los controles, políticas ​y procedimientos existentes; y la contabilización de ​la tecnología que utiliza actualmente la organización
- Los objetivos descritos incluyen la ​implementación de las funciones principales de los marcos, ​como el CSF del NIST; el ​establecimiento de políticas y procedimientos para ​garantizar el cumplimiento; y el fortalecimiento de los controles del sistema
- El siguiente elemento es realizar una evaluación de riesgos, ​que se centra en identificar ​posibles amenazas, riesgos y vulnerabilidades
- Esto ayuda a las organizaciones a considerar ​qué medidas de seguridad deben ​implementarse y supervisarse ​para garantizar la seguridad de los activos
- Al igual que para establecer el alcance y los objetivos, los ​gerentes u otra parte interesada suelen completar una evaluación de riesgos
- Sin embargo, es posible que se le pida que analice ​los detalles proporcionados en la evaluación de riesgos ​para considerar qué tipos de ​controles y normas de cumplimiento ​deben existir para ayudar a ​mejorar la postura de Seguridad de la organización. 
- ​Por ejemplo, esta evaluación de riesgos ​destaca que existen controles ​, procesos y procedimientos ​inadecuados para proteger los activos de la organización
- En concreto, hay una falta de gestión adecuada de los ​activos físicos y digitales, ​incluido el equipo de los empleados
- El equipo utilizado para ​almacenar datos no está debidamente protegido
- Y es ​probable que el acceso a la información privada almacenada en la red interna de la organización necesite controles más sólidos

---

## Completar una auditoría de seguridad
- Como recordatorio, los elementos de planificación de las auditorías de Seguridad Interna incluyen ​establecer el alcance y los objetivos, y luego realizar una evaluación de riesgos
- Los elementos restantes son completar una evaluación de los controles, ​evaluar el cumplimiento y comunicar los resultados
- Antes de completar estos tres últimos elementos, tendrá que revisar el alcance y los objetivos, ​así como la evaluación de riesgos, y hacerse algunas preguntas. ​Por ejemplo: 
   - ¿Qué se pretende lograr con la auditoría?
   - ¿Qué activos están en mayor riesgo? 
   - ¿Son suficientes los controles actuales para proteger esos activos?
   - ​Si no es así, ¿qué controles y normas de cumplimiento deben implementarse?
- Tener en cuenta preguntas como estas puede mejorar su capacidad ​para completar el siguiente elemento: una evaluación de controles
- Una evaluación de controles implica revisar minuciosamente ​los activos existentes de una organización y, a continuación, evaluar los riesgos potenciales para esos activos, ​a fin de garantizar que los controles y procesos internos sean efectivos
- Para ello, a los analistas principiantes se les podría encomendar la tarea de ​clasificar los controles en las siguientes categorías: controles administrativos, controles ​técnicos y controles físicos
- Los controles administrativos están relacionados con el componente humano de la ciberseguridad.
- Incluyen políticas y procedimientos que definen la forma en que una organización ​administra los datos, como la implementación de políticas de contraseñas. 
- Los controles técnicos son soluciones de hardware y software que se utilizan para proteger los activos, ​como el uso de sistemas de detección de intrusos (IDS) y la encriptación
- Los controles físicos se refieren a las medidas implementadas para impedir el ​acceso físico a los activos protegidos, como las cámaras de vigilancia y las cerraduras
- El siguiente elemento es determinar si ​la organización cumple o no con las normas de cumplimiento necesarias
- Como recordatorio, las regulaciones de cumplimiento son leyes que las ​organizaciones deben seguir para garantizar que los datos privados permanezcan seguros
- En este ejemplo, la organización realiza negocios en la Unión Europea y ​acepta pagos con tarjeta de crédito.
- ​Por lo tanto, deben cumplir con el GDPR y el ​Estándar de seguridad de datos para la industria de tarjetas de pago, o PCI DSS.
- ​El último elemento común de una auditoría de Seguridad Interna es la comunicación.
- Una vez finalizada la auditoría de Seguridad Interna, los resultados y ​las recomendaciones deben comunicarse a la parte interesada
- En general, este tipo de comunicación resume el alcance y los ​objetivos de la auditoría
- Luego, enumera los riesgos existentes y señala la rapidez con la que deben abordarse esos riesgos
- Además, identifica las normas de cumplimiento que ​la organización debe cumplir y proporciona recomendaciones para ​mejorar la postura de Seguridad de la organización
- ​Las auditorías internas son una excelente manera de identificar las brechas dentro de una organización. 
- Cuando trabajaba en una empresa anterior, mi equipo y yo realizamos una ​auditoría interna de contraseñas y descubrimos que muchas de las contraseñas no eran seguras.
- ​Una vez que identificamos este problema, el equipo de cumplimiento tomó la iniciativa y ​comenzó a aplicar políticas de contraseñas más estrictas.
- Las auditorías son una oportunidad para determinar qué medidas de seguridad ​tiene implementadas una organización y qué áreas deben mejorarse para ​lograr la postura de seguridad deseada por la organización
- Las auditorías de seguridad son muy complicadas, pero tienen un valor extremo para las organizaciones

---

## Más información sobre auditorías de seguridad
- Anteriormente, se le presentó cómo planificar y completar una auditoría interna de Seguridad
- Auditorías de seguridad
   - Una Auditoría de seguridad es una revisión de los Controles de seguridad, políticas y Procedimientos de una organización contra un conjunto de expectativas
   - Las auditorías son revisiones independientes que evalúan si una organización cumple los criterios internos y externos
      - Los criterios internos incluyen las políticas, los procedimientos y las mejores prácticas descritas.
      - Los criterios externos incluyen el cumplimiento normativo, las leyes y las regulaciones federales. 
   - Además, una Auditoría de seguridad puede utilizarse para evaluar los Controles de seguridad establecidos por una organización
   - Como recordatorio, los Controles de seguridad son salvaguardas diseñadas para reducir riesgos de Seguridad específicos.
   - Las auditorías ayudan a garantizar que se realizan controles de seguridad (es decir, el seguimiento diario de la información de seguridad y los paneles de gestión de eventos), para identificar amenazas, riesgos y vulnerabilidades
   - Esto ayuda a mantener la postura de seguridad de una organización. Y, si hay Problemas de Seguridad, debe existir un proceso de remediación.
- Metas y objetivos de una auditoría
   - El objetivo de una auditoría es garantizar que las prácticas de tecnología de la información (TI) de una organización cumplen las normas del sector y de la organización
   - El Objetivo es identificar y abordar las áreas de remediación y crecimiento
   - Las auditorías proporcionan dirección y claridad al identificar cuáles son los fallos actuales y desarrollar un plan para corregirlos.
   - Deben realizarse auditorías de seguridad para salvaguardar los Datos y evitar sanciones y multas de las agencias gubernamentales
   - La frecuencia de las auditorías depende de las leyes locales y de las regulaciones federales de cumplimiento.
- Factores que afectan a las auditorías
   - Los factores que determinan los tipos de auditorías que implementa una organización incluyen:
      - Tipo de industria
      - Tamaño de la organización
      - Vínculos con las regulaciones gubernamentales aplicables
      - La ubicación geográfica de un negocio (Business-to-Business)
      - Una decisión empresarial de adherirse a un cumplimiento normativo específico
- Función de los marcos y controles en las auditorías
   - Junto con el cumplimiento, es importante mencionar el papel de los marcos y controles en las auditorías de Seguridad
   - Marcos como el Marco de Ciberseguridad del Instituto Nacional de Estándares y Tecnología (NIST CSF) y la serie de normas internacionales para la seguridad de la información (ISO 27000) están diseñados para ayudar a las organizaciones a prepararse para las auditorías de seguridad de cumplimiento normativo
   - Al adherirse a estos y otros marcos relevantes, las organizaciones pueden ahorrar tiempo a la hora de realizar auditorías externas e internas
   - Además, los marcos, cuando se utilizan junto con los controles, pueden apoyar la capacidad de las organizaciones para alinearse con los Requisitos y Estándares de cumplimiento normativo
   - Existen tres categorías principales de controles a revisar durante una auditoría, que son los controles administrativos y/o de gestión, técnicos y físicos. Para obtener más información sobre los controles específicos relacionados con cada categoría, [revise la plantilla](./plantilla_control_categories.docx).
- Lista de control de auditoría
   - Es necesario crear una lista de comprobación de la auditoría antes de llevarla a cabo
   - Por lo general, una lista de comprobación se compone de las siguientes áreas de atención:
   - Identificar el alcance de la auditoría
      - La auditoría debe:
         - Lista de los recursos que se evaluarán (por ejemplo, los firewalls están configurados correctamente, la PII está segura, los recursos físicos están bloqueados, etc.)
         - Indicar cómo la auditoría ayudará a la organización a alcanzar sus objetivos deseados
         - Indique con qué frecuencia debe realizarse una auditoría
         - Incluya una evaluación de las políticas, protocolos y procedimientos de la organización para asegurarse de que funcionan según lo previsto y de que los empleados los implementan
   - Completar una evaluación de riesgos
      - Se utiliza una Evaluación de riesgos para valorar los riesgos organizativos identificados en relación con el Presupuesto, los controles, los procesos internos y los Estándares externos (es decir, las Regulaciones).
   - Realizar la auditoría
      - Al realizar una auditoría interna, evaluará la seguridad de los recursos identificados que figuran en la lista del alcance de la auditoría.
   - Cree un plan de mitigación
      - Un plan de mitigación es una estrategia establecida para reducir el nivel de riesgo y los posibles costes, sanciones u otros problemas que puedan afectar negativamente a la postura de seguridad de la organización.
   - Comunicar los resultados a las partes interesadas
      - El resultado final de este proceso es la presentación de un informe detallado de los resultados, las mejoras sugeridas necesarias para reducir el nivel de riesgo de la organización y las Regulaciones y Estándares a los que la organización debe adherirse. 

---

## Ponga a prueba sus Conocimientos: Principios OWASP y Auditorías de Seguridad

1. Un analista de Seguridad desactiva ciertas características del software para reducir las vulnerabilidades potenciales que un atacante podría explotar en su organización. ¿Qué principio de Seguridad OWASP describe este escenario?
- [ ] Defensa en profundidad
- [ ] Solucionar correctamente los problemas de Seguridad
- [ ] Separación de funciones
- [x] Minimizar la superficie de ataque
> Este escenario describe la minimización de la superficie de ataque. 

2. Rellene el espacio en blanco: Un _____ de seguridad es una revisión de los controles, políticas y procedimientos de seguridad de una organización comparándolos con un conjunto de expectativas.
- [ ] clasificación
- [ ] examen
- [ ] encuesta
- [x] auditoría
> Una Auditoría de seguridad es una revisión de los Controles de seguridad, políticas y Procedimientos de una organización contra un conjunto de expectativas.

3. Un profesional de la seguridad examina de cerca la red de su organización y, a continuación, evalúa los riesgos potenciales para la red. Su objetivo es garantizar que las salvaguardas y los procesos internos son eficaces. ¿Qué concepto de Seguridad describe este escenario?
- [ ] Comunicación de resultados
- [x] Evaluación de los controles
- [ ] Recomendaciones de seguridad
- [ ] Cumplimiento normativo
> Este escenario describe una evaluación de controles. Una evaluación de los controles implica revisar detenidamente los recursos existentes de una organización y, a continuación, evaluar los riesgos potenciales para dichos recursos con el fin de garantizar que los controles y procesos internos son eficaces. 

4. Se pide a un profesional de la seguridad que comunique los resultados de una auditoría interna de Seguridad a las partes interesadas. ¿Qué debe incluirse en esa comunicación? Seleccione tres respuestas
- [x] Lista de Riesgos y Requisitos de Cumplimiento normativo que deben abordarse
- [ ] Lista de preguntas para que respondan las partes interesadas
- [x] Una recomendación sobre cómo mejorar la postura de seguridad de la organización
- [x] Resumen del alcance y los objetivos de la auditoría
> Al comunicar los resultados de una auditoría interna a las partes interesadas, la comunicación debe incluir un resumen del alcance y los objetivos de la auditoría; una lista de los riesgos y los requisitos de cumplimiento que deben abordarse; y una recomendación sobre cómo mejorar la postura de seguridad de la organización.

---

## Actividad de Portfolio: Realización de una Auditoría de Seguridad
- Resumen de la actividad
- En la primera parte de esta actividad, realizarás una auditoría de seguridad interna, que puedes incluir en tu portafolio de ciberseguridad
- Como recordatorio, las auditorías ayudan a garantizar que se realizan comprobaciones de seguridad, para controlar las amenazas, riesgos o vulnerabilidades que pueden afectar a la continuidad del negocio y a los activos críticos de una organización.
- Asegúrate de completar esta actividad y responder a las preguntas que siguen antes de continuar
- El siguiente punto del curso le proporcionará un ejemplo completado para que lo compare con su propio trabajo.  
- Escenario
- Revise el siguiente escenario. A continuación, complete las instrucciones paso a paso.

- Este escenario se basa en una empresa ficticia:
- Botium Toys es una pequeña empresa estadounidense que desarrolla y vende juguetes
- La empresa tiene una única ubicación física, que sirve como oficina principal, escaparate y almacén para sus productos
- Sin embargo, la presencia en línea de Botium Toy ha crecido, atrayendo a clientes en los EE.UU. y en el extranjero
- Como resultado, su departamento de tecnología de la información (TI) está bajo una presión cada vez mayor para apoyar su mercado en línea en todo el mundo.
- La directora del departamento de TI ha decidido que es necesario realizar una auditoría interna de TI
- Le preocupa mantener el cumplimiento y las operaciones comerciales a medida que la empresa crece sin un plan claro
- Ella cree que una auditoría interna puede ayudar a proteger mejor la infraestructura de la empresa y ayudarles a identificar y mitigar los posibles riesgos, amenazas o vulnerabilidades de los activos críticos
- El directivo también está interesado en asegurarse de que cumplen la normativa relacionada con el procesamiento interno y la aceptación de pagos en línea y la realización de negocios en la Unión Europea (UE)
- El responsable de TI comienza aplicando el Marco de Ciberseguridad del Instituto Nacional de Estándares y Tecnología (NIST CSF), estableciendo un ámbito y unos objetivos de auditoría, enumerando los activos gestionados actualmente por el departamento de TI y completando una evaluación de riesgos
- El objetivo de la auditoría es proporcionar una visión general de los riesgos y/o multas que la empresa podría experimentar debido al estado actual de su postura de seguridad
- Su tarea consiste en revisar el alcance, los objetivos y el informe de evaluación de riesgos del responsable de TI
- A continuación, realice una auditoría interna completando una lista de comprobación de controles y cumplimiento.

- Instrucciones paso a paso

1. Acceso a los materiales de apoyo
- Los siguientes materiales de apoyo le ayudarán a completar esta actividad. Mantenga los materiales abiertos mientras avanza a los siguientes pasos.
- [Botium Toys: Scope, goals, and risk assessment report](./audit-scope_goals_risk-assessment-report.docx)
- [Control categories](./control_categories.docx)
- [Controls and compliance checklist](./controls_and_compliance_checklist.docx)

2. Realización de la auditoría: Lista de control y conformidad
- Realice la auditoría de seguridad cumplimentando la lista de comprobación de controles y conformidad.
- Para completar la lista de comprobación, abra los materiales de apoyo proporcionados en el Paso 1. A continuación:
   1. Revise Botium Toys: Alcance, objetivos e informe de evaluación de riesgos, centrándose en:
      - Los activos gestionados actualmente por el departamento de TI
      - Las viñetas bajo "Comentarios adicionales" en la sección Evaluación de riesgos
   2. Considere la información proporcionada en el informe mediante el documento Categorías de controles.
   3. A continuación, revise la lista de comprobación de controles y cumplimiento y seleccione "sí" o "no" para responder a la pregunta de cada sección (nota: la sección de recomendaciones es opcional)*
- Qué incluir en su respuesta
- Asegúrese de abordar los siguientes elementos en su actividad completada:
   - Lista de comprobación de controles y cumplimiento
      - se selecciona "Sí" o "No" para responder a la pregunta relacionada con cada control enumerado
      - se selecciona "Sí" o "No" para responder a la pregunta relacionada con cada una de las mejores prácticas de cumplimiento
      - Se proporciona una recomendación para el responsable de TI (opcional)

### Controls and compliance checklist
- Controls assessment checklist
- select “yes” or “no” to answer the question: Does Botium Toys currently have this control in place?

| Yes | No | Control | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | Least Privilege | Se recomienda modificar la configuración por defecto de los usuarios para que por defecto tengan los mínimos privilegios necesarios. |
| ⚫ | ✅ | Disaster recovery plans | Se recomienda urgentemente generar plan de backups de datos críticos, con verificación semanal de la integridad del respaldo |
| ⚫ | ✅ | Password policies | Existe un política pero no cumple con estándares mínimos |
| ⚫ | ✅ | Separation of duties | Se recomienda separar las funciones críticas entre diferentes personas para reducir el riesgo de fraude o error. |
| ✅ | ⚫ | Firewall | |
| ⚫ | ✅ | Intrusion detection system (IDS) | Se recomienda la instalación de un sistema de detección de intrusiones para monitorear y alertar sobre actividades sospechosas. |
| ⚫ | ✅ | Backups | Punto ya abordado anteriormente |
| ✅ | ⚫ | Antivirus software | |
| ✅ | ⚫ | Manual monitoring, maintenance, and intervention for legacy systems | No existe claridad de los procedimientos a realizar |
| ⚫ | ✅ | Encryption | Se recomienda encriptar la información sensible tanto en tránsito como en reposo. |
| ⚫ | ✅ | Password management system | Se recomienda uso de sistema informático para gestionar de manera segura las contraseñas. |
| ✅ | ⚫ | Locks (offices, storefront, warehouse) | |
| ✅ | ⚫ | Closed-circuit television (CCTV) surveillance | |
| ✅ | ⚫ | Fire detection/prevention (fire alarm, sprinkler system, etc.) | |

- Compliance checklist
- select “yes” or “no” to answer the question: Does Botium Toys currently adhere to this compliance best practice? 

- Payment Card Industry Data Security Standard (PCI DSS)

| Yes | No | Best practice | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | Only authorized users have access to customers’ credit card information | Se recomienda minimizar los permisos para que solo los usuarios autorizados tengan acceso. |
| ⚫ | ✅ | Credit card information is stored, accepted, processed, and transmitted internally, in a secure environment | Se recomienda manejar fuera de la base de datos de uso general. |
| ⚫ | ✅ | Implement data encryption procedures to better secure credit card transaction touchpoints and data | Los datos no están encriptados, esto no permite mantener la confidencialidad. |
| ⚫ | ✅ | Adopt secure password management policies. | Las políticas de contraseñas no cumplen estándares, se recomienda reforzar su implementación. |


- General Data Protection Regulation (GDPR)

| Yes | No | Best practice | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | E.U. customers’ data is kept private/secured. | Se recomienda eliminar privilegios de lectura de datos sensibles solo a personal mínimo necesario |
| ✅ | ⚫ | There is a plan in place to notify E.U. customers within 72 hours if their data is compromised/there is a breach. | |
| ⚫ | ✅ | Ensure data is properly classified and inventoried | Se recomienda mantener datos históricos correctamente clasificados e inventariados en base de datos aparte. |
| ✅ | ⚫ | Enforce privacy policies, procedures, and processes to properly document and maintain data | Se recomienda revisar y actualizar regularmente las políticas de privacidad para asegurar el cumplimiento. |



- System and Organizations Controls (SOC type 1, SOC type 2)

| Yes | No | Best practice | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | User access policies are established | Se recomienda revisar regularmente las políticas de acceso de los usuarios, actualizar políticas actuales para cumplir con las regulaciones correspondientes. |
| ⚫ | ✅ | Sensitive data (PII/SPII) is confidential/private | Punto ya abordado, se recomienda manejar privilegios mínimos necesarios. |
| ✅ | ⚫ | Data integrity ensures the data is consistent, complete, accurate, and has been validated. | |
| ✅ | ⚫ | Data is available to individuals authorized to access it | |

3. Evalúe su actividad

1. Ha revisado el Alcance, los Objetivos y el Informe de Evaluación de Riesgos.
- [x] Sí
- [ ] No

2. Ha considerado los riesgos para los Clientes, empleados y/o recursos de Botium Toys, basándose en los controles y las mejores prácticas de cumplimiento que están o no implementadas actualmente
- [x] Sí
- [ ] No

3. Ha revisado el documento de categorías de control
- [x] Sí
- [ ] No

4. Ha seleccionado "sí" o "no" para cada Control de la Lista
- [x] Sí
- [ ] No

5. Ha seleccionado "sí" o "no" para cada una de las mejores prácticas de Cumplimiento normativo
- [x] Sí
- [ ] No