names = ['ahem', 'x', 'y']
age = [20, 34, 23]
salary = [4500000, 434390, 290000]

it = zip(names, age, salary)

lst = list(it)
print(lst)

n , a, s = zip(*lst)
print(n)
print(a)
print(s)

#prob 21.5- wap to obtain transpose of a 3 * 4 matrix

mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
it = zip(*mat)
lst = [[] for i in range(4)]
i = 0
for t in it:
    lst[i] = list(t)
    i += 1
print(lst)

#prob 21.6 - WAP to multiply two matrices x(2*3) and y(3*2) using list compr.
x = [[1,2,3], [4,5,6]]
y = [[11,12], [21,22],[31,32]]
l1 = [xrow for xrow in x]
print(l1)
l2 = [(xrow, ycol) for ycol in zip(*y) for xrow in x]
print(l2)
l3 = [[sum(a * b for a, b in zip(xrow, ycol)) for ycol in zip(*y) for xrow in x]]
print(l3)

#prob 21.7 - suppose we have a list of 5 intergers and a tuple of 5 floats. can we zip them
# and obtain an iterator? if yes, how?
integers = [1,2,3,4,5]
float = (1.1, 2.2, 3.3, 4.4, 5.5)
ti = zip(integers, float)
lst = list(ti)
for i, f in lst:
    print(i, f)

#21.8 - create two lists students and marks. Create a dicitonary from these...
lstnames = ['ahem', 'x', 'y', 'z']
lstmarks = [100, 20, 43, 89]
d = {k:v for (k,v) in zip(lstnames, lstmarks)}
print(d)


#prob 21.9-
d = {'rahul':[67, 76, 39], 'sameer':[58,86,78], 'rakesh':[59,70,81]}

lst = [(k,*v) for k,v in d.items()]
print(lst)

lst = [(k,*v) for k,v in sorted(d.items())]
print(lst)

for row in zip(*lst):
    print(row)

for row in zip(*lst):
    print(*row, sep = '\t')