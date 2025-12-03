#Taking input form user 
n = int (input('Enter Your number :'))
total = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    total = total + i / fact

print(total)