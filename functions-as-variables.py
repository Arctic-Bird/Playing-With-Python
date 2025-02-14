x = 5 # Variable! These have a variable name and a value associated with them

def x(): # Function! These have a function name (wow!) and some data associated with them
# Functions are represented as objects in Python
    return 5

print(x.__code__.co_varnames) # Prints variable names. In this case, it only prints "()" because there are no variables in x()
print(x.__code__.co_code) # Prints a Python byte object of all lines of instruction in x()

# Functions are just variables associated with some data!

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate 
velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum.'''

def makeLowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.', '-', ',', '*', ';', ':']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewLines(text):
    text = text.replace('\n', ' ')
    return text

def removeShortWords(text):
    return ' '.join((word for word in text.split() if len(word) > 3))

def removeLongWords(text):
    return ' '.join((word for word in text.split() if len(word) < 6))

# You can mix and match the order you perform these functions in by storing them in a list: 
processingFunctions = {makeLowercase, removePunctuation, removeNewLines, removeShortWords}

for func in processingFunctions:
    text = func(text)

print(text)


''' Lambda functions:
You don't need to give functions a name. You can define small functions without variable names like this:'''

(lambda x: x + 3)(5) # No return statement needed. It's implied.and

myList = [{'num': 3}, {'num': 2}, {'num': 1}] # There isn't an obvious numerical way to sort this. This is a good case where a lambda function would come in handy:
sortedList = sorted(myList, key=lambda x: x['num'])
print(sortedList) # Huzzah!