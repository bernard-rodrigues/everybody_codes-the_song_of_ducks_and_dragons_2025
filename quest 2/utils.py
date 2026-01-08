class Vect:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"

def complex_add(vect1: Vect, vect2: Vect) -> Vect:
    return Vect(vect1.x + vect2.x, vect1.y + vect2.y)

def complex_multiply(vect1: Vect, vect2: Vect) -> Vect:
    return Vect(vect1.x*vect2.x - vect1.y*vect2.y, vect1.x*vect2.y + vect1.y*vect2.x)

def complex_division(vect1: Vect, vect2: Vect) -> Vect:
    return Vect(int(vect1.x/vect2.x), int(vect1.y/vect2.y))