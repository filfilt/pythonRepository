#Comparison and Logical Operators
#Eg1:
'''
n1 = 12
n2 = 13
if n1 == n2 :
    print("Numbers are equal")
elif n1>n2:
    print("Number1 is greater than Number2")
else:
    print("Number2 is greater than Number1")
'''

#Eg2: comparisn operator
'''
mark =int(input("Enter mark:"))
grade = " "
if mark >90:
    grade ="A"
elif mark >80:
    grade ="B"
elif mark >70:
    grade ="C"
elif mark >60:
    grade ="D"
else:
   grade ="F"
print(grade)
'''
#Eg3: Logical Operator
#And
'''
mark =int(input("Enter mark:"))
grade = " "
gender = input("please Enter Gender:")
if mark >90 and gender =='m':
    grade ="A"
elif mark >80 and gender =='f':
    grade ="A"
elif mark >80 and gender == 'm':
    grade ="B"
elif mark >70 and gender == 'f':
    grade ="B"
elif mark >70 and gender == 'm':
    grade ="C"
elif mark >60 and gender == 'm':
    grade ="C"
elif mark >60 and gender == 'm':
    grade ="D"
elif mark >50 and gender == 'f':
    grade ="D"
else:
   grade ="F"
print(grade)
'''
#Or
gender = input("Enter Gender:")
if gender=='m' or gender == 'M':
    print("Gender is Male")
if gender=='f' or gender == 'F':
    print("Gender is female")
    