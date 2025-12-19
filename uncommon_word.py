A = "apple banana mango"
B = "banana fruits mango"

words_A = A.split()
words_B = B.split()

result = []

# Check words from A
for word in words_A:
    count = 0
    # Count how many times word appears in A
    for w in words_A:
        if w == word:
            count = count + 1
    
    # Check if word appears in B
    found_in_B = False
    for w in words_B:
        if w == word:
            found_in_B = True
    
    # If appears once in A and not in B, add to result
    if count == 1 and found_in_B == False:
        result.append(word)

# Check words from B
for word in words_B:
    count = 0
    # Count how many times word appears in B
    for w in words_B:
        if w == word:
            count = count + 1
    
    # Check if word appears in A
    found_in_A = False
    for w in words_A:
        if w == word:
            found_in_A = True
    
    # If appears once in B and not in A, add to result
    if count == 1 and found_in_A == False:
        result.append(word)

print(result)  # ['apple', 'fruits']