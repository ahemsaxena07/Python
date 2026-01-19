def num(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return num(a % b, b) 
    return num(b, a % b)

final = num(10, 15)
print(final)