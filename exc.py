try:
	with open("viki.txt",'r') as f:
		f.read()
except Exception as a:
	print(a)

