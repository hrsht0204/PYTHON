# # def Sum(a , b):
# #     s = a + b
# #     print(s)
# #     return s

# # Sum(6, 7)

# # # def calc_sum(a , b):
# # #     sum = a + b f
# # #     print (sum)
# # #     return sum

# # # calc_sum(6 , 10)


# #4

# # def name ():
# #     a = input(":")
# #     print("Is your namef \n" + a)
# #     return a 

# # name ()

# def average(a , b , c):
#     sum =  a + b + c
#     avg = sum / 3
#     print (avg)
#     return  avg

# average (1 , 1 ,1 )

# num=[]

# k = int(input("enter numbers :\n and type 'stop' to stop\n"))

# def lio():
#     s = len(num)
#     print (s)
#     return s
# for el in k:
#  k == "stop"
#  print(lio())
# else:
#     num.append(k)


num = []

while True:
    k = input("Enter a number (or type 'stop' to finish): ")
    if k == 'stop':
        break
    else:
        k = int(k)
        num.append(k)
    
def lio():
    s = len(num)
    print(s)
    return s

# Call the function to print the length of the list
lio()

