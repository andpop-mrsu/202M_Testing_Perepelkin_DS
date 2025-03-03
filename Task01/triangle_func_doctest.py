class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных длинах сторон треугольника."""
    pass

def get_triangle_type(a, b, c):
    """
    Примеры использования:

    >>> get_triangle_type(3, 3, 3)  # Равносторонний треугольник
    'equilateral'

    >>> get_triangle_type(3, 3, 5)  # Равнобедренный треугольник
    'isosceles'

    >>> get_triangle_type(3, 4, 5)  # Разносторонний треугольник
    'nonequilateral'

    >>> get_triangle_type(1, 1, 3)  # Некорректные стороны (нарушение неравенства треугольника)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Сумма длин любых двух сторон должна быть больше третьей стороны.

    >>> get_triangle_type(-1, 2, 3)  # Некорректные стороны (отрицательная длина)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Длины сторон должны быть положительными числами.

    >>> get_triangle_type(0, 2, 2)  # Некорректные стороны (нулевая длина)
    Traceback (most recent call last):
        ...
    IncorrectTriangleSides: Длины сторон должны быть положительными числами.
    """
    # Проверка на корректность длин сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Длины сторон должны быть положительными числами.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Сумма длин любых двух сторон должна быть больше третьей стороны.")

    # Определение типа треугольника
    if a == b == c:
        return "equilateral"  # Равносторонний треугольник
    elif a == b or a == c or b == c:
        return "isosceles"  # Равнобедренный треугольник
    else:
        return "nonequilateral"  # Разносторонний треугольник

if __name__ == "__main__":
    import doctest
    doctest.testmod()