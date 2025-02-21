# This is the initial Shape class that Square and Triangle will extend:

class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)


# Square class:

class Square(Shape): # See how it inherits the shape class?
    def printRow(self, i):
        Square.print(self.printChar * self.width)

class Triangle(Shape):
    def printRow(self, i):
        '''for char in range(1, i + 1):
            print(self.printChar * char)
        char += 1 -> This works, but because of the print function in the parent class, it's pretty redundant. You can do this instead:'''
        print(self.printChar * (i + 1))

class SymmetricalTriangle(Shape):
    height = 5
    width = 2 * height

    def printRow(self, i):
        triangleWidth = i * 2 + 1
        padding = int((self.width - triangleWidth) / 2)
        print(' ' * padding + self.printChar * triangleWidth)


myShape = Square()
myOtherShape = Triangle()
myOtherShape.print()

mySymmetricalTriangle = SymmetricalTriangle()
mySymmetricalTriangle.print()