# program to write list into a file
my_list = ['Luxor', 'Cairo', 'Alex', 'Cairo']
output_file = 'C:\\MY_FILES\\write_data.txt'

with open(output_file, 'w') as my_file:
    for i in range(len(my_list)):
        if i == len(my_list) - 1: # the last element
            my_file.write(my_list[i])
        else:
            my_file.write(my_list[i]+'\n')