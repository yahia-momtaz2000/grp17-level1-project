# reverse words
# Ex No. 5 : #  program to reverse a string words
statement = "i like this program very much"

#1. convert string to List using split function
words_list = statement.split()

#2. reverse the list
words_list.reverse()

#3. convert list to String
statement = ' '.join(words_list)
print(statement)