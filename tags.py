#!/usr/bin/env python3
import requests
import re
import time

time.sleep(10)

def tag(url):
	try:
		begin = "count"
		end = "page_info"
		request = (requests.get(url)).text
		beg_ind = request.find(begin)+len(begin)
		end_ind = request.find(end)
		count = request[beg_ind:end_ind]
		return (int((re.search('\d+', count)).group()))	
	except TypeError:
		return 0

url_tag = 'https://www.instagram.com/explore/tags/Athenalives/?__a=1' #link for hashtag


tags = 0
tags_prev = 0
while True:

	f = open('data.txt', 'a')
	tags_prev = tag(url_tag)
	time.sleep(2)
	tags = tag(url_tag)
	if tags_prev < tags:
		beats = "Beats_tags!\n"
		f.write(beats)
	f.close()
