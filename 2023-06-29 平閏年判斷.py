
year = eval(input('請入年分?') )

print(year)
print(type(year))

if year % 400 == 0:
    print('潤年')
elif year % 400 != 0 and year % 100 == 0:
    print('平年')
elif year % 4 == 0 and year % 100 != 0:
    print('潤年')
else :
    print('平年')

if year % 4 != 0:
    print('平年')
elif year % 100 != 0:
    print('潤年')
elif year % 400 != 0:
    print('平年')
else :
    print('潤年')

