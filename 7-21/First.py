'''
#DEFINING MULTIPLE VALUE TO VARIABLE

number1,number2=10,20	#Assigning multiple values in single decleration
print number1
print number2
'''

'''
# DEFINING TYPE

num=10.0	#floar type data
num1=111111111111111111111111111111111111111111	#long type data
num= 3 + 4j #complex type data
print type(num)
print type(num1)
'''

'''
#TYPE CASTING

print "Type Casting now"
stringNum='1';
print "String Number:", stringNum
intNum=int(stringNum)
print "After conversion type is :",type(intNum)

'''

'''
#IS_INSTANCE

print isinstance(1,int) #Checks whether the given value and type matches,
						#if matches returns true otherwise false.
print isinstance(1,float)

print isinstance('Hello',str) #str is the type of string
'''
'''
#Printing things multiple time in single print statement
print '@'*20
print '$'*10 , "\n" + "Ethans" + "\n" , '$'*20

'''
'''
#STRING INDEXING

name='ETHANS'

print name[0]

print name[-1]
'''
'''
#STRING SLICING

#Syntax : string [start:stop:step]

name='HYDRABAD'

print name[2:4]	# O/P: DR
print name[2:8:1] # O/P : DRABAD
print name[::2] # O/P  :HDAA
print name[::]	# O/P : HYDRABAD
print name[::-1]# O/P : DABARDYH Printing in reverse order
'''
'''
#STRING FORMATTING

name,age='Ankit',21
# %d is for digit and %s is for string
print "My name is %s and my age is %d " %(name,18)	#Here name value will be taken from variable but age value will be 18
print "My name is %s and my age is %d " %(name,age)	#it will take value from variables
print "My name is %s and my age is %s " %(name,age)	#Here converting both the values into string
print "My name is %d and my age is %s " %(name,age)	#Here It will give ERROR as we are trying to convert name into integer
'''
'''
#PRINT RAW LINE

print "C:\name\age" #It will take \n as new line character;

print r"C:\name\age" # 'r' stands for raw and it will print the string as it is  

'''
'''
#STRIP FUNCTION()
#Removes spaces from START and END of the string only
name="        Ankit Kumar       " 
print name.strip() #Doesn't change the actual value of the variable
'''
'''
#STRING LENGTH

name ="AHEMDABAD"
print len(name)
'''
'''
#STRING LOWER() UPPER()- These are not inline functions i.e they wont change the actual value of variable

name1 ="AHEMDABAD"
name2="hydrabad"
print name1.lower() 
print name2.upper()
'''
'''
#REPLACE()-Not inline function

greet="Good Morning"
print greet

print greet.replace('Morning','Night')
'''
'''
#SPLIT()-Not inline function

greet='Good Afternoon How are you'
print greet.split(' ')	# create an array of string 
'''
'''
#USER INPUT-Always assign value into string format, Hence we need to type cast wherever necessary

name =raw_input('Enter your name:')
print "Your name is "+ name

'''

#PRACTISE PROBLEM
'''
#EXTRA
import datetime
now = datetime.datetime.now()
currentYear=now.year
print currentYear
'''
name= raw_input("Enter your Name:")
age=raw_input("Enter your age:")

name=name.split( )
print "="*20
print "Hello %s %s" %(name[0].upper(),name[1].lower())
year=2018 + (100-int(age))

print "You will turn 100 in year %d" %(year)
print "="*20
