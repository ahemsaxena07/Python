#WAP to create al list of 5 odd integers. Replace the third element with a list of 4 even integers. flatten, sort and print the list
lst = [i for i in range(10) if i % 2 != 0]
even = [i for i in range(2,9) if i % 2 == 0]
lst[2] = even
print(lst)
flat = []
for item in lst:
    if isinstance(item, list):
        for n in item:
            flat.append(n)
    else:
        flat.append(item)
flat.sort()
print(flat)