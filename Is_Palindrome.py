string = input("Enter Your String :")
flag = True

for i in range (0,len(string)//2):
    if string[i]!=string[len(string)-i-1]:
        print('The number is not palindrome')
        break

if flag:
    print("Yes! is is a plaindrome")

