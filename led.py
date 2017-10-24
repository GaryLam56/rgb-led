import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
RGB = [18, 23, 12]
for pin in RGB:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

try:
    request = [0, 0, 1]
    while 1:
        # request = raw_input("RGB: ")
        # if(len(request)==3):
        if request == [0, 0, 1]:
            request = [0, 1, 0]
        elif request == [0, 1, 0]:
            request = [0, 1, 1]
        elif request == [0, 1, 1]:
            request = [1, 0, 0]
        elif request == [1, 0, 0]:
            request = [1, 0, 1]
        elif request == [1, 0, 1]:
            request = [1, 1, 0]
        elif request == [1, 1, 0]:
            request = [1, 1, 1]
        else:
            request = [0, 0, 1]

        for x in range(3):
            if int(request[x]) == 1:
                GPIO.output(RGB[x], 0)
            else:
                GPIO.output(RGB[x], 1)
        sleep(.25)
finally:
    GPIO.cleanup()
