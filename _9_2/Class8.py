# Modules and SubModule
# Relative and Abosulte import

# OS: Module
# This module provides a portable way of using OS dependeant functionality


#Important: To check the functions the module contains do check namespace of the module
'''
import os
print os.getenv('OS')							#Get the current OS ver
print os.getcwd()								#Get CurrentWorkingDirectory
path = r'D:\Ethans\Python\_826'	
print os.chdir(path)							#Change the directory
print os.listdir(path)							#List the contents of the directory
#print os.mkdir(path+r'\CreatedThroughConsole')	#Make a new directory
print dir(os)
'''


# OS.Path: Module
# This module implements some useful functions on pathnames
# OS dependant
# For Windows it is : ntpath

#import ntpath
#print dir(ntpath)


# OS.Path 
# OS is a simple module that does magic/work with sys.modules to inject os.path
# On start py loads some modules itself which can be use after importing your code
# It injects sys.modules['os.path'] = path so that you are able to do 'import os.path' as though it was a SubModule
'''
import os.path
import sys
print sys.modules.keys()
print sys.modules['os']
print sys.modules['os.path']
'''


# Some Examples of os.path
'''
import os
path = r'D:\Ethans\Python\_826'
print os.path.isdir(path)			# Returns True: As the path is dir
print os.path.isfile(path)			# Returns False: As the path is dir
print os.path.getsize(path)			# Returns 4096
print os.path.exists(path)			# Returns True: As the path dir exists
print os.path.join(path,'New')		# Adds the New Folder using the current OS specific delimiter
'''

# OS.Walk
# Is of a generator type
'''
import os
#path = r'D:\Ethans\Python\_826'
path = os.getcwd()
for root, dirs, files in os.walk(path, topdown = False):	#By Default topdown = True
	print 'root: %s' %root
	print 'dirs: %s' %dirs
	print 'files: %s' %files

# Other Way
var = os.walk(os.getcwd())
print var.next()


Output:
root: D:\Ethans\Python\_826
dirs: ['CreatedThroughConsole', 'CreatedThroughConsole1']
files: ['7th_Class.py', 'module1.py', 'module1.pyc', 'module2.py', 'module2.pyc', '__init__.py', '__init__.pyc']
root: D:\Ethans\Python\_826\CreatedThroughConsole
dirs: []
files: []
root: D:\Ethans\Python\_826\CreatedThroughConsole1
dirs: []
files: []
'''

# Pickle
# serializes objects so they can be saved to a file, and loaded in a program again later on
# Pickle is used for serializing and de-serializing Python object structures, also called Marshalling or Flattening
# serialization refers to the process of converting an object in memory toa byte stream that can be stored on disk or sent over n/w
# gets stored in binary format i.e not human readable
'''
dict1 = {
	'one':1,
	'two':2,
	'three':3
}

import pickle
file1 = open('pfile','wb')
pickle.dump(dict1,file1)

dict1 = ''
file1.close()
file1 = open('pfile','rb')
dict2 = pickle.load(file1)

print 'Dictionary 1:', dict1
print 'Dictionary 2:', dict2
'''

#Python Command Line Arguments
#Ref: Module getOPTs
# import sys
# print 'You are running script: ',sys.argv[0]



#Shallow Copy And Deep Copy
'''
#Shallow Copy
list1 = [[1,2],['a','b']]
list2 = list1				#Same Object with two references, Hence: id will be same
list3 = list(list1)			#Using contructor creates a Shallow Copy, Hence: id will be diff
print id(list1), id(list2), id(list3)
print 'Printing List3 before modification  : ',list3
list3.append(['x',700])
print 'Printing List3 after modifying List3: ',list3
list1[1][1] = 'Updated'
print 'Printing List3 after modifying List1: ',list3
print id(list1), id(list2), id(list3)
#Note: Adding new element in List1 won't reflect on the List3 whereas, modifying does

#Deep Copy
import copy
list5 = copy.deepcopy(list1)
print list5
print id(list1),id(list3),id(list5)

'''

# Random: Module
# RandInt: Generates a random Int
# Choice: Select any element depending upon the DT/DS provided
# Shuffle: Shuffles the DT/DS inline, orig value gets affected
# RandRange: Works similar as range, in addition it also provied to generate values randomly 
'''
import random
print 'Any random no. b/w 10 and 15: ', random.randint(10,15)
list7 = [1,2,3,4,5,6,7,8,9,10]
print 'Select any element randomly : ', random.choice(list7)
random.shuffle(list7)
print 'Printing the list after shuffling: ', list7
print 'Printing the randRange from:5 till:100 step:20 :', random.randrange(5,100,20)
'''



# Python Debugger: pdb Module
# import pdb,random; pdb.set_trace()
# n(ext)			: execute the current statement
# s(tep)			: execute the step into function
# r(eturn)			: continue execution until the current function returns
# c(ontinue)		: continue execution until a breakpoint is encountered
# u(p)				: move one level up in the stack trace
# d(own)			: move one level down in the stack trace
# p(rint) expr		: print the value of expr
# pp expr			: pretty-print the value of expr
# w(here)			: print the current position (including stack trace)
# l(ist)			: list 11 lines of code around the current lines
# l(ist) first,last : list from first to last line number
# a(rgs)			: print the args of the current function

#Breakpoints
# b(reak)			: show all the breakpoints
# b(reak) lineNumber: set a breakpoint at lineNumber
# b(reak) function 	: set a breakpoint at the first line of function
# b(reak) fn condtn	: set a breakpoint at the first line of function at specific condition

# Manipulation
# !stmt treats stmt as python stmt rather than pdb Command

# disable bpnumber
# enable bpnumber
# Disp == Keep means it is permanent BP	And Enb= yes means this bp is right now enabled
# tbreak allows us to set a temporary breakpoint. This breakpoint goes away as soon as it is hit once
# cl(ear) [bpnumber]
# condition bpnumber new_condtion

# Decorator
def my_decorator(func):
	def wrapper(*arg):
		print 'Will be executing new function'
		func(*arg)
		print 'Done executing new function'
	return wrapper

@my_decorator
def say_hi(str):
	print 'Hi',str


#say_hi('Ankit')

def random1(func):
	def wrapper():
		print '1'
		func()
		print '2'
	return wrapper
#@random1
def say_hi():
	print 'Hi'

say_hi= random1(say_hi)
say_hi()