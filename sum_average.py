# Write code here

num = int(input('Enter your Number :'))
sum = 0
count = 0
while num !=0:
    sum+=num
    count +=1
    num = int(input('Enter your Number :'))

print(f"total sum {sum}")
average = sum /count
print(f"Average{average}")

