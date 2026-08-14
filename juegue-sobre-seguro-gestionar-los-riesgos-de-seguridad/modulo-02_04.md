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