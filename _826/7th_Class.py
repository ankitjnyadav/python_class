# Modules and Packages
# Py first searches the file in the current directory 
# Then searches in the directories contained Environmental variable
# To check the list of directories import sys and check sys.path
# to add the filepath during runtime you can do: sys.path.append(r'path')

#To check the location of the module we can simply do
# import os
# print os.__file__


#import
# After import just the namespace gets stored, so in order to access we need to access using the moduleName.function/variable

# To import some particular things from the module
# Partial importing:		from theModule import thisVariableOrFunction
# Multiple importing:	import sys,sys
# this form of import places the object names directly into the caller;s symbol table, any objects that already exits with same name gets overwritten
'''
import sys
string_msg='from the file'
from module1 import string_msg
from module2 import _func1
print string_msg
_func1(4)
#print dir(sys)

'''


# This isnt recommended in large scale production code. This is bit dangerous as we are entering names into the local symbol table
# Unless we know them all well can be confident there wont be any conflict

# from module1 import *
# _func1(4)	#Error	trying to access private memeber, when module imported with '*' 


# When to import members and give a new name for the current file
# from module import Variable as NewVariableName
'''
string ='555555'
from module1 import string_msg as stringMsg, _func1 as fn
print string
print stringMsg
fn(5)
'''

# Inorder to import the module with NewName 
# import module as NewModuleName
'''
import module2 as mod
mod._func1(10)
print mod.string_msg
'''

# In-Built Function
# dir()
# The built-in function dir() returns a list of defined names in a namespace 
'''
import sys
a = 56
print dir()

print __doc__	#prints the README sort of data, first multiple line comment block of the file/module/function is printed
'''


# While importing any file as module it also gets executed if it contains any print statement
#This checkwhether file is standole or imported file
#If imported this condition wont get satisfied as __name__ will contain the name  of module from which it got imported
#if __name__ == '__main__':	

'''
import module1
print __name__				#prints :	__main__
print module1.__name__		#prints :	module1	(module name)
'''

# Reloading a Module
# To achieve this we can simply do: reload(moduleName)

# Python Packages
# As the no of modules grows, it becomes
# difficult to keep track of them all if they are dumped into one location. This is particularly so if they have similar names/functionality.
# You might wis for a means of grouping and organizing them.

# To make Packagesin python 2.x
# it is mandatory to create 
# __init__.py file to make any dir a Package

#Whenever we use a page, first __init__.py file gets executed
'''
import sys
print sys.path
import _826
from _826 import global_var
print global_var
'''

# In order to import all the packages into the package
# Need to mention all the modules into __all__ then only it will import all the modules when 
# from package import * is executed
# __all__ maintains a list 
# __all__ = ['module1','module2']
# Example written in init file.	Please refer that


# Sub-Packages
# Additional dot notation is used to separate package from the subpackage name
# All the subpackages will have their own __init__.py file

#absoulte import
#from pkg.sub_package.ode1 import func

# relative import
# .. jumps one level up; refers to the package one level up
# doesnot work more than two level
