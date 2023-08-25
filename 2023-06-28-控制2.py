
age = eval(input('請問你幾歲?') )

student = input('請問你是不是學生?(y/n)')

print(age,student)
print(type(age))

if age > 20 and student != 'y':
    print('150元')
elif 5 <= age <= 20 and student != 'y':
    print('120元')
elif age >= 5 and student == 'y':
    print('100元')
else :
    print('免費')



if age >= 5 and student != 'y':
    if age > 20:
        print('150元')
    else:
        print('120元')
else:
    if age >= 5:   # if age >= 5 and student == 'y':
        print('100元')
    else:
        print('免費')
