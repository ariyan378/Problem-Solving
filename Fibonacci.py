a = 1
b = 2

print(a)
print(b)
# already printed 2 terms, need 8 more

for i in range(8):
    next = a+b
    print(next)
    a=b
    b=next