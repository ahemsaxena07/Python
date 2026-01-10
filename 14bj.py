def string(n):
    if n == "":
        return 0
    if len(n) > 1:
        return 1 + string(n[1:])
    else:
        return 1

stri = "happy to see you" 
final = string(stri)
print(final)   