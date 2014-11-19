#!/usr/bin/env python

import math
import numpy as np
from numpy.linalg import inv

l1 = .3
l2 = .2
l3 = .1
t = 1.2

x = .3 - .1*math.cos(t)
y = .4 - .1*math.sin(t)

theta2 = math.acos(((x*x)+(y*y)-(l1*l1)-(l2*l2))/(2*l1*l2))
theta1 = math.atan(y/x) - math.acos(((x*x)+(y*y)+(l1*l1)-(l2*l2))/(2*(math.sqrt((x*x)+(y*y))*l1)))
theta3 = t - theta1 - theta2


print 't1 = ', theta1 , ' t2 = ', theta2, ' t3 = ', theta3

