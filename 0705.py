import random
import pandas


f = open(r"C:\Users\USER\Desktop\python\尖兵名冊.txt", "r",encoding="utf-8")  # 讀取模式
name_list = f.read().split('\n')

dict1 = {}
dict1['學號'] = [ f"{n+1:02d}" for n in range(23) ]
dict1['姓名'] = name_list
dict1['生日'] = [ str(random.randint(1995,2005))+'-'+f"{random.randint(1,12):02d}"+'-'+f"{random.randint(1,30):02d}"  for n in range(23)]
dict1['繪圖'] = [ random.randint(50,100)  for n in range(23) ]
dict1['語言'] = [ random.randint(50,100)  for n in range(23) ]
dict1['科學'] = [ random.randint(50,100)  for n in range(23) ]
dict1['總分'] = [ dict1['繪圖'][n]+dict1['語言'][n]+dict1['科學'][n]  for n in range(23) ]
dict1

dict1['生日'][6] = "1997-08-16"
dict1['生日'][5] = "1994-09-05"

list_總分排序=sorted(dict1['總分'],reverse=True)#從大到小
目前名次 = 1
list_名次 = []
for n,item in enumerate(list_總分排序,start=1) :
    if n == 1 :
        list_名次.append(1)
    else :
        if list_總分排序[n-2] > list_總分排序[n-1] :
            list_名次.append(n)
            目前名次 = n
        else :
            list_名次.append(目前名次)
list1 = []
for n in range(len(dict1['總分'])) :
    i = list_總分排序.index(dict1['總分'][n])
    list1.append(list_名次[i])
dict1['名次'] = list1

list2 = []
for item in dict1['總分'] :
    if item/3 >= 90 :
        list2.append("A")
    elif item/3 >= 80 :
        list2.append("B")
    elif item/3 >= 70 :
        list2.append("C")
    elif item/3 >= 60 :
        list2.append("D")
    else :
        list2.append("E")
dict1['等級'] = list2



df = pandas.DataFrame(dict1)


# 這兩個參數默認都是False  將寫出的英文跟中文對齊
pandas.set_option('display.unicode.ambiguous_as_wide', True)
pandas.set_option('display.unicode.east_asian_width', True)

with open('0705.txt', 'w') as f:

    d = [df]  #將df轉換成字串data
    for i in d:  # 拿取dict1的數據
        i= str (i).split('[]')  # 將字串i 寫入後刪除[]
        f.writelines(i)
    f.close()
