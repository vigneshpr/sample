class calculate():
	result = 0
	

	def add(self,num1,num2):
		self.result = num1+num2
		return self.result

	def sub(self,num1,num2):
		self.result=num1-num2
		return self.result

	def mul(self,num1,num2):
		self.result = num1*num2
		return self.result

	def div(self,num1,num2):
		self.result = num1/num2
		return self.result


class  result(calculate):
	def welcome(self):
		print "Welcome to calculate \t Enter the 2 values one by one: "
		in1 = int(input("Enter the 1 value:"))
		in2 = int(input("Enter the 2 value:"))

		inp = int(input(" 1.add \n 2.subtract \n 3.Multiply \n 4.Divide \n Enter your Option: "))

		if (inp==1):
			print(self.add(in1,in2))

		elif (inp==2):
			print(self.sub(in1,in2))
		elif (inp==3):
			print(self.mul(in1,in2))
		elif (inp==4):
			print(self.div(in1,in2))
		else:
			print("Enter the proper value")
			exit()

	def  reslt(self,result):
		print(result)
		

fin=result()
fin.welcome()




'''

class Dvinherit(object):	#object is built in global variable and it tells this class is the top of the hierchy
	def name(self):
		print "Base Class"
class Deri(Dvinherit):	
	def name(self):
		print "Derived class"
		super(Deri,self).name()		
class Multi(Deri)		:
	def name(self):
		super(Multi,self).name()
		print "Multiple Derived"
		
new=Multi()
new.name()


#another method to perform inheritance without using super keyword but it is not a valid one

class Dvinherit():	#object is built in global variable and it tells this class is the top of the hierchy
	def name(self):
		print "Base Class"
class Deri(Dvinherit):	
	def name(self):
		print "Derived class"
		Dvinherit.name(self)		
class Multi(Deri)		:
	def name(self):
		print "Multiple Derived"
		Deri.name(self)



new=Multi()
new.name()
'''