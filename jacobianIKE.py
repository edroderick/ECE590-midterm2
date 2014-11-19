#!/usr/bin/env python

import math
import numpy as np
from numpy.linalg import inv

def jacobianIKE(xg,yg):
	threshold = .001
	alpha = .01

	dt1 = .001
	dt2 = .001
	dt3 = .001

	t1 = 0.00
	t2 = 0.00
	t3 = 0.00

	l1 = .3
	l2 = .2
	l3 = .1
	
	e = 1 	

	while (e > threshold):
		#compute current position
		x = l1*math.cos(t1)+l2*math.cos(t1+t2)+l3*math.cos(t1+t2+t3)
		y = l1*math.sin(t1)+l2*math.sin(t1+t2)+l3*math.sin(t1+t2+t3)
		print 'x= ', x, ' y= ', y

		e = math.sqrt((xg - x)**2+(yg - y)**2)

		#compute error by advancing by dt values and subtracting from goal position
		eX = l1*math.cos(t1+dt1)+l2*math.cos(t1+dt1+t2+dt2)+l3*math.cos(t1+dt1+t2+dt2+t3+dt3) - xg
		eY = l1*math.sin(t1+dt1)+l2*math.sin(t1+dt1+t2+dt2)+l3*math.sin(t1+dt1+t2+dt2+t3+dt3) - yg

		dE = np.array([[eX],[eY]])

		#compute jacobian
		dxt1 = l1*math.cos(t1+dt1)+l2*math.cos(t1+dt1+t2)+l3*math.cos(t1+dt1+t2+t3) - x
		dyt1 = l1*math.sin(t1+dt1)+l2*math.sin(t1+dt1+t2)+l3*math.sin(t1+dt1+t2+t3) - y
		dxt2 = l1*math.cos(t1)+l2*math.cos(t1+t2+dt2)+l3*math.cos(t1+t2+dt2+t3) - x
		dyt2 = l1*math.sin(t1)+l2*math.sin(t1+t2+dt2)+l3*math.sin(t1+t2+dt2+t3) - y
		dxt3 = l1*math.cos(t1)+l2*math.cos(t1+t2)+l3*math.cos(t1+t2+t3+dt3) - x
		dyt3 = l1*math.sin(t1)+l2*math.sin(t1+t2)+l3*math.sin(t1+t2+t3+dt3) - y

		J = np.array([[dxt1/dt1, dxt2/dt2, dxt3/dt3],[dyt1/dt1, dyt2/dt2, dyt3/dt3]])
		Jplus = (inv((J.T).dot(J))).dot(J.T)

		dTheta = Jplus.dot(dE)
 
		#calculate new joint angles
		t1 = t1 - dTheta[0,0]*alpha
		t2 = t2 - dTheta[1,0]*alpha
		t3 = t3 - dTheta[2,0]*alpha

		print 'x= ', x, ' y= ', y
	
	return

jacobianIKE(.1,.1)

