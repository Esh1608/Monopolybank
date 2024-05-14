player_1 = 0
player_2 = 0
player_3 = 0
player_4 = 0

def set_money(startmoney):
    global player_1, player_2, player_3, player_4
    startmoney = int(startmoney)
    player_1 = startmoney
    player_2 = startmoney
    player_3 = startmoney
    player_4 = startmoney
    print("Players have $" + str(player_1))

def transfer_money(amount, source_player, destination_player):
    global player_1, player_2, player_3, player_4
    amount = int(amount)
    source_player = int(source_player)
    destination_player = int(destination_player)

    if globals()['player_' + str(source_player)] < amount:
        print("Player " + str(source_player) + " does not have enough money to transfer " + str(amount))

    else:
        if source_player == 1 and destination_player == 2:
            player_1 -= amount
            player_2 += amount
            print("Player 1 transferred " + str(amount) + " to Player 2")
        elif source_player == 1 and destination_player == 3:
            player_1 -= amount
            player_3 += amount
            print("Player 1 transferred " + str(amount) + " to Player 3")
        elif source_player == 1 and destination_player == 4:
            player_1 -= amount
            player_4 += amount
            print("Player 1 transferred " + str(amount) + " to Player 4")
        elif source_player == 2 and destination_player == 1:
            player_2 -= amount
            player_1 += amount
            print("Player 2 transferred " + str(amount) + " to Player 1")
        elif source_player == 2 and destination_player == 3:
            player_2 -= amount
            player_3 += amount
            print("Player 2 transferred " + str(amount) + " to Player 3")
        elif source_player == 2 and destination_player == 4:
            player_2 -= amount
            player_4 += amount
            print("Player 2 transferred " + str(amount) + " to Player 4")
        elif source_player == 3 and destination_player == 1:
            player_3 -= amount
            player_1 += amount
            print("Player 3 transferred " + str(amount) + " to Player 1")
        elif source_player == 3 and destination_player == 2:
            player_3 -= amount
            player_2 += amount
            print("Player 3 transferred " + str(amount) + " to Player 2")
        elif source_player == 3 and destination_player == 4:
            player_3 -= amount
            player_4 += amount
            print("Player 3 transferred " + str(amount) + " to Player 4")
        elif source_player == 4 and destination_player == 1:
            player_4 -= amount
            player_1 += amount
            print("Player 4 transferred " + str(amount) + " to Player 1")
        elif source_player == 4 and destination_player == 2:
            player_4 -= amount
            player_2 += amount
            print("Player 4 transferred " + str(amount) + " to Player 2")
        elif source_player == 4 and destination_player == 3:
            player_4 -= amount
            player_3 += amount
            print("Player 4 transferred " + str(amount) + " to Player 3")

def spend_money(amount, player):
    global player_1, player_2, player_3, player_4
    amount = int(amount)
    player = int(player)

    if globals()['player_' + str(player)] < amount:
        print("Player " + str(player) + " does not have enough money to spend " + str(amount))

    else:
        if player == 1:
            player_1 -= amount
            print("Player 1 spent $" + str(amount))
        elif player == 2:
            player_2 -= amount
            print("Player 2 spent $" + str(amount))
        elif player == 3:
            player_3 -= amount
            print("Player 3 spent $" + str(amount))
        elif player == 4:
            player_4 -= amount
            print("Player 4 spent $" + str(amount))
        else:
            print("Invalid player number")	

def get_money(amount, player):
    global player_1, player_2, player_3, player_4
    amount = int(amount)
    player = int(player)
    if player == 1:
        player_1 += amount
        print("Player 1 got $" + str(amount))
    elif player == 2:
        player_2 += amount
        print("Player 2 got $" + str(amount))
    elif player == 3:
        player_3 += amount
        print("Player 3 got $" + str(amount))
    elif player == 4:
        player_4 += amount
        print("Player 4 got $" + str(amount))
    else:
        print("Invalid player number")

def go_over_start(amount, player):
    global player_1, player_2, player_3, player_4
    amount = int(amount)
    player = int(player)
    if player == 1:
        player_1 += amount
        print("Player 1 got $" + str(amount) + "because going over start")
    elif player == 2:
        player_2 += amount
        print("Player 2 got $" + str(amount) + "because going over start")
    elif player == 3:
        player_3 += amount
        print("Player 3 got $" + str(amount) + "because going over start")
    elif player == 4:
        player_4 += amount
        print("Player 4 got $" + str(amount) + "because going over start")
    else:
        print("Invalid player number")


print("Welcome to Monopoly!")
set_money(input("How much money do you want to start with? "))

print("Enter 1 to transfer money")
print("Enter 2 to spend money")
print("Enter 3 to get money")
print("Enter 4 to go over start")



while True:
    user_input = input("What do you want to do? ")

    if user_input == "1":
        amount = input("How much money? ")
        source = input("From which player? ")
        destination = input("To which player? ")
        transfer_money(amount, source, destination)

    elif user_input == "2":
        amount = input("How much money? ")
        source = input("From which player? ")
        spend_money(amount, source)

    elif user_input == "3":
        amount = input("How much money? ")
        destination = input("To which player? ")
        get_money(amount, destination)

    elif user_input == "4":
        destination = input("To which player? ")
        go_over_start(200, destination)
        
    print("Player 1 has $" + str(player_1))
    print("Player 2 has $" + str(player_2))
    print("Player 3 has $" + str(player_3))
    print("Player 4 has $" + str(player_4))