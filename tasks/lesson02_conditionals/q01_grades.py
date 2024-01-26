# Solve Grades apprev.
# input
grade_apprev = 'GG'

if grade_apprev == 'A':
    grade = 'Excellent'
elif grade_apprev == 'B':
    grade = 'V. Good'
elif grade_apprev == 'C':
    grade = 'Good'
elif grade_apprev == 'D':
    grade = 'Pass'
elif grade_apprev == 'E':
    grade = 'Fail'
else:
    grade = 'Invalid grade'

# output
print('Grade Apprev = ', grade_apprev, ' | grade = ', grade)