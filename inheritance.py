# A class can extend another class. A child class inherits all of the parent class's attributes
class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} says: Bark!")

    def getLegs(self):
        return self._legs

class Chihuahua(Dog): # The parentheses indicates this class is extending the parent Dog class
    def speak(self):
        print(f'{self.name} says: ARF ARF ARF ARF ARF YAP YAP YAP *shivers*')

    def wagTail(self):
        print(f"{self.name} wags their tail in ANGER")

dog = Chihuahua('Bosco')
dog.speak()
dog.wagTail()


# Extending built-in classes:

myList = list()

class UniqueList(list):

    ''' The problem with the below init function is that it would completely override the parent class's init function.
    
    def __init__(self):
        self.someProperty = "Presents lists with no repeating values!"
        
        
        To fix, do this:'''

    def __init__(self):
        super().__init__()
        self.someProperty = "Gets rid of repeating values in a list!"
    def append(self, item):
        if item in self:
            return
        # self.append(item) -> THIS will lead to infinite recursion because self.append is the append function you just defined in this class!

        # To fix this, use the super() function to call the append function in Python's original list() class:
        super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)