# VARIABLES:
'''
<var_name> = <value>
Example: num1 = 10
		 name = 'Karishma'

  var num=10
  File "<stdin>", line 1
    var num=10
          ^
SyntaxError: invalid syntax		
'''



#TYPE OF VARIABLE
'''
type(param)
Gives the data type of the param

firstName='Karishma'


type(firstName)
<type 'str'>

float_num = 3.4
float_num
3.4
type(float_num)
<type 'float'>

long_num=1111111111111111111111111111111
long_num
1111111111111111111111111111111L

type(long_num)
<type 'long'>

'''

#CASTING
'''
Converting one type to another type

Example:
		num1 = '10'   //String
		int(num1)	  //Type casted to int

		name = 'Karishma'
		int(name)		//Error as string Karishma cannot be converted to integer
'''
#COMMENTS
'''
Single Line:
				#	

Multiple Lines	
'''
'''

'''
#ARITHMETIC
'''
print 10+2
print 10 + 2 -1 * 5 /2
Python take cares of BODMAS itself
'''

#ISINSTANCE OF
'''
	isinstance(param,type)
	Boolean function:	returns True is param is of type Type
	else False
	//Checking whether the param is of type (type)

	num=10
	name='Shiro'
	print isinstance(num,int)
	print isinstance(name,str)

'''


#REPITITION
'''
print '*' * 10					**********
print 'Karishma'				Karishma
print '*' * 10					**********   (* 10 times)	
print HI * 2					HIHI		 (HI 2 times)

'''

#STRING INDEXING
'''
Strings can be considered as Array
Indexing begins from 0
name = 'Karishma'
name[2]				//r
'''

#SLICING
'''
name = 'Karishma'
name[start:stop:step]
	Indexing begins from 0
	It does not include Stop index

Start : default= 0
Stop: default= End
Step: default= 1
All are optional

Example:
name ='Karishma'
print name[0:5]   //Karis
print name[:5:2]  //[0:5:2] // Krs
print name[::3]	  //[0:0:3] //Kim	

Reverse order print
	print name[::-1]

'''

#PLACE HOLDER
'''
It places any string or any another variable within one string

name,age = 'Karishma' , 22
print 'We at %s are turning %d today' %(name,age)			# We at Karishma are turning 22 today
print 'We at %s are turning %d today' %('Karishma',22)	    # We at Karishma are turning 22 today
print 'We at %s are turning %d today' %(age,name)			# Error print 'We at %s are turning %d today' %(age,name)
															#TypeError: %d format: a number is required, not str
'''


'''
To interpret as it is what you have written, use  r '' 

print 'This is my file: C:\file\name.py'					#This is my file: C:ile
															#ame.py

print r'This is my file: C:\file\name.py' 					#This is my file: C:\file\name.py									

'''


#IN BUILT PYTHON FUNCITONS
'''
1.	strip()		//String function So var.strip() //Removes any whitespaces from bginning and end
		Example: name = '       Karishma'
		>>> name.strip()										//'Karishma'

2.  len()		// Generalised function So len(var) //Length of the var
		Example:
		>>> len(name)											//	15


3.  lower()		//String function // Converts param to lowercase
		Example:
			>>> name.lower()									//'       karishma'


4. upper() 		//String function // Converts param to uppercase
		Example:
			>>> name.upper()									//'       KARISHMA'


5. replace()    // String function //Replaces param1 with param2
				Changes the output only not the original variable
	param.replace(param1,param2)
		Example:
			1. name.replace('Kar','Shiro')
			'       Shiroishma'			

			2. name= 'Good morning morning morning'
			>>> name.replace('morning','night')					//'Good night night night'



6. split('param')		//Splits string according to param given
						Output is array of splitted string
			Example:
				name= 'Good morning morning morning'
				>>> name.split(' ')								//['Good', 'morning', 'morning', 'morning']
		

'''



#INPUT FROM USER
'''
//Stores the output in strinf format

>>> name = raw_input ('Enter your name:')
Enter your name:Karishma
>>> name
'Karishma'

age = raw_input('Enter your age')
Enter your age22
>>> age
'22'
>>> int(age)
22
'''
#PROGRAM 1

name = raw_input('Enter your name: ')
split_name =name.split(' ')
age = int(raw_input('Enter your age:'))
hundred_age = (100 - age) + 2018

print( '=' * 30)
print 'Hello',split_name[0].upper(), split_name[1].lower(), "\n",'You will turn 100 in year', hundred_age 
print( '=' * 30)


#OUTPUT
'''
Enter your name: Karishma TYAGI
Enter your age:22
==============================
Hello KARISHMA tyagi
You will turn 100 in year 2096
==============================
'''


#.pyc File
'''
It is the byte code generated after compiling .py code.
It gets created only when importing of something A is done in something B.
So .pyc will be generated for A only not for B in B's residing folder.

Example:
			2 files - Day2.py and Day2_Pyc_Test.py
			Day2_Pyc_Test.py imports Day2.py
			Run Day2_Pyc_Test.py
			So it will create Day2.pyc in Python Workspace
'''