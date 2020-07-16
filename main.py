import func
dict={}
func.showList()
sel = int(input())
if sel==1:
	dict = func.addEmployee(dict);
	print(dict[1]['name'])
#elif:
	#func.delEmployee()
