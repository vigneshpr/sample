'''3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string. Go to the editor 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String '''
stri3=raw_input("Enter Sample String:")
stri1='w3resource'
stri2="w3"
def ss:
	print((stri3[0:2])+(stri3[-2:]))
	if(len(stri3)<3):
		print("Invalid")
