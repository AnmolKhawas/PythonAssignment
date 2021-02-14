n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if((n2>n1 and n1>n3) or (n3>n1 and n1>n2)):
    print(n1,'is the second smallest')
elif((n1>n2 and n2>n3) or (n3>n2 and n2>n1)):
    print(n2,'is the second smallest')
elif((n1>n3 and n3>n2) or (n2>n3 and n3>n1)):
    print(n3,'is the second smallest')
