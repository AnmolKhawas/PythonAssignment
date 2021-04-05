#Define a sequence of numbers xn=n^2+1, for integers n=0,1,2,...,N.

N=int(input("Enter the range:"))
n=0
lst=[]
while n<=N:
    y = n**2 + 1
    lst.append(y)
    n=n+1
print(lst)
