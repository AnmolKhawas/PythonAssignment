#Three digit armstrong number
for num in range(100,1000):
    temp=num
    sum=0
    while temp>0:
        a=temp%10
        sum += a**3
        temp //= 10
    if num==sum:
            print(num)
