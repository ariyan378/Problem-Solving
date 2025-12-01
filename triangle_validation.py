#taking angle from user :

angle1 = int(input('Enter your angle :'))
angle2 = int(input('Enter your angle :'))
angle3 = int(input('Enter your angle :'))

#applying logic

if (angle1+angle2+angle3==180) and angle1>0 and angle2>0 and angle3>0:
    print("Yes! It is a triangle ")
else :
    print("Not a trianle")    