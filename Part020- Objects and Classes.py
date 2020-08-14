#Objects and Classes
class student:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def getFullName(self):
        print("your full name is "+self.fname,self.lname)
 #1st parameter       
firstName = "nega"
lastName = "tafere"
    
s1 = student(firstName , lastName)
s1.getFullName()
#2nd parameter
firstName = "Kebede"
lastName = "Demsew"
    
s2 = student(firstName , lastName)
s2.getFullName()
    
        