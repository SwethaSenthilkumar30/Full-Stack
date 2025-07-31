class Employee():


    #setter
    def setEmpId(self,empid):
        self.__empid=empid

    def setEmpName(self,empname):
        self.__empname=empname

    def setEmpPhone(self,empphone):
        self.__empphone=empphone

    # Getter
    def getEmpId(self):
        return self.__empid

    def getEmpName(self):
        return self.__empname

    def getEmpPhone(self):
        return self.__empphone


e1=Employee()
e1.setEmpId(3445)
e1.setEmpName("Swetha")
e1.setEmpPhone(1234567890)

print(e1.getEmpId())
print(e1.getEmpName())
print(e1.getEmpPhone())

e2=Employee()
e2.setEmpId(9087)
e2.setEmpName("kiki")
e2.setEmpPhone(9987654321)

print(e2.getEmpId())
print(e2.getEmpName())
print(e2.getEmpPhone())

e3=Employee()
e3.setEmpId(8765)
e3.setEmpName("somu")
e3.setEmpPhone(7654328900)

print(e3.getEmpId())
print(e3.getEmpName())
print(e3.getEmpPhone())

print("-------User Defined List----------")
l=[e1,e2,e3]
print(l)

print(l[1].getEmpId())
print(l[1].getEmpPhone())
print(l[1].getEmpName())

print("----------For loop-----------")
for i in range(0,len(l),1):
    print(l[i].getEmpId())
    print(l[i].getEmpName())
    print(l[i].getEmpPhone())




















