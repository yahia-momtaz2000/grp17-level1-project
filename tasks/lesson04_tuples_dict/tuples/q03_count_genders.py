# Count and print no. of Male, no. of Female in the list of Tuples
company_employees = [
(101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
(102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
(103, 'Adham Aly', 5000.0, 'Engineer','M'),
(104, 'Islam Hassan', 7000.0, 'Sales','M'),
(105, 'Marwa Esam', 7000.0, 'Marketer','F'),
(106, 'Ola Hassan', 7000.0, 'Engineer','F')
]
count_male, count_female = 0, 0
for employee in company_employees:
    if employee[4] == 'M':
        count_male = count_male + 1
    elif employee[4] == 'F':
        count_female = count_female + 1

print('Count Male = ', count_male)
print('Count Female = ', count_female)
