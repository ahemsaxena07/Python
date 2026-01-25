# #classes and objects
# class Employee:
#     def set_data(self, n, a, s):
#         self.name = n
#         self.age = a
#         self.salary = s

#     def display_data(self):
#         print(self.name, self.age, self.salary)

# e1 = Employee()
# e1.set_data('Ramesh', 23, 25000)
# e1.display_data

class person:
    def __init__(self, n, o):
        print('hey im a person')
        self.name = n
        self.occupation = o
    def info(self):
        print(f'{self.name} is the {self.occupation}')
a = person('ahem', 'founder and ceo')
b = person('aditi', 'ahems wife')
a.info()
b.info()