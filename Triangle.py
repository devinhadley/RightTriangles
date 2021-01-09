import turtle
from formulas import pythag
from math import sqrt, atan, degrees, radians, tan, sin, cos


class RightTriangle():
    
    def __init__(self,a=None, b=None , c=None):
        self.a = a
        self.b = b
        self.c = c
        

        if self.a == None:
           self.a = pythag('a',side_b=self.b, side_c=self.c)
        elif self.b == None:
            self.b =  pythag('b',side_a=self.a,side_c=self.c)
        elif self.c == None:
            self.c = pythag('c', side_a=self.a, side_b=self.b)

        self.angle_a= degrees(atan(self.a/self.b))
        self.angle_b = degrees(atan(self.b/self.a))
 


    def printAngles(self):
        print("Angle A: "+str(self.angle_a))
        print("Angle B: "+str(self.angle_b))


    def showShape(self, multiplier=10):
        board = turtle.Turtle()
         
        board.forward(self.b * multiplier) # draw base
          
        board.left(90)
        board.forward(self.a * multiplier)
           
        board.left(180 - degrees(atan(self.b/self.a)))
        board.forward(self.c * multiplier)
        turtle.done()

    def printSides(self):
        print("Side A: "+str(self.a))
        print("Side B: "+str(self.b))
        print("Side C/Hypotenuese: "+str(self.c))

    def cos(self, angle):
        if angle == 'a' or angle == 'A':
            active_angle = radians(self.angle_a)
        else:
            active_angle = radians(self.angle_b)
        return cos(active_angle)

    def sin(self, angle):
        if angle == 'a' or angle == 'A':
            active_angle = radians(self.angle_a)
        else:
            active_angle = radians(self.angle_b)
        return sin(active_angle)

    def tan(self, angle):
        if angle == 'a' or angle == 'A':
            active_angle = radians(self.angle_a)
        else:
            active_angle = radians(self.angle_b)
        return tan(active_angle)

