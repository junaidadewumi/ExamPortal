import time
import sys
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = "root", passwd = "@Arikeade2408", database = "portal")
cursor = myconn.cursor()

def std():
    acct = input("""
    1. Log in
    2. Create account
    """)
    if acct == "1":
        log_in()
    elif acct == "2":
        create()

def create():
    userinfo = []
    details = ("First_name", "Middle_name", "Last_name", "Email", "Gender", "Level", "Course", "Pswd")
    querry = "INSERT INTO stud(First_name, Middle_name, Last_name, Email, Gender, Level, Course, Pswd) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
    for i in range (8):
        decision = input(f"Enter your {details[i]}: ")
        userinfo.append(decision)
        time.sleep(1)
    val = (userinfo)
    cursor.execute(querry, val)
    myconn.commit()
    time.sleep(2)
    print(f"Registration successful.")
    time.sleep(1)
    log_in()

def log_in():
    username = input("enter your email: ")
    time.sleep(2)
    password = input("enter your password: ")
    val = (username, password)
    querry = "select * from stud where Email = %s and Pswd = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(2)
        print("you have successfully log in ")
        time.sleep(2)
        decide = input("Hello student! Enter 1 to attempt exam and 2 to go quit: ")
        if decide == "1":
            from question import select
            select()
        elif decide == "2":
            sys.exit()
    else:
        print("invalid input, try to log in again ")
        log_in()
        