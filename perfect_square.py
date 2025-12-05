num = int(input('Enter your number :'))

i = 1
is_perfect= False

while i*i<=num:
    if i*i==num:
        is_perfect=True
        break
    i+=1

if is_perfect:
    print(f'{num} is a perfect square')

else:
    print(f'{num} is not  perfect square')
    