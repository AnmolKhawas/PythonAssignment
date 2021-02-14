s1=float(input("Enter marks for subject 1:"))
s2=float(input("Enter marks for subject 2:"))
s3=float(input("Enter marks for subject 3:"))
s4=float(input("Enter marks for subject 4:"))
s5=float(input("Enter marks for subject 5:"))
Total=s1+s2+s3+s4+s5
avg=Total/5
if(avg>=90):
    print("Grade is O")
elif((avg>=80) and (avg<=89)):
    print("Grade is E")
elif((avg>=70) and (avg<=79)):
    print("Grade is A")
else:
    print("Grade is B")

