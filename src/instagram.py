#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import time
from instpector import Instpector, endpoints


instpector = Instpector()
instpector.login("login", "password")


profile = endpoints.factory.create("profile", instpector)
followers = endpoints.factory.create("followers", instpector)
timeline = endpoints.factory.create("timeline", instpector)

parse_profile = profile.of_user("account")
followers_count = 0
followers_count_prev = 0
post_count = 0

likes = []
likes_prev = []
comments = []
comments_prev = []

def data():
	while not rospy.is_shutdown():

		pub = rospy.Publisher('chatter', String, queue_size=10)
		rospy.init_node('insta', anonymous=True)
		rate = rospy.Rate(10)
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
	
		followers_count = parse_profile.followers_count
		if likes_prev != [] or comments_prev != []:
			for index in range(post_count):
			
				if likes_prev[index] < likes[index] or comments_prev[index] < comments[index] or followers_count_prev < followers_count:
					beats = "Beats!"
                                	rospy.loginfo(beats)
                                	pub.publish(beats)
                                	rate.sleep()

if __name__ == '__main__':
	try:
		data()
	except rospy.ROSInterruptException:
		pass
	
	
