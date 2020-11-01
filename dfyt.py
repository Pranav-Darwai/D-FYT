from pytube import YouTube  
import pytube
import re


playlist = pytube.Playlist(input("Enter url : "))
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))


for video in playlist.video_urls:
    print(video)
    yt = pytube.YouTube(video)
    try:
        stream = yt.streams.get_by_itag(248)
        print(stream)
        stream.download('Downloads\\'+input("File Name : "))
        # print(stream)
    except : 
        stream = yt.streams.get_by_itag(22)
        stream.download('Downloads\\'+input("File Name : "))
        print(stream)
       
        
print("done")
