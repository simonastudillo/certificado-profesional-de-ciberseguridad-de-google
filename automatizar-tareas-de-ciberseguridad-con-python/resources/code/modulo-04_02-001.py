# Open a text file
with open("ip_addresses.txt", "r") as file:
   file_text = file.read()
print(file_text)