# use function print_numbers() : to print numbers from 1 to a specific num
# User Defined Function - Sub Program
def print_numbers(max_num):
    sum = 0
    for i in range(1, max_num + 1):
        print(i, end =' ')
        sum = sum + i
    print()  # to print enter a new line
    return sum

# main program
print('start main program')
# Calling function : to print numbers 1 : 10
z = print_numbers(10)
print(z)