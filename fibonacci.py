def fibonacci(N):
    """Возвращает все числа Фибоначчи до N включительно."""
    a = 0
    b = 1
    while a <= N:
        yield a
        temp = a
        a = b
        b = temp + b


print(list(fibonacci(50)))
