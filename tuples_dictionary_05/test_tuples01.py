# program to show tuples
print('---- create and print tuple -----')
person_tuple = (101, 'Ahmed Esam', 7000.0, 'Cairo')
print(person_tuple)
print(type(person_tuple))

print('---------- access element in a tuple by index -------------')
print(person_tuple[1])
# person_tuple[1] = 'Mostafa' # Error : Tuple is immutable

print('------------ un packing tuple ----- ')
id, name, salary, address = person_tuple
print('id = ', id)

print('------ Loop over Tuple -------')
for item in person_tuple:
    print(item)




