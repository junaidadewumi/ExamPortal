import time
import sys
import mysql.connector as connection
myconn = connection.connect(host = "127.0.0.1", user = "root", passwd = "@Arikeade2408", database = "portal")
cursor = myconn.cursor()

def quest():
    querry = "INSERT INTO que(question, optiona, optionb, optionc, answer) VALUES(%s, %s, %s, %s, %s)"
    question = input("Enter question 1: ")
    optiona = input("Enter option A: ")
    optionb = input("Enter option B: ")
    optionc = input("Enter option C: ")
    answer = input("Enter answer: ")
    val = (question, optiona, optionb, optionc, answer)
    cursor.execute(querry, val)
    myconn.commit()

def select():
    score = 0
    selected_que = set()
    ques_id = input("Enter question number: ")
    while ques_id != "stop":
        if ques_id not in selected_que:
            val = (ques_id, )
            querry = "select * from que where id = %s"
            cursor.execute(querry, val)
            result = cursor.fetchone()
            time.sleep(1)
            if result:
                print(result[1])
                print(result[2])
                print(result[3])
                print(result[4])
                answ = input("Enter your answer: ").upper()
                time.sleep(2)
                if answ == result[5]:
                    print("Correct answer")
                    score += 10
                else:
                    print("Wrong answer")
        else:
            print("Selected")
        selected_que.add(ques_id)
        time.sleep(2)
        ques_id = input("Enter question number: ")
    else:
        print(f"""You have attempted all question. Your total score for the exam attempted is 
        {score}. Have a great day!""")

def update_quest():
    dec = int(input("Enter question number to update: "))
    val = (dec, )
    querry = "SELECT * FROM que where id = %s" 
    cursor.execute(querry, val)
    result = cursor.fetchone()
    if result:
        newquestion = input("Enter new question: ")
        optiona = input("Enter optiona: ")
        optionb = input("Enter optionb: ")
        optionc = input("Enter optionc: ")
        answer = input("Enter answer: ")
        val = (newquestion, optiona, optionb, optionc, answer, dec)
        querry = "UPDATE que SET question =%s, optiona= %s, optionb =%s, optionc=%s, answer=%s where id = %s"
        cursor.execute(querry, val)
        myconn.commit()