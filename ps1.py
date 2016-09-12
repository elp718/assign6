###### this is the first .py file ###########

####### write your code here ##########

#import sys module
import sys
from collections import Counter

#intialise the variables and array
j=0
count=0
a={}

#store the command line arguments in list
for i in range(len(sys.argv)-1):
	a[j]=sys.argv[i+1]
	print (a[j])
	j=j+1

#print (a.count(1))
#print (Counter(a))
	
for c in a:
	print(c)
