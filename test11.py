

#!/bin/python




 import sys
def calc(x):
	if((x>=2) & (x<=5)):
		print("Not Weird")
	elif((x>=6)&(x<=20)):
		print("Weird")
	else:
		print("Not Weird")
N = int(raw_input().strip())

if((N%2==1)):
    print("Weird")
else:
    calc(N);


