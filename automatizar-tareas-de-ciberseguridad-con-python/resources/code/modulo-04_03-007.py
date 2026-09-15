new_users = ["sgilmore", "bmoreno"]
approved_users = ["bmoreno", "tshah", "elarson"]
def add_users():
    for user in new_users:
        if user in approved_users:
            print(user,"already in list")
        approved_users.append(user)
add_users()
print(approved_users)
# bmoreno already in list
# ['bmoreno', 'tshah', 'elarson', 'sgilmore', 'bmoreno']