import csv

def name_tuple(r):
	for row in r:
		print((row['STR_NAME'],row['FULL_NAME'],row['FROM_STR'],row['TO_STR']))

def hist(r):
	dic = {}
	for row in r:
		dic[row['MAINTENANCE']] = dic.get(row['MAINTENANCE'],0)+1
	print(dic)

def unique_own(r):
	dic = {}
	for row in r:
		dic[row['OWN']] = dic.get(row['OWN'],0)+1
	print(list(dic.keys()))

def street_class(r):
	dic = {}
	st_list = []
	for row in r:
		if row['ST_CLASS'] not in dic:
			st_list.append(row['STR_NAME'])
			dic[row['ST_CLASS']] = row['STR_NAME']
		else:
			st_list.append(row['STR_NAME'])
			dic[row['ST_CLASS']] += row['STR_NAME']+"  "
	for i,j in dic.items():
		print(i," : ",j)

fin = open("Street_Centrelines.csv")
reader = csv.DictReader(fin)
name_tuple(reader)
hist(reader)
unique_own(reader)
street_class(reader)