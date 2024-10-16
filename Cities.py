import pandas as pd


class game:
    def __init__(self):
        self.__cdb = pd.read_csv("C:/Users/svyat/Desktop/тестирование/PR3/worldcities.csv")
        
    def cdb_setter(self, newdb):
        self.__cdb = newdb

    def cdb_getter(self):
        return  self.__cdb
    
    def pc_setter(self, newpc):
        self.__pc = newpc

    def pc_getter(self):
        return  self.__pc
    
    def player_setter(self, newplayer):
        self.__player = newplayer

    def player_getter(self):
        return  self.__player
    
    def startGame(self):
        self.__pc = self.__cdb.sample().values[0, 1]
        self.__cdb = self.__cdb[self.__cdb.city_ascii != self.__pc]
        print("start of the game, if you get tired write: I'm done")
        self.gameloop()

    def players_move(self):
        print("My word: ", self.__pc,
                "\nyou need a city starting with a letter:", 
                self.__pc[-1].upper())
        
        self.__player = input('your word:')

        if self.__player == "I'm done":
            return("End of game, see you")
        if self.__cdb[self.__cdb.city_ascii == self.__player].empty:
            return("Game over\nThere is no such city or it has already been used")
        if self.__pc[-1] != self.__player[0].lower():
            return("Game over")
        
        self.__cdb = self.__cdb[self.__cdb.city_ascii != self.__player]
        return None
    
    def pcs_move(self):
        if(self.__cdb[self.__cdb['city_ascii'].str[0] == self.__player[-1].upper()].empty):
            return("End of game, you won")

        self.__pc = self.__cdb[self.__cdb['city_ascii'].str[0] == self.__player[-1].upper()].sample().values[0, 1]
        self.__cdb = self.__cdb[self.__cdb.city_ascii != self.__pc]
        return None
    
    def gameloop(self):
        buff1 = self.players_move()
        if (buff1 != None):
            print(buff1)
            return
        
        buff2 = self.pcs_move()
        if (buff2 != None):
            print(buff1)
            return
        
        self.gameloop()

game_inst = game()
print(game_inst.startGame())