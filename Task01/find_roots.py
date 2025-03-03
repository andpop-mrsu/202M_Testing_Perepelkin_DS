import math

def find_roots(a, b, c):
    if a == 0:
        if b == 0:
            return "Нет решений" if c != 0 else "Бесконечно много решений"
        else:
            x = -c / b
            return [x]
        
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return sorted([root1, root2])
    elif discriminant == 0:
        root = -b / (2*a)
        return [root]
    else:
        return "Нет вещественных корней"
