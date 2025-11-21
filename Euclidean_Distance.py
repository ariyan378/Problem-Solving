# Taking Input From User

import math

x1 = int(input("Enter Your Number : "))
x2 = int(input("Enter Your Number : "))

y1 = int(input("Enter Your Number : "))
y2 = int(input("Enter Your Number : "))
# Applying  formula
a = ((x1-x2)**2 + (y1-y2)**2)
final = math.sqrt(a) # aleranative final = a **(1/2)

# printing
print("Euclidean  DisTance : " , final)