import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase):
    def test_equilateral(self):
        """Тест для равностороннего треугольника."""
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

    def test_isosceles(self):
        """Тест для равнобедренного треугольника."""
        self.assertEqual(get_triangle_type(3, 3, 5), "isosceles")
        self.assertEqual(get_triangle_type(5, 3, 5), "isosceles")
        self.assertEqual(get_triangle_type(1, 1, 1.5), "isosceles")

    def test_nonequilateral(self):
        """Тест для разностороннего треугольника."""
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(10, 11, 12), "nonequilateral")

    def test_negative_sides(self):
        """Тест для отрицательных длин сторон."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, -2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, -3)

    def test_zero_sides(self):
        """Тест для нулевых длин сторон."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 2)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 0, 2)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 0)

    def test_inequality_violation(self):
        """Тест для случаев, когда нарушено неравенство треугольника."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 3, 1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 1, 1)

    def test_large_side(self):
        """Тест для случая, когда одна сторона слишком большая."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 10)

    def test_fractional_sides(self):
        """Тест для дробных значений сторон с нарушением неравенства."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0.5, 0.5, 1.5)

if __name__ == "__main__":
    unittest.main()