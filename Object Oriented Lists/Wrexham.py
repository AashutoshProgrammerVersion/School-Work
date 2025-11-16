class Player():

    # self.__PlayerNumber string
    # self.__Forename string
    # self.__Surname string
    # self.__Position string
    # self.__CommunityInvolvement real
    # self.__Injured boolean
    def __init__(self, PlayerNumber, Forename, Surname, Position):
        self.__PlayerNumber = PlayerNumber
        self.__Forename = Forename
        self.__Surname = Surname
        self.__Position = Position
        self.__CommunityInvolvement = 0
        self.__Injured = False

    def GetPlayerInfo(self):
        return self.__Forename, self.__Position
    
    def ChangeCommunityInvolvement(self, change):
        self.__CommunityInvolvement += change

    def ChangeInjured(self, Injured):
        self.__Injured = Injured


Wrexham_players = []

with open("Wrexham.txt", "r") as file:

    for i in range(28):
        PlayerNumber = file.readline()
        Forename = file.readline()
        Surname = file.readline()
        Position = file.readline()

        Player_object = Player(PlayerNumber, Forename, Surname, Position)

        Wrexham_players.append(Player_object)

print(Wrexham_players)