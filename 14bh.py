def lst(n):
    if n == []:
        return n
    if n[0] < 0:
        return [0] + lst(n[1:])
    else:
        return [n[0]] + lst(n[1:])
print(lst([-1, 3, 3, -3]))