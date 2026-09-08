# Assign `system` to a specific operating system
# This variable represents which operating system is running

system = "OS 1"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if either OS 1 or OS 3 is running, display a "update needed" message

if system == "OS 2":
   print("no update needed")
elif system == "OS 1" or system == "OS 3":
   print("update needed")
    