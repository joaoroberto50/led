#!/usr/bin/env python3

def rpg2(a,b,c):
	delta=(b**2-4*a*c)
	print("a =" + str(a) +";b =" + str(b) +";c =" +str(c))  
	print("delta = " + str(delta))
	
	if (delta<0):
		return False
	else:
		if (delta==0):
			return (-b/2*a)
		else:
			return ((-b + delta**0.5)/2*a, (-b - delta**0.5)/2*a)
			

x = rpg2(1,2,3)
print(x, type(x))
x = rpg2(-10,-10,-10)
print(x, type(x))
x = rpg2(-4,4,1)
print(x, type(x))
x = rpg2(4,-4,-1)
print(x, type(x))

