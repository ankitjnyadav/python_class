'''
List
1. Dyanmic
2. Heterogenous
A list is a collection which is ordered and changeable

List - slicing is same as String 
'''

'''
fruitsList=["apple", "banana", "cherry"]
#print fruitsList

groceryList=["Rice", "Milk", "Eggs"]
print len(groceryList)

#type is used to print the type of variable
print type(groceryList)

print(groceryList[0])

'''

'''
list() - constructor
It can be used to create the list

my_list = list(("apple","banana"))
print my_list

# append is used to add the elements
my_list.append("pear")
print my_list

#remove() is used to remove an item
my_list.remove("banana")
print my_list
my_list.remove(my_list[1])
print my_list
print my_list.remove(my_list[-1])
print my_list
''' 

#len() method returns the number of items in a list
#count: returns the number of elements with the specified value
#extend: add the elements of a list, to the end if the current list
#index: returns the index of the first element with the specified value

'''
my_list = ["apple","banana", "pear", "apple"]
print "Length: " , len(my_list)
print "Count of Apple (occurence): ",my_list.count("apple")
print "index of Last Element: ",my_list.index(my_list[-1])

list2 = ['1','2','4']

#Diff between append and extend
my_list.extend(list2)
#my_list.append(list2)
print my_list

'''

'''
#insert: is used to add the element at the specified location
#pop: is used to remove element at specified location
my_list = ["apple","banana", "pear", "orange"]
#my_list.insert(51,"guvava")
my_list.insert(5,"guvava")
#print len(my_list)
my_list.pop(1)
print my_list
'''


'''
#reverse and sort
my_list = [1,2,3,5,4]
my_list.sort()
print my_list
my_list.reverse()
print my_list
'''

'''
#any(): any element is True i.e any element has value 
#all(): all the elements are True 
#i.e all the elements have the value and doesnt have the null value

a=[1,2,3,4,5]
b=[1,2,3,'',5]

print any(a)
print any(b)
print all(a)
print all(b)	
#Can be used when we need to check if any value in the List is not null
'''

'''
#Nested List aka List of List
a = [1,2,3]
b = [7,8,9]
c = [a,b]	#Nesting
print c
print c[0] , c[-1]
'''

'''
#Range
# range(start,stop,step)
# Can be used to generate a random number
print range(4,7)
print range(40,70, 5)
'''

# Q Total Students:5
# Student First names in sorted order
# student Last name reverse word
# Sum of age of students

# student= list((raw_input("Enter the Name, Age, Class : \n")))
# student.append(raw_input("Enter the Name, Age, Class : \n"))
# student.append(raw_input("Enter the Name, Age, Class : \n"))
# student.append(raw_input("Enter the Name, Age, Class : \n"))
# student.append(raw_input("Enter the Name, Age, Class : \n"))


# print student
# print len(student)

'''
Student1 = raw_input("Enter the Name, Age, Class : \n")
Student2 = raw_input("Enter the Name, Age, Class : \n")
Student3 = raw_input("Enter the Name, Age, Class : \n")
Student4 = raw_input("Enter the Name, Age, Class : \n")
Student5 = raw_input("Enter the Name, Age, Class : \n")

studendsList = Student1+""+Student2+""+Student3+""+Student4+""+Student5
print studendsList


Split and all
'''



'''
#Tupple
# A tuple is a collection which is ordered and unchangeable
# Immutable (unchangeable) whereas List is mutable

my_tuple = ("apple", "banana", "pear")
print my_tuple
#print my_tuple[0]="orange"	#Error: List is immutable i.e can't modify value
print len(my_tuple)

myList1 = [1,2,3]
myList2 = [9,8,7]
myNewTuple = ("banana", myList1, myList2, "orange")
print myNewTuple

myList2[-1]=0
print myList2
print myNewTuple

myNewTuple[3][-1]=-1
print myNewTuple

#myNewTuple[3]="changeValue" 
#TypeError: 'tuple' object does not support item assignment

'''

'''
# variable a and b are not to diff variable ... they are storing reference of same list
a = [1,2,3]
b = a
print a
b.append(4)
print a
b1.copy(a)
b1.append

#IQ: diff bw Deep Copy and Shallow copy 
'''

#Sets
# A set is a collection which is unsorded and unindexed
# Set: has a property of only having unique value
#set(): is a constructor like
'''
mySet = {"kiwi", "guvava", "orange"}
mySet = {"kiwi"}
mySet = set(("apple", "banana", "orange"))
mySet.add("cherry")
mySet.add("cherry")
print mySet

setList = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,5]
myNewList = set(setList)
print myNewList
'''

'''
#SetTheory - Union Intersection i.e OR and AND
managers=set(("Yogita","Ankit","Shishir"))
engineers=set(("Ankit",))
#to add a single element we need to explicitly write ','

#To perform AND: &
print managers & engineers

#To perform OR: |
print managers | engineers

#To perform A-B
print managers-engineers

#To perform B-A
print engineers-managers
'''

#Boolean and None Object

