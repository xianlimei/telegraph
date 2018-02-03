import random
import time
import threading

water_sprinkler=False
option=[True,False]
door=random.choice(option)
windows=random.choice(option)

def timer2(n):
	print "Timer set for "+str(n)+" Minutes."
	print "Please Evacuate!"
	windows=True
	door=True
	
	while n>0:
		n=n-1
		if(n==0):
			water_sprinkler=True
			break
				

print "This is a trial Simulation of a Smoke Detector"
while 1:
	ppm=random.randint(1,500)
	print ppm
	if ppm<70:
		water_sprinkler=False
		continue
	elif ppm>=70 and ppm<150:
		timer = threading.Timer(60.0*60.0, timer2)
		timer.start()
		break
	elif ppm>=150 and ppm<400:
		timer = threading.Timer(10.0*60.0, timer2)
		timer.start()		
		break
	else:
		timer = threading.Timer(4.0*60.0, timer2)
		timer.start()
		break


