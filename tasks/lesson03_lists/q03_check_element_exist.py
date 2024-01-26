# Check if an element exists in a list in Python
# find all occurences and put them in a list
my_list = [14, 7, 22, 3, 22, 10, 15, 22]
num = 8
indexes_list = []

is_found = False
for i in range(len(my_list)):
   if num == my_list[i]:
        indexes_list.append(i)
        is_found = True

if is_found:
    print('item is found on indexes : ',indexes_list)
else:
    print('item is not found')