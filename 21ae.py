import random
n = int(input("enter a number: "))
lst = [random.randint(0, 50) for a in range(21)]
print(lst)
for i in range(len(lst)):
    if lst[i] == n:
        print(i)


