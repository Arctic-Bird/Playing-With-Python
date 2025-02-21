class WordSet:
    replacePunctuations = ['!', '.', ',', '\'']
    def __init__(self):
        self.words = set()

    def addText(self, text):
        # text = WordSet.cleanText(text)
        text = self.cleanText(text)
        for word in text.split(): # Takes each word in a sentence and puts them into a list
            self.words.add(word)


    '''cleanText is a static method. By getting rid of the 'self' variable, we're saying this is 
    essentially a part of the WordSet class definition itself, rather than something
    associated with every class *instance.*
    They're not dynamic--they are unchanging.'''


    @staticmethod # This is a function decorator. Decorators are a description for your function definition. This tells Python that 'self' cannot be passed into the cleanText function, which means that you can use self.cleanText in the addText function!
    def cleanText(text):
        # Chaining functions. Don't go too overboard with doing this!
        # text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')

        for punc in WordSet.replacePunctuations:
            text = text.replace(punc, '')

        return text.lower()
wordSet = WordSet()
wordSet.addText('Hi, I\'m Colin! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.') # Following along with the video


print(wordSet.words)