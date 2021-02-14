#WAP to add two integers using function.
def sum(a,b):
    s=a+b
    return s

def main():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    print("Sum=",sum(a,b))

if __name__=='__main__':
    main()
