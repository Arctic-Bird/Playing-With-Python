class NonIntArgumentException(Exception):
    def __init__(self):
        super().__init__("Error: A non-integer argument was passed!")


def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException()
        return func(*args)
    return wrapper

@handleNonIntArguments
def getSum(a, b, c):
    return a + b + c

try:
    result = getSum(1, 'b', 3)
except NonIntArgumentException as e:
    raise e