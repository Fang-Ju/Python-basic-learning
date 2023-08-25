print('Hello World')
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)


import random

print(random.randrange(10))
print(random.randrange(10, 20))
print(random.randrange(10, 20, 2))

print(random.randint(1, 10))


#import random

def generate_lottery_numbers(num_sets, num_range, num_per_set):
    lottery_numbers = []

    for _ in range(num_sets):
        numbers = random.sample(range(1, num_range + 1), num_per_set)
        numbers.sort()
        lottery_numbers.append(numbers)

    return lottery_numbers


# 設定樂透號碼組合的數量、號碼範圍、每組號碼數量
num_sets = 5
num_range = 49
num_per_set = 6

# 產生樂透號碼組合
result = generate_lottery_numbers(num_sets, num_range, num_per_set)

# 輸出結果
for i, numbers in enumerate(result):
    print(f"組合 {i + 1}: {numbers}")
