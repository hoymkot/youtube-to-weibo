import youtube_dl
import shutil
import logging
import logging.config
import os
from config import VideoDir
from config import CoverDir
from PIL import Image

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

def downloadVideosFromYoutube(links):
	titles = [] 

	for idx, link in enumerate(links):
		ydl_opts = {
			# 'writethumbnail': True,
			'outtmpl' : VideoDir+ "\\" +str(idx)+".%(ext)s" 
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([link])
		    info = ydl.extract_info(link, download=False)
		    # logger.info(info)
		    titles.append(info['title'])
		    
		    t = info['thumbnails'][-1]
		    try:
		    	uf = ydl.urlopen(t['url'])
		    	file = CoverDir+"\\"+str(idx)+".cover"
		    	with open(file, 'wb') as thumbf:
		    		shutil.copyfileobj(uf, thumbf)

		    	im = Image.open(file)
		    	rgb_im = im.convert('RGB')
		    	rgb_im.save( CoverDir + "\\"+str(idx)+".jpg")
		    except Exception as err:
		    	logger.error(err)

	return titles




def cleanup():
	for f in os.listdir(VideoDir):
	    os.remove(os.path.join(VideoDir, f))
	 
	f = open(VideoDir + "\\placeholder.txt", 'wb')
	f.close()

	for f in os.listdir(CoverDir):
	    os.remove(os.path.join(CoverDir, f))
	f = open(CoverDir + "\\placeholder.txt", 'wb')
	f.close()