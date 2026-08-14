# Revisión: Marcos de seguridad y controles

## Resumen
- Empezamos por definir qué son los marcos de Seguridad ​y cómo ayudan a las organizaciones a ​proteger la información crítica
- También exploramos los controles de Seguridad ​y el importante papel que ​desempeñan en la protección contra ​los riesgos, las amenazas y las vulnerabilidades
- Esto incluyó una discusión sobre la tríada CID de la CIA ​, que es un modelo de Seguridad fundamental, y dos marcos del NIST ​: el CSF y el S.P. 800-53
- ​A continuación, abordamos algunos de los principios de diseño seguro de OWASP. 
- Terminamos con la introducción de las auditorías de Seguridad centrándonos en ​los elementos de una auditoría interna que se le ​puede pedir que complete o a los que contribuya
- Los profesionales de la seguridad utilizan los conceptos que analizamos ​para ayudar a proteger los activos, los ​datos, los sistemas y las personas de las organizaciones.
- A ​medida que avance en ​su camino hacia la profesión de Seguridad, ​muchos de estos conceptos surgirán repetidamente
- Lo que estamos haciendo ahora es brindarle ​una comprensión básica de ​las prácticas y los temas de Seguridad ​que lo ayudarán en el camino

---

## Glosario de términos del módulo 2
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 2

1. ¿Cuál es el objetivo principal de un marco de seguridad?
- [ ] Aplicar medidas técnicas que reduzcan las vulnerabilidades de los sistemas y aplicaciones.
- [ ] Realizar un análisis y una evaluación detallados de los controles de seguridad actuales de una organización.
- [x] Proporcionar una guía estructurada para que una organización gestione los riesgos de ciberseguridad y proteja los datos.
- [ ] Definir la actitud general y la preparación de una organización frente a las amenazas de ciberseguridad. (Incorrecta)
> Correcta

2. Rellene el espacio en blanco: Un empleado que utiliza la autenticación de múltiples factores para verificar su identidad es un ejemplo del proceso _____.
- [ ] confidencialidad
- [x] autenticación
- [ ] encriptación
- [ ] integridad
> Correcta

3. ¿Cuál de los siguientes es un ejemplo de biometría?
- [ ] Marco de seguridad
- [x] Huella dactilar
- [ ] Encriptación
- [ ] Password (Contraseña)
> Correcta

3. ¿Cuáles de los siguientes son ejemplos de biometría? Seleccione todos los que procedan
- [x] Escaneado de la palma de la mano
- [ ] Contraseña
- [x] Exploración ocular
- [x] Huella dactilar
> Correcta

4. Usted trabaja como analista de seguridad en un banco y necesita asegurarse de que los clientes pueden acceder a la información de sus cuentas. ¿Qué principio básico de la tríada CID utiliza para confirmar que sus Datos les son accesibles?
- [ ] Confidencialidad
- [ ] Integridad
- [x] Disponibilidad
- [ ] Precisión
> Correcta

4. Usted trabaja como analista de seguridad para una organización de la cadena de suministro y necesita confirmar que todos los datos del inventario son correctos, auténticos y fiables. ¿Qué principio básico de la tríada CID está utilizando?
- [ ] Confidencialidad
- [ ] Disponibilidad
- [x] Integridad
- [ ] Credibilidad
> Correcta

5. ¿Cuál de las siguientes afirmaciones describe con exactitud el MCA? Seleccionar all that apply.
- [x] El CSF es un framework voluntario que consiste en estándares, directrices y mejores prácticas para gestionar el riesgo de la ciberseguridad. 
- [ ] La función de identificación del MCA consiste en devolver los sistemas afectados a su funcionamiento normal. (Incorrecta)
- [x] Restaurar los archivos o Datos afectados forma parte de la función Recuperar del LCR.
- [ ] La Función Detectar del MCA consiste en mejorar las capacidades de Monitoreo para aumentar la Velocidad y la Eficacia de las Detecciones.
> Incorrecta

5. ¿Cuál de las siguientes afirmaciones describe con exactitud el MCA? Seleccionar all that apply.
- [ ] La Función Detectar del CSF implica asegurarse de que se utilizan los procedimientos adecuados para contener, neutralizar y analizar los incidentes de Seguridad.
- [x] La función de Proteger del MCA implica implementar políticas, Procedimientos, Entrenamiento y Herramientas para mitigar las Amenazas.
- [x] El CSF es un framework voluntario que consiste en estándares, directrices y mejores prácticas para gestionar el riesgo de la ciberseguridad. 
- [x] Investigar un incidente para determinar cómo se produjo la amenaza, qué se vio afectado y DONDE se originó el ataque forma parte de la función Responder del CSF.
> Correcta

6. Un Equipo de Seguridad se plantea cómo evitar soluciones innecesariamente complicadas a la hora de Implementar Controles de Seguridad. ¿Qué principio OWASP describe este escenario?
- [ ] Solucionar correctamente los problemas de Seguridad 
- [ ] Principio de privilegio mínimo
- [ ] Defensa en profundidad 
- [x] Seguridad sencilla
> Correcta

6. Un Equipo de Seguridad acaba de terminar de solucionar un reciente Incidente de Seguridad. Ahora realizan pruebas para asegurarse de que todas sus reparaciones han tenido éxito. ¿Qué principio OWASP describe este escenario?
- [x] Solucionar correctamente los problemas de Seguridad
- [ ] Separación de funciones
- [ ] Minimizar la superficie de ataque
- [ ] Principio de privilegio mínimo
> Correcta

7. ¿Cuáles son algunos de los principales objetivos de una auditoría interna de Seguridad? Seleccione todos los que correspondan
- [x] Permitir que los equipos de Seguridad evalúen los controles
- [x] Ayude a los equipos de Seguridad a corregir los problemas de cumplimiento normativo
- [x] Identificar cualquier laguna o punto débil en materia de Seguridad dentro de una organización
- [ ] Limitar el Tráfico en el firewall de una organización
> Correcta

7. ¿Cuáles son algunos de los principales objetivos de una auditoría interna de Seguridad? Seleccione todos los que correspondan
- [x] Evite las multas por incumplimiento de la normativa
- [x] Ayudar a los Equipos de Seguridad a Identificar el Riesgo Organizativo
- [ ] Reducir la cantidad de datos en una red
- [x] Determinar qué debe mejorarse para alcanzar la postura de Seguridad deseada
> Correcta

8. Rellene el espacio en blanco: En una Auditoría de seguridad interna, _____ se refiere a la identificación de personas, recursos, políticas, procedimientos y tecnologías que puedan tener un impacto en la Postura de seguridad de una organización
- [x] alcance
- [ ] implementar controles administrativos
- [ ] completar una evaluación de controles
- [ ] objetivos
> Correcta

8. Rellene el espacio en blanco: En una auditoría de seguridad interna, _____ implica la identificación de amenazas, riesgos y vulnerabilidades potenciales para decidir qué medidas de seguridad deben implementarse
- [ ] establecer el alcance y los objetivos
- [x] realizar una evaluación de riesgos
- [ ] evaluar el Cumplimiento normativo
- [ ] comunicación con las partes interesadas
> Correcta

9. Un analista de seguridad realiza una Auditoría de seguridad interna. Revisan los recursos existentes en su empresa y, a continuación, evalúan los riesgos potenciales para dichos recursos. ¿Qué aspecto de una Auditoría de seguridad describe este escenario?
- [ ] Evaluar el cumplimiento normativo
- [ ] Establecer el alcance y los objetivos
- [ ] Comunicación de resultados
- [x] Completar una evaluación de controles
> Correcta

10. ¿Qué información se suele comunicar a las partes interesadas tras la finalización de una auditoría interna de seguridad? Seleccione tres respuestas
- [x] Riesgos existentes que deben abordarse ahora o en el futuro
- [ ] Datos detallados sobre anteriores incidentes de ciberseguridad
- [x] Un resumen de los objetivos
- [x] Estrategias para mejorar la Postura de seguridad
> Correcta

10. ¿Qué información se suele comunicar a las partes interesadas tras la finalización de una auditoría interna de seguridad? Seleccione tres respuestas
- [x] Cumplimiento normativo que debe respetarse
- [x] Resultados y recomendaciones
- [ ] Detalles exhaustivos sobre cada parte del proceso
- [x] Estrategias para mejorar la Postura de seguridad
> Correcta