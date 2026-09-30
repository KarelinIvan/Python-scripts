def func(start, stop, step):
    """Фунуция принемает на вход три параметра для создания числовой последовательности через range.
    Если число не чётное, то выводим квадрат числа. Иначе выводим число с отрицательным знаком.
    """
    for i in range(start, stop, step):
        if i % 2 != 0:
            print(i**2)
        else:
            print(i * -1)


# func()

a = input().split()

for i in map(
    lambda x: x**2 if x % 2 != 0 else x * -1, range(int(a[0]), int(a[1]), int(a[2]))
):
    print(i)
