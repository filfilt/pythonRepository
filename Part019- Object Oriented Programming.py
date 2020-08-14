# Object Oreinted Programming language(OOP)
#Eg:1
'''
class student:
    print("Hello")
s1 = student()
s2 = student()

print(type(s1))
print(type(s2))

print(id(s1))
print(id(s2))
'''

#Eg2:
class student:
    def sayHello(self):
        print("Hello "+self.fname)
s1 = student()
s2 = student()

s1.fname = "nega"
s1.sayHello()
s2.fname = "abebe"
s2.sayHello()