#Train ticket
#Roles- User: Search and book	Admin: Create train listing 
#Securities if any
#Coach Select
#Seat peference
#Ticket print
#Ticket generation
#PNR


#Functions()	in py we call it as definition
def say_hello():
	print "Hello Function"
#say_hello()


def upgradedSayHello(name):
	print 'Say Hello to Mr %s' %name
#upgradedSayHello('AY')


def sayHelloWithGreet(greet,name):
	print 'Hello Mr. %s ... Good %s' %(name,greet)
#sayHelloWithGreet('Morning','AY')

a=say_hello	#Stores the reference of the fn, now we can access a as fn
#a()

#Function with Optional params
def fnWithOptionalValues(greet,name='AY'):
	print "Good %s Mr. %s" %(greet,name)
#fnWithOptionalValues('Morning')

def fnWithDiffValue(name,stream,domain,exp='1 year',company='Cybage'):
	print 'Hello Mr. %s\nStream: %s\nDomain:%s' %(name,stream,domain)


def squares(num):
	sq = num*num
	return sq

#print 'Square of a %s is : %s' %(4,squares(4))

#function without any restriction of arguments:	Takes it as Tupple
# args
def log_me(*num):
	print type(num)
	print len(num)
	print num

#log_me(1)
#log_me(1,2)



# k args 		: Takes as Dictionary
def logMe(**num):
	print type(num)
	print num
	print num.keys()
	print num.get('a')		#If 'a' is not a Key in the dictionary then it wont error out the program it will simply print null

#logMe(a=5,b=6)

def logMe2(*args, **kwargs):
	print args
	print kwargs

#logMe2('Ankit',age=22,sex='Male',id=17926)


#Lambda Functions
#Small anonymous functions.
#Can take any number of arguments, but can only have one expression.

x = lambda a : a*a
#print x(2)

y = lambda a,b : a*b
#print y(2,5)

#HW: Q1. sort dictionary from its keys using lambda function

def test(num):
	return lambda var: var+num

print test(3)	#This prints the lambda() as its getting returned by the test(), BUT lambda expression is not evaluated yet.
a = test(3)		#Storing the lambda() in a
print a(5)		#Now, the lambda expression is getting evaluated.

dict = {'name':'ay','age':'22'}

'''
def interchange(**arg):
	return lambda k,v : arg[v]=k and arg.set()

print interchange('name'='AY','age'=23)
'''
