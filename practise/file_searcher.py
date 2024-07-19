

def find():
    with open("loops.py" , "r") as f:  
        data = f.readline()  
        for line in data:
            word = "learning"
            line = 1
            if word == data:
               print(line)
            line += 1

find()
