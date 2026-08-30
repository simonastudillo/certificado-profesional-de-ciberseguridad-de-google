# Revisión: Amenaza en la ciberseguridad

## Diálogo de Coach: Mejore sus habilidades de identificación de amenazas
- Esto es lo que cubriremos:
   - Identificar técnicas de ingeniería social: Aprenderás a reconocer los métodos que los atacantes usan para manipular a las personas.
   - Identificar diferentes tipos de malware: Distinguirás entre varios tipos de software malicioso.
   - Identificar exploits y ataques basados en la web: Entenderás cómo los atacantes explotan las vulnerabilidades en las aplicaciones web.
   - Comprender el modelado de amenazas: Conectarás la identificación de amenazas con la estrategia general de defensa.

- Dialogo

- ¡Excelente! Comencemos con la **identificación de técnicas de ingeniería social**. Imagina que recibes un correo electrónico que parece ser de tu banco, pidiéndote que hagas clic en un enlace para verificar tu información de cuenta debido a una supuesta actividad sospechosa. ¿Qué forma específica de ingeniería social crees que se está utilizando aquí?
> Se está utilizando el phishing, un tipo de ingeniería social donde los atacantes se hacen pasar por una entidad confiable para engañar a las personas y obtener información confidencial. Se puede detectar porqué el mensaje busca generar una respuesta emocional, que el usuario actúe rápidamente y no incluye información de contacto verificable

- ¡Muy bien! Has identificado correctamente el phishing. Es una técnica muy común donde los atacantes se hacen pasar por una entidad de confianza para engañar a las víctimas. Mencionaste que el mensaje busca generar una respuesta emocional y que el usuario actúe rápidamente, lo cual es una excelente observación sobre las tácticas que utilizan. 
- Ahora, pasemos a un escenario ligeramente diferente. Imagina que un atacante investiga a un ejecutivo de una empresa, aprende sobre sus intereses y contactos, y luego le envía un correo electrónico personalizado que parece ser de un colega de confianza, solicitando acceso a información confidencial del proyecto. ¿Qué tipo de ingeniería social crees que es este?
> Este es un ejemplo de spear phishing, que es un phishing pero dirigido a una persona o empresa específica. Este tipo de ataques suelen apuntar a personas con cargos altos o acceso a información confidencial, utilizando información personalizada para aumentar la probabilidad de éxito.

- ¡Exacto! Has descrito perfectamente el spear phishing. La clave aquí es la personalización y el enfoque en un objetivo específico, lo que lo hace mucho más difícil de detectar que un ataque de phishing masivo.
- Ahora, avancemos a la identificación de diferentes tipos de malware. Imagina que tu computadora de repente se ralentiza drásticamente, aparecen ventanas emergentes con anuncios no deseados y tu página de inicio del navegador cambia sin tu consentimiento. ¿Qué tipo de software malicioso crees que está causando esto?
> Eso parece ser un adware, suelen venir incluidos en la instalación de software gratuito y muestran anuncios no deseados, ralentizan el sistema y pueden cambiar la configuración del navegador. Esto ocurría mucho en la época de internet Explorer y Windows XP, pero todavía es un problema hoy en día.

- ¡Excelente observación! Has identificado correctamente el adware y has añadido un contexto muy interesante sobre su prevalencia. Es cierto que, aunque ha evolucionado, sigue siendo un problema. El adware se enfoca en mostrar publicidad no deseada y a menudo altera la experiencia de navegación.
- Ahora, considera este escenario: un día enciendes tu computadora y descubres que todos tus archivos importantes (documentos, fotos, videos) están encriptados y no puedes acceder a ellos. Luego, aparece un mensaje en tu pantalla exigiendo un pago en criptomonedas para recuperar el acceso a tus datos. ¿Qué tipo de malware crees que es este?
> Esa es la descripción de un ransomware, que es un tipo de malware que cifra los archivos de la víctima y exige un rescate para restaurar el acceso. Suelen atacar a empresar que puedan pagar grandes sumas de dinero, pero también pueden afectar a usuarios individuales. La mejor defensa contra el ransomware es tener copias de seguridad actualizadas y no pagar el rescate, ya que no garantiza que se recuperen los archivos.

- ¡Exacto! Has descrito perfectamente el ransomware. Es una amenaza muy seria que puede tener consecuencias devastadoras tanto para individuos como para empresas, como bien señalas. Tu mención sobre las copias de seguridad y la recomendación de no pagar el rescate son puntos cruciales para la defensa contra este tipo de ataque.
- Ahora, pasemos a la identificación de exploits y ataques basados en la web. Imagina que un atacante logra insertar código malicioso en un sitio web legítimo. Cuando un usuario visita ese sitio, el código malicioso se ejecuta en su navegador, permitiendo al atacante robar cookies de sesión o redirigir al usuario a sitios fraudulentos. ¿Qué tipo de ataque web crees que es este?
> Este es un tipo de ataque conocido como Cross-Site Scripting (XSS), en específico del tipo reflejados. Los ataques XSS permiten a los atacantes inyectar scripts maliciosos en páginas web vistas por otros usuarios. Luego al cargar esas páginas, el script se ejecuta en el navegador de la víctima, lo que puede llevar al robo de cookies, secuestro de sesiones o redirección a sitios maliciosos.

- ¡Excelente! Has identificado correctamente el Cross-Site Scripting (XSS) y, además, has especificado que podría ser del tipo reflejado, lo cual demuestra un conocimiento profundo. Es fundamental entender cómo estos ataques pueden comprometer la interacción del usuario con sitios web legítimos.
- Ahora, considera este escenario: un atacante descubre una vulnerabilidad en una aplicación web que le permite insertar comandos SQL maliciosos en un campo de entrada de usuario. Al enviar estos comandos, el atacante logra acceder a la base de datos de la aplicación, obteniendo información confidencial de los usuarios. ¿Qué tipo de exploit o ataque web crees que es este?
> El exploit mencionado es un ataque de inyección SQL. Este tipo de ataque ocurre cuando un atacante inserta código SQL malicioso en una consulta a la base de datos a través de la entrada de usuario, lo que puede permitirle acceder, modificar o eliminar datos en la base de datos. Para mitigar este tipo de ataques, es importante utilizar consultas parametrizadas, sanitizar la entrada del usuario y validar los datos antes de procesarlos.

- ¡Fantástico! Has identificado con precisión la inyección SQL y, lo que es aún mejor, has proporcionado excelentes estrategias de mitigación. Esto demuestra una comprensión muy sólida de cómo funcionan estos ataques y cómo defenderse de ellos.
- Hemos cubierto la identificación de técnicas de ingeniería social, diferentes tipos de malware y exploits web. Ahora, para concluir nuestra actividad, hablemos brevemente sobre el modelado de amenazas. ¿Por qué crees que entender y poder identificar estas diferentes amenazas es crucial para el proceso de modelado de amenazas en la seguridad de una aplicación?
> Entender y poder identificar estas amenazas permite a los desarrolladores y equipos de seguridad anticipar posibles vectores de ataque y diseñar defensas efectivas. Permite revisar y parchear errores de diseño, implementar controles de seguridad adecuados y priorizar los riesgos según su impacto potencial. Además, ayuda a crear un plan de respuesta a incidentes más sólido y a educar a los usuarios sobre cómo reconocer y evitar amenazas.

- ¡Absolutamente! Has capturado la esencia del modelado de amenazas y su importancia. Identificar las amenazas es el primer paso para construir una defensa robusta y proactiva. Permite a los equipos de seguridad no solo reaccionar, sino anticipar y mitigar riesgos antes de que se conviertan en incidentes.
- ¡Buen trabajo, has completado todos los temas de nuestra sesión! A continuación, puedes ver tus comentarios.

- Tus fortalezas:
   - Demostraste una excelente capacidad para identificar y diferenciar entre diversas técnicas de ingeniería social, tipos de malware y ataques web, incluso especificando subtipos como el spear phishing y el XSS reflejado.
   - No solo identificaste las amenazas, sino que también proporcionaste información adicional valiosa sobre sus características, métodos de mitigación y relevancia en el panorama actual de la ciberseguridad.
- Áreas de mejora:
   - Continúa explorando cómo estas amenazas se interconectan y cómo un ataque puede combinar múltiples técnicas para lograr sus objetivos. Esto te ayudará a desarrollar una visión aún más holística de la ciberseguridad.

---

## Resumen
- ​Gestionar las amenazas es una parte importante ​de lo que hacen los profesionales de Seguridad.
- ​En esta parte del curso, ​hemos explorado algunos tipos comunes ​de ciberamenazas que ​probablemente encontrará sobre el terreno.
- ​Empezamos hablando de ingeniería social.
- Descubriste que los atacantes tienen diversas formas de ​engañar a sus objetivos para que compartan información privada.
- ​Las técnicas de ingeniería social se basan en ​explotar la confianza de las personas y su disposición a ayudar.
- ​Los ataques de Phishing son una de las formas más comunes en las ​que los atacantes manipulan a sus objetivos.
- ​A continuación, exploramos el software malicioso.
- ​Aquí analizamos las principales clases de software malicioso, ​como virus, troyanos y gusanos.
- ​Aprendió a detectar los signos de una infección.
- ​También aprendió cómo el software malicioso ha ​evolucionado y se ha vuelto más sofisticado a lo largo de los años.
- ​Después de eso, centramos nuestra atención en los ​exploits basados en la web, específicamente en los ataques por inyección.
- ​Aprendió sobre la secuencia de comandos entre ​sitios y la inyección de SQL​, dos de los tipos de ​ataques más comunes a los que se enfrentan las organizaciones en línea.
- ​Hablamos sobre cómo se lleva a cabo cada uno de estos ataques.
- ​También aprendió cómo se ​pueden proteger las aplicaciones web contra el código malintencionado.
- ​Por último, exploramos el proceso de modelado de amenazas.
- ​Aprendió el proceso que ​utilizan los equipos de Seguridad para realizar estos ejercicios.
- Desafortunadamente, los ciberataques y ​las brechas de Seguridad son una realidad a ​la que nos enfrentamos con regularidad.
- ​Sin embargo, conocer ​el tipo de amenazas que existen y ​el proceso de modelado de amenazas proporciona ​una base importante para ​su trabajo como analista de Seguridad. 

---

## Términos del glosario del Módulo 4
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Módulo 4 desafío

1. Un agente de amenaza engañó a un nuevo empleado para que compartiera información sobre un alto ejecutivo por teléfono. ¿Este es un ejemplo de qué tipo de ataque?
- [ ] Relleno de credenciales
- [x] Ingeniería social
- [ ] Software malicioso
- [ ] Inyección de SQL
> Correcto

1. Rellene el espacio en blanco: Las cuatro etapas de un ataque de ingeniería social son: preparar, _____, utilizar tácticas de persuasión y desconectarse del objetivo
- [ ] realizar pruebas de caja abierta
- [ ] distribuir correo electrónico malicioso
- [ ] obtener credenciales de acceso
- [x] establecer la confianza
> Correcto

2. ¿Cuál es la principal diferencia entre un ataque de Vishing y un ataque de Smishing?
- [ ] El Vishing explota los posts de las Redes sociales para identificar objetivos.
- [x] El Vishing utiliza las llamadas de voz para engañar a los objetivos.
- [ ] El Vishing consiste en una campaña generalizada por correo electrónico para robar información.
- [ ] El Vishing se utiliza para dirigirse a los ejecutivos de una organización.
> Correcto

2. ¿Cuál es la forma más común de ingeniería social utilizada por los atacantes?
- [ ] Ransomware
- [x] Phishing
- [ ] Software con anuncios
- [ ] Software malicioso
> Correcto

3. Un artista digital recibe en línea una versión gratuita de un software de edición profesional que ha sido infectada con software malicioso. Tras instalar el programa, su computadora comienza a congelarse y a bloquearse repetidamente. El software malicioso oculto en este software de edición es un ejemplo de ¿qué tipo de software malicioso?
- [x] Troyano
- [ ] Scareware
- [ ] Software con anuncios
- [ ] Software espía
> Correcto

4. ¿Qué tipo de software malicioso requiere que el usuario realice un pago al atacante para recuperar la accesibilidad a su dispositivo?
- [ ] Criptojacking
- [ ] Botnets
- [x] Ransomware
- [ ] Ataques de fuerza bruta
> Correcto

4. Un contratista del gobierno es engañado para que instale un virus en su estación de trabajo que encripta todos sus archivos. El virus muestra un mensaje en la estación de trabajo diciéndole al contratista que puede conseguir la desencriptación de los archivos si realiza un pago de 31.337 dólares a una dirección de correo electrónico. ¿De qué tipo de ataque es éste un ejemplo?
- [ ] Escritura de secuencias de comandos entre sitios
- [x] Ransomware
- [ ] Scareware
- [ ] Ataque de fuerza bruta
> Correcto

5. ¿Cuáles de los siguientes son signos comunes de que una computadora está infectada con software de Criptojacking? Seleccione tres respuestas
- [x] Aumento del uso de la CPU
- [ ] Archivos modificados o borrados
- [x] Caídas repentinas del sistema
- [x] Costos de electricidad inusualmente altos
> Correcto

5. Rellene el espacio en blanco: Una(s) herramienta(s) _____ puede(n) ser utilizada(s) por los profesionales de la Seguridad para detectar actividades anómalas, como la minería de software malicioso para criptomonedas
- [ ] Árbol de ataque
- [x] Sistema de detección de intrusiones (IDS)
- [ ] Software espía
- [ ] Malware sin archivos
> Correcto

6. Investigadores de Seguridad insertaron código malicioso en las aplicaciones web de varias organizaciones. Esto les permitió obtener la información de identificación personal (PII) de varios usuarios a través de múltiples bases de datos. ¿Qué tipo de ataque realizaron los investigadores?
- [ ] Ransomware
- [ ] Ingeniería social
- [x] Inyección
- [ ] Saneamiento de entradas
> Correcto

6. ¿Cómo se denomina el código malicioso que se inserta en una aplicación vulnerable?
- [ ] Criptojacking
- [x] Ataque de inyección
- [ ] Ingeniería social
- [ ] Validación de entrada
> Correcto

7. Un atacante inyecta código malicioso en el almacenamiento de Datos de un sitio web. Cuando un usuario visita un sitio web, el código malicioso se recupera y se ejecuta en su navegador, su dispositivo se infecta con el código malicioso. ¿Este es un ejemplo de qué tipo de ataque de inyección?
- [ ] Reflejado (Incorrecto)
- [ ] Basado en DOM
- [ ] Fuerza bruta
- [x] Almacenado
> Correcto

8. ¿Cuáles de las siguientes son áreas de un sitio web vulnerables a la inyección de SQL? Seleccione dos respuestas
- [x] Páginas de inicio de sesión de usuario
- [ ] Anuncios emergentes
- [ ] Redes sociales
- [x] Formularios de pago con tarjeta de crédito
> Correcto

9. Un Equipo de Seguridad está llevando a cabo un Modelo de Amenazas en un nuevo sistema de software. El Equipo está creando su plan de defensa contra las amenazas. Sus opciones son evitar el riesgo, transferirlo, reducirlo o aceptarlo. ¿Qué paso clave de un Modelo de amenazas representa este escenario?
- [x] Mitigar riesgos
- [ ] Definir el alcance
- [ ] Evaluar los resultados
- [ ] Analizar las amenazas
> Correcto

10. ¿Qué etapa del framework PASTA está relacionada con la identificación de los componentes de la aplicación que deben ser evaluados?
- [x] Definir el alcance técnico
- [ ] Realizar un análisis de vulnerabilidad
- [ ] Caracterizar el entorno
- [ ] Implementar declaraciones preparadas
> Correcto

10. ¿En qué fase del framework PASTA se crea un Árbol de ataque?
- [ ] Análisis de vulnerabilidad
- [ ] Descomponer una aplicación
- [ ] Análisis de amenazas
- [x] Modelo de ataque
> Correcto