# Find the Max and Min element from a list
my_list = [14, 7, 48, 3, 22, 10, 15, 22]

max = my_list[0]
min = my_list[0]

for item in my_list:
    if item > max:
        max = item

    if item < min:
        min = item

print('Max = ', max)
print('Min = ', min)
