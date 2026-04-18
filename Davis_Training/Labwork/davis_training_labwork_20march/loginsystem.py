def login():
    correct_user = "admin"
    correct_pass = "1234"
    
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_user and password == correct_pass:
            print("Login Successful")
            return
        else:
            print("Invalid credentials")
            attempts += 1

    print("Account Locked")

login()