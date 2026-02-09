#write a program to create a class that can calculate the surface area and volume of a solid. THe class should also have a provision to accept the date relevant to the solid
class cube:
    def __init__(self, a):
        self.side = a

    def display(self):
        print(f"SA: {6 * (self.side ** 2)}")
        print(f"vol. : {self.side ** 3}")
s1 = cube(10)
s1.display()


class cuboid:
    def __init__(self, l, b, h):
        self.__lenght = l
        self.__breadth = b
        self.__height = h

    def cuboid_display(self):
        print(f"SA: {2 * (self.__lenght * self.__breadth + self.__breadth * self.__height + self.__lenght * self.__height)}")
        print(f"Vol.: {self.__lenght * self.__breadth * self.__height}")
    
s = cuboid(10,20,40)
s.cuboid_display()


class cylinder:
    def data(self):
        self.radius = float(input("enter the radius: "))
        self.height = float(input("enter the height: "))
    def display(self):
        print(f"SA: {2 * 3.14 * self.radius * (self.radius + self.height)}")
        print(f"Vol.: {3.14 * (self.radius ** 2) * self.height}")
s = cylinder()
s.data()
s.display()

    