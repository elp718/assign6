###### this is the first .py file ###########

####### write your code here ##########

#import sys module
import sys
from collections import Counter

#intialise the variables and array
j=0
count=0
k=0
a={}

#store the command line arguments in list
for i in range(len(sys.argv)-1):
	a[j]=sys.argv[i+1]
#	print (a[j])
	j=j+1

#print (a.count(1))
#print (Counter(a))
	
for i in range(len(sys.argv)-1):
	for j in range(len(sys.argv)-1):
		if a[j]==a[i]:
			count=count+1
	print(count,a[i])
	if k < count:
		k = count
#		print(k,a[i])
	count = 0
#	print(k,a[i])
