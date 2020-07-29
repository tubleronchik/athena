#!/usr/bin/env python3
import rospy
import requests
import re
from std_msgs.msg import String
import time


def tag(url):
    begin = "count"
    end = "page_info"
    request = (requests.get(url)).text
    beg_ind = request.find(begin)+len(begin)
    end_ind = request.find(end)
    count = request[beg_ind:end_ind]
    return (int((re.search('\d+', count)).group()))	

url_tag = 'https://www.instagram.com/explore/tags/tag_name/?__a=1' #link for hashtag

def listener_tags():
		
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('tags', anonymous=True)
	rate = rospy.Rate(10)

	tags = 0
	tags_prev = 0

	while not rospy.is_shutdown():

		tags_prev = tag(url_tag)
		time.sleep(2)
		tags = tag(url_tag) 
		
		if tags_prev < tags:
			beats = "Beats!"
			rospy.loginfo(beats)
			pub.publish(beats)
			rate.sleep()


if __name__ == '__main__':
	try:
		listener_tags()()
	except rospy.ROSInterruptException:
		pass
	

		

		
	


