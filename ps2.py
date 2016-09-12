###### this is the second .py file ###########

####### write your code here ##########

import math
import random
#(x,y)=(random.random()*2-1,random.random()*2-1)
#print(x,y)

points = 300
c=0

x = [random.random() for jj in range(points)]
y = [random.random() for xx in x]


for xx, yy in zip(x,y) :
	if xx**2 + yy**2 < 1:
		c=c+1

#sum = 
print (c*100/points)
