class drone : 
    def __init__(self):
        self.height = 0
        print("constructor")
    def fly(self):
        self.height += 1
        print("fly")
    def __del__(self):
        print("destroyer")
    def __str__(self):
        return str(self.height)
    
if __name__ == '__main__':
    d = drone()
    d.fly()
    print(d)
    
    