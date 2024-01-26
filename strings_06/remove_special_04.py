#Ex No. 4 : #  Remove all special characters except letters and numbers

statement = "123abcjw:, .@! eiw"
new_statement = ''
for letter in statement:
    if letter.isalnum():
        new_statement = new_statement + letter

statement = new_statement
print(new_statement)
print(statement)
