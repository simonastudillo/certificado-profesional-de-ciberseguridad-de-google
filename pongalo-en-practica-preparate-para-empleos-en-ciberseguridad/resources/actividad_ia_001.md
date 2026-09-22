# Guía de referencia sobre correos electrónicos de phishing y malware

## 1. Objetivo

Esta guía tiene como objetivo ayudar a identificar, prevenir y reportar correos electrónicos maliciosos utilizados para obtener información confidencial, robar credenciales, instalar malware o engañar a los usuarios para realizar acciones no autorizadas.

La principal regla de seguridad es simple:

**Ante cualquier duda, no abrir enlaces ni archivos adjuntos y verificar el mensaje por un canal alternativo.**

---

## 2. ¿Qué es el phishing?

El **phishing** es una técnica de ingeniería social mediante la cual un atacante intenta engañar a una persona haciéndose pasar por una entidad, empresa, proveedor, compañero de trabajo o persona conocida.

El objetivo puede ser:

- Obtener nombres de usuario y contraseñas.
- Robar información personal o empresarial.
- Conseguir datos bancarios o financieros.
- Inducir al usuario a realizar un pago o transferencia.
- Obtener códigos de autenticación.
- Conseguir acceso a sistemas internos.
- Instalar software malicioso.

El phishing no siempre contiene malware. Muchas veces el ataque simplemente intenta conseguir que la víctima ingrese sus credenciales en una página falsa.

---

## 3. ¿Qué es el malware?

El **malware** es software diseñado para realizar acciones maliciosas en un computador, teléfono, servidor u otro dispositivo.

Puede utilizarse para:

- Robar información.
- Capturar contraseñas.
- Registrar pulsaciones del teclado.
- Espiar la actividad del usuario.
- Tomar control remoto del equipo.
- Cifrar archivos mediante ransomware.
- Instalar otros programas maliciosos.
- Utilizar el dispositivo como punto de acceso hacia otros sistemas de la organización.

Un correo electrónico puede distribuir malware mediante archivos adjuntos, enlaces de descarga o páginas web comprometidas.

---

## 4. Señales de alerta en un correo electrónico

Un correo debe considerarse sospechoso cuando presenta una o varias de las siguientes características.

### Remitente desconocido o dirección extraña

Verificar siempre la dirección completa del remitente.

Por ejemplo:

**Legítimo:**

`soporte@empresa.cl`

**Sospechoso:**

`soporte@empresa-seguridad.com`

`soporte@empersa.cl`

`empresa.soporte@gmail.com`

Los atacantes suelen utilizar dominios visualmente parecidos a los originales.

---

### Sensación de urgencia

Los mensajes fraudulentos suelen intentar impedir que el usuario piense antes de actuar.

Ejemplos:

- "Su cuenta será bloqueada en 30 minutos."
- "Debe verificar inmediatamente su contraseña."
- "Pago pendiente. Último aviso."
- "Actividad sospechosa detectada."
- "Revise urgentemente este documento."

La urgencia por sí sola no significa que un mensaje sea malicioso, pero debe aumentar el nivel de precaución.

---

### Solicitudes inusuales

Desconfiar especialmente de mensajes que soliciten:

- Contraseñas.
- Códigos de autenticación.
- Información bancaria.
- Datos personales.
- Transferencias de dinero.
- Cambio de una cuenta bancaria.
- Instalación de programas.
- Apertura de documentos inesperados.

Una contraseña o código de autenticación no debería enviarse por correo electrónico.

---

## 5. Enlaces sospechosos

Antes de hacer clic en un enlace, debe verificarse su destino.

En computadores normalmente es posible colocar el cursor sobre el enlace sin hacer clic para visualizar la dirección real.

Por ejemplo, el texto puede indicar:

`https://www.microsoft.com`

pero dirigir realmente a:

`https://microsoft-login.ejemplo-malicioso.com`

También debe prestarse atención a direcciones similares:

`micros0ft.com`

`paypa1.com`

`banc0.cl`

Los atacantes pueden reemplazar letras por números o utilizar caracteres visualmente similares.

Si existe alguna duda, es preferible abrir manualmente el sitio oficial desde el navegador en lugar de utilizar el enlace recibido por correo.

---

## 6. Archivos adjuntos

No se deben abrir archivos inesperados, aunque aparentemente provengan de una persona conocida.

Los formatos que requieren especial precaución incluyen:

- `.exe`
- `.msi`
- `.bat`
- `.cmd`
- `.js`
- `.vbs`
- `.scr`
- `.zip`
- `.rar`
- `.iso`

También pueden utilizarse documentos aparentemente normales:

- Word.
- Excel.
- PDF.
- PowerPoint.

Un documento puede intentar convencer al usuario de habilitar macros, contenido activo o alguna función adicional.

Si un archivo solicita acciones como:

**"Habilitar contenido"**,  
**"Habilitar macros"**,  
**"Enable Editing"**,  
**"Enable Content"**,

y el documento no era esperado, debe cerrarse inmediatamente.

---

## 7. Cuidado con archivos comprimidos

Los archivos `.zip`, `.rar` y otros formatos comprimidos se utilizan frecuentemente para evadir algunos sistemas de detección.

Debe desconfiarse especialmente cuando:

- El archivo está protegido con contraseña.
- La contraseña viene escrita en el mismo correo.
- Contiene archivos ejecutables.
- El remitente no había informado previamente del envío.

Un archivo protegido con contraseña puede impedir que algunos sistemas automáticos analicen su contenido.

---

## 8. Correos que aparentan provenir de personas conocidas

Que un mensaje incluya el nombre de un compañero, gerente o proveedor no significa necesariamente que sea legítimo.

Los atacantes pueden:

- Falsificar nombres.
- Crear cuentas similares.
- Comprometer una cuenta real.
- Obtener información de redes sociales.
- Analizar comunicaciones anteriores.

Debe prestarse especial atención a solicitudes inesperadas relacionadas con:

- Transferencias.
- Facturas.
- Cambio de datos bancarios.
- Compra de tarjetas de regalo.
- Envío de documentos confidenciales.
- Cambio de contraseñas.
- Entrega de códigos de verificación.

Ante estas situaciones, confirmar la solicitud mediante teléfono, mensajería corporativa u otro canal conocido.

---

## 9. Phishing dirigido

Algunos ataques son personalizados y utilizan información real sobre la persona o la organización.

Esto se conoce como **spear phishing**.

El atacante puede conocer:

- Nombre del trabajador.
- Cargo.
- Empresa.
- Jefatura.
- Proveedores.
- Clientes.
- Proyectos.
- Compañeros de trabajo.

Un correo que contiene información correcta no necesariamente es legítimo.

---

## 10. Fraude del CEO o Business Email Compromise

Una modalidad frecuente consiste en hacerse pasar por una persona con autoridad dentro de una organización.

Por ejemplo:

> "Estoy en una reunión y necesito que realices esta transferencia inmediatamente."

También pueden falsificarse solicitudes de proveedores indicando un cambio de cuenta bancaria.

Todo cambio financiero relevante debe verificarse mediante procedimientos internos y, preferiblemente, utilizando un segundo canal de comunicación.

---

## 11. Códigos QR

Los códigos QR también pueden utilizarse para phishing.

Un correo puede indicar:

"Escanee este código para volver a validar su cuenta."

El código puede dirigir hacia una página falsa diseñada para obtener credenciales.

Un código QR debe tratarse de la misma manera que cualquier enlace.

---

## 12. Páginas falsas de inicio de sesión

Una técnica habitual consiste en copiar visualmente páginas conocidas como:

- Microsoft 365.
- Google.
- Bancos.
- Servicios de almacenamiento.
- Plataformas corporativas.

Antes de ingresar una contraseña debe verificarse el dominio mostrado en la barra de direcciones.

La presencia de HTTPS o del icono de candado **no garantiza que el sitio sea legítimo**. HTTPS únicamente indica que la conexión entre el navegador y ese sitio está cifrada.

---

## 13. Códigos de autenticación y MFA

La autenticación multifactor reduce considerablemente el riesgo asociado al robo de contraseñas, pero también puede ser atacada.

Nunca deben entregarse a terceros:

- Códigos recibidos por SMS.
- Códigos generados por aplicaciones de autenticación.
- Códigos enviados por correo.
- Códigos de recuperación.

Tampoco debe aprobarse una solicitud de inicio de sesión que el usuario no haya iniciado.

Si aparecen repetidas solicitudes inesperadas de autenticación, deben rechazarse y reportarse.

---

## 14. Qué hacer antes de interactuar con un correo sospechoso

Antes de abrir un enlace, archivo o responder un mensaje:

1. Revisar el remitente completo.
2. Revisar el dominio.
3. Analizar si el mensaje era esperado.
4. Evaluar si existe una urgencia artificial.
5. Verificar hacia dónde dirige cualquier enlace.
6. Revisar cuidadosamente los archivos adjuntos.
7. Confirmar solicitudes sensibles mediante otro canal.
8. Reportar el correo si existen dudas.

---

## 15. Qué NO hacer

Ante un correo sospechoso:

- No hacer clic en enlaces.
- No abrir archivos adjuntos.
- No responder.
- No entregar información.
- No ingresar contraseñas.
- No ingresar códigos de autenticación.
- No reenviar el mensaje a otros trabajadores salvo que exista un procedimiento establecido para reportarlo.
- No instalar programas indicados en el correo.
- No aprobar solicitudes inesperadas de autenticación.

---

## 16. Qué hacer si se abrió un enlace

Haber abierto un enlace no significa necesariamente que el dispositivo haya sido comprometido.

Sin embargo, si el sitio solicita credenciales o información personal:

1. No ingresar información.
2. Cerrar la página.
3. Reportar el incidente al responsable de seguridad o soporte técnico.
4. Informar claramente qué enlace fue abierto.

El equipo técnico podrá determinar si se requieren acciones adicionales.

---

## 17. Qué hacer si se ingresó una contraseña

Si una contraseña fue ingresada en una página sospechosa:

1. Informar inmediatamente al área responsable.
2. Cambiar la contraseña desde el sitio oficial.
3. Cerrar las sesiones abiertas, cuando sea posible.
4. Revisar accesos recientes.
5. Verificar los métodos de recuperación de cuenta.
6. Revisar la configuración de autenticación multifactor.

Si esa misma contraseña se utiliza en otros servicios, también debe cambiarse en ellos.

Por esta razón, no deben reutilizarse contraseñas.

---

## 18. Qué hacer si se abrió un archivo sospechoso

Si se ejecutó o abrió un archivo posiblemente malicioso:

1. Detener cualquier interacción con el archivo.
2. Informar inmediatamente al área técnica.
3. Indicar qué archivo fue abierto.
4. Informar desde qué correo fue recibido.
5. Seguir las instrucciones del equipo de seguridad.

Cuando la organización cuente con un procedimiento de respuesta ante incidentes, debe seguirse dicho procedimiento.

---

## 19. Qué hacer si se ejecutó un programa sospechoso

Debe considerarse un incidente de seguridad.

Dependiendo de las políticas de la organización, puede ser necesario:

- Desconectar temporalmente el equipo de la red.
- Bloquear cuentas potencialmente comprometidas.
- Cambiar credenciales.
- Revisar registros de acceso.
- Ejecutar herramientas de detección.
- Analizar otros dispositivos relacionados.

Estas acciones deben ser coordinadas por el personal técnico o de ciberseguridad.

---

## 20. Ejemplo de correo sospechoso

**Remitente:** Soporte Microsoft  
**Dirección:** `microsoft-security@outlook-verification.example`

**Asunto:** URGENTE: Su cuenta será eliminada

**Mensaje:**

"Detectamos actividad sospechosa. Su cuenta será desactivada dentro de las próximas 2 horas. Confirme inmediatamente sus credenciales utilizando el siguiente enlace."

Señales de alerta:

- Dominio extraño.
- Urgencia.
- Amenaza de bloqueo.
- Solicitud de credenciales.
- Enlace externo.

---

## 21. Ejemplo de solicitud financiera sospechosa

**Remitente:** Gerencia General

"Necesito que realices una transferencia de $2.500.000 a este proveedor. Estoy en reunión y no puedo hablar. Necesito que quede realizada durante los próximos 20 minutos."

Señales de alerta:

- Solicitud inesperada.
- Presión de tiempo.
- Solicitud financiera.
- Intento de impedir una verificación directa.

La solicitud debe confirmarse mediante los procedimientos habituales de autorización.

---

## 22. Señales rápidas para recordar

Un correo merece una revisión adicional cuando existe:

**Urgencia + solicitud inusual + enlace o archivo.**

También debe desconfiarse de mensajes que provoquen deliberadamente:

- Miedo.
- Curiosidad.
- Presión.
- Autoridad.
- Oportunidad económica.
- Amenazas de pérdida de acceso.

Estas emociones pueden ser utilizadas para conseguir que el usuario actúe antes de analizar el mensaje.

---

## 23. Buenas prácticas preventivas

Para reducir los riesgos:

- Utilizar contraseñas únicas.
- Utilizar un administrador de contraseñas.
- Activar autenticación multifactor.
- Mantener los sistemas actualizados.
- Mantener navegador y aplicaciones actualizados.
- Utilizar antivirus o sistemas de protección administrados.
- Realizar copias de seguridad.
- Aplicar el principio de mínimo privilegio.
- Mantener procedimientos de reporte de incidentes.
- Capacitar periódicamente a los usuarios.

---

## 24. Regla final

Un correo electrónico debe considerarse únicamente un medio para recibir información, no una garantía de identidad.

El nombre del remitente, el logotipo de una empresa, una firma profesional o información correcta sobre la organización pueden ser falsificados.

Cuando un mensaje solicite una acción sensible, siempre debe verificarse:

**Quién lo solicita, qué solicita, por qué lo solicita y mediante qué canal puede confirmarse.**

Ante la duda:

**No hacer clic. No descargar. No responder. Verificar y reportar.**