class Father:
    def hobbies(self):
        print("playing crickets, drawing")
    def education(self):
        print("Intermediate")
    def height(self):
        print("6'5")
    def weight(self):
        print("87kg")
class child(Father):
    def weight(self):
        print("66kg")
    def height(self):
        print("6'1")
        
c1 = child()
c1.hobbies()