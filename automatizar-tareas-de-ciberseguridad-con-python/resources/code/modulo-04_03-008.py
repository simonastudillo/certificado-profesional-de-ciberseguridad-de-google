new_users = ["sgilmore", "bmoreno"]
approved_users = ["bmoreno", "tshah", "elarson"]
def add_users():
    for user in new_users:
        print("line 5 - inside for loop")
        if user in approved_users:
            print("line 7 - inside if statement")
            print(user,"already in list")
        print("line 9 - before .append method")
        approved_users.append(user)
add_users()
print(approved_users)
# line 5 - inside for loop
# line 9 - before .append method
# line 5 - inside for loop
# line 7 - inside if statement
# bmoreno already in list
# line 9 - before .append method
# ['bmoreno', 'tshah', 'elarson', 'sgilmore', 'bmoreno']