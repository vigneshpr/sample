ina=int(input("Enter a value:"))
a=[]
for i in range(ina):
	a.append(i)
t=tuple(a)
print hash(t)
