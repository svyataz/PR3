import pandas as pd


class game:
    def __init__(self):
        self.__cdb = pd.read_csv("C:/Users/svyat/Desktop/тестирование/PR3/worldcities.csv")
        
    def startGame(self):
        self.__pc = self.__cdb.sample().values[0, 1]
        self.__cdb = self.__cdb[self.__cdb.city_ascii != self.__pc]
        print("start of the game, if you get tired write: I'm done")
        self.gameloop()

    def gameloop(self):
        print("My word: ", self.__pc,
                "\nyou need a city starting with a letter:", 
                self.__pc[-1].upper())
        
        self.__player = input('your word:')

        if self.__player == "I'm done":
            print("End of game, see you")
            return
        
        if self.__cdb[self.__cdb.city_ascii == self.__player].empty:
            print("Game over\nThere is no such city or it has already been used")
            return

        if self.__pc[-1] != self.__player[0].lower():
            print("Game over")
            return
        
        self.__cdb = self.__cdb[self.__cdb.city_ascii != self.__player]
        self.__pc = self.__cdb[self.__cdb['city_ascii'].str[0] == self.__player[-1].upper()].sample().values[0, 1]
        self.__cdb = self.__cdb[self.__cdb.city_ascii != self.__pc]
        self.gameloop()

game_inst = game()
game_inst.startGame()