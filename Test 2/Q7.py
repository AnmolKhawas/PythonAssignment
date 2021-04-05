#Fibonacci numbers upto a range given by the user.

n=int(input("Enter the range:"))
a=0
b=1
c=0
while c<n:
    print(c)
    a=b
    b=c
    c=a+b
