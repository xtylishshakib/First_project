class Bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def RentForBike(self,q):
        if q<=0:
            print("Enter The positive value or greater than zero")
        elif q>self.stock:
            print("Enter The value(less than stock)")
        else:
            self.stock=self.stock-q
            print("Total prices",q*100)
            print("Total Bikes",self.stock)

while True:
    obj=Bikeshop(100)
    uc=int(input('''
1 Display stocks
2 Rent a bike
3 Exit    
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("enter the qty:---"))
        obj.RentForBike(n)
    else:
        break
