import math
import random

def username():
    name = str(input("Enter Your Username\n"))
    return name
def password():
    key = int(input("Enter Passcode\n"))
    return key
def Random():
    c = random.randrange(1,999999)
    return c

     
def for_real():
    b = 5678
    e = b
def id():
    real_id = new_id 
    return real_id  

choose = str(input("\033[1m Login or Register \n \033[0m"))


if (choose.lower() == "register" ):
        print("\033[1m REGISTRATION SCREEN \033[0m")
        new_user= username()
        new_key = 5678
        new_id = Random()
        print("Your Login iD is\n ", new_id)
        print("please note it down somewhere")
elif (choose.lower() == "login" ):
        print("\033[1m LOGIN SCREEN \033[0m")
        f = int(input("Enter Id"))
        if (f == id()):
            print(for_real())
        elif(f != id()):
            print("Please fill the Corret ID")
        else:
            print("Inavild Number")
elif():
    print("Inavild Action")




