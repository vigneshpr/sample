class Sample():
	accno=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	bal=[6000, 3000, 8000, 4500, 9655, 18651, 23613, 16300, 13500, 10000]
	info={}
	for i in range(len(accno)):
		info[accno[i]]=bal[i]
	def proceed(self):
		print("\n\nHello User!!!\nWelcome!!!!!!\n\n")
		st=str(input("Want to Continue (y or n):"))
		if((st=='y') | (st=='Y')):
			print("1.\tAccount Information:\n2.\tDeposit\n3.\tWithdraw\n")
			v1=input("Enter your Choice:")
			if(v1== 1):
				stat.status(self)
			elif(v1== 2):
				stat.depo(self)
			elif(v1== 3):
				stat.withd(self)
			else:
				print("Enter Proper value:")
		else:
			print("\n\n\nThank You!!!!!!!!")
			exit()

class Inher(Sample):

	def depo(self):
		self.acc_no=int(input("Submit your Account no:"))
		if(self.acc_no in Sample.info.keys()):
			temp=Sample.info.get(self.acc_no)
			amt=int(input("Enter your Deposit amount:"))
			temp+=amt
			Sample.info[self.acc_no]=temp
			print("Transaction Complete!!!!")
			print("Your Account No:",self.acc_no)
			print("Your Current Balance:",temp)
			Sample.proceed(self)

		else:
			print("Invalid Account No!!!!!!")
			Sample.proceed(self)
		
class Multi(Inher):
	def withd(self):
		self.acc_no=int(input("Submit your Account no:"))
		if(self.acc_no in Sample.info.keys()):
			temp=Sample.info.get(self.acc_no)
			print("Your Account No:",self.acc_no)
			print("Your Current Balance:",temp)
			self.witdr=int(input("Enter your Withdraw amount:"))
			if(self.witdr>temp):
				print("Not Enough balance:")
				print("Current balance:",temp)
				Sample.proceed(self)
		
			else:
				temp-=self.witdr
				Sample.info[self.acc_no]=temp
				print("Transaction Complete!!!!")
				print("Your Account No:",self.acc_no)
				print("Your Current Balance:",temp)
				Sample.proceed(self)
		
		else:
			print("Invalid Account No!!!!!!")
			proceed(self)
		
class stat(Multi):
	def status(self):
		self.acc_no=int(input("Submit your Account no:"))
		if(self.acc_no in Sample.info.keys()):
			temp=Sample.info.get(self.acc_no)
			print("Your Account No:",self.acc_no)
			print("Your Current Balance:",temp)
			Sample.proceed(self)
		
		else:
			print("Invalid Account No!!!!!!")
			Sample.proceed(self)

class Last(stat):

	def proceed(self):
		print("\n\nHello User!!!\nWelcome!!!!!!\n\n")
		st=str(input("Want to Continue (y or n):"))
		if((st=='y') | (st=='Y')):
			print("1.\tAccount Information:\n2.\tDeposit\n3.\tWithdraw\n")
			v1=input("Enter your Choice:")
			if(v1== 1):
				stat.status(self)
			elif(v1== 2):
				stat.depo(self)
			elif(v1== 3):
				stat.withd(self)
			else:
				print("Enter Proper value:")
		else:
			print("\n\n\nThank You!!!!!!!!")
			exit()
las=Last()
las.proceed()