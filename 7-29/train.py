#Train

user = {'username':'super','password':'pwd','type':'admin'}
i=0

def signUp():
	username = raw_input('Enter the username: ')
	password = raw_input('Enter the password: ')
	userType = raw_input('Enter the Type (Admin/User): ')
	temp = {'username':username,'password':password,'type':userType}
	for i in user:
		print i
		print user[i]
		print temp['username']
		print temp['type']
		if user[i]==temp['username']:
			if user.get('type')==temp['type']:
				print 'Account already exits'
				break
			elif user.get('type')!=temp['type']:
				user.update(temp)
				print 'Account Created'
				break
		else:
			continue
	else:
		user.update(temp)
		print 'Account Created' 


def login():
	username = raw_input('Enter the username: ')
	password = raw_input('Enter the password: ')
	userType = raw_input('Enter the Type (Admin/User): ')
	temp = {'username':username,'password':password,'type':userType}
	for i in user:
		if user[i]==temp['username']:
			print 'Login Succesfull'
			break
	else:
		print 'Account doesnot exists.' 
	if(checkUserType(user.get('type'))=='user'):
		print 'Guest user'
		guestUserMenu()

	elif(checkUserType(user.get('type'))=='admin'):
		print 'Admin user'
		adminUserMenu()

def bookTrain(source, dest, seat=None):
	


def guestUserMenu():	
	i=0
	while(i!=3):
		print '#'*35
		print '1. Book A Train'
		print '2. Change password'
		print '3. Exit'
		i = int(raw_input('Please enter your choice: '))
		if(i==1):
			bookTrain('Del','Pune','Upper')
		elif(i==2):
			changePassword()
		elif(i==3):
			exit()
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
			continue

def adminUserMenu():
	i=0
	while(i!=3):
		print '#'*35
		print '1. Add a new Train'
		print '2. Change password'
		print '3. Exit'
		i = int(raw_input('Please enter your choice: '))
		if(i==1):
			addNewTrain()
		elif(i==2):
			changePassword()
		elif(i==3):
			exit()
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
			continue

def checkUserType(type):
	return user.get('type')

def exit():
	print '#'*35, '\nVisit Again.\nThank You!'
	

while(i!=3):
	print '#'*35
	print 'Welcome to Train Reservation Center'
	print '#'*35
	print '1. Log in'
	print '2. Sign Up'
	print '3. Exit'
	i = int(raw_input('Please enter your choice: '))
	if(i==1):
		login()	
	elif(i==2):
		signUp()
	elif(i==3):
		exit()
		break
	else:
		i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
		continue
