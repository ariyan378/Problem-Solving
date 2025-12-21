char = input('Enter your string :')
seen_charcater = set()
new_string = ''
for c in char:
    if c not in seen_charcater:
        new_string+=char
        seen_charcater.add(char)
  
print(f'The new string is {new_string}')    