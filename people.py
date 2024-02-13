class People:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age

    def displaywasee(self):
        print(f"My name is {self.Name}",f".I am {self.Age} years old")

obj1=People("Ian",19)
obj2=People("Kennedy",21)
obj3=People("Chelate",18)
obj4=People("Belousov",26)
obj5=People("Sabatier",23)

obj1.displaywasee()
obj2.displaywasee()
obj3.displaywasee()
obj4.displaywasee()
obj5.displaywasee()
