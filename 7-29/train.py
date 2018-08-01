#Train

#variable Declaration section
user = {'username':'super','password':'pwd','type':'admin'}
# Schema is - trainNo,src,dest,days{},coachType{},fare{}
trains =  {'trainNo':'1','src':'Pune', 'dest':'Delhi','days':['Mon','Tues'],'coachType':['SL','AC3'],'fare':{'SL':'500','AC3':'9000'}}
#trains =  {'trainNo':None,'src':None, 'dest':None,'days':[None],'coachType':[None],'fare':{None}}
trains_list = [trains,]
i=0
count = 0
#temp=3



def signUp():
	username = raw_input('Enter the username: ')
	password = raw_input('Enter the password: ')
	#userType = raw_input('Enter the Type (Admin/User): ')
	temp = {'username':username,'password':password}
	for i in user:
		if user[i]==temp['username']:
			print 'Account already exits'
			break
		else:
			continue
	else:
		user.update(temp)
		print 'Account Created' 

def showAllTrains():
	printHash()
	#print trains.items()
	for x in trains_list:
		#print x
		print 'TrainNo:',x['trainNo']
		print 'Source:',x['src']#trains.get('src')
		print 'Destination:',x['dest']#trains.get('dest')
		print 'Days:', x['days']#trains.get('days')
		print 'Coaches Present:',x['coachType']#trains.get('coachType')
		print 'Fare:',x['fare']#trains.get('fare')
		print '-'*30
	'''
		print 'TrainNo:',trains.get('trainNo')
		print 'Source:',trains.get('src')
		print 'Destination:',trains.get('dest')
		print 'Days:', trains.get('days')
		print 'Coaches Present:',trains.get('coachType')
		print 'Fare:',trains.get('fare')
	'''

def splitIntoList(tempList):
	return tempList.split()	


def addNewTrain():
	trainNo=raw_input('Enter the trainNo: ')
	src=raw_input('Enter the Source city: ')
	dest=raw_input('Enter the Destination city: ')
	days=raw_input('Enter the Days working: ')
	days=splitIntoList(days)
	coachType=raw_input('Enter the coachTypes: ')
	coachType=splitIntoList(coachType)
	x=0
	fare={}
	while x<len(coachType):
		tempStr = raw_input('Enter the price associated for %s:' %coachType[x]) 
		tempFare = {coachType[x]:tempStr}
		fare.update(tempFare)
		x=x+1 

	tempTrain={'trainNo':trainNo,'src':src,'dest':dest,'days':days,'coachType':coachType,'fare':fare}
	trains_list.append(tempTrain)

def modifyTrainDetails(modifyTrain):
	for x in trains_list:
		if x['trainNo']==modifyTrain:
			#trainNo=raw_input('Enter the trainNo: ')
			src=raw_input('Enter the Source city: ')
			dest=raw_input('Enter the Destination city: ')
			days=raw_input('Enter the Days working: ')
			days=splitIntoList(days)
			coachType=raw_input('Enter the coachTypes: ')
			coachType=splitIntoList(coachType)
			x=0
			fare={}
			while x<len(coachType):
				tempStr = raw_input('Enter the price associated for %s:' %coachType[x]) 
				tempFare = {coachType[x]:tempStr}
				fare.update(tempFare)
				x=x+1 

'''
			print x['trainNo']
			print modifyTrain
			print x['src'],src
			print x['dest'],dest
			print x['days'],days
			print x['coachType'],coachType
			print x['fare'],fare

			x['trainNo']=modifyTrain
			x['src']=src
			x['dest']=dest
			x['days']=days
			x['coachType']=coachType
			x['fare']=fare
'''
			#x={'trainNo':modifyTrain,'src':src,'dest':dest,'days':days,'coachType':coachType,'fare':fare}
			#trains_list.append(tempTrain)
			break
		
	else:
		print 'no train with trainNo: %s found.' %modifyTrain
def login(count):
	username = raw_input('Enter the username: ')
	password = raw_input('Enter the password: ')
	temp = {'username':username,'password':password}
	for i in user:
		if user[i]==temp['username'] and user.get('password')==temp['password']:
			if(checkUserType()!='super'):
				printHash()
				print 'Login Succesfull\n'
				print 'Welcome %s' %temp['username']
				guestUserMenu()

			elif(checkUserType()=='super'):
				printHash()
				print 'Login Succesfull\n'
				print 'Welcome %s user' %temp['username']
				adminUserMenu()
			break
	else:
		count=count+1
		temp=3-count
		print 'Account details not matching.\nPlease try again.'
		if(count<3):
			print 'You have got %d more chance left!' %temp 
			login(count)
		elif(count==3):
			print 'Maximum attemps ...\nTry after some time'

	

#def bookTrain(source, dest, seat=None):
	





def printHash():
	print '#'*30

def guestUserMenu():	
	i=0
	while(i!=3):
		print '#'*35
		print '1. Book A Train'
		print '2. Change password'
		print '3. Log Out'
		i = int(raw_input('Please enter your choice: '))
		if(i==1):
			bookTrain('Del','Pune','Upper')
		elif(i==2):
			changePassword()
		elif(i==3):
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
			continue

def adminUserMenu():
	i=0
	while(i!=3):
		print '#'*35
		print '1. Add a new Train'
		print '2. Modify Train details'
		print '3. Delete specific Train'
		print '4. Change password'
		print '5. Log Out'
		printHash()
		i = int(raw_input('Please enter your choice: '))
		if(i==1):
			addNewTrain()
		elif(i==2):
			modifyTrain=raw_input('Enter the trainNo you want to modify details of: ')
			modifyTrainDetails(modifyTrain)
		elif(i==3):
			showAllTrains()
			print 'Option under Development'
		elif(i==4):
			print 'Option under Development'
			changePassword()
		elif(i==5):
			break
		else:
			i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
			continue

def checkUserType():
	return user.get('username')

def exit():
	print '#'*35, '\nVisit Again.\nThank You!\n'
	

while(i!=3):
	print '#'*35
	print 'Welcome to Train Reservation Center'
	print '#'*35
	print '1. Log in'
	print '2. Sign Up'
	print '3. Exit'
	i = int(raw_input('Please enter your choice: '))
	if(i==1):
		count=0
		login(count)	
	elif(i==2):
		signUp()
	elif(i==3):
		exit()
		break
	else:
		i = int(raw_input('Thats an incorrect choice...\nPlease try again'))
		
