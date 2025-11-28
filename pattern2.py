#1
#12
#121
#12321
#1234321

row = int(input('Enter Your Number : '))

for  i in range (1,row+1):
    for j in range(1,i+1):
        print(j, end='')
    for k in range(i-1,0,-1):
        print(k, end='')

    print()   