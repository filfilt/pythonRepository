#Dates
#Eg1: Builtten date

import datetime as d
'''
x=d.datetime.now()

print(x)
print(x.year)
print(x.month)
print(x.strftime("%A"))
print(x.strftime("%H"))
print(x.strftime("%Y"))
print(x.strftime("%y"))

'''
#Eg2: Custom date
x=d.datetime(2020,5,11)
print(x)
print(x.year)
print(x.month)
print(x.strftime("%A"))
print(x.strftime("%H"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%B"))