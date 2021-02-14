def pattern2():
    rows=6
    m=(2*rows)-2
    for i in range(rows,-1,-2):
        for j in range(m,0,-1):
            print(end="  ")
        m=m+1
        for j in range(0,i+1):
            print("O",end=" ")
        print("")
    
if __name__=="__main__":
    pattern2()