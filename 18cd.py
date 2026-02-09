class rectangle:
    def data(self):
        self.lenght = float(input("enter the lenght: "))
        self.breadth = float(input("enter the breadth: "))
    def display(self):
        print(f"area: {self.lenght * self.breadth}")
        print(f"perimete: {2*(self.breadth + self.lenght)}")
e = rectangle()
e.data()
e.display()

class circle:
    def data(self):
        self.radius = float(input("enter the radius of circle: "))

    def display(self):
        print(f"area: {3.14 * self.radius ** 2}")
        print(f"perimeter: {2 * 3.14 * self.radius}")
e = circle()
e.data()
e.display()