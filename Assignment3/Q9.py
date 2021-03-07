n=int(input("Enter a number:"))
print("Prime numbers:")
for num in range(1,n+1):
    if n>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)

