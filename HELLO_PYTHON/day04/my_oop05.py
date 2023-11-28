class Xi :
    def __init__(self):
        self.money = 10000;
    
    def bitcoin(self):
        self.money *= 2
        
class LeeSS :
    def __init__(self):
        self.cnt_turtle = 12
    
    def nadaeyong(self):
        self.cnt_turtle += 1
        
class Musk :
    def __init__(self):
        self.companies = []
        
    def tell(self, c_name):
        self.companies.append(c_name)
    
    def show(self):
        for c in self.companies:
            print(c)     
        
class Woo(Xi, LeeSS, Musk):
    def __init__(self):
        Xi.__init__(self)
        LeeSS.__init__(self)
        Musk.__init__(self)
    
if __name__ == '__main__':
    wtw = Woo()
    print(wtw.money)
    print(wtw.cnt_turtle)
    wtw.show()
    wtw.bitcoin()
    wtw.nadaeyong()
    wtw.tell("테슬라")
    wtw.tell("스페이스X")
    print(wtw.money)
    print(wtw.cnt_turtle)
    wtw.show()