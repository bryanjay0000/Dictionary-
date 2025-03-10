def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "Bryanjay" and password == "0000":
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

def hellopo():
    print("Hello po sa taong nagbabasa nitong code ko.")

def nested():
    a1 = int(input("Enter number 1: "))
    a2 = int(input("Enter number 2: "))
    a3 = int(input("Enter number 3: "))
    a4 = int(input("Enter number 4: "))
    a5 = int(input("Enter number 5: "))
    a6 = int(input("Enter number 6: "))
    a7 = int(input("Enter number 7: "))
    a8 = int(input("Enter number 8: "))

    for a in range(a1):
        for b in range(a2):
            for c in range(a3):
                for d in range(a4):
                    for e in range(a5):
                        for f in range(a6):
                            for g in range(a7):
                                for h in range(a8):
                                    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}")

if login():
    while True:
        hellopo()
        nested()
        
        repeat = input("Do you want to run the program again? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Exiting program. Thank you!")
            break