s = input("Enter Your String :")
L=[]

for i in s.split() :
    L.append(i[0].upper() + i[1:].lower())

print(' '.join(L))