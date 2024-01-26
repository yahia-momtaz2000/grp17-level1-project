# program to show employee data
emp_id = 101            # int data type
emp_name = 'Ahmed Amr'  # string data type
emp_salary = 7000.55     # float data type
emp_job = 'Python Developer'    # string data type

# concat  :   Ahmed Amr Works as Python developer
print(emp_name + ' work as '+emp_job)

# concat : Ahmed Amr id = 101
print('--------- Convert from data type to another [ Casting ]  -----------')
print('----------- convert from int, float to str -----------')
print(emp_name + ' id = '+ str(emp_id)  )
print(emp_name + ' takes salary = '+ str(emp_salary) )

print('---------- Casting from float to int -----------')
print(emp_salary)
print(int(emp_salary))  # remove fraction