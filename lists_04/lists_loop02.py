print('--- 1. For i loop [ use list index ] ----------')
numbers_list = [7, 12, 8, 20, 9, 14, 9]
# use index
sum_list = 0
for i in range( len(numbers_list)):
    print(i, numbers_list[i])
    sum_list = sum_list + numbers_list[i] # accumulative sum equation
print('Sum of elements = ',sum_list)

print('--------- 2. For each loop [ for in loop ] : Donot use list index ---------')
sum_list = 0    # reset variable
for item in numbers_list:
    print(item)
    sum_list = sum_list + item
print('Sum of elements = ', sum_list)

print('=========== using General function sum() ===========')
print(sum(numbers_list))
