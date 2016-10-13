#!/usr/bin/python
import sys
import urllib
from bs4 import BeautifulSoup
import math

watch = 'watch'
redirector = 'redirector.googlevideo.com'
youtubeURL = 'https://www.youtube.com'
keepvidURL = 'http://keepvid.com/?url='

print 'Enter the name of the video you want to download!'
command = raw_input()
url = 'https://www.youtube.com/results?'+urllib.urlencode({'search_query': command})
print url
youFile = urllib.urlopen(url)
youHtml = youFile.read()
youFile.close()

soup = BeautifulSoup(youHtml, 'html.parser')
for link in soup.find_all('a', {'class': 'yt-uix-sessionlink'}):
	links = link.get('href')
	if watch in links:
		YouLink = youtubeURL+links
		print YouLink
		break

KeepLink = keepvidURL + YouLink
keepFile = urllib.urlopen(KeepLink)
keepHtml = keepFile.read()
keepFile.close()

soup1 = BeautifulSoup(keepHtml, 'html.parser')
for l in soup1.find_all('a', {'class': 'l'}):
	li = l.get('href')
	break

f = file('-----Your path---------'+command+'.mp4', 'w')
url = urllib.urlopen(li)
print 'Wait, your video is being downloaded'
blocksize = 8192
size = url.info().getheaders('Content-Length')[0]
size = float(size)

data_read = 0
while True:
	buff = url.read(blocksize)
	data_read = data_read + blocksize
	if not buff:
		break
	f.write(buff)
	sys.stdout.write("\rDownloaded %s %%" % math.floor(data_read/size*100))
sys.stdout.flush()
print "\n"

f.close()	
print 'Your video has been downloaded...Enjoy!'		
