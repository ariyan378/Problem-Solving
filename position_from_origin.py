import math
#initializing robot position

x,y = 0,0

#read movement until '!' is encountured 
while True:
    print("! for stop :")

    command = input().strip()#takes input and make multiple string using space

    if command=='!':
        break

    parts = command.split()
    direction=parts[0]
    steps=int(parts[1])

    #updating the position based on direction

    if direction =='up':
        y+=steps
    elif direction =='down':
        y-=steps
    elif direction=="left":
        x-=steps
    elif direction =="right":
        x+=steps

    #calculating euclidean distance from orgin


distance = math.sqrt(x**2+y**2)


#round the result 

result = round(distance)

print(f'The distance is {result}')
        

