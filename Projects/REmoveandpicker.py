lis = []
no = 1

print("\033[1m THIS IS A WISH LIST PROGRAMME \n , Enjoy \033[0m")

f = input("Notice: If you want to end the wish and remove an item , type 's'. \n If you want to end the programme, type 'e'.  \n Press enter to continue: ")

while True:
    a = input(f"{no} Thing: ")
    if a.lower() == "s":
        print(lis)
        t = input("Type to remove: ")
        if t in lis:
            lis.remove(t)
            print(lis)
        else:
            print(f"{t} is not in the list.")
    elif a.lower() == 'e':
        print("Here is your final list:")
        print(lis)
        break
    else:
        lis.append(a)
        no += 1
#hello