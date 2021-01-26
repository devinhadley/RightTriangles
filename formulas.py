from math import sqrt


def find_c(side_b, side_a):
    side_c = sqrt(side_a * side_a + side_b * side_b)
    return side_c

def find_b(side_a, side_c):
    side_b = sqrt((side_c * side_c) - (side_a * side_a))
    return side_b

def find_a(side_b, side_c):
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    return side_a
