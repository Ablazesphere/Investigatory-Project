#Movie List

import os
import time
from cost_movies import *
movie_list = {"Robot 2.0","Badlapur","Hera Pheri","Housefull 4","Avengers : End Game"}
while True:
    print('''
    \t\t\t\t SELECT MOVIE

    1. Robot 2.0
    2. Badlapur
    3. Hera Pheri
    4. Housefull 4
    5. Avengers : End Game

    ''')
    try:
        user = int(input("Enter your choice : "))
    except:
        print("Invalid choice.Try again.")
        time.sleep(1)
    if user == 1:
        os.system("mov1\\reservation.py")
    elif user == 2:
        os.system("mov2\\reservation.py")
    elif user == 3:
        os.system("mov3\\reservation.py")
    elif user == 4:
        os.system("mov4\\reservation.py")
    elif user == 5:
        os.system("mov5\\reservation.py")
    os.system("cls")      
    
