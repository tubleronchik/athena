
#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
#time.sleep(5)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 50)
pwm.start(12)
time.sleep(1.2)
pwm.ChangeDutyCycle(7)
pwm.stop()
GPIO.cleanup()
#f = open('data.txt', 'r')
#k = 0
#while True:
#	k_prev = k
#	k = 0
#	for line in f:
#		k += 1
#	if k_prev < k:
#		pwm.ChangeDutyCycle(12)
#		time.sleep(2)
#		pwm.ChangeDutyCycle(7)

