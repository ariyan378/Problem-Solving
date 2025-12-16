print("===Decimal TO Number===")
decimal =int(input('Enter a decimal :'))

binary =''
num = decimal

if num ==0:
    binary='0'
else:
    while num>0:
        remainder = num%2
        binary=str(remainder)+binary
        num=num//2
print(f"The binary equivalent is {binary}")            

