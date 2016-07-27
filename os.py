import re
hostIP=['1220.0.0.1','192.34.45.56']
pat = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
for i in range(len(hostIP)):
	test = pat.match(hostIP[i])
	if test:
   		print hostIP[i]
   		print "Acceptable ip address"
	else:
		print hostIP[i]
   		print "Unacceptable ip address"

'''import re
hostIP=['10.0.0.1','192.34.45.626']
pat = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
for i in range(len(hostIP)):
	test = pat.match(hostIP[i])
	if test:
   		print "Acceptable ip address"
	else:
   		print "Unacceptable ip address"



'''