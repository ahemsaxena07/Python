# # # # #iterators and generators

# # # # words = ['A', 'coddle', 'called', 'Molly']
# # # # numbers = [10, 20, 30, 40]
# # # # for ele in zip(words, numbers):
# # # #     print(ele[0], ele[1])
# # # # for ele in zip(words, numbers):
# # # #     print(*ele)
# # # # for w, n in zip(words, numbers):
# # # #     print(w, n)
    

# # # words = ['A', 'coddle', 'called', 'Molly']
# # # numbers = [10, 20, 30, 40]
# # # it = zip(words, numbers)
# # # lst = list(it)
# # # print(lst)

# # # it = zip(words, numbers)
# # # tpl = tuple(it)
# # # print(tpl)

# # # it = zip(words, numbers)
# # # s = set(it)
# # # print(s)

# # actual = [1, 0, 1, 1, 0]
# # predicted = [1, 0, 0, 1, 0]
# # for act, pred in zip(actual, predicted):
# #     status = "correct" if act == pred else "wrong"
# #     print(f"Actual: {act}, predicted: {predicted} -- {status}")

# class dog:
#     def __init__(self):
#         self.name = "bunny"
#     def bark(self):
#         print("woof")
# d = dog()
# print(hasattr(d,"name"))
# print(hasattr(d,'bark'))
# print(hasattr(d, 'fly'))

#iterator example
class AvgAdj:
    def __init__(self, data):
        self.__data = data
        self.__len = len(data)
        self.__first = 0
        self.__sec = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__sec == self.__len:
            raise StopIteration
        self.__avg = (self.__data[self.__first] + self.__data[self.__sec]) / 2
        self.__first += 1
        self.__sec += 1
        return self.__avg
lst = [10,20,30,40,50,60,70]
coll = AvgAdj(lst)
for val in coll:
    print(val)

#same example through generator 

def avgadj(data):
    for i in range(0, len(data) - 1):
        yield (data[i] + data[i + 1])/2
lst = [10,20,30,40,50,60,70]
for i in avgadj(lst):
    print(i)

import random
print(max(random.randint(10, 100) for n in range(20)))

print(sum(n * n* n for n in range(20)))