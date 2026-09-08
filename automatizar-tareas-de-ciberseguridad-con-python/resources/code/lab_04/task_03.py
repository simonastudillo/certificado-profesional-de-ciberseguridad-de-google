# Assign `connection_attempts` to an initial value of 0, to keep track of how many times the user has tried to connect to the network

connection_attempts = 0

# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." every iteration, until connection_attempts reaches a specified number

while connection_attempts < 3:
   print("Connection could not be established.")

   # Update `connection_attempts` (increment it by 1 at the end of each iteration) 
   connection_attempts = connection_attempts + 1
# Resultado:
# Connection could not be established.
# Connection could not be established.
# Connection could not be established.