#Program that reads two numbers and an arithmetic operator and displays the result.

n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
op=input("Enter operator:")
if(op=="+"):
    print('Result=',n1+n2)
elif(op=="-"):
    print('Result=',n1-n2)
elif(op=="*"):
    print('Result=',n1*n2)
elif(op=="/"):
    print('Result=',n1/n2)
    