# Introducción a la ciberseguridad

## Introducción a la ciberseguridad
- Las organizaciones deben prepararse para la tormenta asegurándose de que ​tienen las herramientas para mitigar y ​responder rápidamente a las amenazas externas.
- El objetivo es minimizar el riesgo y los posibles daños
- Como analista de seguridad, ​trabajará para proteger a ​su organización y a las personas a las que presta servicio de ​una variedad de riesgos y ​amenazas externas
- La ​ciberseguridad, o Seguridad, es la práctica ​de garantizar la confidencialidad, la integridad ​y la disponibilidad de la información ​mediante la protección de las redes, los dispositivos, las ​personas y los datos contra el ​acceso no autorizado o la explotación delictiva
- Por ejemplo, exigir ​contraseñas complejas para acceder a sitios y ​servicios mejora la confidencialidad al ​hacer que sea mucho más difícil para ​un actor de amenazas comprometerlos
- Un actor de amenazas es cualquier persona ​o grupo que presenta un riesgo de Seguridad
- ​La seguridad protege contra las amenazas externas e internas. 
- Una amenaza externa es una persona ajena ​a la organización que intenta acceder a ​información, redes o dispositivos privados. 
- Una amenaza interna ​proviene de empleados actuales o anteriores ​, proveedores externos o socios de confianza.
- ​A menudo, estas amenazas internas son accidentales, ​como cuando un empleado hace clic en ​un enlace comprometido de un correo electrónico.
- Otras veces, el actor interno participa intencionalmente en ​actividades como el acceso no autorizado a los datos ​o el abuso de los sistemas para uso personal
- Los equipos de seguridad también se aseguran de que ​una organización cumpla con la normativa, o con las ​leyes y directrices, que requieren ​la implementación de estándares de seguridad específicos
- Garantizar que las organizaciones ​cumplan con las normas puede permitirles evitar multas ​y auditorías y, al mismo tiempo, cumplir con ​su obligación ética de proteger a los usuarios.
- ​Los equipos de seguridad también mantienen ​y mejoran la productividad empresarial. 
- Ser consciente de la Seguridad también puede ​reducir los gastos asociados con los riesgos, ​como la recuperación de la pérdida de datos o el tiempo de ​inactividad operativo, y, potencialmente, evitar multas
-  ​Si los servicios o los datos de los clientes se ven comprometidos, ​esto puede reducir la confianza en ​la organización, dañar la marca y perjudicar a la empresa a largo plazo.
- estos ​son algunos títulos de trabajo que quizás desee buscar:
   - analista o especialista en ​seguridad
   - analista o especialista en ​ciberseguridad
   - analista de ​centro de operaciones de seguridad o SOC 
   - analista de seguridad de la información.

---

## Descubra el pez
- Entender el phishing
   - Antes de comenzar este desafío, es esencial distinguir entre una táctica de phishing (el truco psicológico utilizado) y un indicador técnico (el fallo verificable e infalsificable).
      - Tácticas de phishing (ingeniería social): Se trata de trucos psicológicos diseñados para manipularle.
         - Incluyen la creación de un sentido de urgencia ("¡Actúe ahora!"), la creación de miedo ("¡Su cuenta está bloqueada!") o el aprovechamiento de la autoridad (hacerse pasar por un directivo).
      - Indicadores de phishing (banderas rojas): Son las señales verificables de que el mensaje es malicioso.
         - Indicadores técnicos: Las banderas más definitivas. Incluyen dominios de correo electrónico del remitente incorrectos (por ejemplo, bank-support.co en lugar de bank.com) o direcciones de enlaces maliciosos que apuntan a un sitio web distinto del indicado (por ejemplo, el texto visible dice bank.com, pero el enlace apunta a scam.net).
         - Indicadores de contenido: Menos definitivos, pero altamente sospechosos. Incluyen mala gramática, faltas de ortografía, saludos genéricos o solicitudes inusuales (como la compra de tarjetas regalo).
- Instrucciones para la actividad:
   - Para las siguientes cuatro preguntas, examinarás un escenario de correo electrónico sospechoso
   - Su objetivo es encontrar el indicador técnico más sospechoso y definitivo de un intento de phishing, aunque haya otras señales de alarma menos graves.
   - Proceso previsto:
      1. Lea el escenario del correo electrónico.
      2. Evalúe las opciones, centrándose en el  elemento técnico (dominio, enlace).
      3. Envía tu respuesta para obtener una calificación instantánea y retroalimentación.
- Escenario
   - Los correos electrónicos de phishing suelen contener varias "banderas rojas", es decir, señales inusuales que los hacen parecer sospechosos
   - Algunas banderas rojas son sutiles (como un saludo genérico), mientras que otras son indicadores técnicos definitivos que demuestran que el correo electrónico es malicioso (como un nombre de dominio incorrecto).
   - En cada una de las preguntas siguientes, el objetivo es encontrar el indicador técnico más sospechoso y definitivo de un intento de phishing.

1. Recibes este correo electrónico que dice ser de tu banco. ¿Qué elemento es el indicador más sospechoso de que se trata de un intento de phishing?
```text
Asunto del correo electrónico: ALERTA: Se ha detectado un inicio de sesión no autorizado en su cuenta bancaria 

FROM: 'Bank Security' security@yourbank-support.co 

Date: 13 de agosto de 2025 

Cuerpo: 

Estimado cliente,

Hemos detectado un intento sospechoso de acceso a su cuenta desde un dispositivo no reconocido. Por su seguridad, hemos bloqueado temporalmente su cuenta.

Haga clic en el siguiente enlace para verificar su identidad y desbloquear su cuenta.

DESBLOQUEAR MI CUENTA

Muchas gracias,

Su equipo de seguridad bancaria
```
> El texto del enlace "DESBLOQUEAR MI CUENTA" (Incorrecto)
> La frase "bloqueó temporalmente su cuenta"  (Incorrecto)
> La dirección de correo electrónico del remitente: 'security@yourbank-support.co' (Correcto)
> El saludo "Estimado cliente" (Incorrecto)

2. Recibes un correo electrónico de tu operador de telefonía móvil sobre una "actualización gratuita del teléfono". El mensaje contiene varios errores ortográficos y gramaticales. ¿Cuál de las siguientes opciones describe mejor las señales de alarma que indican que se trata de un intento de phishing?
```text
Asunto del correo electrónico: ¡Noticias emocionantes! ¡Su actualización gratuita a un nuevo teléfono! 

De: 'Cellular Service' no-reply@cellularservice.pro 

Date: 13 de Agosto de 2025 

Cuerpo: 

Felicidades, apreciado cliente Usted ha sido elegido para una actualización gratuita a nuestra nueva línea de teléfonos. Para recibir su nuevo teléfono, sólo tiene que rellenar el formulario haciendo clic en el enlace de abajo. RECLAME SU ACTUALIZACIÓN AHORA (http://freeprhone-upgrade.com)
```
> Le pide que haga clic en un enlace para reclamar su recompensa. (Incorrecto)
> Un saludo genérico como "apreciado cliente" (Incorrecto)
> Errores tipográficos, ortográficos y gramaticales. (Correcto)
> Una sensación de urgencia (date prisa para conseguir tu teléfono gratis). (Incorrecto)

3. Recibe un correo electrónico de un compañero de trabajo pidiéndole ayuda. El mensaje parece extraño. ¿Cuál es la táctica de phishing más probable?
```text
Asunto del correo electrónico: Necesito tu ayuda con un pago rápido

FROM: 'Your Manager' <manager.name@gmail.com>

Date: 13 de agosto de 2025

Cuerpo:

Hola equipo,

Estoy en una reunión ahora mismo y necesito urgentemente que compréis unas tarjetas regalo para un cliente. ¿Podríais enviarme los detalles lo antes posible? Os lo reembolsaré más tarde.

Muchas gracias,

Nombre del gerente
```
> El correo electrónico es demasiado corto e informal.
> El nombre del remitente es "Su jefe" (Incorrecto)
> La solicitud de un pago rápido e inusual con tarjetas regalo. (Correcto)
> Asunto: "Necesito tu ayuda"

4. Recibes una alerta de seguridad de una red social. Pasa el ratón por encima del enlace "Verifique su cuenta". ¿Cuál de estas direcciones de enlace es un signo definitivo de un intento de phishing?
```text
Asunto del correo electrónico: Alerta de seguridad: Hemos detectado un inicio de sesión inusual 

FROM: 'Redes sociales' noreply@socialmedia.com 

Date: 13 de agosto de 2025 

Cuerpo: 

Hola Sarah, Alguien acaba de acceder a tu cuenta desde una nueva ubicación. Para proteger tu cuenta, haz clic inmediatamente en el siguiente enlace. [Verificar su cuenta]
```
> http://login-security.net/socialmedia/verify (Correcto)
> https://socialmedia.com/alerts/login_alerts 
> https://social-media.com/login
> http://socialmedia.com/account/verify 

---

## Toni: Mi ruta de acceso a la ciberseguridad
- Nuestros equipos protegen a Google y ​a sus usuarios de amenazas graves.
- ​Por lo general, atacantes respaldados por el gobierno, ​operaciones de influencia coordinadas y actores de amenazas ​graves de ciberdelincuencia
- ​Una de las cosas que tuve que averiguar desde muy temprano en ​este viaje es qué tipo de aprendiz era. ​Trabajo mejor con un estilo de aprendizaje estructurado. 
- ​Así que recurrir a muchos de ​estos cursos y recursos en línea que tomaban ​este material y lo ​estructuraban desde los primeros principios hasta la aplicación me pareció muy bien. 
- ​La mayor parte del trabajo de ciberseguridad se aprenderá en ​el trabajo en el ​entorno específico que estás protegiendo.
- Por lo tanto, tienes que trabajar bien con tus compañeros de equipo ​para poder construir esa base de conocimientos
- ​Mi consejo sería que mantuvieras la curiosidad y siguieras aprendiendo, ​especialmente centrándote en tus habilidades técnicas ​y desarrollándolas a lo largo de tu carrera
- ​Es muy fácil contraer el ​síndrome del impostor en la ciberseguridad porque es muy ​amplio y el dominio de ​todas estas áreas diferentes es el trabajo de toda una vida. 

---

## Responsabilidades de un analista de ciberseguridad de nivel inicial
- ​La tecnología está cambiando rápidamente y ​también lo hacen las tácticas y técnicas que utilizan los atacantes
- ​A medida que evoluciona la infraestructura digital, ​se espera que los profesionales de la seguridad aumenten continuamente ​sus habilidades para ​proteger y asegurar la información sensible
- Los analistas de seguridad son responsables de ​vigilar y proteger la información y los sistemas
   - proteger los sistemas informáticos y de redes
      - Si se detecta una amenaza, entonces ​un analista suele ser el primero en responder
      - ​Los analistas también suelen participar en ejercicios para ​buscar debilidades en los propios sistemas de una organizació
      - Por ejemplo, un analista de seguridad puede ​contribuir a las pruebas de penetración o al hacking ético
   - instalar ​software de prevención con el fin de ​identificar riesgos y vulnerabilidades
      - A menudo trabajarán con equipos de desarrollo para ​apoyar la seguridad de los productos estableciendo ​procesos y sistemas adecuados para ​satisfacer las necesidades de protección de datos de la organización
   - realizar auditorías de seguridad periódicas
      - Una auditoría de seguridad es ​una revisión de los registros de seguridad de una organización, ​actividades y otros documentos relacionados

---

## Nikki: Un día en la vida de un ingeniero de Seguridad
- mi función se ​centra más en detectar amenazas internas o actividades sospechosas internas dentro de la empresa
- ​La razón principal por la que elegí seguir una carrera en ciberseguridad es ​la flexibilidad de la ruta de acceso profesional.
- ​Una vez que estés en Seguridad, hay muchos campos diferentes en los que puedes sumergirte
- ¿ ​Un día en la vida como profesional de Seguridad de nivel inicial? ​Puede cambiar día a día, pero tiene dos partes básicas
   - ​Está el lado de las operaciones, que responde a las detecciones y ​realiza investigaciones
   - Y luego está la parte del proyecto, en la que trabajas con otros equipos para crear ​nuevas detecciones o mejorar las detecciones actuales
- el analista ​se centra más en las operaciones y el ingeniero, ​si bien puede realizar operaciones, también crea las detecciones y realiza un trabajo ​más centrado en el proyecto
- Una de las formas más importantes en las que he tenido un impacto como ​profesional de ciberseguridad principiante es trabajando en los manuales que utiliza nuestro equipo.
- Un manual de estrategias es una lista de cómo realizar una detección determinada y de ​lo que el analista debe analizar para investigar esos incidentes.