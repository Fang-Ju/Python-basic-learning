import fangru0703

print(fangru0703.尖兵)

'''
f = open("尖兵學生資料.txt", 'r')   # 讀取模式
print(f.read())   # 讀中文就發生錯誤
'''

f = open("尖兵學生資料.txt", 'r',encoding="utf-8")   # 讀取模式
name_list = f.read().split('\n')
print(type(name_list))
print(name_list)

name_tuple = tuple(name_list)
print(type(name_tuple))
print(name_tuple)

name_list[6] = '林曉同'
print(name_list)

# name_list[6][2] = '同'
# print(name_list)

name_list.append('林小童')
print(name_list)

# str1 = 'dknfkdnfkslnfdl'
# for item in str1:
#     print(item)


for n,item in enumerate(name_list):
    if item[0] == '張':
        name_list[n] = '王'+item[1:]

print(name_list)

name_list.pop()
print(name_list)

name_list1 = name_list[:]  # 拷貝
name_list2 = name_list[::-1]  # 倒轉
name_list3 = sorted(name_list, reverse=True)  # 排序
name_list4 = sorted(name_list, reverse=False)  # 排序
print(name_list1)
print(name_list2)
print(name_list3)
print(name_list4)