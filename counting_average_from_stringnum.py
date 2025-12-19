s=input("Enter alphanumeric text: ")
sum =0
count=0
for i in s:
    if i.isdigit():
        sum+=int(i)
        count+=1
print(f'The sum of digit is {sum}')
if count>0:
    avg = sum/count
    print(f'the average is {avg}')
else:
    print("No digit found in the string")