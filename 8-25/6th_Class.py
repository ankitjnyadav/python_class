#reduce function
# reduce(func, sequence)
# The function reduce contnually applies the function func() to the squence 
# seq = [s1,s2,s3 .. sn]
# func(s1,s2)

#print reduce(lambda x,y:x+y, [47,11,42,13])


#Generators
# Are iterators but can only use once
# they do not get stored in memory
# Runs the code on the fly
'''
list1 = [x*x for x in range(5) ]
print type(list1)


gen1 = (x*x for x in range(5))
print type(gen1)

print gen1.next()
print gen1.next()
print gen1.next()

for i in gen1:
	print ':',i
'''


#Yield:
#Is a keyword that is used like return, except the function will return a generator
#Also, the function which returns yield is known as genrator function
'''
def findEvenNum(numList):
	evenNum = []
	for n in numList:
		if n%2 ==0:
			evenNum.append(n)
	return evenNum

a= findEvenNum([1,2,3,4,5])
print type(a),':',a


def findEvenNumGenrator(numList):
	evenNum = []
	for n in numList:
		if n%2 ==0:
			yield n

b= findEvenNumGenrator([1,2,3,4,5])
print type(b),':',b

for i in b:
	print i,

'''
#Practical example of generator for searching into the large amount of the data from the file

'''
def holdClient(name):
	yield 'Hello, %s!' %name
	yield 'Dear, %s!' %name
	yield 'Good Morning, %s!' %name
	yield 'Bye, %s!' %name

a = holdClient('ankit')
print a.next()
print a.next()
print a.next()
print a.next()


def holdList(numList):
	for i in numList:
		yield 'Hello AY ', i
		yield 'Hello AY 1 ', i
		yield 'Hello AY 2 ', i
		yield 'Hello AY 3 ', i

b = holdList([1,2,3])
for i in range(12):
	print b.next()
'''


# range Vs xrange
# range() returns a list of numbers
# created using range() function
# xrange() returns the generator() object
# return type are list/xrange	-not generator for xrange
# range takes more memory
# xrange is faster


#Zip
# aggregates elements based on the iterables passed, and returns an iterator of tuples
# zip( *iterators )

'''
ret = zip()
print ret

list1 = [1,2,3]
list2 = ['One','Two','Three']

ret = zip(list2,list1)
print ret

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['One','Two','Three','Four','Five']

ret = zip(list2,list1)
print ret
print zip(*ret)
print list1
print list2
list1,list2 = zip(*ret)
print list1
print list2
'''


#Zip can be used to conver te lists into dict
'''
keys = ['name','age','sex']
values = ['Ankit',21,'Male']

dataDict = dict(zip(keys,values))
print dataDict
'''


#Enumerate
# method adds a counter to an iterable and returns it in a form of enumerate object
# It allows us to loop over something and have an automatic counter
'''
list1 = ['Eat','Sleep','Repeat']
en1 = enumerate(list1)

print en1 
print en1.next()
print list(en1)
print list(en1)	#generator reached its last, so returning null


for c,value in enumerate(list1,1):
	print (c,value)		#() makes it a tuple
'''




# Exception
# Exception error:
# 	Is a type of error occurs whenever syntactically correct Python code results in error
# Type of Errors:
# 1. ImportError
# 2. IndexError
# 3. KeyError
# 4. MemoryError
# 5. NameError
#To throw/raise an Exception: raise Exception('Message')

#raise Exception
#raise Exception('Hello')
'''
pwd = '123'
if pwd != '1234':
	raise Exception('Incorrect Password')
'''

#AssertionError Exception
'''
platform ='linux'
assert 'linux' in platform, "This code runs only on Linux"
assert 'Windows' in platform, "This code runs only on Linux"
'''


# Handling Exceptions
# try and except block in Python is used to catch and handle exceptions
'''
Syntax:
try{
	Run this code
}except{
	Execute this code when exception occurs
}
'''

# We can anticipate multiple execptions and differentiate how the program responds
dict1 = {1:'Ankit',2:'Yadav',3:'Male'}
print dict1[1]

def checkException(i):
	try:
		print 'Checking Key:4 in Dict'
		#import ttt
		print dict1[i]
	except KeyError as e:
		print 'Got Key Error for Key:', e
		print type(e)
	except ImportError as e:
		print 'Got Import Error :', e
	except:
		print '*Execption Occured*'
	else:	#No Exceptions? Run this code
		print 'No Error in the code'
	finally:
		print 'Inside Finally block\nData CleanUp Done'

#checkException(4)