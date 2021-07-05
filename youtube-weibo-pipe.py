# TODO: Logging

from __future__ import unicode_literals
import youtube_dl
import shutil

DOWNLOAD_DIR = "download/"

links = []

with open('youtube-links.txt', 'r') as file:
	links = file.readlines()

print(links)
titles = [] 
for idx, link in enumerate(links):
	ydl_opts = {
		# 'writethumbnail': True,
		'outtmpl' : DOWNLOAD_DIR+str(idx)
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([link])
	    info = ydl.extract_info(link, download=False)
	    titles.append(info['title'])
	    t = info['thumbnails'][-1]
	    print(info['thumbnails'])
	    print(t)
	    try:
	    	uf = ydl.urlopen(t['url'])
	    	with open("download/"+str(idx)+"_thumbnail", 'wb') as thumbf:
	    		shutil.copyfileobj(uf, thumbf)
	    except Exception as err:
        	# TODO: logging
        	print(err)


# selenium realm

