# Assign `system` to a specific operating system as a string

system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of operating system

patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement that checks which operating system is stored in `system` and displays a message showing the corresponding patch date 

if system == "OS 1":
    print("Patch date:", patch_schedule[0])

elif system == "OS 2":
    print("Patch date:", patch_schedule[1])

elif system == "OS 3":
    print("Patch date:", patch_schedule[2])