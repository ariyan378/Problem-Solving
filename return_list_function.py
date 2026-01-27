# ### **`Problem-1:`** Write a Python function that takes a list and returns a new list with unique elements of the first list.



# Input:

# [1,2,3,3,3,3,4,5]

# Output:

# [1, 2, 3, 4, 5]

def unique_list(inputlist):
    
    unique =[]
    
    for i in inputlist:
        
        if i not in unique:
            
            unique.append(i)
        else :
            continue
    return unique    

my_list = [1,2,3,3,3,3,4,5]

print(unique_list(my_list))         