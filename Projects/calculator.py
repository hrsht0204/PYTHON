
#hello
while True:
    type = input("Type 'gui' for operation guid or \n press enter : " )
    if (type.lower() ==  "gui"):
        print("1 = Addition ")
        print("2 = Subtraction ")
        print("3 = Reminder ")
        print("4 = Multiplication ")
        print("5 = Division")
        print("= = The End of the problem")
    elif(type.lower() != "gui"):
        print("Select operation:")
    
    # Get user choice

        while True:
                c = input("Operation Number\n")
                
                
                a = int(input("First:"))
                b = int(input("Second:"))
                
                if (c == "1"):
                    z =  a + b
                    print(a ,"+", b  ,"= ",  z)
                elif (c =="2"):
                    p = a-b
                    print(a,"-",b, "=" , p  )
                elif (c == '3'):
                    k = a %b
                    print(a,'%',b, "=" ,k )
                elif (c == "4"):
                    l = a *b 
                    print(a,'*',b, "=" , l )
                elif (c == "5"):
                    m = a /b 
                    print (a , "÷" , b , '-' , m)
                else:
                    print("invalid expression")
                