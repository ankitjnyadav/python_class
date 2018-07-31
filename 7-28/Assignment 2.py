#Assignment 2



student = {}
'''
print '#'*30
print '1. Enter details of student'
print '2. Show marks of student'
print '3. Exit'
print '#'*30
i = raw_input('Enter your choice:')
'''
i=0
while i != 3:
	print '#'*30
	print '1. Enter details of student'
	print '2. Show marks of student'
	print '3. Exit'
	print '#'*30
	i = int(raw_input('Enter your choice:'))
	if(i==1):
		name = raw_input('Enter name: ')
		rollNo = int(raw_input('Enter rollNo: '))
		mathsMarks = float(raw_input('Enter Maths marks: '))
		engMarks =  float(raw_input('Enter Eng marks: '))
		student= {rollNo:[name,mathsMarks,engMarks]}
		#print student
	elif(i==2):
		searchKey = int(raw_input('Enter the rollNo: '))
		for stud in student:
			if searchKey == student.has_key(rollNo):
				print '\n'
				print 'Name: %s' %student.get(rollNo)[0]
				print '*'*20
				print 'Maths: %s' %student.get(rollNo)[1]
				print 'English: %s' %student.get(rollNo)[2]
			else:
				print'rollNo not present in Student DataBase'
	elif(i==3):
		print '\n'
		print '*'*30
		print 'Thank You!'
		break
	else:
		i=raw_input('Enter your choice:')
		continue		



#dict.update(temp)