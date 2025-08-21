from Rectangle import *

def main():
    rect1 = Rectangle()
    print("Width:", rect1.get_width())
    print("Height:", rect1.get_height())
    print("Area:", rect1.get_area())
    print("Perimeter:", rect1.get_perimeter())

    rect2 = Rectangle(3, 6)
    print("Width:", rect2.get_width())
    print("Height:", rect2.get_height())
    print("Area:", rect2.get_area())
    print("Perimeter:", rect2.get_perimeter())

main()