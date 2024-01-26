# show strings functions
print('---- Create and print string ----')
emp_name = 'Yahia Momtaz'
print(emp_name)
print(type(emp_name))

print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(upper_emp_name)
print(lower_emp_name)
print(emp_name)

print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(upper_emp_name.isupper())
print(lower_emp_name.islower())
print(emp_name.isalpha())   # characters
print(emp_name.isalnum()) # characters or numbers

print('-------------- endsWith() function -----------------')
file_path = 'c:/My_Documents/egypt.pDF'
file_path = file_path.lower() # lower the file path
if file_path.endswith('pdf'):
    print('it is a book')
elif file_path.endswith('jpg') or file_path.endswith('png'):
    print('it is an image')
else:
    print('unknown file type')

print('-------------- startswith() function ---------')
emp_mobile = '+201247897979'
if emp_mobile.startswith('+20'):
    print('it is egypt mobile')
elif emp_mobile.startswith('+966'):
    print('it is saudi mobile')
else:
    print('unknown country code')

print('------ in membership --------------')
emp_cv = 'iam a programmer, i am interest in python, java c++'
if 'python' in emp_cv and 'java' in emp_cv:
    print('This emp is the wanted one')
else:
    print('This is not the required emp')

print('-------------- count function -----------')
emp_cv = 'iam a programmer, i am interest in python, java c++, python, python'
print(   emp_cv.count('python')  )


print('---------- index(),  replace() functions |  slicing---------------')
emp_email = 'yahia.momtaz@gmail.com'
user_name = emp_email[0 : emp_email.index('@') ]
domain_name = emp_email[ emp_email.index('@') + 1  :   ]
real_name = user_name.replace('.',' ')
print(user_name, domain_name, real_name)

print('--------------- Looping :  Loop over letters of string -----------------------')
# foreach with string
for letter in emp_email:
    print(letter)
print('------ for i with string ----')
for i in range(len(emp_email)):
    print(emp_email[i])

print('------- Split function the String into List of Words -------')
my_courses = 'java python oracle linux network'
courses_list = my_courses.split()
courses_list.reverse()
print(courses_list)

print('------ return the list back to string using join() function --------')
new_courses = ' '.join(courses_list)
print(new_courses)



print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')

print('test', end=' ')
print('new test')
