# El ciclo de vida de la Respuesta ante incidentes

## Bienvenido al Módulo 1
- ​Una de las cosas que más me entusiasman de detectar ​incidentes y responder a ellos es el desafío que supone utilizar los datos para comprender lo que ​ha hecho un adversario en el entorno de mi organización.
- ​No hay dos investigaciones iguales, pero hay patrones de comportamiento ​que puedes aprender a detectar a medida que perfeccionas tus habilidades analíticas.
- ​Anteriormente, estableció un conocimiento sólido de la seguridad , las amenazas y las vulnerabilidades de los activos.
- ​Exploró el Marco de Seguridad Cibernética del NIST, o CSF, como metodología para la gestión de riesgos.
- ​Aprendió a mitigar el riesgo organizacional mediante la clasificación ​y la protección de los activos.
- ​También exploró los controles de seguridad y privacidad para proteger los datos.
- ​Utilizó herramientas como MITRE y CVE para investigar vulnerabilidades comunes y ​utilizó técnicas como el modelado de amenazas para desarrollar la mentalidad de un atacante.
- ​A continuación, revisaremos el CSF del NIST centrándonos en el ciclo de vida de la respuesta a los incidentes.
- ​Recibirás tu propio diario de gestión de incidentes, que utilizarás durante ​el resto del curso.
- ​También conocerás a los equipos de respuesta a incidentes, incluidos ​los diferentes roles del equipo y cómo se organizan para responder a los incidentes.
- ​Y, por último, conocerá los diferentes tipos de ​herramientas de documentación, detección y administración que utilizará como profesional de la seguridad que trabaja en la respuesta a incidentes.
- ​Más adelante, tendrás la oportunidad de usar estas herramientas.

---

## Introducción al ciclo de vida de la Respuesta ante incidentes
- ​Los marcos del ciclo de vida de los incidentes proporcionan una estructura de apoyo a las ​operaciones de respuesta ante incidentes.
- ​Los marcos ayudan a las organizaciones a desarrollar un enfoque estandarizado para su ​proceso de respuesta ante incidentes, de modo ​que los incidentes se gestionen de forma eficaz y coherente.
- ​Existen muchos tipos diferentes de frameworks que las organizaciones pueden adoptar ​y modificar según sus necesidades.
- ​En este curso, nos centraremos en el NIST CSF. 
- A continuación, ampliaremos el CSF y ​discutiremos las fases del Ciclo de vida de respuesta ante incidentes del NIST.
- ​Para recordar, las cinco funciones principales del NIST CSF son: Identificar, ​proteger, Detectar, Responder y Recuperar.
- ​Este curso explorará los tres últimos pasos de este framework: ​detectar, Responder y Recuperar.
- ​Estos tres últimos pasos son etapas críticas durante la respuesta a incidentes, y ​como analista, detectará y responderá a incidentes e ​implementará acciones para la recuperación.
- ​El ciclo de vida de respuesta ante incidentes del NIST es otro framework del NIST con subpasos adicionales ​dedicados a la respuesta ante incidentes.
- ​Comienza con la preparación.
- A continuación, la detección y el análisis, y ​luego la contención, la erradicación y la recuperación, y por último la actividad posterior al incidente.
- ​Una cosa que hay que tener en cuenta es que el ciclo de vida del incidente no es un proceso lineal.
- ​Es un ciclo, lo que significa que los pasos pueden solaparse a medida que se hacen nuevos descubrimientos.
- ​Este ciclo de vida nos da un esquema de cómo responder eficazmente a los incidentes, ​pero antes de sumergirnos en la detección y respuesta al incidente, ​tomémonos un tiempo para entender qué es un incidente.
- ​Según el NIST, un incidente es "un suceso que pone en peligro real o inminentemente​, sin autorización legal, la confidencialidad, integridad o ​disponibilidad de la información o de un sistema de información; ​o constituye una violación o amenaza inminente de violación de la ley, ​las políticas de seguridad, los Procedimientos de seguridad o las políticas de uso aceptable.
- Es importante entender que todos los incidentes de seguridad son eventos, pero ​no todos los eventos son incidentes de seguridad.
- ​¿Qué son los eventos?
- ​Un evento es un suceso observable en una red, sistema o dispositivo.
- ​He aquí un ejemplo de un evento. Un usuario intenta iniciar sesión en su cuenta de correo electrónico, ​pero no puede porque ha olvidado su contraseña.
- ​El usuario solicita entonces un restablecimiento de contraseña y cambia con éxito su contraseña.
- ​Este es un evento observable.
- ​¿Por qué? ​Porque los sistemas y aplicaciones registran las solicitudes de restablecimiento de contraseña y ​los registros proporcionan pruebas de que algo ha ocurrido.
- ​Sabemos que alguien solicitó con éxito un restablecimiento de contraseña y ​que no violó las políticas de seguridad para acceder a la cuenta.
- ​Ahora, imagine que en lugar del propietario legítimo de la cuenta, ​un actor malicioso que intenta acceder a la cuenta, ​inició con éxito la solicitud de cambio de contraseña y cambió la contraseña de la cuenta.
- ​Esto se consideraría tanto un evento como un incidente de seguridad.
- ​Es un evento porque es un suceso observable.
- ​También es un incidente de seguridad porque un actor malintencionado violó la política de seguridad ​para acceder ilegalmente a una cuenta que no le pertenece por derecho.
- ​Recuerde, todos los incidentes de seguridad son eventos, pero no todos los eventos son incidentes de seguridad.
- ​Al igual que los detectives que trabajan en un caso manejan y ​documentan cuidadosamente sus pruebas y hallazgos, ​los analistas de seguridad están obligados a hacer lo mismo cuando investigan un ​incidente de seguridad.
- ​Una investigación de incidentes revela información crítica sobre las cinco W ​de un incidente: ​quién desencadenó el incidente, ​qué ocurrió, ​cuándo tuvo lugar el incidente, ​dónde tuvo lugar el incidente y por qué ocurrió el incidente.
- 5 W:
   - Who triggered the incident?
   - What happened?
   - When the incident took place?
   - Where the incident took place?
   - Why the incident occurred?
- ​Mantener un registro de esta información es esencial no sólo durante una ​investigación de un incidente, sino también durante el cierre de una investigación ​cuando llega el momento de redactar el informe final.
- Como analista, necesitará un método ​para documentar y referenciar esta información para poder acceder a ella fácilmente cuando la necesite.
- ​Una buena forma de hacerlo es utilizar un diario del gestor de incidentes, ​que es una forma de documentación utilizada en la respuesta a incidentes.
- ​A lo largo de este curso, utilizará su propio diario del gestor de incidentes para tomar ​notas de cualquier detalle del incidente.

---

## Explore: Aplicar el ciclo de vida del NIST a un escenario de Vishing
- Explore a vishing scenario as it applies to each phase of the NIST incident response lifecycle.
- Vishing attack: how to respond?

1. Preparation: the planning and training process
   - The organization takes action to ensure it has the correct tools and resources in place:
      - Set up uniform company email conventions
      - Create a collaborative, ethical environment where employees feel comfortable asking questions
      - Provide cybersecurity training on a quarterly basis

2. Detection and analysis: the detect and assess process
   - Security professionals create processes to detect and assess incidents:
      - Identify signs of an incident
      - Filter external emails to flag messages containing attachments such as voicemails
      - Have an incident response plan to reference

3. Containment, eradication, and recovery: the minimize and mitigate process
   - Security professionals and stakeholders collaborate to minimize the impact of the incident and mitigate any operational disruption.
      - Communicate with sender to confirm the origin of the voice message
      - Provide employees with an easy way to report and contain suspicious messages

4. Post-incident activity: the learning process
   - New protocols, procedures, playbooks, etc. are implemented to help reduce any similar incidents in the future.
      - Update the playbook to highlight additional red flags employees should be aware of
      - Review processes and workflows related to permissions and adjust oversight of those permissions

---

## Actividad de Portfolio: Documentar un incidente con el Diario del gestor de incidentes
- Resumen de la actividad
   - En esta actividad, revisará los detalles de un incidente de seguridad y documentará el incidente utilizando su Diario del gestor de incidentes.
   - Anteriormente, aprendió sobre la importancia de la documentación en el proceso de respuesta ante incidentes.
   - También ha aprendido cómo se utiliza el Diario del gestor de incidentes para registrar información sobre incidentes de seguridad a medida que se gestionan.
   - A lo largo de este curso, puede aplicar sus habilidades de documentación utilizando su Diario del gestor de incidentes.
   - Con este diario, puede registrar información sobre las experiencias que tendrá analizando escenarios de incidentes de seguridad a través de las actividades del curso. 
   - Para cuando complete este curso, tendrá múltiples entradas en su Diario del gestor de incidentes que podrá utilizar como referencia útil para recordar conceptos y herramientas.
   - Más adelante, añadirá este documento a su cartera de ciberseguridad, que podrá compartir con posibles empleadores o reclutadores.
   - Puede utilizar su Diario del gestor de incidentes como un espacio personal en el que puede realizar un seguimiento de su viaje de aprendizaje a medida que aprende sobre los conceptos de detección y respuesta ante incidentes e interactúa con diferentes herramientas de ciberseguridad.
   - Siéntete libre de incluir tus pensamientos, reflexiones y cualquier otro detalle o información importante.

- Escenario
   - Revise el siguiente escenario. A continuación, complete las instrucciones paso a paso.
   - Una pequeña clínica sanitaria estadounidense especializada en la prestación de servicios de atención primaria experimentó un incidente de seguridad un martes por la mañana, aproximadamente a las 9:00 a.m.
   - Varios empleados informaron de que no podían utilizar sus ordenadores para acceder a archivos como registros médicos.
   - La empresa dejó de funcionar porque los empleados no podían acceder a los archivos y programas informáticos necesarios para realizar su trabajo.
   - Además, los empleados también informaron de que en sus ordenadores aparecía una nota de rescate.
   - En ella se decía que todos los archivos de la empresa habían sido cifrados por un grupo organizado de piratas informáticos poco éticos conocidos por atacar organizaciones de los sectores de la sanidad y el transporte.
   - A cambio de restaurar el acceso a los archivos cifrados, la nota de rescate exigía una gran suma de dinero a cambio de la clave de descifrado.
   - Los atacantes consiguieron acceder a la red de la empresa mediante correos electrónicos de phishing dirigidos, que se enviaron a varios empleados de la empresa.
   - Los mensajes contenían un archivo adjunto malicioso que instalaba malware en el ordenador del empleado una vez descargado.
   - Una vez que los atacantes obtuvieron acceso, desplegaron su ransomware, que cifró archivos críticos.
   - La empresa no pudo acceder a los datos críticos de los pacientes, lo que provocó importantes interrupciones en sus operaciones comerciales.
   - La empresa se vio obligada a apagar sus sistemas informáticos y a ponerse en contacto con varias organizaciones para informar del incidente y recibir asistencia técnica.

- Instrucciones paso a paso

1. Acceder a la plantilla
- [Diario del gestor de incidentes](./resources/Incident-handler-s-journal-.docx)

2. Revisar el escenario
- Revise los detalles del escenario. Considera los siguientes detalles clave:
   - Una pequeña clínica sanitaria estadounidense sufrió un incidente de seguridad el martes a las 9:00 a.m. que interrumpió gravemente sus operaciones comerciales.
   - La causa del incidente de seguridad fue un correo electrónico de phishing que contenía un archivo adjunto malicioso.
   - Una vez descargado, se desplegó un ransomware que encriptó los archivos (informáticos) de la organización.
   - Un grupo organizado de piratas informáticos poco éticos dejó una nota de rescate en la que se indicaba que los archivos de la empresa estaban cifrados y exigía dinero a cambio de la clave de descifrado.

3. Registrar un asiento en el diario
   - Utilice el Diario del gestor de incidentes para documentar su primera anotación en el diario sobre el escenario dado.
   - Asegúrese de rellenar todos los campos:
      1. En la sección Fecha, registre la fecha de su anotación en el diario. Debe ser la fecha real en la que se registra la entrada, no una fecha ficticia.
      2. En la sección Entrada, indique un número de asiento. Por ejemplo, si es su primer asiento, introduzca 1.
      3. En la sección Descripción , introduzca una descripción del asiento.
      4. En la sección Herramienta(s) utilizada (s), si se utilizó alguna herramienta de ciberseguridad, enumérela(s) aquí.
      5. En la sección Las 5 W , registre los detalles sobre el escenario dado.
         - ¿Quién causó el incidente?
         - ¿Qué ha ocurrido?
         - ¿Cuándo se produjo el incidente?
         - ¿Dónde ocurrió el incidente?
         - ¿Por qué ocurrió el incidente?
      6. En la fila de notas adicionales, anota cualquier idea o pregunta que tengas sobre la situación planteada.
   - Por último, asegúrese de guardar una copia de su Diario del gestor de incidentes para poder acceder a él rápidamente a medida que avance en el curso.
   - Puede utilizarlo para su cartera profesional para demostrar sus conocimientos y/o experiencia a posibles empleadores.

- Qué incluir en su respuesta
   - La fecha y el número de la anotación en el diario
   - Una descripción de la anotación en el diario
   - 1-2 frases sobre cada una de las 5 W del escenario
   - 1-2 frases sobre cualquier pensamiento o pregunta adicional sobre el escenario.

4. Evalúe su actividad
- El proceso de autoevaluación es una parte importante de la experiencia de aprendizaje porque le permite evaluar objetivamente su primera entrada en el Diario del gestor de incidentes

- El Diario del gestor de incidentes contiene un asiento fechado y numerado
   - [x] SI
   - [ ] NO

- En la sección Descripción del Diario del gestor de incidentes ha incluido una descripción del mismo
   - [x] SI
   - [ ] NO

- En la sección Las 5 W de su Diario del gestor de incidentes, ha esbozado los detalles de una investigación de incidentes utilizando las 5 W.
   - [x] SI
   - [ ] NO

- En la sección Notas adicionales del Diario del gestor de incidentes, ha incluido pensamientos o preguntas adicionales
   - [x] SI
   - [ ] NO

- El Diario del gestor de incidentes no contiene errores gramaticales, ortográficos ni de puntuación
   - [x] SI
   - [ ] NO

- Incident handler's journal

1. Date: 30/08/2026
2. Description: Documentando un incidente de seguridad en una clínica sanitaria debido a un ataque de ransomware.
3. Tool(s) used: Ninguna herramienta específica utilizada para esta entrada.
4. The 5 W's:
   - Who: Un grupo organizado de piratas informáticos poco éticos.
   - What: Un ataque de ransomware que cifró los archivos críticos de la clínica.
   - When: Martes a las 9:00 a.m.
   - Where: En la red de la clínica sanitaria estadounidense.
   - Why: El ataque se originó a través de un correo electrónico de phishing dirigidos a varios empleados, que contenía un archivo adjunto malicioso que permitió a los atacantes desplegar el ransomware. Esto encriptó los archivos críticos de la clínica, obligandolos a interrumpir sus operaciones. Se deduce que el motivo del ataque fue obtener un rescate a cambio de la clave de descifrado, ya que los atacantes dejaron una nota de rescate solicitando dinero a cambio de restaurar el acceso a los archivos cifrados.
5. Additional notes: ¿Debería la compañía pagar el rescate solicitado por los atacantes? Supongo que depende del nivel de los respaldos de datos y de la capacidad de recuperación de la clínica. Además, ¿qué medidas preventivas se pueden implementar para evitar futuros ataques de phishing y ransomware? Posiblemente no exista una capacitación adecuada para los empleados sobre cómo identificar correos electrónicos de phishing, lo que podría haber prevenido el incidente. Además, ¿Cómo pasaron esos correos los filtros? ¿Existen filtros antiphishing y antimalware adecuados? Posiblemente la respuesta sea que no, y que la compañía debería revisar sus políticas de seguridad y mejorar sus sistemas de filtrado de correos electrónicos para evitar que este tipo de incidentes ocurran en el futuro.