# #n取k
# list1=[0,4,8,1] #n
# x=3 #k
# a=1
# list2=[0 for i in range(x)]
#
# for i in range(x):  #計算所有可能性
#     a=a*len(list1)
# list3 = []
# for j in range(a):  #用list2計數
#     list2[x - 1] = j % (len(list1))
#     list2[x - 2] = j // (len(list1))
#     for i in range(x - 2):
#         list2[x - 3 - i] = list2[x - 2 - i] // (len(list1))
#     for i in range(x - 1):
#         list2[x - 2 - i] = list2[x - 2 - i] % (len(list1))
#
#     list3.append(list2)
#     list2 = [0 for i in range(x)] #歸零
# for i in range(a):  #將要刪掉的重複序列標出
#     for j in range(x):
#         for k in range(x):
#             if list3[i][j]==list3[i][k] and k!=j :
#                 list3[i]=[0 for i in range(x)]
# list_del=[]
# for i in range(a):  #抓出要刪除序列的index(倒述)
#     x_sum=0
#     for j in range(x):
#         x_sum=x_sum+list3[a-1-i][j]
#     if x_sum==0:
#         list_del.append(a-1-i)
# for i in range(len(list_del)): #刪除重複序列
#     list3.pop(list_del[i])
#
# final_list=list3
# for i in range(len(list3)):   #將序列轉回題目
#     for j in range(x):
#         final_list[i][j]=list1[list3[i][j]]
# print(final_list)
# print(len(final_list))



# 遞迴運算 演算法 解決 單純排列
def perm(l):
    # Compute the list of all permutations of l

    if len(l) <= 1:
        return [l]

    r = []
    for i in range(len(l)):
        s = l[:i] + l[i + 1:]
        p = perm(s)  # 自我呼叫 => 遞迴運算(演算法)
        for x in p:
            r.append(l[i:i + 1] + x)
    return r

list1=[0,4,8]
result = perm(list1)
print(result)