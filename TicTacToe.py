class TicTacToe:
    def __init__(self):
        self.game_arr = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.player_arr = []
        self.player = open("PlayersDataFile.txt")
        for details in self.player:
            self.player_arr.append(details.split(","))
        self.player.close()    

    def add_new_players(self):
        name     = input("Enter your Name   : ")
        number   = int(input("Enter your Number : "))
        email_id = input("Enter your Emali  : ")

        player = open("PlayersDataFile.txt", "a")
        player.write(name + "," + str(number) + "," + email_id + "," + "0,0" + ",")
        player.write("\n")
        player.close()

    def play(self):
        print("Player 1")
        player_1 = input("Enter your name : ")
        NUMBER_1 = 1
        print("Player 2")
        player_2 = input("Enter your name : ")
        NUMBER_2 = 0
        for i in range(6):
            print(self.game_arr)
            self.player(player_1, NUMBER_1)
            if self.check(NUMBER_1) == "Win":
                print("Player 1 Wins the game")
                self.add_points(player_1)
                break
            if i == 5:
                break
            self.player(player_2, NUMBER_2)
            if self.check(NUMBER_2) == "Win":
                print("Player 2 Wins the game")
                self.add_points(player_2)
                break


    def player(self, name, NUMBER):
        print(name, "It's your turn!")
        while True:
            row    = int(input("Row    : "))
            column = int(input("Column : "))
            if self.game_arr[row][column] == -1:
                self.game_arr[row][column] = NUMBER
                break
            else:
                print("You can't place here")

      

    def check(self, NUMBER):
        indices = [self.game_arr[0][0], self.game_arr[0][1], self.game_arr[0][2], self.game_arr[1][0], self.game_arr[1][1], self.game_arr[1][2], self.game_arr[2][0], self.game_arr[2][1], self.game_arr[2][2]]
        if   indices[0] == NUMBER  and ((indices[1] == NUMBER and indices[2] == NUMBER) or (indices[3] == NUMBER and indices[6] == NUMBER) or (indices[4] == NUMBER and indices[8] == NUMBER)):
            return "Win"
        elif indices[8] == NUMBER  and ((indices[2] == NUMBER and indices[5] == NUMBER) or (indices[6] == NUMBER and indices[7] == NUMBER)):
            return "Win"
        elif indices[4] == NUMBER  and ((indices[6] == NUMBER and indices[2] == NUMBER) or (indices[1] == NUMBER and indices[7] == NUMBER)):
            return "Win"
        else:
            return "Play"
        
    def add_points(self, name):
        for player in self.player_arr:
            if player[0] == name:
                player[3] += 1


    def leader_board():
        pass


def options(): 
    obj = TicTacToe()   
    while True:
        print(" 1. Play\n", "2. Add new player \n", "3. Leader Board \n", "4. Exit \n")
        option = int(input("Select any of the options : "))
        if option == 1:
            obj.play()

        elif option == 2:
            obj.add_new_players()

        elif option == 3:
            obj.leader_board()        

        elif option == 4:
            break

print("\t Tic Tac Toe")
print("")  
options()  