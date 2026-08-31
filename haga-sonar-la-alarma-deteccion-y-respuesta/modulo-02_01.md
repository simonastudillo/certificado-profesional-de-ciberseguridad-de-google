# Comprender el Tráfico de red

## Bienvenido al módulo 2
- ​​Previamente, se le presentó ​la detección y respuesta ante incidentes.
- Es posible que también recuerde haber aprendido sobre ​las redes en un curso anterior.
- ​Para recapitular, aprendió sobre ​cómo se comunican los dispositivos entre sí ​utilizando protocolos de red y ​los diferentes tipos de ataques a la red.
- También examinó algunas de las mejores prácticas de seguridad de redes.
- ​Aquí, ampliaremos el tema de las redes y ​nos centraremos en el análisis de redes.
- ​En primer lugar, examinará ​las comunicaciones de red ​explorando los flujos de tráfico de red.
- ​A continuación, aprenderá a ver y ​captar el tráfico de red utilizando sniffers de paquetes.
- ​A continuación, se introducirá en el análisis de paquetes, ​donde examinará los campos de paquetes y decodificará ​la comunicación entre dispositivos y redes.
- ​Como profesional de la seguridad, ​tendrá la tarea de supervisar redes e ​infraestructuras de sistemas para detectar actividades maliciosas.
- ​Y esta sección le brindará la oportunidad de ​desarrollar sus habilidades de análisis de redes y paquetes.

---

## Casey: Aplicar las Habilidades interpersonales en la ciberseguridad
- Hola, me llamo Casey y formo parte ​del equipo de ventas de Google Cloud Enterprise Security.
- ​En primer lugar, el mayor ​consejo que puedo dar es: hazlo.
- ​Quiero que estés aquí.
- ​Necesitamos a toda la gente.
- La ​ciberseguridad es un mundo sin parar y en constante cambio, ​por lo que es un lugar tan divertido en el que estar.
- ​Necesitamos más diversidad en materia de Seguridad. ​Necesitamos que todos participen.
- ​Necesitamos personas con diversidad de pensamiento, ​diversidad de antecedentes, diversidad de perspectivas.
- ​Creo que algunas de las habilidades sociales más importantes en ​ciberseguridad son, en primer lugar, ​poder ​resumir claramente lo que se intenta decir, algo sumamente importante.
- ​Una de las otras habilidades sociales que ​creo que podría ser incluso ​más importante que una comunicación clara ​es trabajar con una mentalidad abierta.
- ​El panorama de amenazas cambia continuamente.
- ​Los actores de amenazas, los malos actores, ​nunca duermen y, por lo tanto, nosotros tampoco.
- ​Una de las cosas que hace que la ciberseguridad sea tan divertida, ​en mi opinión, es porque cambia constantemente.
- ​Y si tenemos una mentalidad fija desde el principio, ​y lo que quiero decir con una mentalidad fija es ​que creo que sé la respuesta a esto, ​creo que entiendo exactamente lo que está sucediendo, ​vamos a perder el barco por completo.
- ​Tenemos que ser capaces de mantener siempre la curiosidad.
- ​Y desde el punto de vista de la ciberseguridad, ​es muy importante no dejar piedra sin remover.
- ​Una de las mejores cosas de las ​habilidades blandas es que todos ​las tenemos y ya las estamos usando todos los días.
- ​Así que todos los que estáis viendo ​esto ya tenéis una ventaja en ciberseguridad.

---

## La importancia de los flujos de tráfico en la Red
- ​En muchas organizaciones, la comunicación en red viaja a través de múltiples ​redes en diferentes países y a través de diferentes dispositivos.
- ​Los datos pueden enviarse y almacenarse involuntariamente en lugares inseguros, ​como las bandejas de entrada del correo electrónico personal o las plataformas de almacenamiento en la nube.
- ​Los usuarios confían en que sus datos se envíen y almacenen de forma segura.
- ​Y es el trabajo de los profesionales de la seguridad como usted ayudar a proteger estas ​comunicaciones en tránsito y en reposo.
- ​Posteriormente, puede que recuerde haber aprendido cómo identificar y proteger los activos críticos ​mediante controles de seguridad como la clasificación y el cifrado de datos.
- ​Próximamente, ampliaremos este tema y examinaremos cómo puede ​utilizarse el análisis del tráfico de red para supervisar la actividad de la red e identificar posibles actividades maliciosas.
- ​¿Qué es el tráfico de red? 
- ​El tráfico de red es la cantidad de datos que se mueven a través de una red.
- ​Mientras que los datos de red son los datos que se transmiten entre los dispositivos de una red.
- ​Dependiendo del tamaño de una red, ​puede haber un enorme volumen de tráfico de red en un momento dado.
- ​Por ejemplo, en una gran organización multinacional, puede ​haber miles de empleados enviando y recibiendo correos electrónicos en un momento dado.
- ​Eso es mucho tráfico de red.
- ​Con volúmenes tan grandes de tráfico produciéndose, ​¿cómo sabe lo que es un comportamiento normal, o lo que es inusual y ​requiere ser investigado como un potencial incidente de seguridad?
- ​Imagínese estar atrapado en un tráfico inesperado durante su trayecto habitual al trabajo.
- ​Y, a medida que avanza, se da cuenta de que algo inusual causó el tráfico, ​como una colisión menor de vehículos que ralentizó el flujo esperado.
- ​En la carretera, ​tenemos ciertas expectativas sobre los flujos de tráfico basadas en nuestra experiencia de desplazamiento al trabajo.
- ​Los picos de tráfico, como las horas punta de la mañana y de la tarde, son normales y esperados, ​mientras que el tráfico anormal durante las horas valle revela que ha ocurrido algo ​inesperado, como una colisión de vehículos.
- ​El tráfico de red funciona de la misma manera.
- ​Al comprender cómo deberían fluir los datos a través de la red, ​puede desarrollar una comprensión del flujo de tráfico de red esperado.
- ​Al conocer lo que es normal, puede detectar fácilmente lo que es anormal.
- ​Podemos detectar anomalías en el tráfico mediante la observación para detectar indicadores ​de compromiso, también conocidos como IoC, que son pruebas observables que ​sugieren signos de un posible incidente de seguridad.
- ​Tomemos, por ejemplo, la exfiltración de datos, ​que es la transmisión no autorizada de datos desde un sistema.
- ​Los atacantes utilizan la exfiltración de datos para robar o filtrar datos como nombres de usuario, ​contraseñas o propiedad intelectual.
- ​Al observar el tráfico de red, podemos determinar si hay algún indicador de ​compromiso, como grandes volúmenes de tráfico saliente saliendo de un host.
- ​Esto es un signo de posible exfiltración de datos que puede ser ​investigado más a fondo.
- ​Comprender y monitorizar el tráfico de red en busca de ​inconsistencias es un aspecto importante del trabajo de un profesional de la seguridad.

---

## Mantenga la concienciación con la supervisión de la red
- Eventos como el envío de un correo electrónico, la transmisión de un vídeo o la visita a una página web producen comunicaciones de red en forma de Tráfico de red y Datos de red.
- Como recordatorio, el Tráfico de red es la cantidad de datos que se mueven a través de una red.
- También puede incluir el tipo de datos que se transfieren, como HTTP. Datos de red son los datos que se transmiten entre los dispositivos de una red.
- Monitoreo de red es esencial para mantener el conocimiento de la situación de cualquier actividad en una red.
- Mediante la recopilación y el análisis del tráfico de red, las organizaciones pueden detectar actividades sospechosas en la red.
- Pero antes de poder supervisar las redes, debe saber exactamente qué supervisar.
- En esta lectura, aprenderá más sobre la importancia del monitoreo de redes, las formas de monitorear su red y las herramientas de monitoreo de redes.

- Conozca su red
   - Como ya ha aprendido, las redes conectan dispositivos y éstos se comunican e intercambian datos mediante protocolos de red.
   - Las comunicaciones de red proporcionan información sobre las conexiones, como las direcciones IP de origen y destino, la cantidad de datos transferidos, la fecha y la hora, etc.
   - Esta información puede ser valiosa para los profesionales de la Seguridad a la hora de desarrollar una línea de base del comportamiento normal o esperado.
   - Una línea de base es un punto de referencia que se utiliza para comparar.
   - Probablemente se haya encontrado o haya utilizado líneas de base en algún momento.
   - Por ejemplo, el importe de una compra para un presupuesto personal es un ejemplo de línea de base que puede utilizarse para ayudar a identificar cualquier patrón o cambio en los hábitos de gasto.
   - En seguridad, las líneas de base ayudan a establecer un estándar de comportamiento esperado o normal para sistemas, dispositivos y redes.
   - Esencialmente, al conocer la línea de base del comportamiento normal de la red, podrá identificar mejor el comportamiento anormal de la red.

- Monitoree su red
   - Una vez que haya determinado una línea de base, puede monitorear una red para identificar cualquier desviación de esa línea de base.
   - Monitorear implica examinar los componentes de la red para detectar actividades inusuales, como transferencias de datos grandes e inusuales.
   - He aquí algunos ejemplos de componentes de red que pueden ser monitorizados para detectar actividades maliciosas:
      - Análisis de flujo
         - Flujo se refiere al movimiento de las comunicaciones de red e incluye información relacionada con paquetes, protocolos y puertos.
         - Los paquetes pueden viajar a puertos, que reciben y transmiten comunicaciones.
         - Los puertos suelen estar asociados, aunque no siempre, a protocolos de redes.
         - Por ejemplo, el puerto 443 es utilizado habitualmente por HTTPS, que es un protocolo que proporciona encriptación del tráfico de sitios web.
         - Sin embargo, los actores maliciosos pueden utilizar protocolos y puertos que no están comúnmente asociados para mantener comunicaciones entre el sistema comprometido y su propia máquina.
         - Estas comunicaciones son lo que se conoce como comando y control (C2), que son las técnicas utilizadas por los actores maliciosos para mantener las comunicaciones con los sistemas comprometidos.
         - Por ejemplo, los actores maliciosos pueden utilizar el protocolo HTTPS a través del puerto 8088 en lugar de su puerto comúnmente asociado 443 para comunicarse con los sistemas comprometidos.
         - Las organizaciones deben saber qué puertos deben estar abiertos y aprobados para las conexiones, y vigilar cualquier desajuste entre los puertos y sus protocolos asociados.
      - Información sobre la carga útil de los paquetes
         - Los paquetes de red contienen componentes relacionados con la transmisión del paquete.
         - Esto incluye detalles como la dirección IP de origen y destino, y la información de la carga útil del paquete, que son los datos reales que se transmiten.
         - A menudo, estos Datos están encriptados y requieren desencriptación para que sean legibles.
         - Las organizaciones pueden monitorizar la información de la carga útil de los paquetes para descubrir actividades inusuales, como datos sensibles que se transmiten fuera de la red, lo que podría indicar un posible ataque de exfiltración de datos.
      - Patrones temporales
         - Los paquetes de red contienen información relativa al tiempo.
         - Esta Información es útil para comprender los patrones temporales.
         - Por ejemplo, una empresa que opera en Norteamérica experimenta grandes flujos de tráfico entre las 9 de la mañana y las 5 de la tarde, que es la línea de base de la actividad normal de la red.
         - Si de repente aparecen grandes volúmenes de tráfico fuera de las horas normales de actividad de la red, se considera que está fuera de la línea de base y debe investigarse.
   - Mediante el Monitoreo de red, las organizaciones pueden detectar con prontitud las intrusiones en la red y trabajar para evitar que ocurran asegurando los componentes de la red.

- Proteja su red
   - En este Programa, ha aprendido sobre los centros de operaciones de seguridad (SOC) y su función en la supervisión de los sistemas contra las amenazas y ataques a la Seguridad.
   - Las organizaciones pueden implementar un centro de operaciones de red (NOC), que es una unidad organizativa que supervisa el rendimiento de una red y responde a cualquier interrupción de la red, como un corte de red.
   - Mientras que un SOC se centra en mantener la seguridad de una organización mediante la detección y la respuesta, un NOC es responsable de mantener el rendimiento, la disponibilidad y el tiempo de actividad de la red.
   - Los analistas de seguridad monitorizan las redes para identificar cualquier signo de posibles incidentes de seguridad conocidos como Indicadores de compromiso (IoC) y protegen las redes de amenazas o ataques.
   - Para ello, deben comprender el entorno por el que viajan las comunicaciones de red para poder identificar desviaciones en el Tráfico de red.

- Herramientas de Monitoreo de red
   - El Monitoreo de red puede automatizarse o realizarse manualmente.
   - Algunas herramientas comunes de Monitoreo de red pueden incluir:
      - Sistemas de detección de intrusiones (IDS)
         - Monitorean la actividad del sistema y alertan sobre posibles intrusiones.
         - Un IDS detectará y alertará sobre las desviaciones que usted le haya configurado para detectar.
         - Lo más habitual es que las herramientas IDS monitoricen el contenido de la carga útil de los paquetes para detectar patrones asociados a amenazas como el software malicioso o los intentos de phishing.
      - Analizadores de protocolos de red
         - También conocidos como rastreadores de paquetes, son herramientas diseñadas para capturar y analizar el tráfico de datos dentro de una red.
         - Pueden utilizarse para analizar manualmente las comunicaciones de red en detalle.
         - Algunos ejemplos son herramientas como tcpdump y Wireshark, que pueden utilizar los profesionales de la Seguridad para registrar las comunicaciones de red mediante capturas de paquetes.
         - Las capturas de paquetes pueden investigarse después para identificar actividades potencialmente maliciosas.

- Recursos
   - [Tráfico de red - MITRE ATT&CK®](https://attack.mitre.org/datasources/DS0029/)
   - [técnicas de exfiltración de datos - MITRE ATT&CK®](https://attack.mitre.org/tactics/TA0010/)

---

## Ataques de robo de datos
- ​La supervisión del tráfico de la red ​ayuda a los profesionales de Seguridad a detectar ​, prevenir y responder a los ataques.
- ​En mi experiencia como profesional de Seguridad, la ​supervisión de las desviaciones de los ​patrones de tráfico de red típicos ha dado grandes resultados.
- ​Incluso si la información está cifrada, la ​supervisión del tráfico de la red sigue siendo ​importante por motivos de Seguridad.
- ​Analicemos cómo ​podría funcionar el proceso de detección y respuesta en un ataque de robo de datos.
- ​En primer lugar, describiremos la perspectiva del atacante.
- ​Antes de que los atacantes puedan realizar un robo de datos​, deberán obtener acceso inicial ​a una red y un sistema de computadora.
- ​Esto se puede hacer mediante un ​ataque de ingeniería social, como la suplantación de identidad, ​que engaña a las personas para que revelen datos confidenciales.
- ​Los atacantes pueden enviar correos electrónicos de suplantación de identidad con archivos adjuntos o ​enlaces que engañan ​al objetivo para que introduzca sus credenciales.
- ​Ahora, un atacante ha ​conseguido acceder a su dispositivo.
- ​Tras conseguir su posición inicial en ​el sistema, el atacante no se detendrá ahí.
- ​El objetivo de los atacantes es mantener el acceso ​al entorno y evitar que los ​detecten durante el mayor tiempo posible.
- ​Para ello, realizarán ​una táctica conocida como movimiento lateral o giro.
- ​Es entonces cuando dedicarán tiempo a ​explorar la red con el objetivo de ​expandir y mantener su acceso ​a otros sistemas de la red.
- ​A medida que un atacante ​se desplaza por la red, explorará el entorno ​para identificar activos valiosos, ​como datos confidenciales como el código propietario, información de ​identificación personal, como ​nombres y direcciones, o registros financieros.
- ​Para ello, buscarán ​ubicaciones como recursos compartidos de archivos de red, ​sitios de intranet, repositorios de código y más.
- ​Una vez que el atacante identifique los activos valiosos, ​tendrá que recopilar, ​empaquetar y preparar los datos para su exfiltración fuera de ​la red de la organización y ponerlos en manos del atacante.
- ​Una forma de hacerlo es reduciendo el tamaño de los datos.
- ​Esto ayuda a los atacantes a ocultar ​los datos robados y a eludir los controles de Seguridad.
- ​Por último, el atacante extraerá ​los datos al destino que elija.
- ​Hay muchas maneras de hacerlo.
- Por ejemplo, los ​atacantes pueden ​enviarse por correo electrónico los datos robados utilizando la cuenta de correo electrónico comprometida.
- ​Ahora que ha aprovechado la perspectiva del atacante, ​analicemos cómo las organizaciones ​pueden defenderse de este tipo de ataque.
- ​En primer lugar, los equipos de Seguridad deben impedir el acceso de los atacantes.
- ​Hay muchos métodos que puede utilizar para ​proteger su red de los intentos de suplantación de identidad.
- ​Por ejemplo, exigir ​a los usuarios que utilicen la autenticación multifactor.
- ​Los atacantes que acceden a una red ​pueden pasar desapercibidos durante un tiempo.
- ​Es importante que los equipos de Seguridad ​supervisen la actividad de la red para ​identificar cualquier actividad sospechosa ​que pueda indicar un riesgo.
- ​Por ejemplo, se ​deben investigar los inicios de sesión de varios usuarios que provienen de direcciones IP fuera de la red.
- ​Anteriormente, examinó cómo identificar, clasificar ​y proteger los activos mediante ​inventarios de activos y controles de Seguridad.
- ​Como parte de la política de Seguridad de una organización, ​todos los activos deben catalogarse en un inventario de activos.
- ​También se deben aplicar los controles de seguridad adecuados ​para proteger estos activos del acceso no autorizado.
- ​Por último, si un ataque de robo de datos tiene éxito, ​los equipos de Seguridad deben detectar y detener la exfiltración.
- ​Para detectar el ataque, se ​pueden ​identificar los indicadores de una recopilación de datos inusual mediante el monitoreo de la red.
- ​Estos incluyen: transferencias de archivos internos de ​gran tamaño, cargas externas de gran tamaño ​y escrituras de archivos inesperadas.
- ​Las herramientas SIEM pueden detectar una alerta sobre estas actividades.
- ​Una vez que se envía una alerta, ​los equipos de Seguridad investigan y ​evitan que el ataque continúe.
- ​Hay muchas maneras de detener un ataque como este.
- ​Por ejemplo, una vez identificada la actividad inusual, ​puede bloquear las direcciones IP ​asociadas al atacante mediante reglas de firewall.
- Los ​ataques de exfiltración de datos son solo uno de ​los muchos ataques que se pueden ​detectar mediante la supervisión de la red.