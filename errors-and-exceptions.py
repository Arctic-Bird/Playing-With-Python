# All errors and exceptions extend the base error class

# Try / Except:

try:
    1 / 0
except Exception as e: # e is the instance of the raised exception
    print(type(e)) # Exceptions and errors are just classes!


# Handling exceptions:
def causeError():
    try:
        return 1 / 0
    #except Exception as e:
        #print(f"Error occurred: {e}")
    except ZeroDivisionError:
        print("Divide by zero error!")
    except TypeError:
        print("There was a type error!")
    finally: # finally statements ALWAYS execute no matter what happens inside the "try" block
        print("This will always execute!")

# The order of except statements matters! Python will look at them top-to-bottom. Put your more general exceptions at the top
causeError()


# Custom decorators:
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("There was a type error!")
        except ZeroDivisionError:
            print("Divide by zero error!")
        except Exception:
            print("There was an error!")
    return wrapper

@handleException
def causeErrorAgain():
    return 1 / 0

causeErrorAgain()

# Raising Exceptions:
def raiseError(integer):
    if integer == 0:
        raise Exception()
    print(integer) # Don't need to bother with an else statement here

raiseError(1)
