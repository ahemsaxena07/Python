#pascal triangle 
def pascal_triangle(n):
    row = [0]
    z = [1]
    for x in range(n):
        print(row)
        row = [l + r for l, r in zip(row + z, z + row)]
pascal_triangle(5)