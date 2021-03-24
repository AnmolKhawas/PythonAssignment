class date:
    def __init__(self,d,m,y):
        self.__day=d
        self.__month=m
        self.__year=y

    def showdate(self):
        print(self.__day)
        print(self.__month)
        print(self.__year)
def main():
    d1=date(12,1,1998)
    d1.showdate()
    #print('Month=',d1.__year)   it gives error due to private attribute

if __name__=='__main__':
    main()
