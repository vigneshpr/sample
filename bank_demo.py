accno=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bal=[6000, 3000, 8000, 4500, 9655, 18651, 23613, 16300, 13500, 10000]
info={}
for i in range(len(accno)):
	info[accno[i]]=bal[i]

def proceed():
	print("\n\nHello User!!!\nWelcome!!!!!!\n\n")
	st=str(input("Want to Continue (y or n):"))
	if((st=='y') | (st=='Y')):
		print("1.\tAccount Information:\n2.\tDeposit\n3.\tWithdraw\n")
		v1=input("Enter your Choice:")
		if(v1== 1):
			status()
		elif(v1== 2):
			depo()
		elif(v1== 3):
			withd()
		else:
			print("Enter Proper value:")
	else:
		print("\n\n\nThank You!!!!!!!!")
		exit()


def depo():
	acc_no=int(input("Submit your Account no:"))
	if(acc_no in info.keys()):
		temp=info.get(acc_no)
		amt=int(input("Enter your Deposit amount:"))
		temp+=amt
		info[acc_no]=temp
		print("Transaction Complete!!!!")
		print("Your Account No:",acc_no)
		print("Your Current Balance:",temp)
		proceed()

	else:
		print("Invalid Account No!!!!!!")
		proceed()
		

def withd():
	acc_no=int(input("Submit your Account no:"))
	if(acc_no in info.keys()):
		temp=info.get(acc_no)
		print("Your Account No:",acc_no)
		print("Your Current Balance:",temp)
		witdr=int(input("Enter your Withdraw amount:"))
		if(witdr>temp):
			print("Not Enough balance:")
			print("Current balance:",temp)
			proceed()
		
		else:
			temp-=witdr
			info[acc_no]=temp
			print("Transaction Complete!!!!")
			print("Your Account No:",acc_no)
			print("Your Current Balance:",temp)
			proceed()
		
	else:
		print("Invalid Account No!!!!!!")
		proceed()
		

def status():
	acc_no=int(input("Submit your Account no:"))
	if(acc_no in info.keys()):
		temp=info.get(acc_no)
		print("Your Account No:",acc_no)
		print("Your Current Balance:",temp)
		proceed()
		
	else:
		print("Invalid Account No!!!!!!")
		proceed()

proceed()