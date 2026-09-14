# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# First line of the `with` statement
# Use `open()` to import security log file and store it as a string

with open(import_file, 'r'):