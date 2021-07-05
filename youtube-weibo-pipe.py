import youtube_dl
import shutil
import logging
import logging.config
import upload_to_weibo
import glob
import os
from PIL import Image
from upload_to_weibo import upload_video_to_weibo



logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


def downloadVideosFromYoutube(links):
	titles = [] 

	for idx, link in enumerate(links):
		ydl_opts = {
			# 'writethumbnail': True,
			'outtmpl' : "videos\\" +str(idx)+".%(ext)s" 
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([link])
		    info = ydl.extract_info(link, download=False)
		    # logger.info(info)
		    titles.append(info['title'])
		    
		    t = info['thumbnails'][-1]
		    try:
		    	uf = ydl.urlopen(t['url'])
		    	file = DOWNLOAD_DIR+str(idx)+".cover"
		    	with open(file, 'wb') as thumbf:
		    		shutil.copyfileobj(uf, thumbf)
		    	im = Image.open(file)
		    	rgb_im = im.convert('RGB')
		    	print(DOWNLOAD_DIR+str(idx)+".jpg")
		    	rgb_im.save( "covers\\"+str(idx)+".jpg")
		    except Exception as err:
		    	logger.error(err)

	return titles

os.mkdir(DOWNLOAD_DIR)

links = []

with open('youtube-links.txt', 'r') as file:
	links = file.readlines()

titles = downloadVideosFromYoutube(links)

v_l = glob.glob("videos\\*")
v_l.sort()

for idx, title in  enumerate(titles):
	upload_video_to_weibo(v[idx], str(idx)+'.jpg', title)

for f in os.listdir(DOWNLOAD_DIR):
    os.remove(os.path.join(dir, f))
 
