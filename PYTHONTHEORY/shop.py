class Item():
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def purchase(self,quantity):
        self.quantity-=quantity
        print("Number of items purchased:",quantity)
        print("Number of items in stock:",self.quantity)

    def increaseStock(self,quantity):
        self.quantity+=quantity
        print("Number of items received:",quantity)
        print("Number of items in Stock:",self.quantity)

    def display(self):
        print("Name of the item:",self.name)
        print("Price of the item",self.price)
        print("Quantity of the item",self.quantity)

    def __lt__(self,other):
        if self.quantity<other.quantity:
            return True
        else:
            return False

def main():
    r1=Item('Key',25,40)
    r1.purchase(5)
    r1.display()
    r1.increaseStock(20)
    r1.display()
    r2=Item('Mouse',100,50)
    if(r1<r2):
        print("Order r1")
    else:
        print("Order r2")

if __name__=='__main__':
    main()



