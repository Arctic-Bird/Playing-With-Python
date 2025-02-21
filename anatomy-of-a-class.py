class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4 # Name and legs are instance attributes: attributes that every instance of the "Dog" class has
        # Notice that self.legs is hard-coded, but you can't access it outside of this class!
    def speak(self):
        print("Woof!")

myDog = Dog('Rover')

# You can move legs above the init function in the class in order to be able to access its value:
class OtherDog:
    legs = 4 # Programmers call variables like this static variables. They cannot be changed with each instance
    def __init__(self, name):
        self.name = name

    # "Getter" method/"get" function:
    def getLegs(self): # "self" doesn't need to be passed into this getter function, but it looks a lot nicer
        return self.legs

    def speak(self):
        print("Bark!")

newDog = OtherDog('Having Said That')

# Underscores as the first value in a variable name conventionally means "mess with at your own risk!"
# Example: _legs = 4
newDog.legs = 3
print(newDog.legs)