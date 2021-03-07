def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==n

num=int(input("Enter a natural number:"))

if perfect(num):
    print("This is perfect number.")
else:
    print("This is not a perfect number.")
