class Animal :
    def __init__(self) :
        self.cnt_hair = 1000
    
    def tsshampoo(self):
        self.cnt_hair += 100
       
if __name__ == '__main__':
    ani = Animal()
    print("b",ani.cnt_hair)
    ani.tsshampoo()
    print("b",ani.cnt_hair)
    
class Human(Animal) :
    def __init__(self):
        super().__init__()
        self.flag_dev = False
    
    def principle_voice(self):
        self.flag_dev = True

if __name__ == '__main__':
    hum = Human()
    print(hum.flag_dev)
    print(hum.cnt_hair)
    hum.tsshampoo()
    print(hum.flag_dev)
    print(hum.cnt_hair)