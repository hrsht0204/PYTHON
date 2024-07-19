import random

user_data = {}

def Random():
    c = random.randrange(1,999999)
    return c


def Register():
    username = str(input("Enter Your Username : \n"))
    passcode = int(input("Enter Your Password: \n"))
    Id = Random()
    user_data["Key"]= {'username': username ,"Password" : passcode , "Id" : Id}
    print("Succesfully Registered \nYour Login Id is ")
    print(Id)


def Login():
    Id = int(input("Enter Your Login Id:\n"))
    password = int(input("Enter Your Passcode:\n"))
    if Id in user_data and user_data["Key"][password] == password:
        print("logged in succesfully, please write your \"UserName\"")
    else:
        print("Inavlid Enteries, Please check the entries")


def Interface():
    while True:
        choice = str(input("Login or Register\n"))
        if (choice.lower() == "register"):
            Register()
        elif (choice.lower() == "login"):
             Login()
        else:
            print("invalid action")


if __name__ == "__main__":
    Interface()

    