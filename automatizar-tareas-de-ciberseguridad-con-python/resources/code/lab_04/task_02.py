# Create a variable called `connection_attempts` that stores the number of times the user has tried to connect to the network

connection_attempts = 3

# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`

for i in range(connection_attempts):
   print("Connection could not be established.")
# Resultado:
# Connection could not be established.
# Connection could not be established.
# Connection could not be established.