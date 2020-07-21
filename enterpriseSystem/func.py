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
	if int(ind) in dict.keys():
		print('the index of emplyee already exists')
		return dict
	emInfo = {'name':name,'age':age}
	dict[int(ind)]=emInfo
	return dict
def delEmployee(dict):
	ind=raw_input('please input the index of the employee you want to delete?: ')
	ind = int(ind)
	if ind not in dict:
		print('the index of the employee does not exist.')
		return dict
	del dict[ind]
	print('delete successfully')
	return dict
def queryEmployee(dict):
	ind = raw_input('please input the index of the employee you want to query: ')
	print('the name of the employee is '+dict[int(ind)]['name']+',the age of the employee is '+dict[int(ind)]['age'])
	return dict

def alterInfo(dict):
	ind = raw_input('please input the index of the employee you want to alter: ')
	ind = int(ind)
	name = raw_input('please input the new name of the employee: ')
	age  = raw_input('please input the new age of the employee: ')
	dict[ind]['name']=name
	dict[ind]['age']=age
	return dict

def exitSystem(dict):
	with open('employee.txt','w+') as fw:
		for i in dict.keys():
			fw.write(dict[i]['name']+' '+dict[i]['age'])
			fw.write('\n')

def displayEmployee(dict):
	for i in dict.keys():
		print('No.'+str(i)+': name: '+dict[i]['name']+',  age:'+dict[i]['age']+'\n')

def readInfo(dict):
	with open('employee.txt','r') as fr:
		info = fr.readlines()
		ind = 1
		for i in info:
			name,age=i.rstrip('\n').split()
			info = {'name':name,'age':age}
			dict[ind]=info
			ind=ind+1
	return dict




	
