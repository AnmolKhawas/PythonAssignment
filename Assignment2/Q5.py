def specialNumber(n):
    if(n<10 or n>99):
        print("The given number is not two digit number")
    else:
        print(n,"is a two digit number")
n=int(input("Enter a number:"))
specialNumber(n)
