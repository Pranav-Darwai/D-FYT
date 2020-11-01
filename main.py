from pytube import YouTube  
import pytube
import re


playlist = pytube.Playlist('https://www.youtube.com/watch?v=8AX9LandYJU&list=PLQQoSBmrXmrysEaVNia7KVwf85qATIi1V')
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))


for video in playlist.video_urls:
    print(video)
    yt = pytube.YouTube(video)
    try:
        stream = yt.streams.get_by_itag(248)
        print(stream)
        stream.download('D:\\new\\')
        # print(stream)
    except :
        stream = yt.streams.get_by_itag(22)
        stream.download('D:\\new\\')
        print(stream)
        # YouTube(video).streams.filter(res='720p',progressive=True).first().download('G://')
        print("done")
