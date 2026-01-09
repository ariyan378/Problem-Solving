def is_even(num):
    '''
    Docstring for is_even
    
    return a number is even or odd
    input type : any valid integer
    output : Even/odd

    :param num: Description
    
    '''
    if type(num)==int:
        if num%2==0:
            return 'This is a  Even Number'
        else:
            return 'This is a odd Number'
    else:
        return 'Wrong DataType....Only Integer Allowed'

Name =is_even('Himuuuuu')
print (Name)

for i in range(1,11):
    x = is_even(i)
    print(x)    