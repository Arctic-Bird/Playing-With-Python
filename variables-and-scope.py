# The locals() function

def performOperation(num1, num2, operation='sum'):
    print(locals()) # The variables that are available INSIDE the function!

performOperation(1, 2, operation='multiply')

# The globals() function prints the global variables declared outside of functions, in the main body of your program
# print(globals())

message = 'Hello world!' # This variable was declared in the global scope, so both functions can access it
varA = 2
def function1(varA, varB):
    print(varA) # The local scope always comes first. This statement will therefore print 1.
    print(locals())

def function2(varC, varD):
    print(varA) # Because varA is declared in the global scope, this statement will print 2.
    print(locals())

function1(1, 2)
function2(3, 4)