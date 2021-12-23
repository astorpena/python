import math
a = int(input('This is my quadratic equation solving calculator built in python. What is a?'))
b = int(input('What is b?'))
c = int(input('Finally, what is c?'))
d = (b * b) - (4 * a * c)
if(d < 0):
	print('The discriminant is less than zero. There are no real solutions.')
	exit()
print('x = (-', b, '\u00b1', math.sqrt(d),')', '\n     ', '/', (2 * a))