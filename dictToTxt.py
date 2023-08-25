import random
import pandas

# [將資料放進去]
# 【檔案讀取】
openFile = open("尖兵學生資料名字.txt", 'r', encoding="utf-8")
name_list = openFile.read().split('\n')  # 路徑若有中文就會發生錯誤，解決辦法為 增加設定編碼為utf-8

# <<<<< 字典的動態新增結構 >>>>>>
dict1 = {}  # 空字典
generateFunc1 = [f'{n + 1:02d}' for n in range(23)]  # 生成函式
dict1['學號'] = generateFunc1
dict1['姓名'] = name_list

generatorFunc2 = [str(random.randint(1995, 2005)) + "-" + str(f'{random.randint(1, 12):02d}') + "-" +
                  str(f'{random.randint(1, 30):02d}') for n2 in range(23)]
dict1['生日'] = generatorFunc2

generateFunc3 = [f'{random.randint(0, 100):3d}' for n in range(23)]  # 生成函式
dict1['繪圖'] = generateFunc3
generateFunc4 = [f'{random.randint(0, 100):3d}' for n in range(23)]
dict1['語言'] = generateFunc4
generateFunc5 = [f'{random.randint(0, 100):3d}' for n in range(23)]
dict1['科學'] = generateFunc5

scoreSum = [int(dict1['繪圖'][n]) + int(dict1['語言'][n]) + int(dict1['科學'][n]) for n in range(23)]
dict1['總分'] = scoreSum

# 使用pandas才看得懂 字典 =>
# 查看加入總分的表格
df = pandas.DataFrame(dict1)
# print(df)

# <<<<<< 排名 >>>>>>
# 總分排序
list_sumScoreSort = sorted(dict1['總分'], reverse=True)  # 排序從大到小
# 總分記名次
list_rank = []

for n, item in enumerate(list_sumScoreSort, start=1):
    if n == 1:
        list_rank.append(1)
    else:
        if list_sumScoreSort[n - 2] > list_sumScoreSort[n - 1]:
            list_rank.append(n)
            nowRank = n  # 目前名次
        else:
            list_rank.append(nowRank)  # 當同分的時候就讓它跟上一個名次一樣

# print(list_sumScoreSort)
# print(list_rank)

list1 = []
for n in range(len(dict1['總分'])):
    i = list_sumScoreSort.index((dict1['總分'][n]))
    list1.append((list_rank[i]))
dict1['名次'] = list1
# print(dict1)

print("***************** 處理 平均 與 等級 ************************")
list2 = []  # 平均
list3 = []  # 等級
for n in range(len(dict1['總分'])):
    avg = int(dict1['總分'][n]) // 3
    list2.append(avg)

    # 等級90 80 70 60 不及格
    if (avg >= 90):
        list3.append("A")
    elif ((90 > avg) and (avg >= 80)):
        list3.append("B")
    elif ((80 > avg) and (avg >= 70)):
        list3.append("C")
    elif ((70 > avg) and (avg >= 60)):
        list3.append("D")
    else:
        list3.append("E")

dict1['平均'] = list2
dict1['等級'] = list3

df = pandas.DataFrame(dict1)

# 更改其中一個人的生日
dict1['生日'][6] = "1997-08-16"
print(dict1)

print("***************** 寫入檔案 ************************")

# 將字典轉換為字符串
dict_str = str(dict1)

# 開檔案並寫入內容

with open("dicToTxt_keyRow.txt", "w") as file:
    # 列出第一排 key值
    for key, value in dict1.items():
        file.write('{:5s}'.format(str(key)))
    file.write("\n")

    # 列出對應 key 的內容值
    for v in range(len(generateFunc1)):
        for k, value in dict1.items():
            file.write('{:5s}'.format(str(dict1[k][v])))
        file.write("\n")