# program to read from a file and write to another
with open('C:\\MY_FILES\\read_data.txt','r') as my_file:
    content = my_file.read()

with open('C:\\MY_FILES\\write_data.txt','w') as my_file:
    my_file.write(content)