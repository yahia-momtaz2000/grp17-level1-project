# program to write into text file
"""
1. open for write
2. write
3. close
"""
print('------ first way -----')
my_file = open('C:\\MY_FILES\\write_data.txt', 'w')
my_file.write('I Like programming\n')
my_file.write('I Like Football\n')
my_file.write('Python is a Programming Language')
my_file.close()

print('-------- second way --------- using with ---')
with open('C:\\MY_FILES\\write_data.txt', 'a') as my_file:
    my_file.write('\n')
    my_file.write('My City is Cairo\n')
    my_file.write('My City is Alex\n')
    my_file.write('Iam a SW Engineer')



