import math

dp = "%.2f"

def quadratic():

	
	a = float(input("Please enter coefficient a: "))
	b = float(input("Please enter coefficient b: "))
	c = float(input("Please enter coefficient c: "))

	root = math.sqrt((b * b) - 4 * a * c) 
	x1 = (-b + root) / (2 * a) 
	x2 = (-b - root) / (2 * a) 

	print()
	print("The solutions are:",  dp % x1, dp % x2)
	
