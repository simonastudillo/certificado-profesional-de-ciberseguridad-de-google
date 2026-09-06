# Visión general de las herramientas de gestión de eventos de información de seguridad (SIEM)

## Reexaminar las herramientas SIEM
- Como analista de seguridad, necesitará poder acceder rápidamente a los datos relevantes ​necesarios para desempeñar sus funciones.
- ​Ya sea para clasificar alertas, monitorear sistemas o ​analizar datos de registro durante las investigaciones de incidentes, ​un SIEM es la herramienta adecuada para este trabajo.
- ​Como revisión rápida, un SIEM es una aplicación que recopila y ​analiza los datos de registro para monitorear las actividades críticas de una organización.
- ​Para ello, recopila, analiza e ​informa sobre los datos de seguridad de múltiples fuentes.
- ​Anteriormente, aprendió sobre el proceso SIEM para la recopilación de datos.
- ​Repasemos este proceso. En primer lugar, las herramientas SIEM RECOPILAN Y PROCESAN enormes ​cantidades de datos generados por dispositivos y sistemas de todo el entorno.
- ​No todos los datos son iguales.
- Como ya sabe, ​los dispositivos generan datos en diferentes formatos.
- ​Esto puede ser un desafío porque no existe un formato unificado para representar los datos.
- ​Las herramientas SIEM facilitan a los analistas de seguridad la lectura y el ​análisis de los datos al NORMALIZARLOS.
- ​Los datos sin procesar se procesan, de modo que se les da un formato uniforme y ​solo se incluye la información relevante del evento.
- ​Por último, las herramientas de SIEM INDEXAN los datos, por lo que se puede acceder a ellos mediante una búsqueda.
- Se ​puede acceder a todos los eventos de las diferentes fuentes con la punta de ​los dedos.
- ​¿No es útil? ​Las herramientas SIEM facilitan el acceso rápido y el ​análisis de los flujos de datos que se producen en las redes de un entorno.
- ​Como analista de seguridad, es posible que encuentre diferentes herramientas de SIEM.
- ​Es importante que puedas ajustarte y ​adaptarte a cualquier herramienta que acabe utilizando tu organización.
- ​Con eso en mente, exploremos algunas herramientas de SIEM que se utilizan actualmente en la industria de la seguridad.
- ​Splunk es una plataforma de análisis de datos.
- ​Splunk Enterprise Security proporciona soluciones SIEM que le permiten buscar ​, analizar y visualizar los datos de seguridad.
- ​En primer lugar, recopila datos de diferentes fuentes.
- Esos datos se procesan y ​almacenan en un índice.
- Luego, se puede acceder a él de varias maneras diferentes, ​como mediante la búsqueda.
- ​Chronicle es el SIEM de Google Cloud, que almacena datos de seguridad ​para la búsqueda, el análisis y la visualización.
- ​Primero, los datos se envían a Chronicle.
- ​Luego, estos datos se normalizan o se limpian, por lo que son más fáciles de procesar e indexar.
- ​Finalmente, los datos están disponibles para acceder a ellos a través de una barra de búsqueda.
- Chronicle Security Operations o Chronicle SecOps ha pasado a llamarse Google Security Operations (Google SecOps).

---

## Fuentes de registro e ingestión de registros
- Recordará que las herramientas de gestión de eventos e información de seguridad (SIEM) recopilan y analizan datos de registro para supervisar actividades críticas en una organización.
- También ha aprendido sobre el análisis de registros, que es el proceso de examinar los registros para identificar eventos de interés.
- Entender cómo se introducen las fuentes de registro en las herramientas SIEM es importante porque ayuda a los analistas de seguridad a entender los tipos de datos que se están recopilando, y puede ayudar a los analistas a identificar y priorizar los incidentes de seguridad.

- Visión general del proceso SIEM
   - Anteriormente se ha tratado el proceso SIEM.
   - A modo de repaso, el proceso consta de tres pasos:
      - Recopilar y agregar datos:
         - Las herramientas SIEM recopilan datos de eventos de varias fuentes de datos.
      - Normalizar los datos:
         - Los datos de eventos recopilados se normalizan.
         - La normalización convierte los datos a un formato estándar para que estén estructurados de forma coherente y sean más fáciles de leer y buscar.
         - Aunque la normalización de datos es una característica común en muchas herramientas SIEM, es importante tener en cuenta que las herramientas SIEM varían en sus capacidades de normalización de datos.
      - Analizar los datos:
         - Una vez recopilados y normalizados los datos, las herramientas SIEM los organizan e indexan para poder analizarlos y correlacionarlos con el fin de identificar patrones comunes que indiquen actividad inusual.

- Ingesta de registros
   - Una herramienta SIEM recopila datos de diversas fuentes.
   - Los datos son necesarios para que las herramientas SIEM funcionen eficazmente.
   - Las herramientas SIEM primero deben recopilar datos mediante la ingesta de registros.
   - La ingesta de registros es el proceso de recopilación e importación de datos de fuentes de registros a una herramienta SIEM.
   - Los datos proceden de cualquier fuente que genere datos de registro, como un servidor.
   - En la ingestión de registros, el SIEM crea una copia de los datos de eventos que recibe y la conserva en su propio almacenamiento.
   - Esta copia permite al SIEM analizar y procesar los datos sin modificar directamente los registros de la fuente original.
   - La recopilación de datos de eventos proporciona una plataforma centralizada para que los analistas de seguridad analicen los datos y respondan a los incidentes.
   - Estos datos de eventos incluyen intentos de autenticación, actividad de la red, etc.

- Transmisores de registros
   - Hay muchas formas de que las herramientas SIEM ingieran datos de registro.
   - Por ejemplo, puede cargar los datos manualmente o utilizar software que le ayude a recopilar los datos para la ingesta de registros.
   - La carga manual de datos puede resultar ineficaz y llevar mucho tiempo, ya que las redes pueden contener miles de sistemas y dispositivos.
   - Por lo tanto, es más fácil utilizar software que ayude a recopilar datos.
   - Una forma común en que las organizaciones recopilan datos de registro es utilizar reenviadores de registro.
   - Estos programas automatizan el proceso de recogida y envío de datos de registro.
   - Algunos sistemas operativos tienen reenviadores de registro nativos.
   - Si utiliza un sistema operativo que no tiene un reenviador de registros nativo, deberá instalar un software de reenvío de registros de terceros en un dispositivo.
   - Después de instalarlo, configuraría el software para especificar qué registros reenviar y dónde enviarlos.
   - Por ejemplo, puede configurar los registros para que se envíen a una herramienta SIEM.
   - La herramienta SIEM procesaría y normalizaría los datos.
   - Esto permite que los datos se puedan buscar, explorar, correlacionar y analizar fácilmente.
   - Muchas herramientas SIEM utilizan sus propios reenviadores de registros.
   - Las herramientas SIEM también pueden integrarse con reenviadores de registros de código abierto.
   - La elección del reenviador de registros adecuado depende de muchos factores, como los requisitos específicos de su sistema u organización, la compatibilidad con su infraestructura existente, etc.

- Recursos
   - [Guía sobre la ingestión de datos en Splunk](https://docs.splunk.com/Documentation/SplunkCloud/9.0.2303/Data/Howdoyouwanttoadddata)
   - [Guía sobre la ingestión de datos en Google Security Operations](https://cloud.google.com/chronicle/docs/data-ingestion-flow)

---

## Consulta de eventos con Splunk
- ​Ahora que hemos repasado cómo funciona un SIEM, ​aprendamos a buscar y ​consultar eventos en una base de datos SIEM.
- ​Se puede acceder a los datos que se han importado a un SIEM ​introduciendo consultas en el motor de búsqueda del SIEM.
- ​En una base de datos SIEM se pueden almacenar cantidades ingentes de datos.
- ​Algunos de estos datos pueden remontarse a años atrás.
- ​Esto puede hacer que la búsqueda de eventos de seguridad sea todo un reto.
- ​Por ejemplo, digamos que está ​buscando encontrar un evento de inicio de sesión fallido.
- ​Busca el evento utilizando las palabras clave: inicio de sesión fallido.
- ​Esta es una consulta muy amplia, que ​puede devolver miles de resultados.
- ​Consultas de búsqueda amplias como esta, ​ralentizan los tiempos de respuesta de un motor de búsqueda ​ya que está buscando en todos los datos indexados.
- ​Pero, si especifica parámetros adicionales, ​como el ID de un evento y un rango de fechas y horas, ​puede acotar la búsqueda para obtener resultados más rápidos.
- ​Es importante que las consultas de búsqueda ​sean específicas, para que pueda encontrar ​exactamente lo que busca y ​ahorrar tiempo en el proceso de búsqueda.
- ​Diferentes herramientas SIEM utilizan diferentes métodos de búsqueda.
- ​Por ejemplo, Splunk utiliza ​su propio lenguaje de consulta llamado ​Lenguaje de Procesamiento de Búsqueda, ​o SPL para abreviar.
- ​SPL tiene muchas opciones de búsqueda diferentes que puede utilizar para ​optimizar los resultados de búsqueda, de modo que ​pueda obtener los datos que está buscando.
- ​Por ahora, demostraré ​una búsqueda de registros sin procesar en Splunk Cloud para eventos que ​remitan a errores o fallos para ​una tienda en línea ficticia llamada Buttercup Games.
- ​En primer lugar, utilizaremos la barra de búsqueda para escribir nuestra consulta: ​buttercupgames error OR fail*
- ​Esta búsqueda está especificando el índice, ​que es buttercupgames.
- ​También especificamos los términos de búsqueda: error OR fail.
- ​El operador booleano OR garantiza ​que se buscarán ambas palabras clave.
- ​El asterisco al final del término ​fail* se conoce como comodín.
- ​Esto significa que buscará ​todas las terminaciones posibles que contengan el término fail.
- ​Esto nos ayuda a ampliar nuestros resultados de búsqueda ​porque los eventos pueden etiquetar los fallos de forma diferente.
- ​Por ejemplo, algunos eventos pueden utilizar el término failed.
- ​A continuación, seleccionaremos un rango de tiempo ​utilizando el selector de rango de tiempo.
- ​Recuerde, cuanto más específica sea nuestra búsqueda, mejor. ​Busquemos datos de los últimos 30 días.
- ​Debajo de la barra de búsqueda, tenemos los resultados de nuestra búsqueda.
- ​Hay una línea de tiempo, que nos ofrece ​una representación visual de ​el número de eventos a lo largo de un periodo.
- ​Esto puede ser útil para identificar ​patrones de eventos, como picos de actividad.
- ​Debajo de la línea de tiempo, está el visor de eventos, que ​nos ofrece una lista de eventos que coinciden con nuestra búsqueda.
- ​Note cómo los términos de nuestra búsqueda: ​buttercupgames y error ​están resaltados en cada evento.
- ​No parece que se haya encontrado ningún evento ​que coincida con el término fail.
- ​Cada evento tiene una marca de tiempo y datos de registro sin procesar.
- ​Para los eventos con errores, ​parece que hay un error relacionado con ​las cookies HTTP utilizadas en el sitio web de Buttercup Games.
- ​Al final de los datos de registro sin procesar, ​hay alguna información relacionada con la fuente de datos, ​incluyendo el nombre del host, ​la fuente y el tipo de fuente.
- ​Esta información nos dice de dónde proceden los Datos del Evento​, como un dispositivo o un archivo.
- ​Si hacemos clic en él, podemos elegir ​excluirlo de los resultados de la búsqueda.
- ​En la barra de búsqueda, podemos examinar ​que se han cambiado los términos de búsqueda ​y ¡host!=www1 se ha añadido, ​lo que significa no incluir los hosts www1.
- ​Note que los nuevos resultados de búsqueda no ​contienen www1 como host, ​pero contienen www2 y www3.
- ​Esta es sólo una de las muchas formas en que puede orientar ​sus búsquedas para recuperar la información que está buscando.
- ​Esta búsqueda se conoce como búsqueda de registro sin procesar, ​que tiene un rendimiento de búsqueda más lento ya que extrae ​campos de datos de registro durante el proceso de búsqueda.
- ​Como analista de seguridad, ​utilizará diferentes comandos para optimizar ​el rendimiento de la búsqueda y obtener resultados de búsqueda más rápidos.
- ​Con esto finaliza la consulta en Splunk.
- ​Ha aprendido la importancia de las consultas efectivas ​y cómo realizar una búsqueda básica en Splunk.