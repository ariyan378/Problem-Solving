N = int(input("Enter your number :"))
num = 1
total = 0

while num<=N:
    if num % 5 !=0:
        if total+num >300:
            break
        total = total+num
    num+=1


print(total)    


