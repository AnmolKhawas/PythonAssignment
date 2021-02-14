a=float(input("Enter length of side a:"))
b=float(input("Enter length of side b:"))
c=float(input("Enter length of side c:"))
if(a==b and b==c):
    print("Equilateral.")
elif(a==b or b==c or a==c):
    print("Isosceles.")
else:
    print("Scalane.")

