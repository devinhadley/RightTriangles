from math import sqrt

def pythag(formula,side_a=None, side_b=None, side_c=None):
	if formula == 'c':
		side_c = sqrt(side_a * side_a + side_b * side_b)
		
		return(side_c)

	elif formula == 'a':
		side_a = sqrt((side_c * side_c) - (side_b * side_b))
		
		return(side_a)

	elif formula == 'b':
		side_c = sqrt(side_c * side_c - side_a * side_a)
		
		return(side_c)

	else:
		print('Please select a side between a, b, c')


