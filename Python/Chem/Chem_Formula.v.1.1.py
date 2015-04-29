import string
inputList=0.0
x=True
h, h2='''Type the molecular formula here to find its molar mass:
==>'''.title(), 'Invalid'
while x==True:
	inputList=list(raw_input(h))
	x=False 
	for i in inputList:
		#to check for non lettr or numbr chars in input
		if i in string.ascii_letters or i in string.digits:
			pass
		else:#if i is not s letter or number then repeat
			x=True 
			print h2
	
theList=[]
ascUp, ascLow, ascNum= list(string.ascii_uppercase), list(string.ascii_lowercase), list(string.digits)

for i in inputList:
	if i in ascUp:
 		theList.append(i)
	elif i in ascLow:
		theList[-1]+=((i))
	elif i in ascNum:
		theList[-1]+=((i))
	else: raise(TypeError)
#print theList,'check 1'
liss,lisst='',[]
for i in theList:
	for j in list((i)):
		liss+=str(j)
	lisst.append(liss)
	liss=''
theList=lisst
#print theList,'check2'
theListSep=[]
f=open('atg.txt','r')
fileRead=(f.read())
#print fileRead,'check3a'
listOFelements=fileRead.split('_')
listOFelements[-1]='na'
#print listOFelements,'check3b'

listOFeMass,listOFeName, listOFmult= [],[],[]
#print theList,'check 4'
for i in theList:
	eName,numOFe,hgh='',[],False 
	uyt=-1*(len(i)+1)
	for h in range(-1,uyt,-1):
		if i[h] in list(string.digits):
			numOFe.insert(0,i[h])
			hgh=True 
		elif hgh: 
			eName=''.join(i[0:h+1])
			break 
		else: eName=''.join(i)
	if not hgh:
		numOFe=str(1)
	else:
		numOFe=''.join(numOFe)
	#print eName,'-', numOFe,'check5'
	
	if listOFelements.count(eName.lower())>0:
		tempx=listOFelements.index(eName.lower())
		eMass=listOFelements[tempx-1]
		#print eMass
		eMassTot=float(0.00)
		eMassTot=float(eMass)*float(numOFe)
		listOFmult.append(numOFe)
		listOFeMass.append(eMassTot)
		listOFeName.append(eName)
	else:#print 'olo'
		pass
totalFormMass=0
for i in listOFeMass:
	totalFormMass+=float(i)
print totalFormMass,'g/mol'#'grams per mol'
print 'Would you like to see the math?'
CtheMath=raw_input(' (Yes or No): ')
if 'y' in CtheMath:
	for i in range(len(listOFeMass)):
		print '  ',
		print str(listOFmult[i]).rjust(3),
		print (listOFeName[i]+"'s").rjust(4),
		print '='+ str(listOFeMass[i]).rjust(8)
        

