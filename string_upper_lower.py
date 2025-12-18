str1='PyNaTive'

upper=''
lower=''

for s in str1:
    if s.isupper():
        upper +=s
    else:
        lower+=s

result = lower+upper
print(result)