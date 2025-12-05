
string = input('Enter a string :')
char_to_count = input('Enter a charcater to count :')
count = 0
index = 0

while index<len(string):
    if string[index]==char_to_count:
        count+=1
    index+=1

print(count)    



