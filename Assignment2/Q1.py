a=float(input("Enter marks of subject 1:"))
b=float(input("Enter marks of subject 2:"))
c=float(input("Enter marks of subject 3:"))
d=float(input("Enter marks of subject 4:"))
Total=a+b+c+d
av=Total/4
print('Your Grade is:',av)
if av<=40:
    print("Sorry you Failed.")
elif av>40:
    print("Congratulations you have Passed.")