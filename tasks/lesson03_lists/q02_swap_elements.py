#2: Create a program to swap 2 elements at given positions
#inputs
my_list = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print('Original = ', my_list)
#swapping
temp = my_list[pos1]
my_list[pos1] = my_list[pos2]
my_list[pos2] = temp

print('After Swapping = ', my_list)