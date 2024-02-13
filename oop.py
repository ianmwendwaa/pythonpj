class fruits:
    def __init__(self, name, price, color, vitamin):
        self.name = name
        self.price = price
        self.color = color
        self.vitamin = vitamin

    def onyesha(self):
        print(f"My favorite fruit is {self.name}" f" ,it costs Ksh.{self.price}",f", it is {self.color} in color"" and"
                                                                                 f" it is rich in {self.vitamin}")


myobj = fruits("grapes", 60, "purple","Vitamin K.")
myobj2 = fruits("oranges",25,"yellow","Vitamin C")
myobj3= fruits("Watermelon",100,"Green","Vitamin A")
myobj4=fruits("Mango",25,"red","Vitamin B")
myobj.onyesha()
myobj2.onyesha()
myobj3.onyesha()
myobj4.onyesha()

