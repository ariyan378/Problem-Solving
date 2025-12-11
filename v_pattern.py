row = int(input("Enter Your row number :"))

if row<=15:
    for i in range(1,row-1):
        for j in range(i):
            print("*" , end=' ')
        print()    
    for i in range(row-1,0,-1):
        for j in range(i):
            print("*" , end=' ')
        print()    
else:
    print("Too high row number")                    
