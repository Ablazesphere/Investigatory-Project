import os
import time
import json
from booking_seats_mov1  import *
        
def print_board():
    print()
    print("X = Booked")
    print()
    print("   A   B   C   D   E")
    print()
    print(" ","   |   |   |   |   ")
    print("1"," "+board[1]+" | "+board[2]+" | "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print(" ","   |   |   |   |   ")
    print(" ","---|---|---|---|---")
    print(" ","   |   |   |   |   ")
    print("2"," "+board[6]+" | "+board[7]+" | "+board[8]+" | "+board[9]+" | "+board[10]+" ")
    print(" ","   |   |   |   |   ")
    print(" ","---|---|---|---|---")
    print(" ","   |   |   |   |   ")			
    print("3"," "+board[11]+" | "+board[12]+" | "+board[13]+" | "+board[14]+" | "+board[15]+" ")
    print(" ","   |   |   |   |   ")
    print(" ","---|---|---|---|---")
    print(" ","   |   |   |   |   ")
    print("4"," "+board[16]+" | "+board[17]+" | "+board[18]+" | "+board[19]+" | "+board[20]+" ")
    print(" ","   |   |   |   |   ")
    print(" ","---|---|---|---|---")
    print(" ","   |   |   |   |   ")
    print("5"," "+board[21]+" | "+board[22]+" | "+board[23]+" | "+board[24]+" | "+board[25]+" ")
    print(" ","   |   |   |   |   ")
    print(" ","---|---|---|---|---")
    print()
    print()
    print(" ","-------------------")
    print(" ","      SCREEN       ")
    print(" ","-------------------")
while True:
    os.system("cls")
    print_board()
    seats = {'A1':1,'B1':2,'C1':3,'D1':4,'E1':5,
             'A2':6,'B2':7,'C2':8,'D2':9,'E2':10,
             'A3':11,'B3':12,'C3':13,'D3':14,'E3':15,
             'A4':16,'B4':17,'C4':18,'D4':19,'E4':20,
             'A5':21,'B5':22,'C5':23,'D5':24,'E5':25}
    
    choice = input("Select a seat eg. A4  : ")
    if choice == "":
        break
    if choice not in seats.keys():
        print()
        print("Invalid choice.")
        time.sleep(1)
        break
    
    else:
        seat_choice = int(seats[choice])    
        if board[seat_choice] == " ":
            board[seat_choice] = "X"
        
            with open("booking_seats.py", "w") as sh:
                sh.write("board = ")
                data = json.dump(board, sh)
            
        else:
            print()
            print("Already Booked")
            time.sleep(1)
    choice2 = input("Do you want to book another seat or move on with the transaction? (y/n) : ").lower()
    if choice2 == 'n':
        os.system("UNBOUND")
        break
    
