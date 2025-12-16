
num1 = int(input('Enter your 1st number :'))
num2 = int(input('Enter your 2nd number :'))

a = num1
b = num2

while b != 0:
    temp = b
    b = a%b
    a = temp

hcf = a
lcm = (num1*num2)//hcf

print(f"The hcf is {hcf}")
print(f"The lcm is {lcm}")

