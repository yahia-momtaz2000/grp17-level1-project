# create 4 functions:
# 1.  sum_numbers with 2 parameters : return the result of adding these numbers
# 2.  multiply_numbers with 3 parameters : return the result of multiply these numbers
# 3.  abs_numbers with 1 parameter : check if the numbers is -ve : return the +ve value
# 4. divide_numbers with 2 parameters : return the result of division
#     check the second numbers is not Zero
import math


def sum_numbers(x, y = 22):
    """
    this function to sum 2 numbers x and y
    :param x: the first parameter
    :param y: the second parameter
    :return: the sum of the 2 numbers
    """
    sum = x + y
    return sum

# main program


res = sum_numbers(5, 3) # positional  x = 5,  y = 3
print(res)

value = 70
res = sum_numbers(y= 7, x = value) # named argument  x   y
print(res)

res = sum_numbers(5)
print(res)

print(res, end=' ')  # named parameter  end
my_list = [14, 5, 2, 5, 7]
my_list.sort(reverse=True) # named parameter   reverse


