s = input("Enter Your String :")
L = []
temp = ''

for i in s:
    if i != ' ':
        temp += i
    else:
        L.append(temp)  # Fixed: was L.append(L)
        temp = ''

if temp:  # Only append if temp is not empty
    L.append(temp)

print(L)

