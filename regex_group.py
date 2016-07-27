import re

f=open("dummy_file.txt",'r')
st=re.compile('(a-z\s){*}')
reg=[]
for line in f.readlines():
	reg.append(re.findall(st,line)
print (type(reg))	
#	m.append(re.findall(st,line))
#print len(m)-1




	#1 \t\t\t111713104001\tABHINAYA R\t\t16\t\t\tabhi13101.cs@rmkec.ac.in


'''
for serial no extract
st=re.compile('(\d){,2}')
reg=[]
for line in f.readlines():
	mo=re.match(st,line)
	reg.append(mo.group())
print (type(reg))	
---------------------------------------------------------
for reg_no extrac
	st=re.compile(r'(\d{12})')
#st=re.compile(r'((\d){,2})')
m=[]
for line in f.readlines():
	m.append(re.findall(st,line))
print len(m)-1
print sorted(m)
'''