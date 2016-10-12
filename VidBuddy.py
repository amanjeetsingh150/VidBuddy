#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

watch = 'watch'
redirector = 'redirector.googlevideo.com'
youtubeURL = 'https://www.youtube.com'
keepvidURL = 'http://keepvid.com/?url='

print 'Enter the name of the video you want to download!'
command = raw_input()
commands = command
command = command.replace(' ','+')
url = 'https://www.youtube.com/results?search_query='+command
youFile = urllib2.urlopen(url)
youHtml = youFile.read()
youFile.close()

soup = BeautifulSoup(youHtml,'html.parser')
for link in soup.find_all('a',{'class':'yt-uix-sessionlink'}):
	links = link.get('href')
	if watch in links:
		YouLink = youtubeURL+links
		print YouLink
		break	
		
KeepLink = keepvidURL+YouLink
keepFile = urllib2.urlopen(KeepLink)
keepHtml = keepFile.read()
keepFile.close()

soup1 = BeautifulSoup(keepHtml,'html.parser')
for l in soup1.find_all('a',{'class':'l'}):
	li = l.get('href')
	print li
	break
		
f = file('-----Your path---------'+commands+'.mp4', 'w')
url = urllib2.urlopen(li)
print 'Wait, your video is being downloaded'
blocksize = 8192
while True:
	buff = url.read(blocksize)
	if not buff:
		break
	f.write(buff)	
f.close()	
print 'Your video has been downloaded...Enjoy!'		
		
	
	

