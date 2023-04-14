s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            print(x, y)