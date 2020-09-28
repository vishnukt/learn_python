import math


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = length*breadth


class Square:
    def __init__(self, length):
        self.length = length
        self.area = length*length


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi*radius**2


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
        # rect1.length = int(input("Enter Length : "))
        # rect1.breadth = int(input("Enter Breadth : "))
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
