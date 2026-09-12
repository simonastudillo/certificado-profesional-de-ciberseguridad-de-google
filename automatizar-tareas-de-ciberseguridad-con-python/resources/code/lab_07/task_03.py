# Assign `employee_id` to a four digit number as an initial value

employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string

employee_id = str(employee_id)

# Display the `employee_id` as it currently stands

print(employee_id)

# Conditional statement that updates the `employee_id` if its length is less than 5 digits

### YOUR CODE HERE ###:
if len(employee_id) < 5:
    employee_id = "E" + employee_id

# Display the `employee_id` after the update
    
### YOUR CODE HERE ###
print(employee_id)
