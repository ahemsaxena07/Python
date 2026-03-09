# # # #iterators and generators

# # # words = ['A', 'coddle', 'called', 'Molly']
# # # numbers = [10, 20, 30, 40]
# # # for ele in zip(words, numbers):
# # #     print(ele[0], ele[1])
# # # for ele in zip(words, numbers):
# # #     print(*ele)
# # # for w, n in zip(words, numbers):
# # #     print(w, n)
    

# # words = ['A', 'coddle', 'called', 'Molly']
# # numbers = [10, 20, 30, 40]
# # it = zip(words, numbers)
# # lst = list(it)
# # print(lst)

# # it = zip(words, numbers)
# # tpl = tuple(it)
# # print(tpl)

# # it = zip(words, numbers)
# # s = set(it)
# # print(s)

# actual = [1, 0, 1, 1, 0]
# predicted = [1, 0, 0, 1, 0]
# for act, pred in zip(actual, predicted):
#     status = "correct" if act == pred else "wrong"
#     print(f"Actual: {act}, predicted: {predicted} -- {status}")

class dog:
    def __init__(self):
        self.name = "bunny"
    def bark(self):
        print("woof")
d = dog()
print(hasattr(d,"name"))
print(hasattr(d,'bark'))
print(hasattr(d, 'fly'))