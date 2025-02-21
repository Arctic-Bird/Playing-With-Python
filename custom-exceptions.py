class CustomException(Exception): # The key is in the class name here
    pass # Congrats, you've written a custom exception!

'''def causeError():
    raise CustomException("You called the causeError() function!")

causeError()'''

# Adding Attributes:
class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = "Not found"

class ServerError(HttpException):
    statusCode = 500
    message = "The server errored!"

def raiseServerError():
    raise ServerError()

raiseServerError()