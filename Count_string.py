word = input('Enter your Sentence :')
vowel = 'aeiou'
count = 0
index = 0

while index<len(word):
    if word[index].lower()  not in vowel and word[index].isalpha():
        count+=1
    index+=1

print(f"The number of consonant is {count}")        




