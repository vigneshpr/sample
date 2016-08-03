l=[72, 14, 1, 77, 16, 84, 9, 93, 45, 12, 10, 72, 57, 59, 23, 51, 28, 70, 95]
def gene():
	for i in range(len(l)):
		print(l[i])
		yield l[i**2]
m=gene()
print(next(m))
