# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
# This loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100

while i <= 5150: 
   print(i)
   if i == 5100:
      print("Only 10 valid employee ids remaining")
   i = i + 5
# Resultado:
# 5000
# 5005
# 5010
# 5015
# 5020
# 5025
# 5030
# 5035
# 5040
# 5045
# 5050
# 5055
# 5060
# 5065
# 5070
# 5075
# 5080
# 5085
# 5090
# 5095
# 5100
# Only 10 valid employee ids remaining
# 5105
# 5110
# 5115
# 5120
# 5125
# 5130
# 5135
# 5140
# 5145
# 5150