import turtle
from formulas import find_a, find_b, find_c
from math import atan, degrees, radians, tan, sin, cos


class RightTriangle():

    def __init__(self, a=None, b=None, c=None):
        '''
        Instantiates right triangle using (optional) only two sides.

        '''
        self.a = a
        self.b = b
        self.c = c

        if self.a is None:
            if self.b is None or self.c is None:
                raise Exception("Please define at least two side lengths.")
            self.a = find_a(side_b=self.b, side_c=self.c)
        elif self.b is None:
            if self.a is None or self.c is None:
                raise Exception("Please define at least two side lengths.")
            self.b = find_b(side_a=self.a, side_c=self.c)
        elif self.c is None:
            if self.b is None or self.a is None:
                raise Exception("Please define at least two side lengths.")
            self.c = find_c(side_a=self.a, side_b=self.b)

        self.angle_a = degrees(atan(self.a / self.b))
        self.angle_b = degrees(atan(self.b / self.a))

    def printAngles(self):
        '''
        Prints the interior angles of the triangle.

        '''
        print("Angle A: "+str(self.angle_a))
        print("Angle B: "+str(self.angle_b))

    def showShape(self, multiplier=10):
        '''
        Displays the shape of the triangle using a turtle.
        You can pass multiplier to increase size.

        '''
        board = turtle.Turtle()

        board.forward(self.b * multiplier)  # draw base

        board.left(90)

        board.forward(self.a * multiplier)

        board.left(180 - degrees(atan(self.b/self.a)))

        board.forward(self.c * multiplier)

        turtle.done()

    def printSides(self):
        '''
        Prints all side lengths of the triangle.

        '''
        print("Side A: "+str(self.a))
        print("Side B: "+str(self.b))
        print("Side C/Hypotenuese: "+str(self.c))

    def cos(self, angle):
        '''
        Computes and returns the cosign of the chosen angle.

        '''

        if angle == 'a' or angle == 'A':
            active_angle = radians(self.angle_a)
        else:
            active_angle = radians(self.angle_b)
        return cos(active_angle)

    def sin(self, angle):
        '''
        Computes and returnsthe sine of the chosen angle.

        '''
        if angle == 'a' or angle == 'A':
            active_angle = radians(self.angle_a)
        else:
            active_angle = radians(self.angle_b)
        return sin(active_angle)

    def tan(self, angle):
        '''
        Computes and returns the tangent of the chosen angle.

        '''
        if angle == 'a' or angle == 'A':
            active_angle = radians(self.angle_a)
        else:
            active_angle = radians(self.angle_b)
        return tan(active_angle)
