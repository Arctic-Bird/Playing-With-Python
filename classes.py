class Game:
    def __init__(self, name, genre, sp_or_mp):
        self.name = name
        self.genre = genre
        self.mode = sp_or_mp

    def printname(self):
        print("Your game's name is: " + self.name)

    def printgenre(self):
        print("Your game's genre is: " + self.genre)

    def printmode(self):
        print("Is your game single-player or multiplayer (co-op and/or player vs. player)?: " + self.mode)

game_name = input("What is your game's name: ")

game_genre = input("What is your game's genre: ")

game_modes = input("Is your game single-player or multiplayer: ")

my_game = Game(game_name, game_genre, game_modes)

my_game.printname()
my_game.printgenre()
my_game.printmode()