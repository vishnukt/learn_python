import math

class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = length*breadth

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(length,breadth)

class Square(Shape):
    def __init__(self, length):
        super().__init__(length,length)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius,radius*math.pi)
        #self.area = math.pi*self.area


choice = 1
while choice != 4:
    print("\n[1] Rectangle")
    print("[2] Square")
    print("[3] Circle")
    print("[4] Exit")
    choice = int(input("\nChoice : "))
    if choice == 1:
        rect = Rectangle(
            int(input("Enter Length : ")),
            int(input("Enter Breadth : ")))
        print("Area =", rect.area)
    elif choice == 2:
        sqr = Square(
            int(input("Enter Length : ")))
        print("Area =", sqr.area)
    elif choice == 3:
        cir = Circle(
            int(input("Enter Radius : ")))
        print("Area =", cir.area)
    elif choice == 4:
        exit
    else:
        print("Invalid Option")
