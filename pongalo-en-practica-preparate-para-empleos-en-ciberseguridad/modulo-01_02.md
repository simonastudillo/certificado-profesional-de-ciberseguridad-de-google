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