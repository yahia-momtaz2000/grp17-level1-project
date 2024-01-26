# Using Lists
print('---- 1. Creating, Printing List ---- ')
numbers_list = [7, 12, 8, 20, 9, 14, 9]
print(numbers_list)
print( type(numbers_list) )

print('---- 2. adding element to list [ append function , insert function ] --- ')
numbers_list.append(11)
numbers_list.insert(1, 77)
print(numbers_list)

print('---- 3. Access element by index and change it -----')
print(numbers_list[4])
numbers_list[4] = 22 # change it
print(numbers_list)

print('----- 4. count elements of list _ Len function : General Function -------')
print(  len(numbers_list) )

print('-------- 5. delete element from the list -- remove , pop functions -----')
numbers_list.remove(9) # delete the element 9
numbers_list.pop(4) # delete at index 4 = 22  # numbers_list.pop() : remove last element
print(numbers_list)
del(numbers_list[4])
print(numbers_list)

print('-------- 6. reverse list ----------')
numbers_list.reverse()
print(numbers_list)

print('------- 7. sort list -------------')
# numbers_list.sort()
numbers_list.sort(reverse= True)
print(numbers_list)

