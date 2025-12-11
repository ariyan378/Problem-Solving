row = int(input("Enter your row number Between 1-15 :"))

if row <=15:
    for i in range(1,row + 1):
        for j in range(row-i):
            print(' ', end=' ')
        for k in range(2*i-1):
            print('*',end=' ')    
        print()
else:
    print("High number!!Please Try Again")        