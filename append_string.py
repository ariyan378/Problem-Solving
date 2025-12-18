str1 = str(input('Enter your string :'))
str2 = str(input('Enter your string :'))


mid = len(str1)//2
result  = str1[:mid]+str2 +str1[mid:]
print(result)