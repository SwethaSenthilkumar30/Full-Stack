#Abstraction---- It is a process of hiding the logic or statement
#Types
#1.Partial---- it contains both abstract and non-abstract method
#         ---- we can't create object
#2.Fully----- We don't have fully abstraction in python

# from abc import ABC, abstractmethod
# class RbiBank():
#     @abstractmethod
#     def savings(self):
#         pass
#
#     @abstractmethod
#     def current(self):
#         pass
#
#     def fixed(self):
#         print("Fixed is 7%")
#
# class GreensBank(RbiBank):
#     def savings(self):
#         print("Savings is 5%")
#
#     def current(self):
#         print("Current is 6%")
#
# g=GreensBank()
# g.savings()
# g.current()
# g.fixed()

print("----------------------")
#public
class Employee():

    def empId(self):
        self.empid=234
        print(self.empid)

    def empName(self):
        print(self.empid)

e=Employee()
e.empId()
print(e.empid)
e.empName()

print("-----private--------")
class Employee():

    def __empId(self):
        self.__empid=567
        print(self.__empid)

    def empName(self):
        self.__empId()
        print(self.__empid)


e=Employee()
e.empName()

















