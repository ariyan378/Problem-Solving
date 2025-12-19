str1 = input('Enter your string : ')
result =''

for s in str1:
    if s.isdigit():
        result+=str(s)

print(result)