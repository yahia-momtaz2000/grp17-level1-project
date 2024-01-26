# program to check for person age
# inputs
person_name = 'Yahia Momtaz'
person_age = input('Please Enter your age ')
person_age = int(person_age)

# processing [ calculation ]
if person_age > 16:
    print('You are a man')
# elif person_age >= 11 and person_age <= 16:
elif person_age >= 11:
    print('You are a boy')
else:
    print('You are a child')