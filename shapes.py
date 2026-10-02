class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius**2


class CalculateCircleLengthMixin:
    def calculate_length(self):
        return 2 * super().radius * super().pi


class CircleWithMixin(CalculateCircleLengthMixin, Circle):
    pass


circle_with_mixin = CircleWithMixin(2)
print(circle_with_mixin.calculate_length())
