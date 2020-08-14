#Class Variables Vs Instance

#Eg1:
'''
class student:
    schoolName = "Ethio Computer"
s1=student()
print(s1.schoolName)

s2=student()
print(s2.schoolName)
'''
#Eg2:
'''
class student:
    schoolName = "Ethio Computer"
s1=student()
s2=student()
s2.schoolName = "Science" #change for only s2
print(s1.schoolName)
print(s2.schoolName)
'''
#Eg3:
class student:
    def __init__(self,fn,ln):
        self.fname =fn
        self.lname = ln

    def getName(self):
        print("your full name is "+ self.fname+" "+self.lname)
    
s1=student("nega","tafere")
s2=student("alemu","worku")

print(s1.getName())
print(s2.getName())


