import pytube   
import os
import subprocess

v_list = [
"'https://youtu.be/Z67cI0-qJeY'"
]

def onP(stream, chunk, bytes_remaining):
    pass

def onC(stream, file_path):
    fileobj = {}
    fileobj['name'] = os.path.basename(file_path)

    if stream.resolution == '1080p':
        os.rename(fileobj['name'],'video1080.mp4')
    if stream.abr == "128kbps" :
        os.rename(fileobj['name'],'video.mp4')
        str1 = 'ffmpeg -i video.mp4 -c:a libmp3lame -q:a 4 music.mp3'
        subprocess.run(str1, capture_output=True) # capture_output 设为 true，stdout 和 stderr 将会被捕获。
        str1 = 'ffmpeg -i video1080.mp4 -i music.mp3 -acodec copy -vcodec copy mix01.mp4'   # 將 mp3(128kb 轉成 mp3檔的) 和 mp4(1080P) 成 新的 mp4 (我們要的 高清1080P影音檔)
        subprocess.run(str1, capture_output=True)
        os.rename('mix01.mp4',fileobj['name'])
        os.remove('music.mp3')
        os.remove('video.mp4')
        os.remove('video1080.mp4')
        print("1080P mix audio compelete !!")

download_location = r'C:\Users\USER\Desktop\Python_fangru\20230704\2023-07-04 上課錄影'  # 存放位置要和其他用到的音訊軟體放同資料夾
for video_url in v_list :    

    yt = pytube.YouTube(video_url, on_progress_callback=onP,on_complete_callback=onC) # 連結網址，產生一個串流物件
    yt.streams.filter(res="1080p").first().download(download_location)
    yt.streams.filter(abr="128kbps").first().download(download_location)

        