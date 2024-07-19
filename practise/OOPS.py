class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def avg(self):
        s = 0
        for i in self.marks:
            s += i
        print("Your avg is " , s/3)
            
    

si =  Student("Harshut", [90 ,90 ,90])
si.avg()

