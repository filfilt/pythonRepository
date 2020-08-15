#Types of Methods
#Eg1:Instance Method
'''
class student:
    schoolName = "school of techinology"
    def __init__(self,fn,ln):
        self.fname =fn
        self.lname = ln

    def getName(self):
        self.fname=self.fname+"1st"
        print("your full name is "+ self.fname+" "+self.lname)
    
s1=student("nega","tafere")
s1.getName()
'''''
#Eg2:Class =>to modify only class variable not instance
class student:
    schoolName = "school of techinology"
    def __init__(self,fn,ln):
        self.fname =fn
        self.lname = ln

    def getName(self):
        self.fname=self.fname+"1st"
        print("your full name is "+ self.fname+" "+self.lname)
    @classmethod
    def myClassmethod(cls):
       cls.schoolName="Medicine"
    
s1=student("nega","tafere")
s1.getName()
s1.myClassmethod()