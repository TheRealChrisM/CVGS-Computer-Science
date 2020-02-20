#Christopher Marotta
#Lab E Part 3 (Point Class)

class Point:
    #Constructs the point object.
    def __init__(self,xCord=0,yCord=0):
        self.__x = xCord
        self.__y = yCord

    #Returns the X-value of the point.
    def getX(self):
        return self.__x

    #Returns the Y-value of the point.
    def getY(self):
        return self.__y

    #Calculates the distance between the two points.
    def distance(self, otherPoint):
        ySquared = (otherPoint.getY() - self.getY())**2
        xSquared = (otherPoint.getX() - self.getX())**2
        numsSquaredAdded = xSquared + ySquared
        totalDistance = numsSquaredAdded**(1/2)
        return totalDistance
    
    #Outputs whether the points have a distance less than 5.
    def isNearBy(self, p1):
        nearBy = False
        if (self.distance(p1)<5):
            nearBy = True
        return nearBy
    
    #Overloads str function to allow printing the object.
    def __str__(self):
        return ("("+str(self.getX())+","+str(self.getY())+")")
    
#Asks user to input 2 points.
x1 = eval(input("Please enter the X-value for Point 1: "))
y1 = eval(input("Please enter the Y-value for Point 1: "))
x2 = eval(input("Please enter the X-value for Point 2: "))
y2 = eval(input("Please enter the Y-value for Point 2: "))

#Constructs Point class based on input.
p1 = Point(x1,y1)
p2 = Point(x2,y2)

#Displays the distance between the two points.
print("The distance between the two points is " + str(format(p1.distance(p2), ".2f")))

#Displays whether the points are close to each other.
if (p1.isNearBy(p2)):
    print("The two points are near each other.")
else:
    print("The two points are not near each other.")
