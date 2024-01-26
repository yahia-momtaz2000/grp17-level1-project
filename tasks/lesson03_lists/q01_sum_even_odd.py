# No. 1: # get the sum, count of even numbers, odd numbers from a list
# input
my_list = [14, 7, 2, 3, 22, 10, 15]

# process
sum_even, sum_odd, count_even, count_odd = 0, 0, 0 , 0
for item in my_list:
    if item % 2 == 0:
        sum_even = sum_even + item
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + item
        count_odd = count_odd + 1

# output
print('Sum Even = ', sum_even,' | Count Even = ', count_even)
print('Sum Odd = ', sum_odd,' | Count Even = ', count_odd)