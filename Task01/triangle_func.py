class IncorrectTriangleSides(Exception):
    """Исключение, выбрасываемое при некорректных длинах сторон треугольника."""
    pass

def get_triangle_type(a, b, c):
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