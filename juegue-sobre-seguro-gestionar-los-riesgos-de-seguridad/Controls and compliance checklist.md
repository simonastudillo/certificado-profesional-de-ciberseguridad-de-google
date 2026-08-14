# Controls and compliance checklist

## Controls assessment checklist
- select “yes” or “no” to answer the question: Does Botium Toys currently have this control in place?

| Yes | No | Control | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | Least Privilege | Se recomienda modificar la configuración por defecto de los usuarios para que por defecto tengan los mínimos privilegios necesarios. |
| ⚫ | ✅ | Disaster recovery plans | Se recomienda urgentemente generar plan de backups de datos críticos, con verificación semanal de la integridad del respaldo |
| ⚫ | ✅ | Password policies | Existe un política pero no cumple con estándares mínimos |
| ⚫ | ✅ | Separation of duties | Se recomienda separar las funciones críticas entre diferentes personas para reducir el riesgo de fraude o error. |
| ✅ | ⚫ | Firewall | |
| ⚫ | ✅ | Intrusion detection system (IDS) | Se recomienda la instalación de un sistema de detección de intrusiones para monitorear y alertar sobre actividades sospechosas. |
| ⚫ | ✅ | Backups | Punto ya abordado anteriormente |
| ✅ | ⚫ | Antivirus software | |
| ✅ | ⚫ | Manual monitoring, maintenance, and intervention for legacy systems | No existe claridad de los procedimientos a realizar |
| ⚫ | ✅ | Encryption | Se recomienda encriptar la información sensible tanto en tránsito como en reposo. |
| ⚫ | ✅ | Password management system | Se recomienda uso de sistema informático para gestionar de manera segura las contraseñas. |
| ✅ | ⚫ | Locks (offices, storefront, warehouse) | |
| ✅ | ⚫ | Closed-circuit television (CCTV) surveillance | |
| ✅ | ⚫ | Fire detection/prevention (fire alarm, sprinkler system, etc.) | |

## Compliance checklist
- select “yes” or “no” to answer the question: Does Botium Toys currently adhere to this compliance best practice? 

### Payment Card Industry Data Security Standard (PCI DSS)

| Yes | No | Best practice | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | Only authorized users have access to customers’ credit card information | Se recomienda minimizar los permisos para que solo los usuarios autorizados tengan acceso. |
| ⚫ | ✅ | Credit card information is stored, accepted, processed, and transmitted internally, in a secure environment | Se recomienda manejar fuera de la base de datos de uso general. |
| ⚫ | ✅ | Implement data encryption procedures to better secure credit card transaction touchpoints and data | Los datos no están encriptados, esto no permite mantener la confidencialidad. |
| ⚫ | ✅ | Adopt secure password management policies. | Las políticas de contraseñas no cumplen estándares, se recomienda reforzar su implementación. |


### General Data Protection Regulation (GDPR)

| Yes | No | Best practice | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | E.U. customers’ data is kept private/secured. | Se recomienda eliminar privilegios de lectura de datos sensibles solo a personal mínimo necesario |
| ✅ | ⚫ | There is a plan in place to notify E.U. customers within 72 hours if their data is compromised/there is a breach. | |
| ⚫ | ✅ | Ensure data is properly classified and inventoried | Se recomienda mantener datos históricos correctamente clasificados e inventariados en base de datos aparte. |
| ✅ | ⚫ | Enforce privacy policies, procedures, and processes to properly document and maintain data | Se recomienda revisar y actualizar regularmente las políticas de privacidad para asegurar el cumplimiento. |



### System and Organizations Controls (SOC type 1, SOC type 2)

| Yes | No | Best practice | Notes |
| --- | --- | --- | --- |
| ⚫ | ✅ | User access policies are established | Se recomienda revisar regularmente las políticas de acceso de los usuarios, actualizar políticas actuales para cumplir con las regulaciones correspondientes. |
| ⚫ | ✅ | Sensitive data (PII/SPII) is confidential/private | Punto ya abordado, se recomienda manejar privilegios mínimos necesarios. |
| ✅ | ⚫ | Data integrity ensures the data is consistent, complete, accurate, and has been validated. | |
| ⚫ | ✅ | Data is available to individuals authorized to access it | Si bien la información está disponible para los individuos autorizados, tambien está disponible para todos, se recomienda ajustar privilegios de todos los usuarios y permitir solo a los mínimo necesarios |