class person:
    def __init__(self,first,last):
        self.firstName = first
        self.lastName = last

    def getName(self):
        return self.firstName + " " + self.lastName

#----- child class: Employee inherited from person --------
class Employee(person):
    def __init__(self,first,last,staffNum):
        person.__init__(self,first,last)
        self.staffNum = staffNum

    def getEmployee(self):
        return self.getName() + ": " + self.staffNum
#----- child class: Employee inherited from person --------
class Boss(person):
    def __init__(self,first,last,title):
        person.__init__(self,first,last)
        self.title = title

    def getBoss(self):
        return self.getName() + ": Employee ID: " + self.title

#----- instantiate class --------    
person_1 = person("Math", "Hoang")
Employee_1 = Employee("Math", "Hoang", "12344")
Employee_2 = Employee("Blog", "spot", "43211")
Boss_ = Boss("Mathhoang", "Blogspot.com", "CEO")

#------ print out information ------
print(person_1.getName())
print(Employee_1.getEmployee())
print(Employee_2.getEmployee())
print(Boss_.getBoss())
