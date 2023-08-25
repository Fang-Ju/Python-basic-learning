import os

def batch_print_filenames(directory):
    for filename in os.listdir(directory):
        print(filename)

# 指定目錄路徑
directory_path = r"C:\Users\USER\Desktop\Python_fangru\20230705"

# 呼叫函式以列印檔案名稱
batch_print_filenames(directory_path)
