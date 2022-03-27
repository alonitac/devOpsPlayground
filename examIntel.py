def func2(number=12):
    new = number >> 1
    return new

def func1(number=4):
    new = number << 1
    return new

answer2 = func2()
answer1 = func1(number=3)

if answer1 > answer2:
    print('it is sunny today')
elif answer1 <answer2:
    print('it is cloudy today')
elif answer1 == answer2:
    print('rain is about to start')