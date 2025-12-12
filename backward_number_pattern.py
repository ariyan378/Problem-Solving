
row = 5
if row <=15:
    for i in range(1,row+1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print()
else:
    print("High row value!")