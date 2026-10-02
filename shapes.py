class Circle:
    """Класс, представляющий геометрическую фигуру 'Круг'.
    Хранит радиус круга и предоставляет методы для вычисления его площади.
    Число Пи определено как атрибут класса.
    Attributes:
        _pi (float): Константа Пи, используемая для расчетов.
        _radius (float): Радиус круга (защищенный атрибут).
    """

    _pi = 3.14

    def __init__(self, radius):
        # Инициализирует новый экземпляр круга.
        self._radius = radius

    @property
    def radius(self):
        # Возвращает радиус круга.
        return self._radius

    @property
    def pi(self):
        # Возвращает значение числа pi, в расчётах
        return self._pi

    def calculate_area(self):
        # Вычисляет площадь круга по формуле S = π * r².
        return self._pi * self._radius**2


class CalculateCircleLengthMixin:
    """Миксин, добавляющий метод для вычисления длины окружности."""

    def calculate_length(self):
        return 2 * super().radius * super().pi


class CircleWithMixin(CalculateCircleLengthMixin, Circle):
    """Класс круга, расширенный возможностью вычисления длины окружности."""

    pass


circle_with_mixin = CircleWithMixin(2)
print(circle_with_mixin.calculate_length())
