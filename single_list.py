'''Here I make use of LIST for implementation.Here the address be the index values and the value be the actual data'''


import time
base_ls=[1,2,3,4,5,6]
def dis():
	if(len(base_ls)==0):
		print("Empty Linked_list")
		proceed()
	else:
		print("Display Linked_list")
		for i in range(len(base_ls)):
			print("Key-->",i,"Value-->",base_ls[i])
			#time.sleep(2)
		proceed()
def inser():
	print("---------------------------------------------------------------------------")
	print("Select Your Option:\n---------------------------------------------------------------------------")
	print("1.Insert at begin.|\t2.Insert at Last.|\t3.Insert in Between.\n---------------------------------------------------------------------------")
	sam=int(raw_input("Enter your option:"))
	if(sam==1):
		a=input("Enter the Value to insert:")
		print("Before Insert:",base_ls)
		base_ls.insert(0,a)
		
		print("After Insert:",(base_ls))
		proceed()
	elif(sam==2):
		a=input("Enter the Value to insert:")
		print("Before Insert:",base_ls)
		base_ls.append(a)
		
		print("After Insert:",(base_ls))
		proceed()
	elif(sam==3):
		print(base_ls)
		b=input("Enter the position to insert:")
		a=input("Enter the Value to insert:")
		print("Before Insert:",base_ls)
		base_ls.insert(b,a)
		
		print("After Insert:",(base_ls))
		proceed()
	else:
		print("Invalid Option")
		proceed()
def rem():
	print("---------------------------------------------------------------------------")
	print("Select Your Option:\n---------------------------------------------------------------------------")
	print("1.Delete at begin.|\t2.Delete at Last.|\t3.Delete in Between.\n---------------------------------------------------------------------------")
	sam=int(raw_input("Enter your option:"))
	if(sam==1):
		print("Before Insert:",base_ls)
		base_ls.pop(0)
		
		print("After Insert:",(base_ls))
		proceed()
	elif(sam==2):
		print("Before Delete:",base_ls)
		base_ls.pop()
		
		print("After Delete:",(base_ls))
		proceed()
	elif(sam==3):
		print(dis())
		a=input("Enter the Key_value Value to Delete:")
		
		print("Before Delete:",base_ls)
		base_ls.pop(a)
		
		print("After Delete:",base_ls)
		proceed()
	else:
		print("Invalid Option")
		proceed()
def disp():
	print("-------------------------Single Linked List--------------------------------")
	
	print("Select Your Option:\n---------------------------------------------------------------------------")
	
	print("1.Display List.|\t2.Insertion Operation.|\t3.Deletion Operation.\n---------------------------------------------------------------------------")
	
	opt=int(input("Enter a Option:"))
	if(opt==1):
		dis()
	elif(opt==2):
		inser()
	elif(opt==3):
		rem()
	else:
		print("Invalid Option")
		proceed()

def proceed():
	try:
		st=str(input("Want to Continue (y or n):"))
		if((st=='y') | (st=='Y')):
			disp()
		else:
	
			print("\nExiting!!!!!!!!\n")
			exit()
	except:
		proceed()
disp()