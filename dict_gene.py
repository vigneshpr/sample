'''6. Write a Python script to generate and print a dictionary that contains number (between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) : 
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
d= input("Enter the value n:")
dic={}
for i in range(d):
	dic[i]=i**2
print dic
'''
tu=(1, 2, 3, 4, 5, 1)
ls=range(len(tu))
di={}
for i in range(len(tu)):
	di[tu[i]]=ls[i]
print(di)