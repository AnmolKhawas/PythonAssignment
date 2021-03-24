class Bank():
    def __init__(self,name,acc,t,a=0,i=0):
        self.name=name
        self.accno=acc
        self.type=t
        self.amount=a
        self.interest=i

    def deposit(self,a):
        self.amount+=a
        print("Amount deposited:",a)
        print("Current balance:",self.amount)

    def withdrawl(self,a):
        if self.amount>=a:
            self.amount-=a
            print("Amount withdrew:",a)
            print("Current balance:",self.amount)
        else:
            print("Insufficiet balance.")

    def findinterest(self):
        if(self.amount>=500000):
            self.interest=(self.amount*1*8)/100
        elif(self.amount>=300000 and self.amount<500000):
            self.interest=(self.amount*1*7)/100
        elif(self.amount>=100000 and self.amount<300000):
            self.interest=(self.amount*1*5)/100
        elif(self.amount<100000):
            self.interest=(self.amount*1*3)/100
        print("Interest amount:",self.interest)

    def __str__(self):
        print('Account Holder Name:{}'.format(self.name))
        print('Account Number:{}'.format(self.accno))
        print('Account Type:{}'.format(self.type))
        print('Account Ammount:{}'.format(self.amount))


a1=Bank('Anmol khawas',12345678,'Savings')
a1.deposit(20000)
a1.__str__()
a1.findinterest()
a1.withdrawl(2000)
a1.__str__()

