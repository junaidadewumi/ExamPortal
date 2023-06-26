import time
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = "root", passwd = "@Arikeade2408", database = "portal")
cursor = myconn.cursor()

def Admin():
    acct = input("""
    1. Log in
    2. Create account
    """)
    if acct == "1":
        log_in()
    elif acct == "2":
        create()

def create():
    userInfo = []
    details = ("First_name", "Last_name", "Email", "Pswd")
    querry = "INSERT INTO admins(First_name, Last_name, Email, Pswd) VALUES (%s, %s, %s, %s)"
    for i in range (4):
        decision = input(f"Enter your {details[i]}: ")
        userInfo.append(decision)
        time.sleep(2)
    val = (userInfo)
    cursor.execute(querry, val)
    myconn.commit()
    print(f"Registration successful.")
    time.sleep(1)
    log_in()

def log_in():
    username = input("enter your email: ")
    time.sleep(2)
    password = input("enter your password: ")
    val = (username, password)
    querry = "select * from admins where Email = %s and Pswd = %s"
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        time.sleep(2)
        print("you have successfully log in ")
        time.sleep(2)
        dec()
    else:
        print("invalid input, try to log in again ")
        time.sleep(1)
        log_in()


def dec():
    print("""Hello Admin! What would like to do?
              1. set question
              2. change question""")
    decide = input(">>> ")
    if decide == "1":
        que = input("""
            1. Next
            2. Back
            >>> """)
        while que != '2':
            from question import quest
            time.sleep(2)
            quest()
            time.sleep(2)
            que = input("""
                1. Next
                2. Back
                >> """)
        else:
            dec()
    elif decide == "2":
        from question import update_quest
        update_quest()
    
        