#1
# numbers = 'one', 'two', 'three'
# print(numbers)  # ('one', 'two', 'three') 元組 --> 重點讓人讀資料用，能用的函示很少
# funcs = []
# for n in numbers:
#     funcs.append(lambda: print(n))  # lambda: print(n) --> 代表有一個函式作為物件放進串列裡  # 電腦都認定是print('three') 是電腦記憶體的關西
#     # def _() :
#     #     return print(n)  # 全域變數自動帶進程式裡
#
# for f in funcs:   # 函式呼叫三次的意思
#     f()

'''
# 自己測式的部分
print(funcs)  # [f1, f2, f3] 三個函式
funcs[0]()    # list中的第一個函式 再呼叫()  # -> three
funcs[1]()    # -> three
print(id(funcs[0]))   # 1241938476576  兩個不同位置
print(id(funcs[1]))   # 1241941987904  兩個不同位置

# 全域變數自動帶進程式裡  --> 測試
a = 10
def func() :
    print(a)

func()
'''


# --------上與下程式比較----------

#2
# numbers = 'one', 'two', 'three'
# funcs = []
# for n in numbers:
#     funcs.append(lambda n=n: print(n))  # n(區域變數n) = n(全域變數n)  print(n 區域變數n)
#
# for f in funcs:
#     f()

'''
# 上面程式用自己寫程式的邏輯應該式...
# n = 'one'
n = 'two'
# n = 'three'
def func1(n=n) :  # 預設值給一個變數(全域變數)
    return print(n)

func1(n)

# 但通常部會在參數裡寫 n=n，會寫...
# n = 'one'
n = 'two'
# n = 'three'
def func1(n='one') :  # 預設值給一個值
    return print(n)

func1(n)
'''


# #2程式 相當於 下面
#3
numbers = 'one', 'two', 'three'
funcs = []
for item in numbers:
    funcs.append(lambda n=item: print(n))  # 內定值 第一次 是'one' 第二次是'two' 第三次是'three'
    # 將三個不同的函式物件存在list中 (內容有不同的內定值)
for f in funcs: # 迴圈依序呼叫list中的函式
    f('AAA')  # 因為有內定值呼叫時可以不給參數 也可給
'''
>>>
AAA
AAA
AAA
'''


'''
# 學下面要自及查查看 closure
#0
def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
'''
