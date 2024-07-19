print("\033[1mWelcome to the Board of Inda\033[0m")
a = input(" Enter your Name : \n ")
while True:

    b = int (input(" Enter B.O.Y :\n"))
    if (b < 1990 ):
        print("You are not Eligible for this Examination\n the right age for you have pased by \n  ")
        break
    elif( b > 2009):
        print("You are not Eligible for this Examination\n Try again After you became 18 ")
        break
    else:
        print("Do You Want To use a Code?" ) 
        c = bool(input("Yes or No\n"))  
        
        if (c == "yes"):
           print(int (input("Use a Code : \n")))

        else:
            print("Welcome " + a + ' , ')
            print(" kindly fill the rest details")
            Num = int (input("Enter your phone mo. \n"))
            int(input("Enter the verification code \n"))
            print("\nThanks for participating in this exam \n "    """ The exam will be held on 25 th of june, thanks """)
            
            print ("If you Want to know the syallabus \n click on this link here \n")


#hello

