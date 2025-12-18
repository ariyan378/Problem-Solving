String = input("Enter your string :")
words = String.split()
result =''

for word in words :
    if word:
        result+= word[0].upper()

print(f"The result is {result}")        