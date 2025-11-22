# taking input from user

n = int(input("Enter Your Number :"))

sum = 0

for i in range(1,n+1):
    sum = sum + i**2

print('Sum : ', sum)    