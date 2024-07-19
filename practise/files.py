# add data 
{
# f = open("practice.txt", "w")
# data = f.write("Hi everyone \n we are learning file i|o \n using java. \n i like programing in java")
# print(data)
# f.close()
}
#  replace 

{
# f = open("practice.txt", "r")
# data = f.read()

# new = data.replace("java", "python")
# print(new)
# f.close()

# f = open("practice.txt", "w")
# f.write(new)
}


# find for word

{
# f = open("practice.txt", "r")
# data = f.read()
# if data.find("learning"):
#     print("found")
# else:
#     print("not found")

# new = data.find("learning")
# print(new)
}

#  find a word line version

def checkword():
    word = "learning"
    ln = 1
    with open ("practice.txt", "r") as f:
        while True:
            data = f.readline()
            if (word in data):
                print(ln)
                return
            ln += 1 
checkword()


    
# total number of even number
# count= 0
# with open ("practice.txt", "r") as  f:
#     data=f.read()

#     nums = data.split(",")
#     for i in nums:
#         if (int(i) % 2 == 0 ):
#             count += 1



# print(count)      

        
        
    
