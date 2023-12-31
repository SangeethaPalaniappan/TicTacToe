import datetime
import random
import time
class TicTacToe:
    def __init__(self):
        self.player_arr = []
        player_det = open("../TicTacToe/PlayersDataFile.txt")
        for details in player_det:
            self.player_arr.append(details.split(","))
        player_det.close()

        self.game_history_arr = []
        game_hist = open("../PycharmProjects/TicTacToe/GameHistory.txt")
        for history in game_hist:
            self.game_history_arr.append(history.split(","))
        game_hist.close()

        
    def add_new_players(self):
        name     = input("Enter your Name   : ")
        number   = int(input("Enter your Number : "))
        email_id = input("Enter your Emali  : ")
        self.player_arr.append([name, number, email_id, "0", "\n"])
        player = open("../PycharmProjects/TicTacToe/PlayersDataFile.txt", "a")
        player.write(name + "," + str(number) + "," + email_id + "," + "0" + ",")
        player.write("\n")
        player.close()

    def play(self):
        n = int(input("n : "))
        game_arr = []   
        for i in range(n): 
            game_arr = [list(range(1 + n * i, 1 + n * (i + 1)))] + game_arr
        for j in range(n):
            for k in range(n):
                game_arr[j][k] = -1
 
        self.print_arr(game_arr)        
        print("Player 1")
        player_1 = input("Enter your name : ")
        NUMBER_1 = 1
        p1_choice = input("Enter your choice(Head/Tail) : ")
        print("Player 2")
        player_2 = input("Enter your name : ")
        NUMBER_2 = 0
        p2_choice = "Head"
        if p1_choice == "Head":
            p2_choice = "Tail"
        print(p2_choice)    

        toss_result = random.randint(0, 1)
        if toss_result == 1:
            print(p1_choice, "\nPlayer_1 wins the toss")
            self.game_running(player_1, p1_choice, player_1, player_2, NUMBER_1, NUMBER_2, game_arr)
            
        else:
            print(p2_choice, "\nPlayer_2 wins the toss")
            self.game_running(player_2, p2_choice, player_2, player_1, NUMBER_2, NUMBER_1, game_arr)

    def game_running(self, player, choice, p1, p2, NUMBER_1, NUMBER_2, game_arr):
        print(player, "wins the toss")
        time =datetime.datetime.now()
        date_time = time.strftime("%c")
        n = len(game_arr) 
        if n % 2 == 0:
            for i in range((n ** 2) // 2):
                if self.game_play(p1, p1, p2, NUMBER_1, game_arr, date_time) == "break":
                    break
                
                if self.game_play(p2, p1, p2, NUMBER_2, game_arr, date_time) == "break":
                    break
        elif n % 2 == 1:
            no_of_iterations = ((n ** 2) // 2) + 1
            for i in range(no_of_iterations):
                if self.game_play(p1, p1, p2, NUMBER_1, game_arr, date_time) == "break":
                    break
                if i == no_of_iterations - 1:
                    self.game_draw_details(p1, p2, date_time)
                    break

                if self.game_play(p2, p1, p2, NUMBER_2, game_arr, date_time) == "break":
                    break        

    def add_to_game_history(self, player, p1, p2, date_time):
        winner = player + " wins the game"
        print(winner)
        self.game_history_arr.append([p1, p2, winner, date_time])
        self.game_history()
        self.add_points(player)

    def game_draw_details(self, p1, p2, date_time):
        print("Match Draw")
        winner = "Match Draw"
        self.game_history_arr.append([p1, p2, winner, date_time])
        self.game_history()

    def get_input(self, name, number ,game_arr):
        print(name, "It's your turn!")
        while True:
            start = time.time()
            row    = int(input("Row    : "))
            column = int(input("Column : "))
            if row >= len(game_arr) or column >= len(game_arr):
                print("Give input within n")
                continue
            if time.time() - start <= 10:
                if game_arr[row][column] == -1:
                    game_arr[row][column] = number
                    self.print_arr(game_arr)
                    if self.undo(row, column, game_arr) != None:
                        continue
                    else:    
                        return None
                else:
                    print("You can't place here")

            else:
                return "Out of time"                        

               

    def game_play(self, player, p1, p2, number, game_arr, date_time):
        input_func = self.get_input(player, number ,game_arr)
        if input_func == None:
            self.print_arr(game_arr) 
        
            if self.check(number ,game_arr) == "Win":
                self.add_to_game_history(player, p1, p2, date_time)
                return "break"

        else:
            print(input_func)
            
            if player != p2:
                player = p2 
            else:
                player = p1    
            self.add_to_game_history(player, p1, p2, date_time)
            return "break"

    def check(self, number ,game_arr):
        n = len(game_arr)
        init = 0
        for i in range(n):
            if game_arr[i][i] == number: 
                init = 1
                
            else:
                init = 0
                break
        if init == 1:
            return "Win" 
        for i in range(n):
            if init == 1 or init == 0:
                for j in range(n):
                    if game_arr[i][j] == number:
                        init = 1
                        if j == n - 1:
                            return "Win"
                    elif init == 0  or init == 1:
                        init = 0
                        break  
 

       
        for i in range(n):
            if init == 1 or init == 0:
                for j in range(n):
                    if game_arr[j][i] == number:
                        init = 1
                        if j == n - 1:
                            return "Win"
                    elif init == 0 or init == 1:
                        init = 0
                        break   
    

                     
        j = n -1
        for i in range(n):
            if game_arr[i][j] == number:
                init = 1
                j -= 1
            else:
                init = 0
                break    
        if init == 1:
            return "Win" 
        
    def add_points(self, name):
        for player in self.player_arr:
            if player[0] == name:
                player[3] = int(player[3]) + 1
                self.over_ride_details()
                break
                
    def over_ride_details(self):
        player = open("../PycharmProjects/TicTacToe/PlayersDataFile.txt", "w")
        for details in self.player_arr:
            player.write(details[0] + "," + details[1] + "," + details[2] + "," + str(details[3])  + ",")
            player.write("\n")
        player.close()            


    def game_history(self):
        game_hist = open("../PycharmProjects/TicTacToe/GameHistory.txt", "w")
        for history in self.game_history_arr:
            game_hist.write(history[0] + "," +  history[1] + "," +  history[2] + "," +  str(history[3] + ",\n"))
        game_hist.close()

    def print_arr(self ,game_arr):
        n = len(game_arr)
        for i in range(n):
            for j in range(n):
                print(game_arr[i][j] , "\t", end = "")
            print("\n")    


    def leader_board(self):
        players_dict = {}
        player_det = open("../PycharmProjects/TicTacToe/PlayersDataFile.txt")
        i = 0
        for details in player_det:
            players_dict[self.player_arr[i][0]] = int(self.player_arr[i][3])
            i += 1
        player_det.close()  
        print("Name", "\t\t", "Score", "\t", "Rank", "\n") 
        sorted_val_arr = list(players_dict.values())
        sorted_val_arr.sort(reverse = True)
        val_arr = list(players_dict.values())
        key_arr = list(players_dict.keys())
        rank = 1
        leader_board_file = open("../PycharmProjects/TicTacToe/LeaderBoardFile.txt", "w")
        for value in range(len(sorted_val_arr)):
            index = val_arr.index(sorted_val_arr[value])
            player = key_arr[index]
            score = val_arr[index]
            players_dict[player] = -1
            val_arr[index] = -1
            leader_board_file.write(player + " - " + str(score) + " - " + str(rank) +"\n")
            print(player, "\t", score, "\t", rank)
            rank += 1
        leader_board_file.close()

    def undo(self, row, column, game_arr):
        option = input("Do you want to Undo? (Yes/No) : ")
        if option == "Yes":
            game_arr[row][column] = -1
            self.print_arr(game_arr)
            return game_arr
        else:
            return None
        
    def timer(self):
        start = time.time()
        print(start)
        i = 0
        while time.time() - start <= 10:
            if int(time.time() - start) == 5 and i == 0:
                print("5 seconds more")
                i = 1
        print("Your opponent have won the match")            

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