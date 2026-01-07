from utils import Vect, complex_add, complex_multiply, complex_division

R = Vect(0, 0)
A = Vect(151, 50)

# Apply 3 times the following operations
for _ in range(3):
    R = complex_multiply(R, R)
    R = complex_division(R, Vect(10, 10))
    R = complex_add(R, A)

print(R)