# reverses the number of list that received
def number(n):
    if len(n) <= 1:
        return n
    return n[-1] + number(n[:-1])
lst = input()
final = number(lst)
if final:
    print(f'the reversed list is: {final}')