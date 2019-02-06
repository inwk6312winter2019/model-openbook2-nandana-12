import csv

def acc_areterial(r1,r2):
	count1 = 0
	l1 = []
	l2 =[]
	for i in r1:
		if(i['ACCESSIBLE'] == 'Accessible'):
			l1.append(i['FDMID'])
	for j in r2:
		if (j['ST_CLASS']=='ARTERIAL'):
			l2.append(j['FDMID'])
	
	for e1 in l1:
		for e2 in l2:
			if(e1==e2):
				count1+=1
	return count1

def non_local(r3,r4):
	count2 = 0
	l3 = []
	l4 =[]
	for i in r3:
		if(i['ACCESSIBLE'] == 'Non-Standard'):
			l3.append(i['FDMID'])
	for j in r4:
		if (j['ST_CLASS']=='LOCAL STREET'):
			l4.append(j['FDMID'])
	
	for e3 in l3:
		for e4 in l4:
			if(e3==e4):
				count2+=1
	return count2

def in_minor(r5,r6):
	count3 = 0
	l5 = []
	l6 =[]
	for i in r5:
		if(i['ACCESSIBLE'] == 'Inaccessible'):
			l5.append(i['FDMID'])
	for j in r6:
		if (j['ST_CLASS']=='MINOR COLLECTOR'):
			l6.append(j['FDMID'])
	
	for e5 in l5:
		for e6 in l6:
			if(e5==e6):
				count3+=1
	return count3




f_bus = open("Bus_Stops.csv")
f_street = open("Street_Centrelines.csv")

r1 = csv.DictReader(f_bus)
r2 = csv.DictReader(f_street)

print(acc_areterial(r1,r2))
print(non_local(r1,r2))
print(in_minor(r1,r2))