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