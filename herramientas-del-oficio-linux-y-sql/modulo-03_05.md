# Revisión: Comandos Linux en el shell Bash

## Resumen
-  ​En esta sección, usted utilizó la línea de comandos para comunicarse con el OS.
- ​Parte de esto fue el uso de comandos para navegar y gestionar el sistema de archivos.
- ​Y usted utilizó otros comandos para autenticar y autorizar usuarios.
- ​Todas estas son tareas que un analista de seguridad es probable que encuentre. 
- Finalmente, usted aprendió sobre el acceso a recursos que soportan ​el aprendizaje de nuevos comandos de Linux.
- ​Con estos Conocimientos, podrá seguir aprendiendo más y ​más sobre el uso de la línea de comandos.

---

## Guía de referencia: Linux
- La guía de referencia de Linux contiene los comandos clave de Linux que los profesionales de la Seguridad utilizan para realizar las tareas básicas de su trabajo.
- La guía de referencia está dividida en seis categorías diferentes de comandos Linux útiles para las tareas relacionadas con la Seguridad:
   - Navegar por el sistema de archivos
   - Leer archivos
   - Gestionar el sistema de archivos
   - Filtrar contenidos
   - Gestionar usuarios y sus permisos
   - Obtener ayuda en Linux
- Dentro de cada categoría, los comandos están organizados alfabéticamente.
- [Reference Guide Linux](./resources/Reference Guide Linux.pdf)

---

## Términos del glosario del Módulo 3
- El glosario completo se encuentra [aquí](./README.md#glosario)

---

## Desafío del módulo 3

1. ¿Cuáles son los argumentos en grep bmoreno Q4users.txt? Seleccione dos respuestas
- [x] Q4users.txt
- [ ] .txt
- [ ] grep
- [x] bmoreno
> Correcto

2. ¿Cuál de los siguientes elementos representa el directorio raíz?
- [ ] *home
- [ ] *
- [x] /
- [ ] /home
> Correcto

3. Un analista de Seguridad introduce grep OS updates.txt en la línea de comandos. ¿Qué le dice esto al sistema operativo que haga?
- [x] Busca en el archivo updates.txt y devuelve todas las líneas que contengan la cadena OS
- [ ] Cree un nuevo Directorio llamado OS y un nuevo archivo llamado updates.txt
- [ ] Mueva el archivo updates.txt al directorio OS 
- [ ] Cree un nuevo archivo llamado updates.txt en el directorio OS 
> Correcto

4. ¿Cuál de estos comandos crea un nuevo archivo?
- [ ] cd
- [ ] mkdir
- [x] touch
- [ ] chmod
> Correcto

5. ¿Qué son leer, escribir y ejecutar?
- [ ] Los tres tipos de propietarios para archivos y directorios
- [x] Los tres tipos de permisos para los usuarios autorizados
- [ ] Comandos específicos de Linux utilizados para cambiar los permisos de archivo
- [ ] Diferentes métodos para editar archivos
> Correcto

6. Un analista de Seguridad introduce chmod u+w,g-r access.txt en la línea de comandos. ¿Qué le dice este comando al sistema operativo que haga? Seleccione todo lo que corresponda
- [ ] Añada permisos de escritura al grupo para el archivo access.txt 
- [x] Añada permisos de escritura al usuario para el archivo access.txt 
- [x] Elimine los permisos de lectura del grupo para el archivo access.txt 
- [ ] Elimine los permisos de lectura del usuario para el archivo access.txt 
> Correcto

7. ¿Qué hace sudo?
- [x] Concede temporalmente permisos elevados a usuarios específicos
- [ ] Añade usuarios al sistema
- [ ] Elimina usuarios del sistema
- [ ] Cambia el propietario asociado a un archivo concreto
> Correcto

8. ¿Qué debe especificar en el argumento que sigue al comando cd?
- [x] El Directorio al que desea navegar
- [ ] Su directorio actual
- [ ] El archivo que desea crear
- [ ] La Cadena que desea buscar
> Correcto

9. Un analista de Seguridad introduce apropos password en la línea de comandos. ¿Qué le dice esto al sistema operativo que haga?
- [ ] Cambie su Directorio actual a /password
- [ ] Mostrar información detallada sobre el comando password y su funcionamiento
- [ ] Muestra una descripción del comando password en una sola línea
- [x] Salida de todos los comandos que contienen la palabra "contraseña" en sus descripciones de la página man
> Correcto

10. Dados los siguientes permisos drw-rw-r--, ¿qué carácter indica si se trata de un archivo o de un directorio?
- [x] Primero
- [ ] Segundo
- [ ] Quinto
- [ ] Décima
> Correcto