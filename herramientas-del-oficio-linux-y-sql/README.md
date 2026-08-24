# Herramientas del oficio: Linux y SQL
---
- Módulo 1: Introducción a los sistemas operativos
   - [Comenzar el curso](./modulo-01_01.md)
   - [El maravilloso mundo de los sistemas operativos](./modulo-01_02.md)
   - [El sistema operativo en funcionamiento](./modulo-01_03.md)
   - [Interfaz de usuario](./modulo-01_04.md)
   - [Repaso: Introducción a los sistemas operativos](./modulo-01_05.md)
- Módulo 2: El sistema operativo Linux
   - [Todo sobre Linux](./modulo-02_01.md)
   - [Distribuciones Linux](./modulo-02_02.md)
   - [El shell](./modulo-02_03.md)
   - [Revisión: El sistema operativo Linux](./modulo-02_04.md)
- Módulo 3: Comandos Linux en el shell Bash
   - [Navegar por el sistema de archivos de Linux](./modulo-03_01.md)
   - [Gestionar el contenido de los archivos en Bash](./modulo-03_02.md)
   - [Autenticación y autorización de usuarios](./modulo-03_03.md)
   - [Obtener ayuda en Linux](./modulo-03_04.md)
   - [Revisión: Comandos Linux en el shell Bash](./modulo-03_05.md)
- Módulo 4: Bases de datos y SQL
   - [Introducción a SQL y a las bases de datos](./modulo-04_01.md)
   - [Consultas SQL](./modulo-04_02.md)
   - [Más filtros SQL](./modulo-04_03.md)
   - [Uniones SQL](./modulo-04_04.md)
   - [Revisión: Bases de datos y SQL](./modulo-04_05.md)
   - [¡Enhorabuena por haber completado el Curso 4!](./modulo-04_06.md)

## Habilidades y conceptos a aprender
---

### Habilidades técnicas (hard skills)

- **Linux Command Line (Bash)**: Navegación y gestión del sistema de archivos (`pwd`, `ls`, `cd`, `mkdir`, `rmdir`, `touch`, `rm`, `mv`, `cp`), lectura de archivos (`cat`, `head`, `tail`, `less`), filtrado de contenido (`grep`, `find`, piping `|`), y redirección de salida (`>`, `>>`).
- **Gestión de usuarios y permisos en Linux**: Configuración de autorización y autenticación (`chmod`, `chown`, `useradd`, `usermod`, `userdel`), uso de `sudo` para privilegios elevados, e interpretación de la cadena de 10 caracteres de permisos (`rwx`).
- **SQL (Structured Query Language)**: Consultas a bases de datos relacionales (`SELECT`, `FROM`, `ORDER BY`), filtrado de datos (`WHERE`, `LIKE`, comodines `%` y `_`, `BETWEEN`, operadores de comparación `=`, `>`, `<`, `>=`, `<=`, `<>`, `!=`), operadores lógicos (`AND`, `OR`, `NOT`), uniones de tablas (`INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`), y funciones de agregación (`COUNT`, `AVG`, `SUM`).
- **Gestión de paquetes de software**: Instalación y desinstalación de aplicaciones con administradores de paquetes (`APT`, `YUM`, `dpkg`, `RPM`).
- **Editores de texto en línea de comandos**: Edición de archivos con `nano` (conocimiento básico de `Vim` y `Emacs`).
- **Análisis de registros (logs)**: Revisión y filtrado de registros de seguridad para identificar accesos no autorizados, patrones sospechosos y vulnerabilidades.

### Conceptos clave

- **Sistemas operativos (OS)**: Funciones principales, relación entre hardware, software y aplicaciones, proceso de arranque (`BIOS`, `UEFI`, `bootloader`), y gestión de recursos (CPU, RAM, disco duro).
- **Interfaces de usuario**: Diferencias entre GUI (Graphical User Interface) y CLI (Command-Line Interface), ventajas de la CLI en ciberseguridad (eficiencia, archivo de historial).
- **Arquitectura de Linux**: Componentes del sistema (usuario, aplicaciones, shell, `Filesystem Hierarchy Standard (FHS)`, `kernel`, hardware).
- **Distribuciones de Linux**: `Kali Linux` (pentesting y forense digital), `Ubuntu`, `Red Hat Enterprise Linux`, `Parrot`, `CentOS`, `AlmaLinux`.
- **Virtualización**: Máquinas virtuales (VM), hipervisores (`KVM`), entornos aislados (`sandbox`) para análisis de malware.
- **Bases de datos relacionales**: Estructura de tablas (columnas/campos, filas/registros), claves primarias y foráneas, tipos de datos (cadenas, numéricos, fecha/hora), valores `NULL`.
- **Autenticación y autorización**: Principio de privilegio mínimo (`Principle of least privilege`), usuario root vs. `sudo`, archivo `sudoers`, gestión de grupos primarios y suplementarios.
- **Ciberseguridad práctica**: Pruebas de penetración (`penetration testing`), análisis forense digital (`digital forensics`), herramientas de seguridad (`Metasploit`, `Burp Suite`, `John the Ripper`, `Wireshark`, `tcpdump`, `Autopsy`, `Suricata`), gestión de vulnerabilidades y parches, sistemas operativos heredados (`legacy OS`).

### Habilidades transferibles (soft skills)

- **Resolución de problemas (Troubleshooting)**: Análisis de eventos de seguridad, rastreo de flujo de procesos para identificar dónde ocurrió un incidente, y uso de recursos comunitarios (`Stack Overflow`, `Stack Exchange`) para solucionar problemas técnicos.
- **Pensamiento analítico**: Filtrado y análisis de grandes volúmenes de datos para identificar patrones inusuales, anomalías y posibles amenazas de seguridad.
- **Toma de decisiones basada en datos**: Uso de consultas SQL y análisis de registros para respaldar decisiones de seguridad y comunicar hallazgos a las partes interesadas.
- **Documentación y reporte**: Creación de informes de actividades de seguridad, documentación de comandos y procedimientos para portafolios profesionales.
- **Aprendizaje continuo y autodidacta**: Uso de recursos integrados (`man`, `whatis`, `apropos`) y búsqueda en línea para aprender nuevos comandos y herramientas de forma autónoma.
- **Atención al detalle**: Revisión exhaustiva de permisos de archivos, verificación de configuraciones de seguridad, y análisis detallado de registros para detectar irregularidades.
- **Comunicación efectiva**: Explicación de conceptos técnicos y hallazgos de seguridad a audiencias con distintos niveles de conocimiento técnico.


## Descripción del curso
---
- Este curso se centra en los conocimientos informáticos básicos que respaldan el trabajo de un analista de seguridad.
- Comienza con una introducción a los sistemas operativos informáticos, seguida de una exploración más detallada de Linux, un sistema operativo utilizado habitualmente por los profesionales de la seguridad.
- Al final de este curso, los alumnos serán capaces de utilizar la línea de comandos de Linux a través del intérprete de comandos Bash para navegar y gestionar el sistema de archivos y para autenticar y autorizar a los usuarios, y también serán capaces de utilizar SQL para comunicarse con una base de datos.
- Al final de este curso, usted podrá:
   - Explicar la relación entre los sistemas operativos, las aplicaciones y el hardware.
   - Comparar una interfaz gráfica de usuario con una interfaz de línea de comandos.
   - Identificar las características únicas de las distribuciones comunes de Linux.
   - Navegar y gestionar el sistema de archivos utilizando comandos de Linux a través del intérprete de comandos Bash.
   - Utilizar comandos de Linux a través del intérprete de comandos Bash para autenticar y autorizar a los usuarios.
   - Describir cómo se organiza una base de datos relacional.
   - Utilizar SQL para recuperar información de una base de datos.
   - Aplicar filtros a las consultas SQL y utilizar uniones para combinar varias tablas.


## Glosario
---
- `Absolute file path`: The full file path, which starts from the root
- `Application`: A program that performs a specific task
- `Argument (Linux)`: Specific information needed by a command
- `Authentication`: The process of verifying who someone is
- `Authorization`: The concept of granting access to specific resources in a system
- `Bash`: The default shell in most Linux distributions
- `Basic Input/Output System (BIOS)`: A microchip that contains loading instructions for the computer and is prevalent in older systems
- `Bootloader`: A software program that boots the operating system
- `CentOS`: An open-source distribution that is closely related to Red Hat
- `Central Processing Unit (CPU)`: A computer’s main processor, which is used to perform general computing tasks on a computer
- `Command`: An instruction telling the computer to do something
- `Command-line interface (CLI)`: A text-based user interface that uses commands to interact with the computer
- `Database`: An organized collection of information or data
- `Date and time data`: Data representing a date and/or time
- `Digital forensics`: The practice of collecting and analyzing data to determine what has happened after an attack
- `Directory`: A file that organizes where other files are stored
- `Distributions`: The different versions of Linux
- `Exclusive operator`: An operator that does not include the value of comparison
- `File path`: The location of a file or directory
- `Filesystem Hierarchy Standard (FHS)`: The component of the Linux OS that organizes data
- `Filtering`: Selecting data that match a certain condition
- `Foreign key`: A column in a table that is a primary key in another table
- `Graphical user interface (GUI)`: A user interface that uses icons on the screen to manage different tasks on the computer
- `Hard drive`: A hardware component used for long-term memory
- `Hardware`: The physical components of a computer
- `Inclusive operator`: An operator that includes the value of comparison
- `Internal hardware`: The components required to run the computer
- `Kali Linux ™`: An open-source distribution of Linux that is widely used in the security industry
- `Kernel`: The component of the Linux OS that manages processes and memory
- `Legacy operating system`: An operating system that is outdated but still being used
- `Linux`: An open-source operating system
- `Log`: A record of events that occur within an organization's systems
- `nano`: A command-line file editor that is available by default in many Linux distributions
- `Numeric data`: Data consisting of numbers
- `Operating system (OS)`: The interface between computer hardware and the user
- `Operator`: A symbol or keyword that represents an operation
- `Options`: Input that modifies the behavior of a command
- `Package`: A piece of software that can be combined with other packages to form an application
- `Package manager`: A tool that helps users install, manage, and remove packages or applications
- `Parrot`: An open-source distribution that is commonly used for security
- `Penetration test (pen test)`: A simulated attack that helps identify vulnerabilities in systems, networks, websites, applications, and processes
- `Peripheral devices`: Hardware components that are attached and controlled by the computer system
- `Permissions`: The type of access granted for a file or directory
- `Primary key`: A column where every row has a unique entry
- `Principle of least privilege`: The concept of granting only the minimal access and authorization required to complete a task or function
- `Query`: A request for data from a database table or a combination of tables
- `Random Access Memory (RAM)`: A hardware component used for short-term memory
- `Red Hat`: A subscription-based distribution of Linux built for enterprise use
- `Relational database`: A structured database containing tables that are related to each other
- `Relative file path`: A file path that starts from the user's current directory
- `Root directory`: The highest-level directory in Linux
- `Root user (or superuser)`: A user with elevated privileges to modify the system
- `Shell`: The command-line interpreter
- `SQL (Structured Query Language)`: A programming language used to create, interact with, and request information from a database
- `Standard error`: An error message returned by the OS through the shell
- `Standard input`: Information received by the OS via the command line
- `Standard output`: Information returned by the OS through the shell
- `String data`: Data consisting of an ordered sequence of characters
- `Syntax`: The rules that determine what is correctly structured in a computing language
- `Ubuntu`: An open-source, user-friendly distribution that is widely used in security and other industries
- `Unified Extensible Firmware Interface (UEFI)`: A microchip that contains loading instructions for the computer and replaces BIOS on more modern systems
- `User`: The person interacting with a computer
- `User interface`: A program that allows the user to control the functions of the operating system
- `Wildcard`: A special character that can be substituted with any other character


## Recursos del curso
---
- [Stack Exchange. (s.f.). Unix y Linux.](https://unix.stackexchange.com/)

## Citas
---
> Oficina de Estadísticas Laborales de EE.UU. (2022, 8 de septiembre). Analistas de seguridad de la información.
> [https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm)

> Krzyzanowski, P. (2015, 27 de enero). Sistemas operativos. Rutgers.
> [https://people.cs.rutgers.edu/~pxk/416/notes/01-intro.html](https://people.cs.rutgers.edu/~pxk/416/notes/01-intro.html)

> Instituto Nacional de Normas y Tecnología. (s.f.). Glosario. Consultado en diciembre de 2022.
> [https://csrc.nist.gov/glossary](https://csrc.nist.gov/glossary)

> Apple. (s.f.). Lanzamientos. Código abierto.
> [https://opensource.apple.com/releases/](https://opensource.apple.com/releases/)

> Apple, Darwin XNU. (s.f.). Repositorio GitHub. Apple.
> [https://github.com/apple/darwin-xnu](https://github.com/apple/darwin-xnu)

> Apple. (s.f.). Aplicar actualizaciones de seguridad.
> [https://support.apple.com/en-us/HT201222](https://support.apple.com/en-us/HT201222)

> Belding, G. (2020, 1 de septiembre). Por qué su programa de gestión de riesgos de seguridad debe incluir los sistemas heredados. Gestión, cumplimiento y auditoría.
> [https://resources.infosecinstitute.com/topic/why-your-security-risk-management-program-should-include-legacy-systems/](https://resources.infosecinstitute.com/topic/why-your-security-risk-management-program-should-include-legacy-systems/)

> Google. (s.f.). Chromium. Código abierto.
> [https://opensource.google/projects/chromiumos](https://opensource.google/projects/chromiumos)

> Google. (s.f.). Boletines de seguridad. Atención al cliente de Google Cloud.
> [https://cloud.google.com/support/bulletins](https://cloud.google.com/support/bulletins)

> Microsoft. (s.f.). Guía de actualizaciones de seguridad.
> [https://msrc.microsoft.com/update-guide/vulnerability](https://msrc.microsoft.com/update-guide/vulnerability)

> Singer, N. (2017, 13 de mayo). Cómo Google se apoderó de las aulas. The New York Times.
> [https://www.nytimes.com/2017/05/13/technology/google-education-chromebooks-schools.html](https://www.nytimes.com/2017/05/13/technology/google-education-chromebooks-schools.html)

> Stallman, R. (s.f.). Sistema operativo GNU.
> [https://www.gnu.org/gnu/thegnuproject.html](https://www.gnu.org/gnu/thegnuproject.html)

> StatCounter. (s.f.). Cuota de mercado mundial de sistemas operativos de escritorio: Sept 2022.
> [https://gs.statcounter.com/os-market-share/desktop/worldwide/#monthly-202209-202209-bar](https://gs.statcounter.com/os-market-share/desktop/worldwide/#monthly-202209-202209-bar)

> Los proyectos Chromium. (sin fecha). Preguntas frecuentes sobre Chromium OS.
> [https://www.chromium.org/chromium-os/chromium-os-faq/](https://www.chromium.org/chromium-os/chromium-os-faq/)

> Los editores de la Enciclopedia Británica. (2009, 30 de diciembre). Android. Enciclopedia Británica.
> [https://www.britannica.com/technology/Android-operating-system](https://www.britannica.com/technology/Android-operating-system)

> Los Editores de la Enciclopedia Británica. (s.f.). Chrome .  Enciclopedia Británica.
> [https://www.britannica.com/technology/Chrome](https://www.britannica.com/technology/Chrome)

> Los Editores de la Enciclopedia Británica. (s.f.). iOS. Enciclopedia Británica.
> [https://www.britannica.com/technology/iOS](https://www.britannica.com/technology/iOS)

> Los Editores de la Enciclopedia Británica. (s.f.). Linux. Enciclopedia Británica.
> [https://www.britannica.com/technology/Linux](https://www.britannica.com/technology/Linux)

> Los Editores de la Enciclopedia Británica. (s.f.). Mac OS. Enciclopedia Británica.
> [https://www.britannica.com/technology/Mac-OS](https://www.britannica.com/technology/Mac-OS)

> Los Editores de la Enciclopedia Británica. (s.f.). Microsoft Windows. Enciclopedia Británica.
> [https://www.britannica.com/technology/Windows-OS](https://www.britannica.com/technology/Windows-OS)

> Ubuntu. (s.f.). Informes CVE.
> [https://ubuntu.com/security/cves](https://ubuntu.com/security/cves)

> Proyecto de documentación de Linux. (s.f.). 3. ¿Qué ocurre cuando se enciende un ordenador? The Unix and Internet Fundamentals HOWTO.
> [https://tldp.org/HOWTO/Unix-and-Internet-Fundamentals-HOWTO/bootup.html](https://tldp.org/HOWTO/Unix-and-Internet-Fundamentals-HOWTO/bootup.html)

> Zetter, K. (2015, 20 de marzo). Hackear los chips de la BIOS ya no es sólo cosa de la NSA. WIRED.
> [https://www.wired.com/2015/03/researchers-uncover-way-hack-bios-undermine-secure-operating-systems/](https://www.wired.com/2015/03/researchers-uncover-way-hack-bios-undermine-secure-operating-systems/)

> Franklin, C., & Pollette, C. (2022, 7 de julio). Cómo funcionan los sistemas operativos. Cómo funcionan las cosas.
> [https://computer.howstuffworks.com/operating-system2.htm](https://computer.howstuffworks.com/operating-system2.htm)

> Universidad de Helsinki. (s.f.). Sistema operativo e interfaz de usuario. Habilidades digitales del estudiante.
> [https://blogs.helsinki.fi/students-digital-skills/1-introduction-to-the-use-of-computers/1-1-computer-functionality/operating-system-and-user-interface/#:~:text=A%20user%20interface%20(UI)%20refers,command%20line%20using%20a%20keyboard.](https://blogs.helsinki.fi/students-digital-skills/1-introduction-to-the-use-of-computers/1-1-computer-functionality/operating-system-and-user-interface/#:~:text=A%20user%20interface%20(UI)%20refers,command%20line%20using%20a%20keyboard.)

> Red Hat. (2023, 3 de enero). ¿Qué es Linux? Understanding Linux.
> [https://www.redhat.com/en/topics/linux/what-is-linux](https://www.redhat.com/en/topics/linux/what-is-linux)

> Siever, E., Figgins, S., Weber, A., Love, R., & Robbins, A. (2005). Linux en pocas palabras. O'Reilly Media, Inc. Libros electrónicos.
> [https://repo.zenk-security.com/Linux%20et%20systemes%20d.exploitations/Linux-in-a-Nutshell-6th-Edition.pdf](https://repo.zenk-security.com/Linux%20et%20systemes%20d.exploitations/Linux-in-a-Nutshell-6th-Edition.pdf)

> SUSE. (s.f.). ¿Qué es una distribución Linux?
> [https://www.suse.com/suse-defines/definition/linux-distribution/](https://www.suse.com/suse-defines/definition/linux-distribution/)

> Kali. (s.f.). ¿Debería utilizar Kali Linux?
> [https://www.kali.org/docs/introduction/should-i-use-kali-linux/](https://www.kali.org/docs/introduction/should-i-use-kali-linux/)

> Red Hat. (2021, 23 de marzo). ¿Qué es CentOS?
> [https://www.redhat.com/en/topics/linux/what-is-centos](https://www.redhat.com/en/topics/linux/what-is-centos)

> Gedris, V. (2003, 15 de junio). Una introducción al shell de comandos de Linux para principiantes.
> [https://www2.karlin.mff.cuni.cz/~hron/NMNV532/ShellIntro.pdf](https://www2.karlin.mff.cuni.cz/~hron/NMNV532/ShellIntro.pdf)

> Instituto Tecnológico de Massachusetts. (s.f.). Permisos de archivos y directorios en UFS y NFS.
> [http://web.mit.edu/sipb/doc/working/afs/html/subsection3.1.html](http://web.mit.edu/sipb/doc/working/afs/html/subsection3.1.html)

> Linuxize. (2020, 30 de mayo). Cómo crear usuarios en Linux.
> [https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/#how-to-create-a-new-user-in-linux](https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/#how-to-create-a-new-user-in-linux)

> Prakash, A. (2022, 1 de febrero). Permisos y propiedad de archivos en Linux explicados con ejemplos. Manual de Linux.
> [https://linuxhandbook.com/linux-file-permissions/](https://linuxhandbook.com/linux-file-permissions/)

> Stack Exchange. (s.f.). Unix y Linux.
> [https://unix.stackexchange.com/](https://unix.stackexchange.com/)

>Oracle. (2022, 2 de junio). ¿Qué es una base de datos?
> [https://www.oracle.com/database/what-is-database/](https://www.oracle.com/database/what-is-database/)

> Oracle. (2022, 2 de junio). ¿Qué es una base de datos relacional?
> [https://www.oracle.com/database/what-is-a-relational-database/](https://www.oracle.com/database/what-is-a-relational-database/)

## Resumen de módulos
---

### Módulo 1: Introducción a los sistemas operativos
- El **sistema operativo (OS)** es la interfaz entre el hardware y el usuario: hace que la computadora funcione de forma eficiente, permite ejecutar múltiples aplicaciones a la vez y salva la brecha de comunicación entre humanos y el lenguaje binario de las máquinas.
- Sistemas operativos comunes en el sector: **Windows** y **macOS** (código cerrado/parcialmente abierto), **Linux** (completamente de código abierto y clave en seguridad), **ChromeOS** (educación) y los móviles **Android** e **iOS**.
- La seguridad del OS implica asegurar archivos, acceso a datos y autenticación de usuarios; los analistas gestionan cortafuegos, políticas de seguridad, antivirus y auditorías.
- **Proceso de arranque**: al encender el equipo se activa el microchip **BIOS** (sistemas antiguos) o **UEFI** (posteriores a 2007, con mejoras de seguridad), que carga el **bootloader** (cargador de arranque), y éste inicia el sistema operativo. La BIOS suele no ser explorada por antivirus, por lo que es vulnerable a infecciones.
- **Flujo de una tarea** (4 partes): el usuario utiliza una **aplicación**, ésta envía la solicitud al **sistema operativo**, el OS la dirige al **hardware** (CPU, disco duro) y el resultado regresa por el mismo camino. Rastrear este flujo ayuda a investigar dónde ocurrió un evento de seguridad.
- El OS **gestiona los recursos** (CPU, memoria, almacenamiento, ancho de banda) asignándolos donde más se necesitan; el administrador de tareas permite detectar anomalías, como malware consumiendo recursos.
- **Virtualización**: las máquinas virtuales (VM) son versiones de software de computadoras físicas, gestionadas por **hipervisores** (como **KVM**, integrado en el kernel de Linux). Ofrecen entornos aislados (*sandbox*) ideales para analizar malware de forma segura y eficiencia al compartir hardware, aunque no son infalibles (un programa malicioso podría escapar al host).
- **GUI vs CLI**: la interfaz gráfica (GUI) usa iconos y permite una petición a la vez; la línea de comandos (CLI) es basada en texto, más flexible y potente, permite múltiples tareas simultáneas y **registra un historial de comandos**, útil para verificar pasos de un manual de respuesta a incidentes o rastrear las acciones de un atacante.
- **Sistemas operativos heredados** (legacy): obsoletos pero aún en uso por compatibilidad; ya no reciben soporte ni actualizaciones, lo que los hace vulnerables a nuevas amenazas. Mantener los sistemas actualizados es clave.

### Módulo 2: El sistema operativo Linux
- **Linux** es un sistema operativo completamente de código abierto, nacido de la unión del **kernel de Linus Torvalds** y el proyecto **GNU de Richard Stallman**, bajo la Licencia Pública GNU. Es central en ciberseguridad: se usa para examinar registros, verificar acceso y autorización, y ejecutar herramientas de seguridad.
- **Arquitectura de Linux** (6 componentes): **usuario** → **aplicaciones** (distribuidas por administradores de paquetes; ej. el editor nano) → **shell** → **Filesystem Hierarchy Standard (FHS)** (organiza los datos) → **kernel** (gestiona procesos y memoria, comunica con el hardware mediante controladores) → **hardware** (periféricos como monitores e impresoras, e internos como CPU, RAM y disco duro). Linux es un sistema **multiusuario**.
- **Distribuciones**: versiones derivadas del kernel abierto, creadas según necesidades del usuario:
   - **Kali Linux™** (derivada de Debian): diseñada para **pruebas de penetración** y **análisis forense digital**; incluye Metasploit, Burp Suite, John the Ripper, tcpdump, Wireshark y Autopsy. Debe usarse en máquina virtual.
   - **Ubuntu**: fácil de usar, con CLI y GUI, gran comunidad de soporte y muy usada en computación en la nube.
   - **Red Hat Enterprise Linux**: por suscripción, para uso empresarial con soporte dedicado.
   - **Parrot**: herramientas de seguridad preinstaladas y GUI amigable.
   - **CentOS** (descontinuado) y **AlmaLinux** (su reemplazo estable): relacionadas con Red Hat.
- **Gestión de paquetes**: los paquetes contienen archivos y dependencias; `dpkg` (archivos `.deb`, Debian) y `RPM` (archivos `.rpm`, Red Hat) son administradores de paquetes, mientras que **APT** (Debian) y **YUM** (Red Hat) son herramientas de gestión desde la CLI (ej. `sudo apt install suricata`). Mantener versiones recientes garantiza parches de seguridad actualizados.
- **El shell**: intérprete de línea de comandos que traduce las órdenes del usuario al kernel. Tipos: **Bash** (predeterminado en la mayoría de distribuciones y el más usado en ciberseguridad), csh, ksh, tcsh y zsh.
- **Comunicación con el shell**: **entrada estándar (stdin)** — información enviada al OS; **salida estándar (stdout)** — respuesta del OS; **error estándar (stderr)** — mensajes de error. Comandos básicos: `echo` (emitir texto), `expr` (cálculos), `clear` (limpiar pantalla).

### Módulo 3: Comandos Linux en el shell Bash
- **Sistema de archivos (FHS)**: estructura jerárquica que parte del **directorio raíz (`/`)**; directorios estándar como `/home` (directorios personales), `/bin` (ejecutables), `/etc` (configuración), `/tmp` (temporales, frecuentemente abusado por atacantes) y `/mnt` (medios montados). Se navega con **rutas absolutas** (desde la raíz) o **relativas** (desde el directorio actual, con `.`, `..` y `~`). Los comandos y nombres de archivo **distinguen mayúsculas y minúsculas**.
- **Navegación y lectura**: `pwd` (directorio actual), `ls` (listar contenido), `cd` (cambiar directorio), `whoami` (usuario actual); `cat` (contenido completo), `head`/`tail` (primeras/últimas 10 líneas, ajustable con `-n`), `less` (paginado con avance/retroceso).
- **Filtrado de contenido**: `grep` devuelve líneas que contienen una cadena; la **tubería (`|`)** envía la salida de un comando como entrada de otro (ej. `ls | grep users`); `find` busca archivos por criterios con opciones `-name`/`-iname` (con comodín `*`), `-mtime`/`-mmin` (por tiempo de modificación).
- **Gestión de archivos y directorios**: `mkdir`/`rmdir` (crear/eliminar directorios), `touch`/`rm` (crear/eliminar archivos), `mv` (mover o renombrar), `cp` (copiar); edición con **nano** (`Ctrl+O` guardar, `Ctrl+X` salir); redirección con `>` (sobrescribe) y `>>` (añade al final).
- **Permisos y autorización**: se representan con una **cadena de 10 caracteres** (tipo de archivo + permisos de lectura `r`, escritura `w` y ejecución `x` para **usuario**, **grupo** y **otros**). Se inspeccionan con `ls -l`, `ls -a` (ocultos) y `ls -la`, y se modifican con `chmod` en modo simbólico (`u`/`g`/`o` con operadores `+`, `-`, `=`). Se aplica el **principio de privilegio mínimo**: conceder solo el acceso estrictamente necesario.
- **Autenticación y gestión de usuarios**: la autenticación verifica la identidad del usuario. Ejecutar todo como **root** es mala práctica (riesgo de compromiso, errores irreversibles y falta de trazabilidad); se recomienda **`sudo`**, que otorga privilegios elevados temporales a usuarios autorizados en el **archivo sudoers**. Comandos: `useradd` (crear usuario, con `-g` grupo primario y `-G` grupos suplementarios), `usermod` (modificar: `-a -G` añadir grupos, `-d` directorio personal, `-l` nombre, `-L` bloquear cuenta), `userdel` (eliminar, `-r` borra también su directorio personal) y `chown` (cambiar propietario de usuario o `:grupo`).
- **Obtener ayuda**: la comunidad global de Linux (búsquedas en línea, Unix & Linux Stack Exchange) y el soporte integrado: `man` (página de manual completa), `whatis` (descripción en una línea) y `apropos` (busca comandos por palabras clave, `-a` para combinar varias).

### Módulo 4: Bases de datos y SQL
- **Bases de datos relacionales**: colecciones organizadas de datos en **tablas** relacionadas entre sí, accesibles por múltiples usuarios y capaces de almacenar volúmenes masivos de información. Las tablas tienen **columnas** (campos) y **filas** (registros); se conectan mediante **claves primarias** (valores únicos, no nulos ni duplicados) y **claves foráneas** (columna que es clave primaria en otra tabla). Los valores faltantes se representan como **NULL**.
- **SQL (Structured Query Language)**: lenguaje para crear, interactuar y consultar bases de datos; permite buscar entre millones de registros en segundos, por lo que es esencial para analizar logs de seguridad. Tipos de datos comunes: **cadenas**, **numéricos** y **fecha/hora** (las cadenas y fechas van entre comillas; los números no).
- **Consultas básicas**: `SELECT` (columnas a devolver, `*` para todas) y `FROM` (tabla a consultar), finalizando con `;`; `ORDER BY` ordena resultados de forma ascendente por defecto (`DESC` para descendente, y admite varias columnas).
- **Filtrado**: la cláusula `WHERE` define condiciones con operadores de comparación (`=`, `>`, `<`, `>=`, `<=`, `<>`/`!=`); `LIKE` con los comodines `%` (cero o más caracteres) y `_` (un carácter) busca **patrones**; `BETWEEN ... AND ...` filtra rangos **inclusivos** de números o fechas.
- **Operadores lógicos**: `AND` (ambas condiciones deben cumplirse), `OR` (basta con una) y `NOT` (niega la condición); combinables para filtros complejos (ej. intentos de acceso fallidos fuera del horario laboral).
- **Uniones (JOIN)**: combinan tablas con una columna en común, indicando la coincidencia con `ON tabla.columna = tabla.columna`:
   - `INNER JOIN`: solo las filas coincidentes en ambas tablas.
   - `LEFT JOIN`: todas las filas de la tabla izquierda más las coincidencias de la derecha.
   - `RIGHT JOIN`: todas las filas de la tabla derecha más las coincidencias de la izquierda.
   - `FULL OUTER JOIN`: todos los registros de ambas tablas (con NULL donde no hay coincidencia).
- **Funciones de agregación**: `COUNT` (número de filas), `AVG` (promedio) y `SUM` (suma) calculan sobre conjuntos de datos sin devolver los datos individuales.
- **SQL vs filtrado en Linux**: SQL ofrece resultados estructurados y permite unir tablas, ideal para bases de datos; Linux (grep, find, etc.) es necesario cuando los datos están en archivos de texto no compatibles con SQL. Ambas herramientas se complementan en el análisis de seguridad.
