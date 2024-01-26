# Count occurrence of a number in a list
# inputs
my_list = [14, 7, 22, 3, 22, 10, 15, 22]
num = 22

# process
count_occur = 0
for item in my_list:
    if item == num:
        count_occur = count_occur + 1

print('Count occurence = ',count_occur)
