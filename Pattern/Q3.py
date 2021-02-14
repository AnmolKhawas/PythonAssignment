def pattern3():
    n=1
    rows=4
    stop=2
    for i in range(rows):
        for j in range(1,stop):
            print(n,end=' ')
            n=n+1
        print(" ")
        stop+=1

if __name__=="__main__":
    pattern3()         