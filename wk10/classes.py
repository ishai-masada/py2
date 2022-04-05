#####################################################################################
#
# Name:   Ishai Masada
#
# Date:   3/29/22
#
# Purpose:  Use Classes
#
# Functions:       part_one, part_two, part_three, main
#
# Update:   None
#
#####################################################################################

class Student:
    """Represenets a Student"""

    def __repr__(self):
        """Represents the Studenet by its name"""
        return self.name

    def __init__(self, name, grade1, grade2, grade3):
        """Constructs a Student with the given arguments."""
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def get_avg(self):
        """Calculates the average grade"""
        return round((self.grade1 + self.grade2 + self.grade3) / 3)

class Rectangle:
    """Represents a Rectangle."""

    def __repr__(self):
        """Represents the Rectangle by its name."""
        return self.name

    def __init__(self, name, length, width):
        """Constructs a Rectangle with the given arguments."""
        self.name = name
        self.length = length
        self.width = width

    def get_area(self, side_one, side_two):
        """Calculates the area of the Rectangle using its length and width."""
        return side_one * side_two

    def get_peri(self, side_one, side_two):
        """Calculates the perimeter of the Rectangle using its length and width."""
        return 2 * (side_one + side_two)

class Box(Rectangle):
    """Represents a Box."""
    def __repr__(self):
        """Represents the Box by its name"""
        return self.name

    def __init__(self, name, length, width, depth):
        """Constructs a Rectangle with the given arguments."""
        self.name = name
        self.width = width
        self.length = length
        self.depth = depth

    def get_vol(self, width, length, depth):
        """Calculates the volume of the Box using its length, width, and depth."""
        return round(self.width * self.length * self.depth)

    def get_surface_area(self, width, length, depth):
        """Calculates the volume of the Box using its length, width, and depth."""
        surface_area = 2 * ((Rectangle.get_area(self, width, length)) +
                            (Rectangle.get_area(self, depth, width)) +
                            (Rectangle.get_area(self, length, depth)))

        return surface_area

#####################################################################################
#
# Function Name:  part_one
#
# Date:           3/29/22
#
# Purpose:       Use Rectangle Class
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def part_one():
    students = [Student("Rogers", 94, 87, 90), Student("Becca", 89, 98, 91),
                Student("Simon", 96, 82, 100)]

    for student in students:
        print(f"Student: {student}")
        print(f"Average score: {student.get_avg()}")

#####################################################################################
#
# Function Name:  part_two
#
# Date:           3/29/22
#
# Purpose:       Use Box Class
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def part_two():
    rectangles = [Rectangle("Long Rectangle", 4, 10), Rectangle("Sqaure", 6, 6),
                Rectangle("Short Rectangle", 10, 4)]

    for rectangle in rectangles:
        print(f'Name: {rectangle}')
        print(f'Length: {rectangle.length}')
        print(f'Width: {rectangle.width}')
        print(f'Area: {rectangle.get_area(rectangle.width, rectangle.length)}')
        print(f'Perimeter: {rectangle.get_peri(rectangle.width, rectangle.length)}\n')

#####################################################################################
#
# Function Name:  part_three
#
# Date:           3/29/22
#
# Purpose:       Create several different plots
#
# Who called:           main function
#
# Functions:             None
#
# Update:                 None
#
#####################################################################################
def part_three():
    boxes = [Box("Cube", 6, 6, 6), Box("Long Box", 10, 4, 3), Box("Short Box", 4, 10, 3)]
    for box in boxes:
        print('I am the child class!')
        print(f'Name: {box}')
        print(f'Length: {box.length}')
        print(f'Width: {box.width}')
        print(f'Depth: {box.depth}')
        print(f'Surface Area: {box.get_surface_area(box.width, box.length, box.depth)}')
        print(f'Volume: {box.get_vol(box.width, box.length, box.depth)}\n')

#####################################################################################
#
# Function Name:  main
#
# Date:           3/29/22
#
# Purpose:       Call the three functions
#
# Who called:           None
#
# Functions:             part_one, part_two, part_three
#
# Update:                 None
#
#####################################################################################
def main():
    part_one()
    print()
    part_two()
    part_three()

main()
