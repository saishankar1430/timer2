class student:
    
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def printInfo(self):
        print(f"Name is {self.name}, Age = {self.age}, Marks = {self.marks} ")
    
    def calcCgpa(self):
        self.cgpa = self.marks / 10
        print(f"CGPA = {self.cgpa}")
    
    print("This is all the details")


s1 = student("Shubham", 19, 97)

s1.printInfo()
s1.calcCgpa()

        