from pytube import YouTube  
import pytube
import re
import terminal_banner, termcolor, platform, datetime


banner_text = """

█▀▀▄ ░ ░ █▀▀ █░░█ ▀▀█▀▀
█░░█ ▀ ▀ █▀▀ █▄▄█ ░░█░░
▀▀▀░ ░ ░ ▀░░ ▄▄▄█ ░░▀░░

"""
sub_text = "YouTube Playlist Downloader."
dev_info = """
v1.1
Developed by: Pranav Darwai
"""


banner = terminal_banner.Banner(banner_text)
print(termcolor.colored(banner.text,'cyan'), end="")
print(termcolor.colored(sub_text,'white', attrs=['bold']), end = "")
print(termcolor.colored(dev_info,'yellow'))


playlist = pytube.Playlist(input("Enter url : "))
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
folder = 'Downloads\\'+input("Folder Name : ")


for video in playlist.video_urls:
    print(video)
    yt = pytube.YouTube(video)
    try:
        stream = yt.streams.get_by_itag(248)
        print(stream)
        stream.download(folder)
        # print(stream)
    except : 
        stream = yt.streams.get_by_itag(22)
        stream.download(folder)
        print(stream)
       
        
print("done")
