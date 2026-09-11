# Return information from a funcion
def calculate_fails(total_attempts, failed_attempts):
   fail_percentage = failed_attempts / total_attempts
   return fail_percentage

percentage = calculate_fails(4, 2)
if (percentage >= 0.5):
   print("Account locked")