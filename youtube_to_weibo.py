import  download_from_youtube 
from upload_to_weibo import upload_video_to_weibo
import os

from config import VideoDir

download_from_youtube.cleanup()

links = []

with open('youtube-links.txt', 'r') as file:
	links = file.readlines()


titles = download_from_youtube.downloadVideosFromYoutube(links)

v = os.listdir(VideoDir)
v.sort()

for idx, title in  enumerate(titles):
	if (v[idx] != "placeholder.txt"):
		upload_video_to_weibo(v[idx], str(idx)+'.jpg', title)


download_from_youtube.cleanup()