import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты
def test_equilateral_triangle():
    """Проверка создания равностороннего треугольника и работы его методов."""
    triangle = Triangle(3, 3, 3)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 9

def test_isosceles_triangle():
    """Проверка создания равнобедренного треугольника и работы его методов."""
    triangle = Triangle(3, 3, 5)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 11

def test_nonequilateral_triangle():
    """Проверка создания разностороннего треугольника и работы его методов."""
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

# Негативные тесты
def test_negative_sides():
    """Проверка создания треугольника с отрицательными сторонами."""
    with pytest.raises(IncorrectTriangleSides, match="Длины сторон должны быть положительными числами."):
        Triangle(-1, 2, 3)

def test_zero_sides():
    """Проверка создания треугольника с нулевыми сторонами."""
    with pytest.raises(IncorrectTriangleSides, match="Длины сторон должны быть положительными числами."):
        Triangle(0, 2, 2)

def test_inequality_violation():
    """Проверка создания треугольника с нарушением неравенства треугольника."""
    with pytest.raises(IncorrectTriangleSides, match="Сумма длин любых двух сторон должна быть больше третьей стороны."):
        Triangle(1, 1, 3)

def test_large_side():
    """Проверка создания треугольника, где одна сторона слишком большая."""
    with pytest.raises(IncorrectTriangleSides, match="Сумма длин любых двух сторон должна быть больше третьей стороны."):
        Triangle(1, 1, 10)
