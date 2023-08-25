import pytube

v_list = [ # 下載的網址放這，可一次多部
"'https://youtu.be/UFqFBtr85OA'"
]

download_location = r'C:\Users\USER\Desktop\Python_fangru\youtube_vedio'    # 下載目錄要講清楚
for video_url in v_list :
    yt = pytube.YouTube(video_url)
    print('開始下載')
    stream = yt.streams.filter(res="720p").first()  # filter 過濾器 => 只留下res="720p" .first() 要res="720p"的第一個
    print(stream)
    stream.download(download_location)
    print('下載完成!!')
