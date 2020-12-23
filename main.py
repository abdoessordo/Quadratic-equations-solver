from math import sqrt

def solve(a, b, c):
	d = calculate_det(a, b, c)
	if d<0:
		return None
	x = ((-b+sqrt(d))/2*a, (-b-sqrt(d))/2*a)
	if d==0:
		return (x[0])
	return x


def calculate_det(a, b, c):
	return b**2 - 4*a*c

if __name__ == "__main__":
	a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
	print(solve(a, b, c))
