#Datatype-Dictionary
student = {'Fname':'nega','Lname':'tafere','Age':30}
#Eg1:
#print(student)
#print(student['Fname'])
#print(student.values())
#print(student.keys())

#Eg2:
# for s in student.values():
#     print(s)

#Eg3:
for key,value in student.items():
    print(key+': '+str(value))