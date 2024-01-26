# show all printing options
import math

emp_id = 101
emp_name = 'Esam Omar'
emp_salary = 7895453.6782123
print('------ 1. print with concat -------')
print('Emp has id = '+ str(emp_id) +', his name is '+emp_name+',\n\t\ttakes salary = '+ str(emp_salary))
print('------ 2. print with multi parameters -------')
print('Emp has id = ', emp_id, ', his name is ', emp_name, ', takes salary = ',emp_salary)
print(150, 120, 200, 30, sep='-')
for i in range(1, 11):
    print(i, end=' ')
print('\ntest')
print('test2')

print('------ 3. String Formatting using placeholders ---- %s %d %f ---')
print('Emp has id = %d, his name is %s, takes salary = %.2f' %(emp_id, emp_name, emp_salary))

print('------ 4. String Formatting using Format Function ----------')
print('Emp has id = {}, his name is {}, takes salary = {}'.format(emp_id, emp_name, emp_salary))
print('Emp has id = {:d}, his name is {:s}, takes salary = {:,.2f}'.format(emp_id, emp_name, emp_salary))

print('------ 5. String Formatting using F-String function --------')
print(F'Emp has id = {emp_id}, his name is {emp_name}, takes salary = {emp_salary:,.2f}')

# ---------- Numbers Functions accuracy :    round, math.trunc, math.ceil, math.floor
emp_salary = 7895453.2782123
print(f'Using round function, result = {round(emp_salary, 2)}')
print(f'Using round function, result = {round(emp_salary, 2):,.2f}')
print(f'Using trunc function, result = {math.trunc(emp_salary)}')
print(f'Using ceil function, result = {math.ceil(emp_salary) }')
print(f'Using floor function, result = {math.floor(emp_salary)}')