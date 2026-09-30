import turtle
import math

bob = turtle.Turtle()
print(bob)


def polyline(t, n, length, angle):
    """Рисует n отрезков с заданной длинно length и углами angle
    (в градусах) между ними, t - это черепашка
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def circle(t, r):
    arc(t, r, 360)


polyline(bob, 36, 30, 10)


turtle.mainloop()
