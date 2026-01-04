list = [2,4,6,10,1]

result=[]

for i in  list:
    sum = 0
    for j in list:
        if j>=i:
            sum+=j
    result.append(sum)        


print(result)