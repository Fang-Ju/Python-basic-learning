import pytube   
import os
import subprocess

v_list = [
"'https://youtu.be/Z67cI0-qJeY'",
]

def onP(stream, chunk, bytes_remaining):     # 參數是模組規定， 會自動傳入資料(無法控制)
    pass   # 什麼都不要 要寫pass

def onC(stream, file_path):   # 影音格式的轉換
    fileobj = {}  # 建立空字典
    fileobj['name'] = os.path.basename(file_path).split('.')[0]+'.mp3'   # 只拿檔名 並 切割(分成檔名和副檔名) => 留下檔名 將副檔名改成 .mp3 => 存到動態新增的 字典 裡 fileobj['name']
    os.rename(os.path.basename(file_path),'video.mp4') # 將當下該首歌改名改成video.mp4
    
    str1 = 'ffmpeg -i video.mp4 -c:a libmp3lame -q:a 4 music.mp3'  # 呼叫 ffmpeg 給他要的參數 將 mp4 轉成 mp3  (video.mp4 -> music.mp3)
    subprocess.run(str1, capture_output=True) # capture_output 设为 true，stdout 和 stderr 将会被捕获。  # 開始執行上一行  # 在subprocess模組 run => 叫電腦去cmd命令提示字元 執行'ffmpeg -i video.mp4 -c:a libmp3lame -q:a 4 music.mp3' 指令
    os.rename('music.mp3',fileobj['name'])   # 將 轉好的 mp3檔(music.mp3) 改名改成 字典裡存的正確名稱
    os.remove('video.mp4')  # 刪除原本的 mp4 檔案 (先前已改過名成 video.mp4)
    print("mp3 download compelete !!")
    
download_location = r'C:\Users\USER\Desktop\Python_fangru\20230704\2023-07-04 上課錄影'
for video_url in v_list :    
    yt = pytube.YouTube(video_url, on_progress_callback=onP,on_complete_callback=onC)
    yt.streams.filter(abr="128kbps").first().download(download_location)
    # 下載結束後會得到 XXX.mp4 (影音檔) ，故要轉成mp3(影音格式的轉換)
        