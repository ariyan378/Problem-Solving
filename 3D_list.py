L = [[[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]]]

print(L[0][1][0])

print(L[0][1][:])#for every D , 1[] needed

s = [13,14,15]
i = [16,17,18]
j = [19,20,21]

L[1].append(s)
#we can append in multidimension list using indexing
print("After Appending ")
print(L)

L[1].extend([i])
#we can expand multiple item as a single list item using []
print("After Extending ")
print(L)

L[1].insert(4,j)
#we can insert any list ,location will need to give first then the item we want to add
print("After Inserting ")
print(L)