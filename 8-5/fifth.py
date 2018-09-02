#File Handling
'''
fh = opene(path,accessSpecifier,bufferSize)
fh.closed = returns true if file is still open
fh.mode = returns the accessSpecifier
fh.name = returns the name of file
'''
# fh.close() : method flushes any unwritten info and closes the file object, after which no more writing can be done
# py automatically closes a file when ref ob of a files is reassignd


#write() writes any string to an open file
# does npt add a newLine ch at the end of string
# need to specify \n explicity

#read([count])	optional params
#if count is provied, will be the length till the file handler will read

'''
path = r'D:\Ethans\Python\8-5\word.txt'
fh = open(path,'w+')
if not fh.closed:
	print 'File Open'
	print 'Performing write operation...'
	fh.write('This is text msg from Py Console.\n')
	fh.close()
	print 'File closed'


fh = open(path,'r+')
if not fh.closed:
	print 'File Open'
	print 'Performing read operation...'
	#print 'Whole contents in File are:\n',fh.read()
	#fh.write('This is text msg from Py Console.\n')
	print 'Reading till a count of 5 in File: \n',fh.read(5)
	fh.close()
	print 'File closed'
'''
#tell() method tiells the curren positon withi  the file
#seek(offset[,from])
#offset indicates the no of bytes to be movied
#0: beginning of file
#1: current position in the file
#2: End of the file
'''
path = r'D:\Ethans\Python\8-5\word.txt'
fh = open(path,'r+')
if not fh.closed:
	print 'File Open'
	print 'Performing write operation...'
	fh.write('This is text msg from Py Console.\n')
	print fh.tell()
	#print fh.read()
	#fh.seek(1)
	#print fh.read()
	#fh.seek(1)
	#fh.write('New Msg added')
	#print fh.read()
	
	fh.close()
	print 'File closed'

'''
#fileObject.readline(size)
#if you want to ready a file line by line
#as opposed to pulling the content of the entire file at once

#fileObject.readlines()
#reads a file line by line
#returns a list of lines
'''
path = r'D:\Ethans\Python\8-5\word.txt'
fh = open(path,'w+')
if not fh.closed:
	print 'File Open'
	print 'Performing read operation...'
	#print 'Whole contents in File are:\n',fh.read()
	fh.write('This is text msg from Py Console.\nThis is secondLine')
	#print 'Reading till a count of 5 in File: \n',fh.read(5)
	print fh.tell()
	fh.seek(0)
	print fh.readline()
	print fh.readlines()
	fh.close()
	print 'File closed'


'''

'''
#mutiple lines
path = r'D:\Ethans\Python\8-5\word.txt'
fh = open(path,'w+')
linesOfText=["Line1\n","Line2\n","Line3"]
if not fh.closed:
	print 'File Open'
	print 'Performing read operation...'
	fh.writelines(linesOfText)
	#fh.read()	Erroneous Code segment here...
	fh.seek(0)
	print fh.readline()
	print fh.readlines()
	fh.close()
	print 'File closed'
'''

'''
#with Statement
#any files opened will be closed automatically after you are done
# with open(path) as fh
path = r'D:\Ethans\Python\8-5\word.txt'
with open(path,'w+') as fh:
	linesOfText=["Line1\n","Line2\n","Line3"]
	if not fh.closed:
		print 'File Open'
		print 'Performing read operation...'
		fh.writelines(linesOfText)
		#fh.read()	Erroneous Code segment here...
		fh.seek(0)
		print fh.readline()
		print fh.readlines()
'''

#list comprehension
#  result = [transform	iteration	filter]

'''
x = [i for i in range(10)]
print 'No. from 1-10: ',x
squares = [x**2 for x in range(10)]	#	** is used as power
print 'Sq of No. from 1-10: ',squares
itemList = [1,2,3,4,5]
multiplied = [item*10 for item in itemList]
print 'No. multiplied by 10: ',multiplied
#Q. WAP to create list of first letter of list2 in uppercase

nameList = ['ankit','karishma']
upperList = [i[0].upper() for i in nameList ]
print upperList

#now using Filters in List Comprehension
str = 'Value of PI = 3.144'
pi = [i for i in str if i.isdigit()]
print 'Digits in PI =',pi

#this loop will become nested
z= [x+y for x in [10,20,30,40] for y in[20,40,60]]
print z

'''


#MAP
#Applies a function to all the items in an input_list
#map(function_to_apply, list_of_inpuits)
'''
def square(x):
	return x*x
myList = [1,2,3,4,5]
print map(square,myList)

def addingTitle(x):
	return 'Mr. %s' %str(x)
myList = [1,2,3,4,5]
print map(addingTitle,myList)

strings = ['1','2','3']
print map(int,strings)	#typeCasted the strings to int
'''

'''
#Lambda
list1 = [1,2,3,4,5]
squared = map(lambda x:x**2,list1)
print squared
'''

def multiply(x):
	return x*x
def addition(x):
	return x+x

functions=[multiply,addition]

for i in range(5):
	value = map(lambda x:x(i),functions)	#[multiply(i),addition(i)]
	#print value

#Expertise in Lambda function required
#Filter - creates a list of elements for which a function returns true

numList = range(-5,5)
lessThanZero = filter(lambda x: x<0,numList)
print numList
print lessThanZero
