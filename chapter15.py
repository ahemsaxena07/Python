# # def func():
# #     print('hello')
# # def sum(x,y):
# #     print(x + y)
# # f = func
# # f()
# # g = sum
# # g(10,20)

# def sum(x,y,f):
#     print(x + y)
#     f()
# def func():
#     print('hello')
# f = func
# sum(10,20,f)

p = lambda n: n * n * n
q = lambda x, y, z: (x + y + z)/3
r = lambda s: s.lstrip().rstrip().upper()
print(p(3))
print(q(30,40,20))
print(r('  nagpur  '))

lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40]
print((lambda l: sum(l)/len(l))(lst1))
print((lambda l: sum(l)/len(l))(lst2))

d = {'oil': 230, 'clip':150, 'stud': 175, 'nut': 130}
d1 = sorted(d.items(), key = lambda kv: kv[1])
print(d1)

#map()
import math
def fun(n):
    return n * n
lst = [1,2,3,4,5]
m1 = map(math.radians, lst)
m2 = map(math.factorial, lst)
m3 = map(fun, lst)
print(list(m1))
print(list(m2))
print(list(m3))

#filter()
def num(n):
    if n % 5 == 0:
        return True
    else: 
        return False
lst1 = ['A', 'X', '32', 'T', '23', 'B']
l1 = filter(str.isalpha, lst1)
print(list(l1))

lst2 = [5, 10, 15, 18, 27, 25]
l2 = filter(num, lst2)
print(list(l2))

#reduce()
import functools
def getsum(x,y):
    return x + y
def getprod(x,y):
    return x * y
lst = [1,2,3,4,5]
s = functools.reduce(getsum, lst)
p = functools.reduce(getprod, lst)
print(s)
print(p)

def fun():
    print('in fun')
def disp():
    print('in disp')
def msg():
    print('in msg')
lst = [fun, disp, msg]
for f in lst:
    f()

lst1 = [1,2,3,4,5,6]
lst2 = [6,5,4,3,2,1]
l = map(lambda x, y: x + y, lst1, lst2)
print(list(l))

lst1 = [1,2,3,4,5,6,7]
lst2 = list(map(lambda n: n ** 2, lst1))
print(lst2)

def my_map(fun, seq):
    result = []
    for ele in seq:
        result.append(fun(ele))
    return result
lst1 = [1,2,3,4,5,5]
lst2 = list(my_map(lambda n: n ** 2, lst1))
print(lst2)

import operator
lst = [('anil', 21, 80), ('sohail', 20, 90), ('sunil', 20, 91), ('sobha', 18, 93), ('anil', 19, 85),('sobha', 20, 92)]
print(sorted(lst, key = operator.itemgetter(0,1,2)))
print(sorted(lst, key = lambda tpl: (tpl[0], tpl[1], tpl[2])))

d = {'x': 500, 'y': 890, 'z': 5609}
min_keys = min(d.keys(), key = (lambda k: d[k]))
max_keys = max(d.keys(), key = (lambda k: d[k]))
print('maximum value: ', d[max_keys])
print('minimum value: ', d[min_keys])