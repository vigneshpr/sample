class base:
   def __init__(self):
      print "Animal created"

   def whoAmI(self):
      print "Animal"

   def eat(self):
      print "Eating"


class Dog(base):
   def __init__(self):
      base.__init__(self)
      print "Dog created"

   def whoAmI(self):
   		base.whoAmI(self)
   		print "Dog"

   def bark(self):
      print "Woof!"


d = Dog()
d.whoAmI()
d.eat()
d.bark()
















'''class first:
	def base(self):
		print("First class")
class second (first):
	def base(self):
		super(second,self).base()
		print("Second class")

f=second()
f.base()
'''