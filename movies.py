#Movie List
import os
import time
from cost_movies import *
movie_list = {"Robot 2.0","Badlapur","Hera Pheri","Housefull 4","Avengers : End Game"}
while True:
    os.system("cls")
    print('''
    \t\t SELECT MOVIE
 
    1. Robot 2.0                  Rs {}
    2. Badlapur                   Rs {}
    3. Hera Pheri                 Rs {}
    4. Housefull 4                Rs {}
    5. Avengers : End Game        Rs {}


    6. Exit
    '''.format(cost[0],cost[1],cost[2],cost[3],cost[4]))
    try:
        user = int(input("Enter your choice : "))
    except:
        print("Invalid choice.Try again.")
        time.sleep(1)
    if user == 1:
        with open("mov1//current_booked.py", "w") as SH:
            SH.write("nos2 = {}")
        os.system("mov1\\reservation.py")
        time.sleep(5)
    elif user == 2:
        with open("mov2//current_booked.py", "w") as SH:
            SH.write("nos2 = {}")
        os.system("mov2\\reservation.py")
        time.sleep(5)
    elif user == 3:
        with open("mov3//current_booked.py", "w") as SH:
            SH.write("nos2 = {}")
        os.system("mov3\\reservation.py")
        time.sleep(5)
    elif user == 4:
        with open("mov4//current_booked.py", "w") as SH:
            SH.write("nos2 = {}")
        os.system("mov4\\reservation.py")
        time.sleep(5)
    elif user == 5:
        with open("mov5//current_booked.py", "w") as SH:
            SH.write("nos2 = {}")
        os.system("mov5\\reservation.py")
        time.sleep(5)
    elif user == 6:
        print("<<<THANKS FOR USING BOOK MY SHOW>>>")
        break
    os.system("cls")

    
