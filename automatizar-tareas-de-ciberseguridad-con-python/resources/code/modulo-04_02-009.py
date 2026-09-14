approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)
approved_users = ",".join(approved_users)
print("after .join():", approved_users)
# before .join(): ['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab']
# after .join(): elarson,bmoreno,tshah,sgilmore,eraab