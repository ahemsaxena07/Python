def lst(n):
    if len(n) == 1:
        return n[0]                
    if len(n) > 0:
        return n[0] + lst(n[1:])
    else:
        return 0
given = [1,2,3,4,5]
divide = lst(given)
final = divide / len(given)
print(final)