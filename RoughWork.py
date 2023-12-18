name     = input("Enter your Name   : ")
number   = int(input("Enter your Number : "))
email_id = input("Enter your Emali  : ")


player = open("PlayersDataFile.txt", "a")
player.write(name + "," + str(number) + "," + email_id + "," + "0" + "," + "0" + ",")
player.write("\n")
player.close()