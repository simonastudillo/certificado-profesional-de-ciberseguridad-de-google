# Open, read, and split a text file
with open("login_attempts.txt", "r") as file:
   file_text = file.read()
print(file_text.split())