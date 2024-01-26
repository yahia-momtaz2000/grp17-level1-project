# program to search for item in a list or not - if found print its index -
# if not found  : print it is not found in the list
my_list = [14, 5, 2, 3, 7, 8, 7, 9, 7, 12, 2]
num = 7
indexes_list = []

is_found = False  # Flag : data type [    boolean    ]
for i in range( len(my_list) ): # for i loop index
    if num == my_list[i]:
        is_found = True
        required_index = i
        indexes_list.append(i)
        # break

if is_found == True:
    # print('Number is found in the list, at index = ', required_index)
    print('Number is found in the list, at index = ', indexes_list)
else:
    print('Number is not found in the list')
