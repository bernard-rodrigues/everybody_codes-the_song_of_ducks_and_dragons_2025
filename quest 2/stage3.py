from utils import Vect, complex_add, complex_multiply, complex_division

A = Vect(-79785, -16616)
B = complex_add(A, Vect(1000, 1000))

def verify(vect: Vect):
    # Define a Vect output starting as [0,0]
    output = Vect(0,0)

    # Apply 100 times the following operations
    for _ in range(100):
        # Complex multiply current output with itself
        output = complex_multiply(output, output)
        # Complex divide it by [100000, 100000]
        output = complex_division(output, Vect(100000, 100000))
        # Complex add it with the current point
        output = complex_add(output, vect)
        # Engrave it only if output x and y coordinates are between -1000000 and 1000000 (at ANY iteration)
        if abs(output.x) > 1000000 or abs(output.y) > 1000000:
            return False
    return True

def show_percentage(iterations: int, total: int):
    percent = (iterations * 100) // total
    print(f"\rProgresso: {percent}% [{iterations}/{total}]", end="", flush=True)

# list of points to be engraved
point_list = []

iterations = 0

# Complexidade está alta
for i in range(A.x, B.x + 1, 1):
    for j in range(A.y, B.y + 1, 1):
        point_list.append(Vect(i, j))
    
engraved_points = []

for point in point_list:
    if verify(point):
        engraved_points.append(point)
    iterations += 1
    show_percentage(iterations, 1001*1001)

# Output must be 64369
print(f"\nPoints engraved: {len(engraved_points)}")