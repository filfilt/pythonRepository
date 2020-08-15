#Scope
'''
class student:
    def getName():
        Age = 45
        def getAge():
            print(Age)
        getAge()
            
student.getName() #but not student.getAge()
'''
#Eg2:
class student:
    def getName():
        global Age=45
        def getAge():
            print(Age)
        getAge()
            
student.Age=45
print(student.Age)