pwd = input("Enter the master password!!")

def add():
    name =  input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write("name: " + name + " | " "password: "+pwd + "\n")

def view():
    with open('password.txt', 'r' ) as f:
        for line in f.readlines():
            print(line)


while True:
    mode = input("Would you like to add a new password or view existing one? (view/add) or press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
       add()
    else:
        print("Invalid Input!")
        continue

