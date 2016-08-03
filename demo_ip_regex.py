import socket
import re
try:

	hostIP=socket.gethostbyname(socket.gethostname())
#	ip_list=[hostIP]
	pat = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
#for i in range(len(hostIP)):
	#pat=re.compile(r'^(?:(?&.upto255)\.){3}(?&.upto255)&')
	test = pat.match(hostIP)

	if test:
		print hostIP
		print "Acceptable ip address"
	else:
		print "Unacceptable ip address"
except:
	print("Enter Proper Ip address")

#https://www.debuggex.com/r/QrC7blrmD11myKEc for regex username vignesh.itian@gmail.com 
# unexpected changes for checking
