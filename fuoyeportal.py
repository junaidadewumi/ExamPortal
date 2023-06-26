import time
def portal():
    print("""Welcome to FUOYE Portal.
    1. Admin
    2. Student
    """)
    time.sleep(2)
    decision = input(">>> ")
    if decision == "1":
        from admin import Admin
        Admin()
    elif decision == "2":
        from student import std
        std()
    else:
        print("You seems to have entered wrong code, Retry!")
        portal()
portal()
