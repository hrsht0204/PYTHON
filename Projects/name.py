print("\033[1mLogin Screen \033[0m")


name = input("Enter Your Username : \n")

if (name == "Harshit Krishan"):
    print("Welcome to Windows 10")
    password = input("Enter Your Password : \n")
    if(password != "Abc@1234"):
     print(" Password is incorrect ")
    else:
      while True:
            a = 0
            print("Welcome , Harsh Windows is now \n Starting ....." , a  , "s")
            if a != 0 :
               a -= 1
               break
            else:
               print("Loading....\n Welcome ")

else:
 print("Invalid Username")

#hello