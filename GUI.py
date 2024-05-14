import tkinter as tk
import customtkinter as ctk

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

    p1_var.set(player_1)
    p2_var.set(player_2)
    p3_var.set(player_3)
    p4_var.set(player_4)

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
    
    p1_var.set(player_1)
    p2_var.set(player_2)
    p3_var.set(player_3)
    p4_var.set(player_4)

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

    p1_var.set(player_1)
    p2_var.set(player_2)
    p3_var.set(player_3)
    p4_var.set(player_4)

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

    p1_var.set(player_1)
    p2_var.set(player_2)
    p3_var.set(player_3)
    p4_var.set(player_4)

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

    p1_var.set(player_1)
    p2_var.set(player_2)
    p3_var.set(player_3)
    p4_var.set(player_4)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

p1_var = ctk.StringVar(value=0)
p2_var = ctk.StringVar(value=0)
p3_var = ctk.StringVar(value=0)
p4_var = ctk.StringVar(value=0)

root.geometry("1000x600")

frame_sm = ctk.CTkFrame(master=root)
frame_sm.pack(pady=50, padx=60, fill="both", side="right", expand=False)

label = ctk.CTkLabel(master=frame_sm, text="Starting Capital")
label.pack(pady=12, padx=30)

entry_sc = ctk.CTkEntry(master=frame_sm, placeholder_text="Starting Capital")
entry_sc.pack(pady=12, padx=30)

button = ctk.CTkButton(master=frame_sm, text="Set", command=lambda: set_money(entry_sc.get()))
button.pack(pady=12, padx=30)


#P1
frame_p1 = ctk.CTkFrame(master=root)
frame_p1.pack(pady=50, padx=60, fill="both", side="left", expand=False)

label = ctk.CTkLabel(master=frame_p1, text="Player 1")
label.pack(pady=12, padx=30)

label = ctk.CTkLabel(master=frame_p1, textvariable=p1_var)
label.pack(pady=12, padx=30)



label = ctk.CTkLabel(master=frame_p1, text="Transfer Money")
label.pack(pady=5, padx=30)

entry_amount_p1_trans = ctk.CTkEntry(master=frame_p1, placeholder_text="Amount")
entry_amount_p1_trans.pack(pady=5, padx=30)

entry_dest_p1_trans = ctk.CTkEntry(master=frame_p1, placeholder_text="Destination Player")
entry_dest_p1_trans.pack(pady=5, padx=30)

button = ctk.CTkButton(master=frame_p1, text="Transfer", command=lambda: transfer_money(entry_amount_p1_trans.get(), 1, entry_dest_p1_trans.get()))
button.pack(pady=5, padx=30)



label = ctk.CTkLabel(master=frame_p1, text="Spend Money")
label.pack(pady=5, padx=30)

entry_amount_p1_spend = ctk.CTkEntry(master=frame_p1, placeholder_text="Amount")
entry_amount_p1_spend.pack(pady=5, padx=30)

button = ctk.CTkButton(master=frame_p1, text="Spend", command=lambda: spend_money(entry_amount_p1_spend.get(), 1))
button.pack(pady=5, padx=30)



label = ctk.CTkLabel(master=frame_p1, text="Get Money")
label.pack(pady=5, padx=30)

entry_amount_p1_get = ctk.CTkEntry(master=frame_p1, placeholder_text="Amount")
entry_amount_p1_get.pack(pady=5, padx=30)

button = ctk.CTkButton(master=frame_p1, text="Get", command=lambda: get_money(entry_amount_p1_get.get(), 1))
button.pack(pady=5, padx=30)



label = ctk.CTkLabel(master=frame_p1, text="Go over start")
label.pack(pady=5, padx=30)

button = ctk.CTkButton(master=frame_p1, text="Get", command=lambda: get_money(200, 1))
button.pack(pady=5, padx=30)


#P2
frame_p2 = ctk.CTkFrame(master=root)
frame_p2.pack(pady=50, padx=5, fill="both", side="left", expand=False)

label = ctk.CTkLabel(master=frame_p2, text="Player 2")
label.pack(pady=12, padx=30)

label = ctk.CTkLabel(master=frame_p2, textvariable=p2_var)
label.pack(pady=12, padx=30)

label = ctk.CTkLabel(master=frame_p2, text="Transfer Money")
label.pack(pady=5, padx=30)

entry_amount_p2_trans = ctk.CTkEntry(master=frame_p2, placeholder_text="Amount")
entry_amount_p2_trans.pack(pady=5, padx=30)

entry_dest_p2_trans = ctk.CTkEntry(master=frame_p2, placeholder_text="Destination Player")
entry_dest_p2_trans.pack(pady=5, padx=30)

button = ctk.CTkButton(master=frame_p2, text="Transfer", command=lambda: transfer_money(entry_amount_p2_trans.get(), 2, entry_dest_p2_trans.get()))
button.pack(pady=5, padx=30)

root.mainloop()