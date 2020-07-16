#!/usr/bin/python
def showList():
	print("*"*30)
	print('Employee manegement system')
	print(' 1. Add emplyee information')
	print(' 2. Delete employee information')
	print(' 3. Edit employee information')
	print(' 4. Find employee information')
	print(' 5. Display all employee information')
	print(' 6. exit the system')
	print("*"*30)
	print('please input your choice')
def addEmployee(dict):
	ind  = raw_input('please input the index of emplyee: ')
	name = raw_input('please input the name of employee: ')
	age  = raw_input('please input the age of employee: ')
	emInfo = {'name':name,'age':age}
	dict[int(ind)]=emInfo
	return dict
