l=[]
d=str(raw_input("Enter a Value:\n\nA-->Append\n\nS-->Show list\n\nQ-->Quit\n\n"))
if(d==a & d==A):
	app()
elif('d'=='s' & 'd'=='S'):
	show()
else:#:('d'=='q' & 'd'=='Q'):
	exit()
def app():
	d1=raw_input("Enter many values to append:")
	for i in range(d1):
		s=input("Enter a value to append:")
		l.append(s)
def show():
	print(l)
def exiit():
	quit()



