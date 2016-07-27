'''Write a Python program to accept a filename from the user print the extension of that.

Sample filename : abc.java 
Output : java

Sample Solution :-

Python Code :

view plaincopy to clipboardprint?'''
name = raw_input("Input the Filename with its extension: ")  
print ("The  extension of the file is : " ,name[name.index('.')+1:] )  