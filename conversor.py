import os
import glob
from pytube import YouTube, Playlist
from pydub import AudioSegment


yt_folder = "/home/daniel/Music/yt_folder/"
mp3_folder = "/home/daniel/Music/mp3/"
extension_list = ('*.mp4', '*.webm')

option = input("1 - Playlist | 2 - Single Video\nOption: ")
link = input("Enter the link: ")
error = False

if option == "1":
    print("Baixar Playlist")
    pl = Playlist(link)
    for l in pl:
        yt = YouTube(l)
        try:
            print(yt.streams.filter(only_audio=True, file_extension="webm")[-1].download(yt_folder))
        except:
            print("WEBM ERROR, downloading mp4 instead")
            print(yt.streams.filter(only_audio=True, file_extension="mp4")[-1].download(yt_folder))

if option == "2":
    print("Baixar Video")
    yt = YouTube(link)
    try:
        print(yt.streams.filter(only_audio=True, file_extension="webm")[-1].download(yt_folder))
    except:
        print("WEBM ERROR, downloading mp4 instead")
        print(yt.streams.filter(only_audio=True, file_extension="mp4")[-1].download(yt_folder))


os.chdir(yt_folder)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')

