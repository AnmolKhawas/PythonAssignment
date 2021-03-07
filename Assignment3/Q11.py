#a
#for row in range(1,8,2):
#    print(" " *(8-row) + "O "*row)

#b
#for row in range(1,8,2):
#    print(" " *(row-1) + "O "*(8-row))

#c
n=1
rows=4
stop=2
for i in range(rows):
    for j in range(1,stop):
        print(n,end=' ')
        n=n+1
    print(" ")
    stop+=1
