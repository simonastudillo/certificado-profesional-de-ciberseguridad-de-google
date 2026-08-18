# Revisión: Operaciones de red

## Resumen
- ​En primer lugar, analizamos los protocolos de red comunes como TCP, ARP, HTTPS y DNS.
- ​Y luego explicamos cómo se ​pueden usar las redes privadas virtuales, o VPN, para mantener la privacidad en una red pública.
- ​Por último, analizamos cómo los firewalls, las zonas de Seguridad y ​los servidores proxy ayudan a proteger la infraestructura de red.
- ​En general, las operaciones de red son un tema amplio que involucra varias herramientas ​, protocolos y técnicas que ayudan a las redes a funcionar sin problemas y de forma segura.

---

## Glosario de términos del módulo 2
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 2

1. ¿Qué protocolo de red ayuda a que los datos lleguen al lugar correcto determinando la dirección MAC del siguiente router o dispositivo en su ruta?
- [x] protocolo de resolución de direcciones (ARP)
- [ ] Protocolo seguro de transferencia de hipertexto (HTTPS)
- [ ] Protocolo de control de transmisión (TCP)
- [ ] Capa de sockets seguros/Seguridad de la capa de transporte (SSL/TLS)
> Correcto

1. ¿Qué protocolo de comunicación de Internet permite a dos dispositivos establecer una conexión y transmitir datos?
- [x] Protocolo de control de transmisión (TCP)
- [ ] Protocolo seguro de transferencia de hipertexto (HTTPS)
- [ ] Protocolo de resolución de direcciones (ARP)
- [ ] Capa de sockets seguros/Seguridad de la capa de transporte (SSL/TLS)
> Correcto

2. Rellene el espacio en blanco: La _______ mantiene los Estándares Wi-Fi.
- [x] IEEE 802.11
- [ ] Protocolo de control de transmisión (TCP)
- [ ] Sistema de nombres de dominio (DNS)
- [ ] Acceso WiFi protegido (WPA)
> Correcto

2. ¿Cuál de las siguientes afirmaciones describe con exactitud los protocolos inalámbricos? Seleccione tres respuestas
- [x] El conjunto de Estándares IEEE 802.11 también se conoce como Wi-Fi.
- [x] El Instituto de Ingenieros Eléctricos y Electrónicos mantiene los Estándares Wi-Fi.
- [ ] Los protocolos Wi-Fi proporcionan niveles de Seguridad significativamente inferiores a los de las conexiones por cable.
- [x] WPA es un protocolo de seguridad inalámbrico relativo a la conexión a Internet.
> Correcto

3. ¿Qué tipo de firewall analiza el tráfico de red en busca de características y comportamientos sospechosos e impide que entren en la red?
- [ ] Basado en la Nube
- [x] Con estado
- [ ] Firewall de nueva generación (NGFW)
- [ ] Sin estado
> Correcto

3. Un administrador de firewall instala una función de firewall para bloquear o permitir determinados números de puerto para limitar la comunicación no deseada. ¿Qué función describe este escenario?
- [ ] Enmascaramiento de la ubicación
- [ ] Organización de paquetes de datos
- [ ] Uso de cortafuegos basados en la nube
- [x] Filtrado de puertos
> Correcto

4. ¿Qué firewall ofrece más características de Seguridad?
- [ ] Firewall documentado
- [ ] Sin estado firewall
- [x] Firewall de nueva generación (NGFW)
- [ ] Con estado firewall
> Correcto

4. Rellene el espacio en blanco: Un firewall ____ puede conectarse a servicios de inteligencia sobre amenazas basados en la nube y actualizarse rápidamente contra las ciberamenazas emergentes
- [ ] con estado
- [x] firewall de nueva generación (NGFW)
- [ ] documentado
- [ ] sin estado
> Correcto

5. Un profesional de la seguridad establece una medida de seguridad para permitir a los empleados trabajar desde casa de forma segura a la vez que tienen acceso a los recursos de la red interna. ¿Qué describe este escenario?
- [ ] Protocolo de resolución de direcciones (ARP)
- [ ] Firewall
- [ ] Proveedor de servicios en la nube (CSP)
- [x] Red privada virtual (VPN)
> Correcto

5. ¿Qué servicio de seguridad de red enmascara la ubicación virtual de un dispositivo para mantener la privacidad de los datos mientras se utiliza una red pública?
- [ ] Proveedor de servicios en la nube (CSP)
- [x] Red privada virtual (VPN)
- [ ] Sistema de nombres de dominio (DNS)
- [ ] Segmentador de red
> Correcto

6. Rellene el espacio en blanco: Los servicios VPN realizan _____ para proteger los datos sensibles envolviéndolos en otros paquetes de datos
- [ ] control de transmisión
- [ ] segmentación de red
- [x] encapsulación
- [ ] sniffing de paquetes
> Correcto

6. ¿Qué utiliza un servicio VPN para transferir datos encriptados entre un dispositivo y el servidor VPN?
- [ ] control de transmisión
- [x] encapsulación
- [ ] segmentación de red
- [ ] sniffing de paquetes
> Correcto

7. ¿Qué redes forman parte de la Zona no controlada?
- [ ] Subredes
- [x] Internet
- [ ] Servidores web
- [ ] Redes internas
> Correcto

7. ¿Qué zona de la red contiene Internet y otros servicios que están fuera del control de una organización?
- [ ] Controlada
- [x] Sin control
- [ ] Restringido
- [ ] Desmilitarizado (Incorrecta)
> Correcto

8. ¿Cuál es la función de la Zona desmilitarizada (DMZ)?
- [ ] Cifrar datos mientras viajan por Internet
- [ ] Proteger la Información altamente confidencial accesible sólo a los empleados con ciertos privilegios
- [x] Aislar los servidores expuestos a Internet del resto de una red
- [ ] Organizar Datos reenviándolos a otros servidores
> Correcto

8. ¿Qué zona de red actúa como perímetro de la red interna aislando los servidores que están expuestos a Internet?
- [ ] Zona restringida
- [ ] Zona no controlada
- [x] Zona desmilitarizada
- [ ] Red privada virtual
> Correcto

9. ¿Cuál de las siguientes herramientas puede atender las peticiones de los clientes reenviándolas a otros servidores?
- [x] Servidor proxy
- [ ] Firewall
- [ ] Red privada virtual (VPN)
- [ ] Router
> Correcto

9. Un analista de seguridad implementa un servidor proxy para proteger las redes internas. ¿Cuáles son algunas de las funciones principales del servidor proxy? Seleccione tres respuestas
- [x] Utilice direcciones IP públicas diferentes del resto en la red privada
- [x] Determinar si se permiten las solicitudes de conexión a un sitio web
- [x] Almacena temporalmente Datos solicitados con frecuencia por servidores externos
- [ ] Divida la red en segmentos para mantener la privacidad dentro de los grupos corporativos
> Correcto

10. Rellene el espacio en blanco: Un ____ acepta Tráfico de partes externas, lo aprueba y luego lo reenvía a servidores internos
- [ ] servidor proxy de reenvío
- [x] servidor proxy inverso
- [ ] firewall de nueva generación (NGFW)
- [ ] red privada virtual (VPN)
> Correcto

10. ¿Cuál de las siguientes afirmaciones describe con exactitud los servidores proxy de reenvío y proxy inverso? Seleccione tres respuestas
- [ ] Los servidores proxy inverso funcionan ocultando la dirección IP de un usuario y aprobando todas las solicitudes salientes. 
- [x] Los servidores proxy de reenvío regulan y restringen el acceso de una persona a Internet. 
- [x] Los servidores proxy de reenvío reciben el Tráfico saliente de un empleado, lo aprueban y luego lo reenvían a su destino en Internet.
- [x] Los servidores proxy inversos aceptan el tráfico de partes externas, lo aprueban y luego lo reenvían a servidores internos. 
> Correcto