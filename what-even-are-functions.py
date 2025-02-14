import math

'''def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply'
        return num1 * num2
performOperation(2, 3, 'sum')

This is *okay,* but in cases like this, it's good to pass a default value for the operation variable:
'''

''' def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2

performOperation(2, 3, 'multiply')'''
# You can also specify the variable you're passing the value to in the function call! Like so:
performOperation(4, 5, operation='multiply')


# The *args argument allows any number of arguments to be passed into a function

# **kwargs handles keyword arguments: performOperation(*args, **kwargs)

# This version of the performOperation() function is designed to be flexible thanks to the *args syntax
def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return math.sum(args)
    if operation == 'multiply':
        return math.prod(args)

