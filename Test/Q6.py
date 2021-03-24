#pattern
count=0
for i in range(0,5):
    for j in range(1,i+1):
        print(count%2,end=' ')
        count+=1
    print()
    if(i%2==1):
        count=1
    else:
        count=0
