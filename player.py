class player () :
    def __init__(self, name , age , rank):
        self.name = name
        self.age  = age
        self.rank = rank

    
    def info(self) :
        print(f"player:{self.name}\nage   :{self.age}\nrank  : {self.rank} :")
player1= player ("Maradona","19","90")


player1.info()

   