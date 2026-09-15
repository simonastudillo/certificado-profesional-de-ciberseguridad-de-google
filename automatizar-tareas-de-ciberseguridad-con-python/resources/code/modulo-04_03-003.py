# Parse information from a log file if the status code != 200
# def parse_line(line) # Error de sintaxis: falta el signo de dos puntos al final de la definición de la función
def parse_line(line):
   error_code = line[0:3]
   date = line[4:12]
   time = line[13:21]
   # aplication_name = line[22:43] # Error de sintaxis: 'aplication_name' no está definido correctamente, debería ser 'application_name'
   application_name = line[22:43]

   if (error_code == "200"):
      return "Successful event - no parsing needed."

   parsed_line = []
   parsed_line.insert(0, error_code)
   parsed_line.insert(1, date)
   parsed_line.insert(2, time)
   parsed_line.insert(3, application_name)

   return parsed_line

   # if (error_code == "200"):
   #    return "Successful event - no parsing needed." # Error lógico: la sentencia if está después de la sentencia return, por lo que nunca se ejecutará. Debería estar antes de la sentencia return para que se ejecute correctamente.

final_parsed_line = parse_line("200 02082022 05:11:00 buffer_application")
print(final_parsed_line)