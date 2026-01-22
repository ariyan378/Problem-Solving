class Fraction:
     
    
    def __init__(self ,x,y):
        self.num = x  # num = numeritor
        self.den = y #den = denominator
        
        
        
    def __str__(self):
        return'{} / {}'.format(self.num,self.den)
    
    def __add__(self , other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den
        
        return "{}/{}".format(new_num,new_den)
    def __sub__(self , other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        
        return "{}/{}".format(new_num,new_den)
    def __mul__(self , other):
        new_num = self.num* other.num
        new_den = self.den*other.den
        
        return "{}/{}".format(new_num,new_den)
    def __truediv__(self , other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        
        return "{}/{}".format(new_num,new_den)
    

num1 = int(input('Enter Numeritor For 1st Fraction :'))    
num2 = int(input('Enter Denominator For 1st Fraction :'))   

 
math1 = Fraction(num1,num2)

num1 = int(input('Enter Numeritor For 2nd Fraction :'))    
num2 = int(input('Enter Denominator For 2nd Fraction:')) 
math2 = Fraction(1,2)

print(math1+math2)
        