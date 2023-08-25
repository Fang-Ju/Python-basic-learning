import os

def rename_files(directory, prefix):
    # 取得指定目錄下的所有檔案名稱
    files = os.listdir(directory)  # listdir 將所有檔案名稱放在一個list
    print(type(files))
    files.sort()  # 根據檔案名稱的排序(簡單排序)

    # 依序修改檔案名稱
    for i, file_name in enumerate(files): # 將檔案一個一個跑 並且帶有編號
        # 檢查是否為檔案
        if os.path.isfile(os.path.join(directory, file_name)): # T/F 條件 => os.path.join(directory, file_name 現做 在 去檢查是不是檔案
            # 新的檔案名稱
            new_file_name = f"{prefix}_{i+1:03d}.mp4"  # 修改檔案副檔名和格式  要補0才不會亂掉

            # 修改檔案名稱
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))  # (舊, 新) 將舊檔名改成新檔名

# 指定目錄和前綴字元
directory = r'.\bat'   # 資料在哪裡 (中文的目錄不見得有辦法做)
prefix = 'PhotoShop教學'    # 前面統一的文字 prefix(前綴)

# 執行檔案名稱修改
rename_files(directory, prefix)