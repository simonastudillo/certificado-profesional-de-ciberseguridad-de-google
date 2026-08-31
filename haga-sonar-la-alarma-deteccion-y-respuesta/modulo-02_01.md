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