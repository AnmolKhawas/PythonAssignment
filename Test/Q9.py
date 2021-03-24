#Sum of fibonacci series
n=int(input("Enter range:"))
if n<1:
    print(n)
else:
    sum=0
    a=0
    b=1
    sum=a+b
    for i in range(2,n+1):
        c=a+b
        sum+=c
        a=b
        b=c
    print("Sum=",sum)

