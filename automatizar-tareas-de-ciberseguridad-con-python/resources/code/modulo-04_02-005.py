approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)
# before .split(): elarson,bmoreno,tshah,sgilmore,eraab
# after .split(): ['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab']