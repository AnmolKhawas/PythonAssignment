#Prime numbers between 98 and 1004

print("Prime numbers between 98 and 1004:")
for i in range(98,1005):
    for j in range(2,i):
        if(i%j)==0:
            break
    else:
        print(i)

