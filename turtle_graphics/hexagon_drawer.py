import turtle

bob = turtle.Turtle()
print(bob)


def figure(segment):
    offset_angle = 360 / segment
    for i in range(segment):
        # Задаем смешение черепашки влево
        bob.left(offset_angle)
        triangle()


def triangle(n=3, length=150, corner=120):
    # Рисуем треугольник с постоянными параметрами
    for i in range(n):
        bob.forward(length)
        bob.left(corner)


figure(segment=6)


turtle.mainloop()
