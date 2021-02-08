n=int(input("Enter two digit number: "))
r=0
while(n>0):
    a=n%10
    r=(r*10)+a
    n=n//10
print('Reverse of the given two digit number is ',r)

