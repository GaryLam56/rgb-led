import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
RGB = [18,23,12]
for pin in RGB:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,1)

try:
	while(1):
		request = raw_input("RGB: ")
		if(len(request)==3):
			for x in range(3):
				if(int(request[x])==1):
					GPIO.output(RGB[x],0)
				else:
					GPIO.output(RGB[x],1)

finally:
	GPIO.cleanup()
