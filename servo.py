#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 50)
pwm.start(12)
time.sleep(1.2)
pwm.ChangeDutyCycle(7)
pwm.stop()
GPIO.cleanup()

