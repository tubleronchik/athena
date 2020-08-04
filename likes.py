#!/usr/bin/env python3
from instpector import Instpector, endpoints
import time 
#import RPi.GPIO as GPIO

time.sleep(10)
#f = open('data.txt', 'a')
#f.write("New_session\n")
instpector = Instpector()
instpector.login("p313617", "BoAthena")

k = 0
profile = endpoints.factory.create("profile", instpector)
followers = endpoints.factory.create("followers", instpector)
timeline = endpoints.factory.create("timeline", instpector)

parse_profile = profile.of_user("losk_p")
followers_count = 0
followers_count_prev = 0
post_count = 0
likes = []
likes_prev = []
comments = []
comments_prev = []

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(13, GPIO.OUT)
#pwm = GPIO.PWM(13, 50)
#pwm.start(9)
#time.sleep(2)
#pwm.ChangeDutyCycle(7)
#f.close()
while True:
	f = open('data.txt', 'a')
	time.sleep(2)
	#f.write(str(k))
	k += 1
	print(k)
	print(likes)
	post_count = 0
	likes_prev = likes
	comments_prev = comments
	likes = []
	comments = []
	followers_count_prev = followers_count
	for post in timeline.of_user(parse_profile.id):
		post_count += 1
		likes.append(post.like_count)
		comments.append(post.comment_count)
	#f.write("\n")
	followers_count = parse_profile.followers_count
	if likes_prev != [] or comments_prev != []:
		for index in range(post_count):
		
			if likes_prev[index] < likes[index] or comments_prev[index] < comments[index] or followers_count_prev < followers_count:
				beats = "Beats!"
				f.write("Beats\n")
				print(beats)
				#pwm.ChangeDutyCycle(9)
				#time.sleep(2)
				#pwm.ChangeDutyCycle(7)
	f.close()

