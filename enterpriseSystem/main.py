import func
dict={}
func.showList()
func.readInfo(dict)
sel = int(input())
while True:
	if sel==1:
		dict = func.addEmployee(dict);
	elif sel==2:
		dict = func.delEmployee(dict)
	elif sel ==3:
		dict =func.alterInfo(dict)
	elif sel ==4 :
		dict = func.queryEmployee(dict)
	elif sel==5:
		func.displayEmployee(dict)
	else :
		func.exitSystem(dict)
		break
	func.showList()
	sel = int(input())
