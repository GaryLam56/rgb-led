import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
RGB = [18,23,12]
for pin in RGB:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,1)

try:
	i = 0
	while(1):
		#request = raw_input("RGB: ")
		#if(len(request)==3):
		if(i%7==0):
			request = [0,0,1]
		elif(i%7==1):
			request = [0,1,0]
		elif(i%7==2):
			request = [0,1,1]
		elif(i%7==3):
			request = [1,0,0]
		elif(i%7==4):
			request = [1,0,1]
		elif(i%7==5):
			request = [1,1,0]
		else:
			request = [1,1,1]
			
		for x in range(3):
			if(int(request[x])==1):
				GPIO.output(RGB[x],0)
			else:
				GPIO.output(RGB[x],1)
		i = (i+1)%7
		sleep(.25)
finally:
	GPIO.cleanup()
