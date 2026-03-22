lst1 = ['ahem', 'x', 'y', 'z', 'm']
lst2 = ['a', 'b', 'c', 'd', 'e']
lst = [a + b for a,b in zip(lst1, lst2)]
print(lst)