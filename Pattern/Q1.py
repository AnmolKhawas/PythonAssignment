def pattern1():
    item=7
    m=(2*item)-2
    for i in range(0,item,2):
        for j in range(0,m):
            print(end="  ")
        m=m-1
        for j in range(0,i+1):
            print("O",end=' ')
        print(" ")

if __name__=="__main__":
    pattern1()
    