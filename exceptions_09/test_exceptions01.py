# to show how to handle exceptions
try:
    first_number = int( input('please enter first number : ') )
    second_number = int ( input('please enter second number : ') )

    result = first_number / second_number
    print('Result = ', result)
    open('C:\\my_files\\edu.txt')
except ValueError:
    print('please only enter numbers')
except ZeroDivisionError:
    print('Cannot divide by Zero')
finally:
    print('This is the finally statement - works any time')

print('Continue or End the program')