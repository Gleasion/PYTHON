class Vehicle :
    def __init__(self): 
        self.cnt_wheel = 4
    def funk(self,cnt):
        self.cnt_wheel -= cnt
        
if __name__ == '__main__':
    veh = Vehicle()
    print(veh.cnt_wheel)
    veh.funk(3)
    print(veh.cnt_wheel)
    
class Car(Vehicle) :
    def __init__(self):
        super().__init__()
        self.volume_speaker = 20
    
    def turnRight(self,cnt):
        self.volume_speaker += cnt
    
    def turnLeft(self,cnt):
        self.volume_speaker -= cnt
    
if __name__ == '__main__':
    c = Car()
    print(c.cnt_wheel)
    print(c.volume_speaker)
    c.funk(1)
    c.turnRight(5)
    print(c.cnt_wheel)
    print(c.volume_speaker)