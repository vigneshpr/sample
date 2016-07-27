'''Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''
text=raw_input("Enter sample String:")
dic={}
for i in text:
	dic[i]=(text.count(i))
print(dic)
	
