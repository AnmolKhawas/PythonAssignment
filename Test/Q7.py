print("Prime numbers between 30 and 100:")
for i in range(30,101):
    for j in range(2,i):
        if(i%j)==0:
            break
    else:
        print(i)
