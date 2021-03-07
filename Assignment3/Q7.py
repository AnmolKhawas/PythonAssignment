n=int(input("Enter a number:"))
if(n<0):
    print("Invalid! Enter a positive number.")
else:
    s=0
    while(n>0):
        s=s+n
        n=n-1
    print("The sum is:",s)
