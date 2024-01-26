# Ex No. 3 : conditional equation
# Write a program to ask the user for the operator
# Then ask the user to enter two values
# Print the result of the equation according to the user input

# ask the user for inputs
first_number = int( input('Enter the first number ') )
second_number = int( input('Enter the second number ') )
operator = int( input('Enter the operator | 1 for + , 2 for -, 3 for *, 4 for / ') )
print('The final equation with result is : ')
if operator == 1:
    final_result = first_number + second_number
    print(first_number, '+', second_number, ' = ', final_result)
elif operator == 2:
    final_result = first_number - second_number
    print(first_number, '-', second_number, ' = ', final_result)
elif operator == 3:
    final_result = first_number * second_number
    print(first_number, '*', second_number, ' = ', final_result)
elif operator == 4:
    final_result = first_number / second_number
    print(first_number, '/', second_number, ' = ', final_result)
else:
    print('Invalid Operator')