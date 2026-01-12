lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
 
output = [] 
for x in lst1:
    if x in lst2:
        output.append(x)

print(f"Output is {output}")        
