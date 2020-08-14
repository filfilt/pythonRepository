#Set is unorderd collections of unique objects
#Eg1:
'''
fruits = {'banana','orange','pear'}
print(fruits)
'''

#Eg2:
'''
fruits = {'banana','orange','pear','banana'}
fruits.add('Apple')
print(fruits)  #this add only the new one
 '''
 #Eg3:
b=frozenset('nega')
print(b)     # from this we cann't add anything because of frozenset