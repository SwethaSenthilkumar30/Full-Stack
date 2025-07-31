# Creating a class
# Class Classname():
#     methods

#creating a method
#def methodname(self):
#    logic

class Employee():
    def emp_id(self):
        print("Employee Id is 8745")

    def emp_name(self):
        print("Employee Name is Swetha")

#object creation
# variableName=className()
e=Employee()

# method calling
# objName.methodName()
e.emp_id()
e.emp_name()

print("--------instance variable-----------")
class Employee():
    def emp_ID(self):
        self.id=456
        print("Employee Id is",self.id)

    def emp_Name(self):
        print("Employee Name is Swetha")
        print(self.id)

e=Employee()
e.emp_ID()
e.emp_Name()

print("------method with argument---------")
class Employee():
    def emp_ID(self,id):
        print("Employee Id is",id)

    def emp_Name(self):
        print("Employee Name is Swetha")

e=Employee()
e.emp_Name()
e.emp_ID(23)

print("-----self keyword can be changed to any name---------")
class Employee():
    def emp_ID(id,self):
        print("Employee Id is",self)

    def emp_Name(self):
        print("Empolyee Name is Swetha")

e=Employee()
e.emp_ID(234)
e.emp_Name()



















