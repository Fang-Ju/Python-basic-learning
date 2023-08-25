import pytube   
# import os    # 內建模組
# import subprocess    # 內建模組


video_url = r"https://youtu.be/VoJraz0Un98"  # 影音網址存在字串變數
# download_location = 'D:/suv/'

yt = pytube.YouTube(video_url)  # 建構式 -> YouTube物件

video_list = yt.streams  # 沒() 較屬性 有()叫函式或方法  # 列出有哪些可以拿取的串流清單
#video_list_length = len(video_list)
print(video_list)

# yt.streams.filter(res="720p").first().download(download_location)

# print(type(video_list[0].audio_codec)) # <class 'str'> mp4a.40.2
# print(video_list[1].audio_codec) # <class 'NoneType'> None

# print(yt.streams.filter(res="1080p").all())
# print(yt.streams.filter(res="1080p")[0])
# print(yt.streams.filter(res="1080p").first())

# yt.streams.filter(res="360p").first().download(download_location)
# yt.streams.filter(res="1080p").first().download(download_location)  # 沒有聲音
# yt.streams.filter(abr="128kbps").first().download(download_location)  # 沒有影像

# ffmpeg -i TAEYEON01.mp4 -i TAEYEON01.mp3 -acodec copy -vcodec copy mix01.mp4
# ffmpeg -i video360.mp4 -c:a libmp3lame -q:a 4 music360.mp3
