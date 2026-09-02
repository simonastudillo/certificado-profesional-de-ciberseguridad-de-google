# Revisión: Monitoreo y análisis de redes

## Resumen
- ​Aprendió cómo los flujos de tráfico de red ​proporcionan una valiosa información estadística sobre las comunicaciones.
- Al ​monitorear la actividad de la red en ​busca de indicadores de riesgo, ​aprendió a detectar ​actividades inusuales en la red, como el robo de datos.
- ​Luego, aprendió a ver y capturar el ​tráfico de red mediante rastreadores de paquetes.
- ​Por último, aprendió a inspeccionar ​paquetes mediante el análisis de paquetes.
- ​Ha diseccionado los campos de datos de los encabezados de los paquetes ​y analizado las capturas de paquetes en detalle.
- ​Ha avanzado mucho ​en el desarrollo de las habilidades que ​necesitará para prepararse para un puesto de nivel inicial en Seguridad.

---

## Glosario de términos del módulo 2
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 2

1. ¿Por qué es importante el Tráfico de red en ciberseguridad? Seleccione dos respuestas
- [x] Ayuda a detectar intrusiones y ataques en la red.
- [x] Ayuda a identificar las desviaciones respecto a los flujos de tráfico previstos.
- [ ] Proporciona un método para clasificar los recursos críticos.
- [ ] Proporciona un Método para la encriptación de las comunicaciones.
> Correcto

2. ¿Qué táctica utilizan los actores maliciosos para mantener y ampliar el acceso no autorizado a una red?
- [ ] Phishing
- [x] Movimiento lateral
- [ ] Reducción del tamaño de los datos
- [ ] Exfiltración
> Correcto

2. ¿Cuáles son algunas medidas defensivas que pueden utilizarse para protegerse contra el robo de datos? Seleccione dos respuestas.
- [x] Implementación de autenticación de múltiples factores
- [x] Monitorear la actividad de la red
- [ ] Reducir el tamaño de los archivos
- [ ] Utilizar el movimiento lateral
> Correcto

3. ¿Qué información contienen los encabezados de los paquetes? Seleccione tres respuestas
- [x] Protocolos
- [ ] Datos de la carga útil
- [x] Puertos
- [x] Direcciones IP
> Correcto

4. Rellene el espacio en blanco: Los analizadores de protocolos de red pueden guardar las comunicaciones de red en archivos conocidos como _____
- [x] captura de paquetes
- [ ] carga útil
- [ ] protocolo
- [ ] paquete de red
> Correcto

4. La práctica de capturar e inspeccionar los paquetes de datos de red que se transmiten a través de una red se conoce como _____
- [ ] captura de protocolos
- [ ] olfateo de puertos
- [ ] captura de paquetes
- [x] sniffing de paquetes
> Correcto

5. ¿Cómo ayudan los analizadores de protocolos de red a los analistas de seguridad a analizar las comunicaciones de red? Seleccione dos respuestas
- [x] Ofrecen la posibilidad de filtrar y ordenar la información de captura de paquetes para encontrar la información relevante.
- [ ] Toman medidas para bloquear las intrusiones en la red.
- [ ] Toman medidas para mejorar el rendimiento de la red.
- [x] Proporcionan la capacidad de recopilar comunicaciones de red.
> Correcto

5. ¿Cómo ayudan los analizadores de protocolos de red a los analistas de seguridad a analizar las comunicaciones de red? Seleccione dos respuestas
- [x] Proporcionan la capacidad de recopilar comunicaciones de red.
- [ ] Toman medidas para mejorar el rendimiento de la red.
- [x] Ofrecen la posibilidad de filtrar y ordenar la información de captura de paquetes para encontrar la información relevante.
- [ ] Toman medidas para bloquear las intrusiones en la red.
> Correcto

6. ¿En qué capa del Modelo TCP/IP opera el Protocolo de Internet (IP)?
- [x] Internet
- [ ] Acceso a la Red
- [ ] Transporte
- [ ] Aplicación
> Correcto

7. ¿Qué Campo IPv4 determina cuánto tiempo puede viajar un paquete antes de ser descartado?
- [ ] Opciones
- [ ] Tipo de servicio
- [ ] Suma de comprobación del Encabezado
- [x] Tiempo de vivir
> Correcto

8. ¿Qué valor tienen las cabeceras IP para los analistas de Seguridad durante las investigaciones?
- [ ] Proporcionan la capacidad de modificar las comunicaciones de red.
- [ ] Proporcionan una visión estadística de los detalles de las comunicaciones en red.
- [ ] Ofrecen la posibilidad de visualizar las comunicaciones en red. (Incorrecto)
- [ ] Proporcionan la base para las comunicaciones a través de Internet.
> Incorrecto

8. ¿Cómo se conoce el proceso de descomposición de paquetes?
- [ ] Banderas
- [ ] Suma de comprobación
- [x] Fragmentación
- [ ] Desplazamiento de fragmentos
> Correcto

9. ¿Qué opción de tcpdump aplica la verbosidad? 
- [x] -v
- [ ] -i
- [ ] -c
- [ ] -n
> Correcto

9. ¿Qué comando tcpdump da salida a información detallada sobre paquetes? 
- [ ] sudo tcpdump -i any -c 100
- [ ] sudo tcpdump -v any -i 
- [ ] sudo tcpdump -i any -n
- [x] sudo tcpdump -i any -v
> Correcto

10. Examine la siguiente salida de tcpdump:
```bash
22:00:19.538395 IP (tos 0x10, ttl 64, id 33842, offset 0, flags [P], proto TCP (6), length 196) 198.168.105.1.41012 > 198.111.123.1.61012: Flags [P.], cksum 0x50af (correct), seq 169, ack 187, win 501, length 42
```
- ¿Cuál es la IP de origen?
- [ ] 198.111.123.1
- [x] 198.168.105.1
- [ ] 41012
- [ ] 22:00:19.538395
> Correcto

10. Examine la siguiente salida de tcpdump:
```bash
22:00:19.538395 IP (tos 0x10, ttl 64, id 33842, offset 0, flags [P], proto TCP (6), length 196) 198.168.105.1.41012 > 198.111.123.1.61012: Flags [P.], cksum 0x50af (correct), seq 169, ack 187, win 501, length 42
```
- ¿Cuál es el valor del Campo Tipo de Servicio?
- [ ] 501
- [ ] 6
- [x] 0x10
- [ ] 0x50af
> Correcto