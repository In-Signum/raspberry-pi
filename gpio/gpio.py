import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin = 4
GPIO.setup(pin, GPIO.OUT)

print('go go spinning motor')
GPIO.output(pin,1)

time.sleep(3)

print('all done')
GPIO.output(pin,0)
