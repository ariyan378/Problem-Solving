# ### Write OOP classes to handle the following scenarios:

# - A user can create and view 2D coordinates
# - A user can find out the distance between 2 coordinates
# - A user can find find the distance of a coordinate from origin
# - A user can check if a point lies on a given line
# - A user can find the distance between a given 2D point and a given line


class Point:
    
    def __init__(self , x , y):
        self.x = x 
        self.y = y
    
    def __str__(self):
        return '<{},{}>'.format(self.x,self.y)
    
    def euclidean(self , other):
        
        return ((self.x - other.x)**2+(self.y-other.y)**2)**0.5    
    
    def distance_from_origin(self):
        return (self.x**2+self.y**2)**0.5
    
    
class Line :
    
    def __init__(self,A,B,C):
        self.A = A 
        self.B = B 
        self.C= C
        
    def __str__(self):
        
        return '{}x + {}y + {()}'.format(self.A,self.B,self.C)
    
    def point_on_lines(line,point):
        if line.A*point.x + line.B*point.y+line.C == 0:
            return 'Yes ! Lies On The Line'
        else:
            'No!! Not Lies On The Line'
    
    def shortest_distance (line,point):
        return abs((line.A*point.x + line.B*point.y + line.C)/(line.A**2 + line.B**2)**0.5)        
            
        
l1 = Line(1,1,-2)
p1 = Point(1,1)
p2 = Point(4,6)
print(p1.euclidean(p2))
print(p1.distance_from_origin())
print(l1.shortest_distance(p1))
print(l1.point_on_lines(p1))
        