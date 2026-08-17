# Revisión: Arquitectura de red

## Resumen
- Hemos explorado la estructura de una red, incluidas las WAN y las LAN
- ​También hemos hablado de las herramientas de redes estándar como hub, switch, ​routers y módems
- Hemos introducido brevemente las redes en la nube y hemos hablado de sus ventajas.
- ​También dedicamos algo de tiempo al Modelo TCP/IP. 
- ​Como recordatorio, los técnicos y los analistas de seguridad suelen utilizar este marco cuando ​comunican dónde se han producido problemas de red

---

## Términos del glosario del Módulo 1
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 1

1. Rellene el espacio en blanco: Una ___ es una red que abarca una zona geográfica extensa, como una ciudad, un estado o un país
- [x] WAN
- [ ] Módem
- [ ] LAN
- [ ] Nube
> Correcto

1. ¿Cómo se denomina a un grupo de dispositivos conectados?
- [ ] Nube
- [x] Red
- [ ] Protocolo
- [ ] Concentrador
> Correcto

1. ¿Qué tipo de red abarca un edificio de oficinas, una escuela o un hogar?
- [x] LAN
- [ ] Módem
- [ ] Nube
- [ ] WAN
> Correcto

2. Rellene el espacio en blanco: Una computadora envía información al router y éste, a su vez, transfiere la información a través de ____ a Internet
- [x] módem
- [ ] concentrador
- [ ] switch
- [ ] LAN
> Correcto

2. ¿Qué dispositivo de red conecta varias redes entre sí?
- [ ] Un Switch
- [ ] Un concentrador
- [x] Un router
- [ ] Un Módem
> Correcto

3. Rellene el espacio en blanco: Un ___ es un dispositivo que establece conexiones entre dispositivos específicos de una red local enviando y recibiendo datos entre ellos
- [x] switch
- [ ] concentrador
- [ ] módem
- [ ] router
> Correcto

3. ¿Cuál de las siguientes afirmaciones describe con exactitud los Switch? Seleccione todas las que correspondan
- [x] Algunas de las ventajas de los Switch son el control eficaz del flujo de tráfico y la mejora del rendimiento de la red.
- [ ] Los Switch son menos seguros que los concentradores.
- [x] Cuando un Switch recibe un paquete de datos, lee la dirección MAC del dispositivo de destino y la asigna a un puerto. 
- [x] Un Switch es un dispositivo que establece conexiones entre dispositivos específicos de una red enviando y recibiendo datos entre ellos
> Correcto

4. ¿Cuáles son algunos de los beneficios que los proveedores de servicios en la Nube (CSP) ofrecen a los profesionales de la Seguridad? Seleccione todas las que correspondan
- [x] Los PSC ofrecen servicios en línea y aplicaciones web a las que se puede acceder desde cualquier lugar. 
- [ ] Los CSP ofrecen análisis de negocio para monitorizar el tráfico web y las ventas.
- [ ] Los servidores CSP, las aplicaciones y los servicios de redes se alojan en dispositivos físicos locales. (Incorrecto)
- [x] Los CSP pueden ahorrar dinero a una organización ofreciéndole una potencia de proceso que sólo se paga cuando se necesita.
> Incorrecto

4. Un profesional de la seguridad está investigando las ventajas e inconvenientes de utilizar un proveedor de servicios en la nube (CSP). ¿Cuáles son algunas de las razones por las que el profesional de la Seguridad podría optar por utilizar un CSP en su trabajo? Seleccione todas las que correspondan
- [ ] Los servicios del CSP no requieren medidas adicionales de Seguridad en la Nube
- [x] Los servidores remotos CSP permiten acceder a las aplicaciones web desde cualquier lugar.
- [x] Una CSP ofrece una potencia de proceso que sólo se paga en función de las necesidades.
- [x] Un CSP proporciona análisis de negocio para monitorizar el tráfico web y las ventas.
> Correcto

5. ¿Para qué sirve el Pie de página de un paquete de datos?
- [ ] Para mostrar la dirección MAC del dispositivo de destino
- [ ] Identificar el mensaje que se transmitirá al dispositivo receptor
- [ ] Para contener la dirección IP de origen
- [x] Señalar al dispositivo receptor que el paquete ha finalizado
> Correcto

6. ¿Cuáles son las dos ventajas de la computación en la nube y de las redes definidas por software (SDN)? Seleccione dos respuestas
- [x] Mayor escalabilidad
- [ ] Aumento de la superficie de ataque
- [x] Disminución de costes 
- [ ] Disminución de la Confiabilidad
> Correcto

6. Rellene el espacio en blanco: _____ se refiere a la práctica de utilizar servidores, aplicaciones y servicios de red remotos que se alojan en Internet, en lugar de en una ubicación física propiedad de una empresa
- [x] Computación en la nube
- [ ] Redes definidas por software (SDN)
- [ ] Entorno de nube híbrida
- [ ] Red de área local (LAN)
> Correcto

7. ¿Qué número de puerto se utiliza para las transferencias de archivos de gran tamaño?
- [ ] 443
- [ ] 25
- [x] 20
- [ ] 37
> Correcto

7. ¿Cuál de los siguientes números de puerto se utiliza para el tráfico de correo electrónico?
- [ ] 23
- [ ] 20
- [x] 25
- [ ] 443
> Correcto

8. Rellene el espacio en blanco: La capa ___ se utiliza para determinar cómo interactuarán los paquetes de datos con los dispositivos receptores, incluidas las transferencias de archivos y los servicios de correo electrónico
- [ ] Capa 1, acceso a la red
- [ ] Capa 2, Internet 
- [ ] Capa 3, transporte
- [x] Capa 4, aplicación
> Correcto

8. ¿Qué capa del Modelo TCP/IP se utiliza para inspeccionar el flujo de tráfico a través de una red?
- [ ] Capa 1, acceso a la red (Incorrecto)
- [ ] Capa 2, Internet 
- [x] Capa 3, transporte
- [ ] Capa 4, aplicación
> Correcto

9. ¿Cuál de las siguientes direcciones es una dirección IPv4 correcta?
- [x] 192.168.0.2
- [ ] 100.234.56.1.3
- [ ] 1001.2345.3234.5678
- [ ] 129.168.10.25678.1
> Correcto

9. Un analista de Seguridad ejecuta un comando para descubrir una dirección IP local. El analista recibe el siguiente resultado: 169.254.255.249. ¿De qué tipo de dirección se trata?
- [ ] MAC
- [x] IPv4
- [ ] Ethernet
- [ ] IPv6
> Correcto

9. Rellene el espacio en blanco: 127.0.0.1 es un ejemplo de dirección ___.
- [x] IPv4
- [ ] Ethernet
- [ ] MAC
- [ ] IPv6
> Correcto

10. ¿Cuál de las siguientes direcciones es una dirección IPv6 correcta?
- [ ] a360::abf7:h234:0011:g126:1130::ffj2
- [x] fda2:7360:1e5b:e8f5:a69f:c8bd:1b3e:2578
- [ ] a634:b123:cd34:3f56:0023:2345:7890:0000:ffff
- [ ] fda2::7361:135b::38f5:c8bd:1b3e:2578
> Correcto

10. Rellene el espacio en blanco: fe80::ab12:cd34:ef56:0023:2345 es un ejemplo de dirección ___ exacta
- [x] IPv6
- [ ] IPv4
- [ ] MAC
- [ ] Ethernet
> Correcto

10. Un analista de Seguridad ejecuta un comando para descubrir una dirección IP local. El analista recibe el siguiente resultado: fd45:3efd:3201:ff22:0000:0000:12ff:0000. ¿De qué tipo de dirección se trata?
- [ ] IPv4
- [ ] Ethernet
- [x] IPv6
- [ ] MAC
> Correcto