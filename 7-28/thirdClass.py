#Third Class - 28 July


#Dictionary
#A dictionary is a collection which is unordered, changeable and indexed

classData = {'name':'Ankit yadav',
				'roll no': 5,
				'address': 'pune'}

#print(classData['name'])

#constructor
#dict()
'''
print(classData.keys())
print(classData.values())
print(classData.items())						#Returns tupple Key and Value
print(classData.has_key('name'))				#checks whether dict has a key with 'name'
print('name' in classData)						#This also check if key is present in dict or not
print(classData.get('name'))					#Returns the value Also if the key is not present in the Dict it returns blank value (in py blank is false)
'''

#To delete a key i. .pop() ii. del(dict[key])
#.popitem()	removes random key value pair
# dict.clear()	it clears the dictionary

'''
print(classData)
popItem=classData.pop('name')	
print(classData)
print("Popped item: "+popItem)
classData['name']='JN Yadav'
print(classData)
del(classData['name'])
print(classData)
classData.popitem()
print(classData)
classData.clear()
print(classData)
'''

'''
print(classData)
newClassData = classData 	#Copies with its references imp: changes reflect on both the variable
print(newClassData)
newClassData['mob']=9999
print "New Class Data: ", newClassData
print "Old Class Data: ", classData


newCopyClassData=classData.copy()	#only copies its values
newCopyClassData['mob']=9999
print "New Class Data: ", newCopyClassData
print "Old Class Data: ", classData


len(classData)
'''


# update()
#This method adds dictionary of dict2's key Value pairs in to dict1's. This function does not returns anything
'''
dict1= {'name': 'AY', 'age':22}
dict2={'sex':'Male', 'age':52}

print "Value Before Updation %s" %dict1
dict1.update(dict2)
print "Value After Updation %s" %dict1

'''

#nested Dictionaries
# dict of dict
# dict of list
# list of dict
# list of list

'''
#Dictionaries of Dictionaries
print 'Dictionaries of Dictionaries'
nestedDict1 = {'name': 'AY', 'Corporate Profile':{'office':'Cybage', 'Location':'Pune'} , 'age': 22}
print nestedDict1

#List of dictionaries
print 'List of dictionaries'
dict1 = {'name':'AY'}
dict2 = {'age':22}
list1 = [dict1,dict2]	
print list1

#Dictionaries of List
print 
print '#'*20 , '\nDictionaries of List'
dictList = {'name': 'Ankit', 'Skills':['Python','Java']}
print dictList
'''

#Conditional Operators

'''
#Membership Operators : 'in'	'not in'
dict1 = {'name':'AY', 'age':23}
print 'name' in dict1
print 'name' not in dict1

#This also works in String
comment = "This is a comment in program"
print 'program' in comment
'''

#Identity Operators

#Primarily checks the IDs of the variable if same or not

#is - Evaluates to true if the variables on the either side of the operator point to the same object otherwise returns false
#is not
'''
a = [1]
b = [1]
print a is b 
print id(a), id(b)
print '*'*20
a = 20
b = 20
c = 20

#Every variable having value 20 will have same id, and reference count increase, when 0 memory is deallocated
print a is b
print id(a), id(b)
print a is not b
'''

#Conditional Statements
'''
name1 = 'Ankit'
name2 = 'Yadav'

if name1 != name2:
	print "Name are not same"
'''

'''
student = {1:{'name':'Ankit', 'age':23},
		   2:{'name':'Amit', 'age':31}}
studentName = 'Ankit'

if student[1]['name']=='Ankit':
	print "Age of Ankit is %s" %student[1]['age']
elif student[1]['name']=='Amit':
	print "Age of Amit is %s" %student[1]['age']
else:
	print "This is not correct name"
'''

#Things treated as false
#Numbers: 0, 0.0
#Empty String, list :[], Dict : {}, Tuple :	(), None, False, Empty Set
'''
dict1 = {}
list1 = ["AY"]
tupple1 = ()
if not (dict1 or list1 or tupple1):
	print 'This is an empty data structure'
else:
	print 'Yippee... Not an empty DS'
'''


#Loops
# i. While
# ii. For
'''
print '*'*20, '\nExample of While Loop'
i=0
while i<3:
	print 'The no. is %d' %i
	i+=1

#While loop can also have 'else' condition
print '*'*20
j=0
while j<3:
	print 'The no. is %d' %j
	j+=1
else:
	print 'Now the value is %d' %j
'''
'''
print '*'*20, '\nExample of For Loop'
for char in 'Ankit':
	print char,			#Prints in one line becoz of ',' 

numbers=range(0,10,2)
for variableNum in numbers:
	print variableNum	#Prints in \n Line
'''
#break - will break the loop
#continue - will continue with the next
'''
print '*'*20, '\nExample of For Break and Continue'
#list1 = [1,2,3,4,5,6,7,8]
list1 = range(1,8)
for n in list1:
	#print 'Inside for Loop'
	if n < 5:
		print n, 'is less than 5'
	elif n==5:
		print 'Value == 5'
		continue
	else:
		print n, 'is greater than 5'
'''

'''
listDict=[{'name':'Ankit','age':22},{'sex':'male'}]
for n in listDict:
	print n['name']
'''