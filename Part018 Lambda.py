#Lambda
#Eg1: Function without parameter
'''
def fn_hello():
    print("Hello")
fn_hello()
'''
#Eg2:with parametere
#Sum two numbers
'''
def fn_addTwonumbers(n1,n2):
    print(n1+n2)
    
fn_addTwonumbers(12,12)
'''

#Eg3: Multi =>bring outside
'''
def fn_mult(n1,n2):
    print(n1*n2)
    
x =int(input("Enter first number: "))
y =int(input("Enter second number: "))

fn_mult(x,y)
'''

#Argument:
'''
def fn_myfun(*stud):
    print(stud)
fn_myfun("nega","Anebe","Wale")
'''
#Key args 
'''
def my_fun(fname,lname,age):
    print("your full name is "+fname+" "+lname)
my_fun(fname="nega",lname="tafere",age=30)
'''

#Eg4:kwargs
'''
def myfn(**student):
    print("The first name is "+ student["fname"])
myfn(fname="nega",lname="tafere")
'''
#default value
def fn_myf(country="USA"):
    print(country)
fn_myf("Ethiopia")

    