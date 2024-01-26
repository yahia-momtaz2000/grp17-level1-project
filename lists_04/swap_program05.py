newList = [12, 35, 9, 56, 24]
print(newList)
temp = newList[0]	# 12
newList[0] = newList[-1] # 24
newList[-1] = temp

print(newList)