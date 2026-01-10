def palin(n):
    if len(n) < 2:
        return True
    t = n.lower()
    if t[0] == t[len(n) - 1]:
        return palin(n[1:-1])
    else:
        return False
word = input('enter a word: ')
isit = palin(word)
if True:
    print(f"it is palindrome")
else:
    print(f'it is not palindrome')