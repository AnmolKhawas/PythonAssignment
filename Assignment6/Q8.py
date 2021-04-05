#Python function that calculates y=6x^2+3x+2.

def eqn(x):
    y=((6*x*x)+(3*x)+2)
    return y
x=int(input("Enter number: "))
print("Output: ",eqn(x))
