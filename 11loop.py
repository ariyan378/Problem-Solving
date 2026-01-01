
vowels = "aeiou"
word = "aaaaaaaa"
count = 0 ;

for char in word:
    if char in vowels:
        count = count +1

print(f"Total  vowels in {word} is {count}")
