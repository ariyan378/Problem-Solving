string = input('Enter your string :')
splited = string.split()
word = input('Enter your word you want to search :')
count = 0 

for s in splited:
    if s!=word:
        count+=1
    if s==word:
        count+=1
        break 

print(f'The position of the word is {count}')
