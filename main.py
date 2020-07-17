import func
dict={}
func.showList()
sel = int(input())
while sel!=0:
	if sel==1:
		dict = func.addEmployee(dict);
		print(dict[1]['name'])
	elif sel==2:
		dict = func.delEmployee(dict)
	elif sel ==3 :
		dict = func.queryEmployee(dict)
	func.showList()
	sel = int(input())
