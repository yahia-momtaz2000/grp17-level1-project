# program to validate password
"""
1. length > 8 letters
2. upper letters >= 1   lower letters >= 1
3. digits >= 1          special characters >= 1
"""
password = 'ASDASDs@#@dfdsAS2023'
count_upper, count_lower, count_digits, count_special = 0,0,0,0
if len(password) > 8:
    # validate letters : Loop over the string [ loop over letter by letter ]
        for letter in password:
           if letter.isupper():
               count_upper = count_upper + 1
           elif letter.islower():
               count_lower = count_lower + 1
           elif letter.isdigit():
               count_digits = count_digits + 1
           elif not letter.isalnum():
               count_special = count_special + 1

       # check for all counters ; if all > 1 then pass is valid
        if count_upper > 0 and count_lower > 0 and count_digits > 0 and count_special > 0:
            print('Password is valid')
        else:
            print('Password is not Valid for letters validation')
else:
    print('Not valid password - len must be > 8 characters')