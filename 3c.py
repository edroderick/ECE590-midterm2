#!/usr/bin/env python

import math
import numpy as np
from numpy.linalg import inv

#l = np.array([.3,.2,.1])
#t = np.array([.3664, 1.2862,-.4525])

def FKE(l,t):
	x = 0
	y = 0
	for i in range (0,l.size):
		theta_total = 0
		for k in range(0,i+1):
			theta_total = theta_total + t[k]
		x = x + l[i]*math.cos(theta_total)
		y = y + l[i]*math.sin(theta_total)

	print x, y
	
x, y = FKE(l,t)
print 'x = ', x, ' y= ', y

'''
l1 = .3
l2 = .2
l3 = .1
t = 1.2

x = .3 - .1*math.cos(t)
y = .4 - .1*math.sin(t)

theta2 = math.acos(((x*x)+(y*y)-(l1*l1)-(l2*l2))/(2*l1*l2))
theta1 = math.atan(y/x) - math.acos(((x*x)+(y*y)+(l1*l1)-(l2*l2))/(2*(math.sqrt((x*x)+(y*y))*l1)))
theta3 = t - theta1 - theta2
'''

#print 't1 = ', theta1 , ' t2 = ', theta2, ' t3 = ', theta3

