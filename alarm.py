import datetime
ow =  datetime.datetime.now().strftime('%H:%M:%S %d:%m:%Y')  # This constructs an infinite loop
print(ow)
ti=raw_input( "Use this format:HH:MM:SS DD:MM:YYYY\n\nExample:15:03:36 12:05:2016:\n>>>")
var = 1
while var == 1 :
	now =  datetime.datetime.now().strftime('%H:%M:%S %d:%m:%Y')  # This constructs an infinite loop
	if(ti==now):
   		import os
   		os.system("pwd")
   		break


