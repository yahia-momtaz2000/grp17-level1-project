# find if a no. is found in list - print its first index
# or print .. no. is not found using a Else Loop
my_list = [14, 5, 22, 10, 30]
num = 24

for item in my_list:
    if num == item:
        print('No. is found at index = ', my_list.index(num))
        break
else:
    print('No is not found')
