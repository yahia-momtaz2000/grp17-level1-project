# program to check for even | odd :
# %  mod  modulos  remainder باقى القسمة

print( 4 / 2) # divide = 2
print( 4 % 2 ) # mod remainder = 0
print ( 11 % 2 ) # 1
print( 437 % 3 ) # 2
# 14 months :  how many years - how many remaining months ?
print('Years ', int(14 / 12)   )
print('Remaining Months ', 14 % 12)

num = 0
if num == 0:
    print('This no is Zero')
elif num % 2 == 0:
    print('It is even no.')
else:
    print('It is odd no.')