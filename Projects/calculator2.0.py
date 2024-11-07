while True:
    type = input("Type 'gui' for operation guid or \n press enter : " )
    if (type.lower() ==  "gui"):
        print("1 = Addition ")
        print("2 = Subtraction ")
        print("3 = Reminder ")
        print("4 = Multiplication ")
        print("5 = Division")
    elif(type.lower() != "gui"):
        print("Select operation:")



        b = 1 
        num = []

        while True:
            
            a = int(input(f"{b} No: "))
            c = int(input("Operation no. : \n"))

            if c == "s":
                num.append(a)

            elif c == "1":
                print()

            
   #hello             



