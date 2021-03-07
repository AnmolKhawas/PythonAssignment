n=int(input("Enter a natural number:"))
if n>1:
    for i in range(2,int(n/2)):
        if(n%i==0):
            print("Non prime number.")
            break
    else:
            print("Prime number.")
else:
    print("Non prime number.")
