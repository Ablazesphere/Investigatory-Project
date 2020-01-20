import random,os,time,numpy,mysql.connector as sqltor
def regno():
    if os.path.isfile('./regno.txt')!=True:
        file=open('regno.txt','w')
        list=[str(i)+'\n' for i in range(1000,2000)]
        file.writelines(list)
        file.flush()
        file.close()
    return
def database():
    mycon=sqltor.connect(host='localhost',user='root',passwd='')
    cursor=mycon.cursor()
    if mycon.is_connected():
        print("CONNECTION ESTABLISHED")
        print()
        print()
    else:
        print("UNABLE TO CONNECT WITH SQL SERVER")
    cursor.execute("CREATE DATABASE IF NOT EXISTS MOVIE ")
def table():
    mycon=sqltor.connect(host='localhost',user='root',passwd='',database='movie')
    cursor=mycon.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_DETAILS(Reg_no int(30) NOT NULL PRIMARY KEY,customer_name char(20),username varchar(20) UNIQUE,password varchar(20),phone_no varchar(10) NOT NULL UNIQUE)")
def register():
    try:
        file=open('regno.txt','r')
        data=file.readlines()
        regno=data.pop(0)
        file.close()
        print("LOGIN TO BOOK TICKETS")
        user=input("ENTER YOUR USERNAME:")
        password=input("ENTER YOUR PASSWORD:")
        phone=int(input("ENTER YOUR PHONE NUMBER:"))
        name=input("ENTER YOUR NAME:")
        cap=hex(random.randint(1,1500))
        print("\t\t\tCAPTCHA::",cap)
        response=input("RE-ENTER CAPTCHA:")
        if response==str(cap):
            cursor.execute("INSERT INTO CUSTOMER_DETAILS (Reg_no,customer_name,username,password,phone_no) VALUES({},'{}','{}','{}',{})".format(regno,name,user,password,phone))
            print("successfully registered")
            file=open('regno.txt','w')
            file.writelines(data)
            file.flush()
            file.close()
            time.sleep(2)
            os.system('cls')
            hello(regno)
    except:
        print("oops!!!! something went wrong")
        time.sleep(3)
        os.system("cls")
        print("TRY!!!AGAIN")
        register()

def check(user,password):
    try:
        point=cursor.execute("SELECT REG_NO FROM CUSTOMER_DETAILS WHERE USERNAME='{}' AND PASSWORD='{}'".format(user,password))
        data=cursor.fetchall()
        hello(data[0][0])
    except:
        print("INCORRECT CREDENTIALS")
        time.sleep(3)
        os.system("cls")
        choice=input("DO YOU WANT TO REGISTER AGAIN(y,n):")
        if choice=='y':
            register()
        else:
            print("Try Again")
            login()
def login():
    user=input("ENTER YOUR USERNAME:")
    password=input("Password:")
    os.system('cls')
    check(user,password)
def hello(regno):
    cursor.execute("SELECT CUSTOMER_NAME FROM CUSTOMER_DETAILS WHERE REG_NO={}".format(regno))
    data=cursor.fetchall()
    print("HELLO",data[0][0].upper(),"ITS MOVIE TIME")
    time.sleep(3)
    os.system('movies.py')
database()
table()
regno()
mycon=sqltor.connect(host='localhost',user='root',passwd='',database='movie')
cursor=mycon.cursor()
while True:
    choice=input("HELLO!!!! ARE YOU A REGISTERED USER (y/n):").lower()
    print()
    if choice=='y':
        login()
        break
    elif choice=='n':
        register()
        break
    else:
        print("ERROR!!!! TRY AGAIN")
        os.system("cls")
        continue

