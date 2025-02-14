# Given the triangle() function:

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1) # A little recursion here, I see

# The challenge is to complete the square() function that returns the square of a number using ONLY the triangle() function

# Remember: no multiplication or exponents allowed

# HINT: Two triangles make a square when they're added together
def square(num):
    '''square(4) = triangle(3) + triangle(4) = (3 + 2 + 1) + (4 + 3 + 2 + 1) = 16
    triangle(num - 1) + triangle(num)?'''

    return triangle(num - 1) + triangle(num)

print(square(3)) # Prints 9. Good start!

print(square(4)) # Prints 16. No way it's THAT easy, right?

print(square(5)) # Prints 25. Huh, I guess it is?