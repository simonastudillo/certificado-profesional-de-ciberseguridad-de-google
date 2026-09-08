# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device

if username in approved_list:
   print("This user has access to this device.")

else:
   print("This user does not have access to this device.")

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours

organization_hours = True

# If the entered `organization_hours` has a value of True, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."

if organization_hours == True:
   print("Login attempt made during organization hours.")
else:
   print("Login attempt made outside of organization hours.")
    