from time import time

date = 500


def measurement_for(date):
    floop = []
    for a in range(1, date):
        for b in range(a, date):
            floop.append(divmod(a, b))


def measurement_compr():
    compr = [divmod(a, b) for a in range(1, date) for b in range(a, date)]


def measurement_gener():
    gener = list(divmod(a, b) for a in range(1, date) for b in range(a, date))


def measurement(func, *args, **kwargs):
    """Измеряет время выполнения функции"""
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "заняло времени:", time() - t)


measurement(measurement_for, date)
measurement(measurement_compr)
measurement(measurement_gener)
