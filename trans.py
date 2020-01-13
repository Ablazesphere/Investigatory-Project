import os,time
print("Transaction")
print("1.RESERVE TICKETS")
print("2.DEBIT CARD")
print("3.CANCEL TICKETS")
def rt():
    print("TICKETS RESESRVED SUCCESSFULLY")
    print("PLEASE PAY AT TICKET COUNTER")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|MOVIE:                       |")
    print("|AMOUNT:                      |")
    print("|SEAT NO.:                    |")
    print("|TIME: 9:00 AM                |")
    print("|SCREEN:PVR                   |")
    print("|DATE:                        |")
    print("|  THANK YOU!!!! FOR USING    |")
    print("|     #Book My Show#          |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(5)
def dc():
    CARDNO=input("ENTER YOUR 16 DIGIT CARD NUMBER: ")
    CVV=input("ENTER 3 DIGIT CVV:")
    EXPMONTH=input("ENTER EXPIRY MONTH (eg jan):")
    EXPYEAR=input("ENTER EXPIRY YEAR (eg yyyy):")
    os.system("cls")
    if len(CARDNO)==16 and len(CVV)==3:
        print("TRANSACTION SUCCESSFULL")
        print("PLEASE SHOW YOUR TICKET AT THE ENTRY::")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|MOVIE:                       |")
        print("|AMOUNT:                      |")
        print("|SEAT NO.:                    |")
        print("|TIME: 9:00 AM                |")
        print("|SCREEN:PVR                   |")
        print("|DATE:                        |")
        print("|  THANK YOU!!!! FOR USING    |")
        print("|     #Book My Show#          |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(5)
    else:
        print("INVALID DATA!!! TRY AGAIN")
        dc()    
while True:
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice==1:
        rt()
        break
    elif choice==2:
        dc()
        break
    elif choice==3:
        break
    else:
        print("INVALID SYNTEX")
