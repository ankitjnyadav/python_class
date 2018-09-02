#array [2,4,1,1,4]
#array [3,2,1,0,4]


#a = [2,4,1,1,4]
a = [3,2,1,0,4]

aLen = len(a)-1
#bLen = len(b)-1

#aStep = aLen


i=0
while (i<=aLen):
	aStep = a[i]
	print 'A[]',a[i]
	i = i + aStep	
	print 'step',aStep
	print 'index',i
	if (i==aLen):
		print "True"
		break
	else:
		print "False"
		