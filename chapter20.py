# # #containership 

# # # class Department:
# # #     def set_department(self):
# # #         self.__id = input("enter department id: ")
# # #         self.__name = input("enter department name: ")

# # #     def display_department(self):
# # #         print("department id: ", self.__id)
# # #         print("department name: ", self.__name)
# # # class Employee:
# # #     def set_employee(self):
# # #         self.__eid = input("enter employee id: ")
# # #         self.__ename = input("enter employee name: ")
# # #         self.__dobj = Department()
# # #         self.__dobj.set_department()

# # #     def display_employee(self):
# # #         print("employee id: ", self.__eid)
# # #         print("employee name: ", self.__ename)
# # #         self.__dobj.display_department()
# # # obj = Employee()
# # # obj.set_employee()
# # # obj.display_employee()

# # #inheritance

# # class index:
# #     def __init__(self):
# #         self._count = 0

# #     def display(self):
# #         print("count =" + str(self._count))

# #     def incr(self):
# #         self._count += 1

# # class NewIndex(index):
# #     def __init__(self):
# #         super().__init__()

# #     def dec(self):
# #         self._count -= 1

# # i = NewIndex()
# # i.incr()
# # i.incr()
# # i.incr()
# # i.display()
# # i.dec()
# # i.display()
# # i.dec()
# # i.display()


# # print(dir(NewIndex))
# # print(dir(index))

# class product:
#     def __init__(self):
#         self.__name = input("enter name of produc: ")
#         self.__price = input("enter the price of product: ")
#     def display_data(self):
#         print(self.__name, self.__price)

# class sales:
#     def __init__(self):
#         self.__salesfigure = [int(x) for x in input('ENTer salses fig: ').split()]

#     def display_sales(self):
#         print(self.__salesfigure)

# class hardwareitem(product, sales):
#     def __init__(self):
#         product.__init__(self)
#         sales.__init__(self)
#         self.__category = input('enter category: ')
#         self.__oem = input('enter oem: ')

#     def display_data(self):
#         product.display_data(self)
#         sales.display_sales(self)
#         print(self.__category, self.__oem)

# hw1 = hardwareitem()
# hw1.display_data()
# hw2 = hardwareitem()
# hw2.display_data()

#diamond problem
class Base:
    def display(self):
        print('in base')
class derived1(Base):
    def display(self):
        print('in derived1')
class derived2(Base):
    def displaye(self):
        print('in derived2')
class der(derived1, derived2):
    def display(self):
        super().display()
        derived1.display(self)
        derived2.display(self)
        print(der.__mro__)
d1 = der()
d1.display()


#abstract classes
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod 
    def draw(self):
        pass

class rectangle(shape):
    def draw(self):
        print('in reactange.draw')

class circle(shape):
    def draw(self):
        print('in circle.draw')

c = circle()
c.draw()


#prob 20.1

class shape:
    pass

class rectangle(shape):
    pass

class circle(shape):
    pass

s = shape()
c = circle()

print(isinstance(s, shape))
print(isinstance(s,rectangle))
print(isinstance(s, circle))
print(issubclass(rectangle, shape))
print(issubclass(circle, shape))

#prob 20.2

class base:
    def __method(self):
        print("in base.__method")

    def func(self):
        self.__method()

class derived(base):
    def __method(self):
        print('in derives __method')
b = base()
b.func()
d = derived()
d.func()