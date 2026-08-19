# Revisión: Seguridad contra la intrusión en la red

## Resumen
- Hemos hablado de cómo proteger las redes. 
- También hemos aprendido sobre tácticas de intrusión en redes ​como el sniffing de paquetes maliciosos y la Suplantación de IP.
- ​Por último, hemos hablado de cómo ​un analista de seguridad puede protegerse contra estos ataques.
- ​Ha aprendido sobre los ataques DoS y DDoS ​como la Inundación ICMP, los ataques SYN, ​y el Ping de la muerte, ​que intentan saturar una red ​inundándola con paquetes de datos no deseados.
- ​Ahora, piense en todo lo que ​ya sabe sobre los ataques a las redes. 

---

## Términos del glosario del Módulo 3
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 3

1. ¿Cuál es el objetivo de los ataques de denegación de servicio (DoS) a nivel de red?
- [x] Ancho de banda de la red
- [ ] Información personal de los empleados
- [ ] Todo el hardware de una organización
- [ ] Aplicaciones de software de uso común
> Correcto

2. ¿Cuál de las siguientes afirmaciones describe con exactitud los ataques de denegación de servicio (DoS) y de denegación de servicio distribuido (DDoS)? Seleccione tres respuestas.
- [x] Un ataque DoS implica que un host lleva a cabo el ataque.
- [x] Un ataque DDoS implica múltiples hosts que llevan a cabo el ataque.
- [x] Un dispositivo de red que experimenta un ataque DoS es incapaz de responder a los usuarios legítimos.
- [ ] Tanto en los ataques DoS como en los DDoS, todas las partes de la red deben estar sobrecargadas para que los ataques tengan éxito.
> Correcto

3. Un responsable de Seguridad está entrenando a su equipo para identificar cuándo un servidor ha sufrido un Ataque de SYN flood. ¿Qué podría indicar a los Miembros del equipo que su organización está en riesgo?
- [ ] Se envía un gran número de paquetes ICMP a los servidores de la organización.
- [x] El servidor ha dejado de responder tras recibir un número inusualmente alto de paquetes SYN entrantes.
- [ ] Se envía un paquete ICMP sobredimensionado al servidor de redes.
- [ ] Los números de puerto de los paquetes de datos son incorrectos.
> Correcto

4. Rellene el espacio en blanco: El ataque DoS _____ se produce cuando un actor malicioso envía un paquete ICMP sobredimensionado a un servidor.
- [ ] en ruta
- [ ] SYN flood
- [x] Ping de la muerte
- [ ] pitufo
> Correcto

5. ¿Cuál de las siguientes afirmaciones describe correctamente el sniffing de paquetes pasivo y activo? Seleccione tres respuestas
- [x] Utilizar una VPN para encriptar Datos ofrece a una empresa protección frente al sniffing de paquetes.
- [x] El rastreo pasivo de paquetes permite a los actores maliciosos ver la información que entra y sale del dispositivo objetivo.
- [x] Rastreo activo de paquetes implica la manipulación de paquetes de datos en tránsito.
- [ ] El objetivo del sniffing activo de paquetes es leer paquetes de datos en tránsito.
> Correcto

6. Como profesional de la Seguridad, usted investiga los ataques en ruta, de repetición y "Ataque Smurf" para implementar procedimientos que protejan a su empresa de estos incidentes. ¿Qué tipo de ataque está investigando?
- [ ] Sniffing de paquetes
- [x] Suplantación de IP
- [ ] Ping de la muerte
- [ ] Inundación SYN flood
> Correcto

7. ¿Cuáles son algunos de los ataques habituales de Suplantación de IP? Seleccione todo lo que corresponda
- [x] ataques en ruta
- [x] ataques de repetición
- [x] ataques Smurf
- [ ] Ataques KRACK
> Correcto

8. ¿En qué ataque los actores maliciosos se hacen pasar por un navegador o un servidor web colocándose entre los dos dispositivos y, a continuación, olfatean la información de los paquetes para descubrir sus direcciones IP y MAC?
- [x] Ataque en ruta
- [ ] Ataque Smurf
- [ ] Ataque por inundación de paquetes
- [ ] Ataque de software malicioso
> Correcto

9. Rellene el espacio en blanco: El ataque a la red _____ se produce cuando un atacante intercepta un paquete de datos en tránsito y luego lo repite en otro momento.
- [ ] SYN flood
- [x] reproducir
- [ ] en ruta
- [ ] pitufo
> Correcto

10. ¿Qué ataque implica que un atacante husmee la dirección IP de un usuario autorizado y lo inunde de paquetes?
- [ ] Ataque en ruta
- [ ] Ping de la muerte
- [ ] Ataque de repetición
- [x] Ataque Smurf
> Correcto