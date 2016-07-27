import datetime


with open('/home/local/TAG/vigneshwarann/html/demo.txt','a+') as f:	
	d=f.read()
	d=d.replace('viki','is')
	print(d)