import turtle

from math import sqrt, atan, degrees

def pythag(formula,side_a=None, side_b=None, side_c=None):
	if formula == 'c':
		side_c = sqrt(side_a * side_a + side_b * side_b)
		
		return(int(side_c))

	elif formula == 'a':
		side_a = sqrt((side_c * side_c) - (side_b * side_b))
		
		return(int(side_a))

	elif formula == 'b':
		side_c = sqrt(side_c * side_c - side_a * side_a)
		
		return(int(side_c))

	else:
		print('Please select a side between a, b, c')




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

        self.angle_1 = degrees(atan(self.a/self.b))
        self.angle_2 = degrees(atan(self.b/self.a))
 


    def printAngles(self):
        print(self.angle_1, self.angle_2)


    def showShape(self):
        board = turtle.Turtle()
         
        board.forward(self.b * 10) # draw base
          
        board.left(90)
        board.forward(self.a * 10)
           
        board.left(180 - degrees(atan(self.b/self.a)))
        board.forward(self.c * 10)
        turtle.done()

    def printSides(self):
        print(self.a)
        print(self.b)
        print(self.c)

test = RightTriangle(b=4,c=5)

test.printAngles()
test.printSides()
test.showShape()
