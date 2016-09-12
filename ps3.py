###### this is the third .py file ###########

####### write your code here ##########

#initialisation
name={}
city={}
district={}
state={}
i=0

#take no. of users data in database
count=input('No of Database inputs')

#take database input from user
for i in count:
	name[i]=input('Name of the person')
	city[i]=input('city info')
	district[i]=input('district info')
	state[i]=input('state info')

#now enter the person info which has to be checked in database
name_i=input('Name of the person')
city_i=input('city info')
district_i=input('district info')
state_i=input('state info')

# to modify the database
edit=input('do you want to modify database?[y/n]')
if edit=='y':
	i=i+1
	name[i]=input('Name of the person')
	city[i]=input('city info')
	district[i]=input('district info')
	state[i]=input('state info')

#check whether input info is present in the database
for i in count:
	if name_i==name[i] && city_i==city[i] && district_i==district[i] && state_i==state[i]:
		
		
		
