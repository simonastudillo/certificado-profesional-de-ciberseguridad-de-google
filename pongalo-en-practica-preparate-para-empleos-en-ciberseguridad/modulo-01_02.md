# Detección de Eventos e Incidentes

## Bienvenido al módulo 1
- ​Bienvenido a la primera sección del curso.
- Hablaremos de lo que significa tener una mentalidad de seguridad, ​y de cómo utilizar esa mentalidad para ​proteger los datos y activos de una organización.
- ​A continuación, exploraremos el proceso de ​escalado de incidentes en caso de infracción.
- ​Por último, compartiremos ​información que le ayudará a comprender mejor ​la naturaleza sensible de ​los datos que tendrá que proteger.
- ​A continuación, nos centraremos en ​cómo desarrollar una mentalidad de seguridad ​y utilizarla para proteger a las organizaciones ​y a las personas a las que sirven.

---

## Analiza los registros de eventos con Gemini Notebook
- Situación
   - Eres un analista de seguridad junior, un profesional principiante encargado de supervisar redes e investigar incidentes de seguridad.
   - Tu sistema ha detectado cierta actividad inusual.
   - Tu tarea consiste en revisar los siguientes datos de registro simplificados para identificar posibles amenazas o incumplimientos de las políticas.

- Tu objetivo
   - Analiza los datos de registro que aparecen a continuación, identifica cualquier evento sospechoso y utiliza tus conclusiones para responder a las preguntas.

- Instrucciones
   - Copia los datos de registro: copia todo el texto del bloque de código que aparece a continuación.
   ```log
   Log File: system_activity_log_2025-07-30.txt
   TIMESTAMP            | USER          | SOURCE_IP        | EVENT_TYPE         | DETAILS
   ---------------------|---------------|------------------|--------------------|--------------------------------------------
   2025-07-30 08:00:15  | admin         | 192.168.1.1      | Login_Success      | User 'admin' logged in from internal network
   2025-07-30 08:05:30  | John.Doe      | 192.168.1.5      | File_Access        | Opened: /documents/report_draft.docx
   2025-07-30 08:10:45  | jane.smith    | 192.168.1.10     | Email_Sent         | To: allstaff@company.com, Subject: Important Update
   2025-07-30 08:15:00  | guest         | 10.0.0.100       | Login_Failed       | User 'guest' attempted login from unknown IP (1 attempt)
   2025-07-30 08:15:05  | guest         | 10.0.0.100       | Login_Failed       | User 'guest' attempted login (2 attempts)
   2025-07-30 08:15:10  | guest         | 10.0.0.100       | Login_Failed       | User 'guest' attempted login (3 attempts)
   2025-07-30 08:20:20  | John.Doe      | 192.168.1.5      | File_Access        | Copied: /finance/budget_2026_final.xlsx to /public_share
   2025-07-30 08:25:35  | system        | N/A              | Service_Status     | Web server (Apache) is running.
   2025-07-30 08:30:40  | admin         | 203.0.113.25     | Login_Success      | User 'admin' logged in from external IP (unusual location)
   2025-07-30 08:35:50  | mary.jones    | 192.168.1.12     | File_Deletion      | Deleted: /personal/vacation_photos.jpg
   2025-07-30 08:40:05  | system        | N/A              | Software_Update    | Antivirus
   ```
   - Inicia Gemini Notebook: Accede a https://notebook.google.com/
   - Crea un nuevo cuaderno de Gemini: haz clic en «Crear nuevo cuaderno»
   - Crea un nuevo documento: Pega los datos de registro que aparecen a continuación en un nuevo documento de Gemini Notebook.
   - Investiga con la IA: Piensa como un detective. Haz preguntas a Gemini Notebook para que te ayude a entender los datos. Algunas buenas preguntas para empezar podrían ser:
      - «¿Qué me dicen estos registros sobre la actividad de los usuarios?»
      - «¿Puedes identificar algún evento que parezca fuera de lo normal?»
      - «Desde el punto de vista de la seguridad, ¿cuáles son las entradas de registro más preocupantes y por qué?»
   - Responde a las preguntas: Utiliza los conocimientos que has obtenido de tu investigación para completar el cuestionario

1. Según tu análisis con Gemini Notebook, ¿qué entrada del registro es la más sospechosa y probablemente requeriría una escalación inmediata?
   - [ ] 2025-07-30 08:00:15 | admin | 192.168.1.1 | Login_Success
   - [x] 2025-07-30 08:20:20 | John.Doe | 192.168.1.5 | File_Access | Copiado: /finance/budget_2026_final.xlsx a /public_share
   - [ ] 2025-07-30 08:40:05 | system | N/A | Software_Update | Definiciones de antivirus actualizadas correctamente
   - [ ] 2025-07-30 08:15:10 | guest | 10.0.0.100 | Login_Failed | User 'guest' attempted login (3 attempts)
>

2. ¿Qué dos entradas de registro separadas, cuando se combinan, podrían indicar un posible compromiso de la cuenta o una amenaza interna maliciosa?
   - [ ] El inicio de sesión de administrador desde 192.168.1.1 y la actualización del software de sistema.
   - [ ] Los múltiples inicios de sesión fallidos del usuario invitado y la eliminación del archivo mary.jones.
   - [ ] El inicio de sesión de administrador desde 203.0.113.25 y los inicios de sesión de invitados fallidos.
   - [x] El login admin desde 203.0.113.25 y la copia del fichero por John.Doe.
> Correcto

3. El registro muestra varios intentos fallidos de inicio de sesión desde una dirección IP específica. Según su análisis de NotebookLM, ¿qué usuario y dirección IP estuvieron implicados en esta actividad?
   - [z] Usuario: invitado, Dirección IP: 10.0.0.100
   - [ ] Usuario: admin, Dirección IP: 192.168.1.1
   - [ ] Usuario: John.Doe, dirección IP: 192.168.1.5
   - [ ] Usuario: invitado, Dirección IP: 192.168.1.10
> Correcto

---

## Seguridad como mentalidad
- Dediquemos un poco de tiempo a analizar ​un concepto que lo ayudaría a lo ​largo de su carrera en Seguridad: ​tener una mentalidad de seguridad.
- ​En cursos anteriores, analizamos diversas amenazas, riesgos ​y vulnerabilidades y cómo pueden afectar a las ​operaciones de la organización y a las personas a las que ​prestan servicio esas organizaciones.
- ​Estos conceptos son consideraciones clave a la ​hora de pensar en tener una mentalidad de Seguridad.
- ​Tendrás que reconocer no solo lo que defiendes, ​sino también contra qué o contra quién te defiendes.
- ​Por ejemplo, es importante ​reconocer los tipos de activos que son ​esenciales para mantener ​las funciones empresariales de una organización, ​junto con los tipos de amenazas, riesgos y vulnerabilidades que ​pueden afectar negativamente a esos activos.
- ​Y de eso se trata tener una mentalidad de Seguridad.
- ​Una mentalidad de Seguridad es la ​capacidad de evaluar el riesgo y ​buscar e identificar constantemente ​la violación potencial o real de un sistema, aplicación o datos.
- ​Anteriormente en el programa, ​analizamos las amenazas, los riesgos ​y las vulnerabilidades que plantean los ​ataques de ingeniería social, como la suplantación de identidad.
- ​Estos ataques están diseñados para comprometer los ​activos de una organización y ayudar ​al actor o actores de la amenaza ​a acceder a información confidencial.
- ​El uso de nuestra mentalidad de Seguridad puede ​ayudar a prevenir este tipo de ataques.
- ​Es importante que nos mantengamos constantemente ​al día con los tipos de ataques que se están produciendo.
- ​Para ello, es bueno desarrollar el hábito de buscar ​información sobre ​las últimas amenazas o vulnerabilidades de Seguridad.
- ​Al hacerlo, es ​posible que se le ocurran nuevas ideas para proteger los datos de la empresa.
- ​La seguridad es un objetivo diario ​para todos los equipos de seguridad de la industria.
- ​Por lo tanto, tener una mentalidad de Seguridad ayuda a los analistas a ​defenderse de la presión constante de los atacantes.
- ​Esa mentalidad puede hacerte pensar: «Cada clic del ​ratón tiene el potencial de provocar una violación de la Seguridad».
- ​Ese nivel de escrutinio como profesional de Seguridad ​lo ayuda a prepararse para ​el peor de los casos, incluso si no sucede.
- ​Los analistas principiantes pueden ayudar a proteger los activos de bajo nivel, ​como la red WiFi para huéspedes de una organización, y ​los activos de gran importancia, como la propiedad intelectual, los ​secretos comerciales, la PII e incluso la información financiera.
- ​Su mentalidad de Seguridad le permite ​proteger todos los niveles de activos.
- ​Sin embargo, si se produce un incidente, ​eso no significa que respondas a ​todos los incidentes de la misma manera.
- ​Por lo tanto, analizaremos la priorización de los incidentes ​un poco más adelante en el curso.
- ​Tener una mentalidad de seguridad sólida ​puede ayudarlo a diferenciarse de ​otros candidatos mientras se ​prepara para ingresar a la profesión de seguridad.
- ​Incluso puede ser una buena idea hacer ​referencia a esa base en futuras entrevistas de trabajo.
- ​Hablaremos ​en detalle sobre la preparación de la entrevista más adelante en el curso.
- ​Próximamente, nos centraremos en la ​detección de incidentes con mayor detalle. 