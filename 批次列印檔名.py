import os

def list_files(directory, output_file):
    with open(output_file, 'w') as file:  # (較安全的)開檔  'w'模式 寫資料 'w'模式沒有檔案會自動開個新檔  file式檔案物件的變數名稱
        for root, dirs, files in os.walk(directory):   # 走房間  # os.walk(directory) 一定是可迭代物件 => 會回傳3個資料
            for filename in files:  # 看此房間的檔案  # 要的是列出來的 檔名
                file.write(os.path.join(root, filename) + '\n')  # 絕對路徑 + 檔名 + 跳行  => 寫進output

# 指定目錄路徑
directory_path = r"C:\Users\USER\Desktop\Python_fangru\20230705"

# 指定輸出文件路徑
output_file_path = r"C:\Users\USER\Desktop\Python_fangru\20230705\output.txt"

# 請用函式生成列表
list_files(directory_path, output_file_path)