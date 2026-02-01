# Q1:Count number of instances of a class created in Python?
# Example: Say Car is any class.

# maruti = Car()
# bmw = Car()
# honda = Car()
# So after creating above instances. We want to count how many instances are created of Car class.

# For above example no of instances = 3.

# Write a program for above problem.

class Car:
    
    __counter = 0
    
    def __init__(self):
        Car.__counter +=1
        
    def show():
        
        return Car.__counter
    
c1 = Car()        
c2 = Car()        
c3 = Car()        
c4 = Car() 

print(Car.show())