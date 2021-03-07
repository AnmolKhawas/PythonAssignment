#Armstrong no between 1 and 1000
print("Armstrong Numbers in the range 1 to 1000 are:")
for num in range(1,1000):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum += digit ** 3
        temp //= 10
    if num==sum:
        print(num)
