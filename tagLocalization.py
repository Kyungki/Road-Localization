import serial
from serial.serialutil import SerialException
import math
#from correction import * #uncomment this line to use corrected range ang change code as refered below.
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


Writer = animation.writers['ffmpeg']
writer = Writer(fps=4, metadata=dict(artist='Me'), bitrate=1800)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

fig, ax1 = plt.subplots(figsize=(8, 25))
ax1.set(xlim=(-3, 5), ylim=(-1, 20))
ax1.tick_params(labelsize=14)
scat1 = ax1.scatter(0, 0, color='blue',s=50)


anchor1 = "1235"
anchor2 = "1236"
anchor3 = "1237"
sub = "range:"
a1Pos = [0,0] #define the position of Anchor 1235 [x,y]
a2Pos = [0,1.5] #define the position of Anchor 1236 [x,y]
a3Pos = [1.5,1.5] #define the position of Anchor 1237 [x,y]
a1Range = []
a2Range = []
a3Range = []
def distance(x1,x2,y1,y2):
	return math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))

def trilateration(x1,x2,x3,y1,y2,y3,r1,r2,r3):

#	print r1, r2, r3

	xp1 =0
	xp2 =0
	xp3 =0

	yp1 =0
	yp2 =0
	yp3 =0

	############### round 1 ###################

	dx,dy = x2-x1,y2-y1
	d = math.sqrt(dx*dx+dy*dy)
	if d > r1+r2:
		print ("1#1")
		return 'err','err' # no solutions, the circles are separate
	if d < abs(r1-r2):
		print ("1#2")
		return 'err','err' # no solutions because one circle is contained within the other
	if d == 0 and r1 == r2:
		print ("1#3")
		return 'err','err' # circles are coincident and there are an infinite number of solutions

	a = (r1*r1-r2*r2+d*d)/(2*d)
	h = math.sqrt(r1*r1-a*a)
	xm = x1 + a*dx/d
	ym = y1 + a*dy/d
	x11 = xm + h*dy/d
	x12 = xm - h*dy/d
	y11 = ym - h*dx/d
	y12 = ym + h*dx/d

	if (distance(x11,x3,y11,y3) <= distance(x12,x3,y12,y3)):
		xp1 = x11
		yp1 = y11
	else:
		xp1 = x12
		yp1 = y12

	############### round 2 ###################

	dx,dy = x2-x3,y2-y3
	d = math.sqrt(dx*dx+dy*dy)

	if d > r2+r3:
		print ("2#1")
		return 'err','err' # no solutions, the circles are separate
	if d < abs(r2-r3):
		print ("2#2")
		return 'err','err' # no solutions because one circle is contained within the other
	if d == 0 and r2 == r3:
		print ("2#3")
		return 'err','err' # circles are coincident and there are an infinite number of solutions

	a = (r3*r3-r2*r2+d*d)/(2*d)
	h = math.sqrt(r3*r3-a*a)
	xm = x3 + a*dx/d
	ym = y3 + a*dy/d
	x21 = xm + h*dy/d
	x22 = xm - h*dy/d
	y21 = ym - h*dx/d
	y22 = ym + h*dx/d

	if (distance(x21,x1,y21,y1) <= distance(x22,x1,y22,y1)):
		xp2 = x21
		yp2 = y21
	else:
		xp2 = x22
		yp2 = y22

	############### round 3 ###################

	dx,dy = x3-x1,y3-y1
	d = math.sqrt(dx*dx+dy*dy)
	if d > r1+r3:
		print ("3#1")
		return 'err','err' # no solutions, the circles are separate
	if d < abs(r1-r3):
		print ("3#2")
		return 'err','err' # no solutions because one circle is contained within the other
	if d == 0 and r1 == r3:
		print ("3#3")
		return 'err','err' # circles are coincident and there are an infinite number of solutions
	a = (r1*r1-r3*r3+d*d)/(2*d)
	h = math.sqrt(r1*r1-a*a)
	xm = x1 + a*dx/d
	ym = y1 + a*dy/d
	x31 = xm + h*dy/d
	x32 = xm - h*dy/d
	y31 = ym - h*dx/d
	y32 = ym + h*dx/d

	if (distance(x31,x2,y31,y2) <= distance(x32,x2,y32,y2)):
		xp3 = x31
		yp3 = y31
	else:
		xp3 = x12
		yp3 = y32

	lx = [xp1,xp2,xp3]
	ly = [yp1, yp2, yp3]
	x = sum(lx)/len(lx)
	y = sum(ly)/len(ly)


	return x, y
def animate(i):

	while True:
		line = ser.readline()
		vals = line.split()
		print (vals)
		if(anchor1 and sub in vals):
			idx = vals.index(sub)
			value = vals[idx+1]
			rangeValue = float(value)
			print ("anchor1")
			print (rangeValue)
			if(len(a1Range) ==1):
				a1Range[0] = rangeValue  #to use corrected range just do a1Range[0] = correctRange(rangeValue)
			else:
				a1Range.append(rangeValue)  #to use corrected range just do cr = correctRange(rangeValue)
																			#a1Range.append(cr)
		if(anchor2 and sub in vals):
			idx = vals.index(sub)
			value = vals[idx+1]
			rangeValue = float(value)
			print (anchor2)
			print (rangeValue)
			if(len(a2Range) ==1):
				a2Range[0] = rangeValue #to use corrected range just do a2Range[0] = correctRange(rangeValue)
			else:
				a2Range.append(rangeValue)  #to use corrected range just do cr = correctRange(rangeValue)
																			#a2Range.append(cr)
		if(anchor3 and sub in vals):
			idx = vals.index(sub)
			value = vals[idx+1]
			rangeValue = float(value)
			print (anchor3)
			print (rangeValue)
			if(len(a3Range) == 1):
				a3Range[0] = rangeValue  #to use corrected range just do a3Range[0] = correctRange(rangeValue)
			else:
				a3Range.append(rangeValue) #to use corrected range just do cr = correctRange(rangeValue)
																			#a3Range.append(cr)

		if(len(a1Range)>0 and len(a2Range) >0 and len(a3Range)>0):
			x, y = trilateration(a1Pos[0], a2Pos[0], a3Pos[0], a1Pos[1], a2Pos[1], a3Pos[1], a1Range[0], a2Range[0], a3Range[0])
			print ("printing localization")
			print (x, y)
			if (x != 'err' and y != 'err'):
				#xp1 = sum(x1[-3:])/len(x1[-3:])
				scat1.set_offsets(np.c_[x,y])
			
		else:
			print ("no three vals")
			continue

anim = FuncAnimation(fig, animate, interval=10)

plt.show()
