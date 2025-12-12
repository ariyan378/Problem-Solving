x  = int(input("Enter your value of x :"))
n  = int(input("Enter your value of n :"))

sum = 0.0

if n <0:
    print("Error: n must be non negative integer")
    sum = None
elif n == 0:
    sum = 0.0
else:
    sum= 1.0
    for i in range(2,n+1):
        sum+=(x**i)/i

if sum is not None:
    print(f"The sum of  the series till the {n} th term is :{sum}")



