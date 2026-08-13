# Revisión: Dominios de seguridad

## Resumen
- Comenzamos explorando el enfoque de los ocho dominios de Seguridad de la CISSP
- discutimos las amenazas, riesgos y ​vulnerabilidades, y cómo pueden afectar a las organizaciones
- Esto incluyó un examen detallado del ransomware y ​una introducción a las tres capas de la web
- Por último, nos centramos en siete pasos del NIST Riesgo ​Management Framework, también llamado RMF

---

## Términos del glosario del Módulo 1
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 1

1. Rellene el espacio en blanco: Seguridad _____ se refiere a la capacidad de una organización para gestionar su defensa de activos y datos críticos, así como su capacidad para reaccionar ante los cambios
- [ ] endurecimiento 
- [ ] gobierno
- [x] postura
- [ ] arquitectura
> Correcto

2. ¿Cuáles de los siguientes ejemplos son áreas clave del dominio de Seguridad y Gestión de riesgos? Seleccione tres respuestas
- [ ] Realizar pruebas de control
- [x] Definir los objetivos de Seguridad
- [x] Seguidor de las regulaciones legales
- [x] Mantener la continuidad del negocio
> Correcto

2. ¿Cuáles de los siguientes ejemplos son áreas clave del dominio de Seguridad y Gestión de riesgos? Seleccione tres respuestas
- [ ] Almacene los datos correctamente
- [x] Mitigar riesgos
- [x] Seguidor de las regulaciones legales
- [x] Mantener la continuidad del negocio
> Correcto

3. ¿Cómo permite la continuidad del negocio que una organización mantenga la productividad diaria?
- [ ] Esbozando políticas de fracaso en el Negocio a negocio (Business-to-Business)
- [ ] Garantizando el Retorno de la inversión
- [ ] Explotando vulnerabilidades
- [x] Estableciendo planes de recuperación ante desastres de riesgo
> Correcto

3. ¿Qué término describe la capacidad de una organización para mantener su productividad diaria mediante el establecimiento de planes de recuperación ante desastres?
- [ ] Mitigación
- [ ] Defensa diaria
- [ ] Recuperación
- [x] Continuidad del negocio
> Correcto

4. ¿Qué concepto de Seguridad implica que todos los individuos de una organización asuman un papel activo en la reducción del Riesgo y el mantenimiento de la Seguridad?
- [ ] Programación segura
- [x] Responsabilidad compartida
- [ ] Retención de empleados
- [ ] Servicios a distancia
> Correcto

4. ¿La Responsabilidad compartida es un concepto central de qué dominio?
- [ ] Valoración y control de activos
- [ ] Protección de redes y datos
- [x] Arquitectura de seguridad e ingeniería 
- [ ] Evaluación de riesgos y Gestión de riesgos
> Correcto

5. Un analista de seguridad se asegura de que los empleados sólo puedan revisar los datos que necesitan para realizar su trabajo. ¿A qué dominio de Seguridad se refiere este escenario?
- [x] gestión de identidad y acceso
- [ ] Comunicación y Seguridad de redes
- [ ] Evaluación y pruebas de seguridad
- [ ] Seguridad en el desarrollo de software
> Correcto

5. Un analista de Seguridad verifica a los usuarios y monitorea los intentos de inicio de sesión de los empleados. El objetivo es mantener seguros los recursos de la empresa. ¿Qué dominio de Seguridad describe este escenario?
- [ ] Operaciones de Seguridad
- [ ] Comunicación y Seguridad de redes
- [x] Gestión de identidad y acceso
- [ ] Evaluación y pruebas de seguridad
> Correcto

5. Un analista de Seguridad investiga formas de mejorar la accesibilidad y la autorización en su empresa. Su objetivo principal es mantener la seguridad de los Datos. ¿Qué dominio de Seguridad describe este escenario?
- [ ] Seguridad de los recursos
- [ ] Comunicación y Seguridad de redes
- [x] Gestión de identidad y acceso 
- [ ] Evaluación y pruebas de seguridad
> Correcto

6. Se pide a un analista de seguridad que lleve a cabo una Auditoría de seguridad para identificar vulnerabilidades. ¿Con qué dominio de Seguridad está relacionada esta tarea?
- [ ] Comunicación y Seguridad de redes
- [ ] Seguridad en el desarrollo de software
- [ ] Arquitectura de seguridad e ingeniería
- [x] Evaluación y pruebas de seguridad
> Correcto

6. ¿Cuáles de las siguientes son etapas de la aplicación de Controles de seguridad? Seleccione tres respuestas
- [ ] Seguimiento de las acciones de los usuarios (Incorrecto)
- [x] Evaluar la eficacia de las salvaguardias actuales
- [x] Revisión periódica de la información sobre seguridad
- [x] Autenticación de múltiples factores
> Correcto

7. Rellene el espacio en blanco: El dominio de la Seguridad en el desarrollo de software implica el uso del desarrollo de software___, que es un proceso eficaz utilizado por los equipos para crear rápidamente productos y servicios de software
- [ ] funcionalidad
- [x] ciclo de vida
- [ ] puesta en escena
- [ ] operaciones
> Correcto

7. Cuando se trabaja en el dominio de la Seguridad en el desarrollo de software, ¿cuáles de las siguientes son tareas que los miembros del Equipo de Seguridad pueden llevar a cabo durante las distintas fases del ciclo de vida del desarrollo de software? Seleccione tres respuestas
- [x] Iniciación de una revisión de diseño segura
- [ ] Participar en la investigación de incidentes
- [x] Realización de revisiones seguras del Código
- [x] Realización de pruebas de penetración
> Correcto

7. Rellene el espacio en blanco: Cuando se trabaja en el dominio de la seguridad del desarrollo de software, los miembros del equipo de seguridad pueden utilizar cada fase del desarrollo de software _____ para llevar a cabo revisiones de seguridad y garantizar que la seguridad puede integrarse plenamente en los productos de software
- [ ] manipulación
- [ ] secuenciación
- [ ] operaciones
- [x] ciclo de vida
> Correcto

8. ¿Cuál de las siguientes afirmaciones describe con exactitud el Riesgo? Seleccione todas las que correspondan
- [x] Otra forma de pensar en el Riesgo es la probabilidad de que se produzca una amenaza.
- [x] Si se ve comprometido, un recurso de riesgo medio puede causar algún daño a las operaciones en curso de una organización.
- [x] Un recurso de alto riesgo es cualquier información protegida por Regulaciones o leyes.
- [ ] Si se comprometiera, un recurso de bajo riesgo tendría un grave impacto negativo en la reputación actual de una organización.
> Correcto

8. ¿Cuál de las siguientes afirmaciones describe con exactitud el Riesgo? Seleccione todas las que correspondan
- [ ] Si se ve comprometido, un recurso de riesgo medio puede causar algún daño a la reputación de una organización. 
- [x] En caso de verse comprometido, un recurso de bajo riesgo no requeriría una vigilancia o acción continuas. (incorrecta)
- [x] Determinar si un riesgo es bajo, medio o alto depende de la posible amenaza y del recurso implicado.
- [x] Los recursos con SPII, PII o propiedad intelectual son ejemplos de recursos de alto riesgo
> Incorrecto

9. Una empresa sufre un ataque. Como consecuencia, un importante medio de comunicación informa sobre el ataque, lo que crea mala prensa para la organización. ¿Qué tipo de consecuencia describe este escenario?
- [ ] Falta de Compromiso
- [x] Daños a la Reputación
- [ ] Pérdida de identidad
- [ ] Aumento de los beneficios
> Correcto

10. Rellene el espacio en blanco: En el marco de gestión de riesgos (RMF), el paso _____ podría implicar la implementación de un plan para cambiar los requisitos de las contraseñas con el fin de reducir las solicitudes para restablecer las contraseñas de los empleados
- [x] implementar
- [ ] autorizar
- [ ] categorizar
- [ ] preparar
> Correcto

10. Rellene el espacio en blanco: En el marco de gestión de riesgos (RMF), el paso_____ implica saber cómo funcionan los sistemas y evaluar si esos sistemas apoyan o no los objetivos de seguridad de la organización
- [ ] categorizar
- [ ] implementar
- [x] monitorear
- [ ] autorizar
> Correcto