'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

Sample String : 'restart'
Expected Result : 'resta$t'''
#Check Version

import sys
print(sys.version)

stri="restart"
strr=stri[0]
strm=stri[1:]
print(strr+strm.replace(strr,'$',1))