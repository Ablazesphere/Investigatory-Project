import os,time
from current_booked import *
def dc():
    print()
    CARDNO=input("ENTER YOUR 16 DIGIT CARD NUMBER: ")
    CVV=input("ENTER 3 DIGIT CVV:")
    EXPMONTH=input("ENTER EXPIRY MONTH (eg jan):").lower()
    EXPYEAR=int(input("ENTER EXPIRY YEAR (eg yyyy):"))
    os.system("cls")
    if len(CARDNO)==16 and len(CVV)==3:
        if EXPYEAR > 2020:
            for i in range(4):
                print(".")
                time.sleep(1)
            seats = str(nos2.keys())
            print("TRANSACTION SUCCESSFULL")
            print("PLEASE SHOW YOUR TICKET AT THE ENTRY::")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("|MOVIE:  HERA PHERI                       |")
            print("|SEAT NO.:  {}                |".format(seats[9:]))
            print("|TIME: 9:00 AM                            |")
            print("|SCREEN:PVR                               |")
            print("|DATE:                                    |")
            print("|        THANK YOU!!!! FOR USING          |")
            print("|                                         |")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(5)
    else:
        print("INVALID DATA!!! TRY AGAIN")
        os.system("cls")
        dc()    
while True:
    os.system("cls")s
    print("Transaction")
    print()
    print("1.DEBIT CARD")
    print("2.CANCEL")
    print()
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice==1:
        dc()
        with open('current_booked.py', 'w') as reboot:
            reboot.write("nos2 = {}")
        break
    elif choice==2:
        break
    else:
        print("INVALID SYNTAX")
