sub1=float(input("Enter marks for subject 1:"))
sub2=float(input("Enter marks for subject 2:"))
sub3=float(input("Enter marks for subject 3:"))
sub4=float(input("Enter marks for subject 4:"))
sub5=float(input("Enter marks for subject 5:"))
Total=sub1+sub2+sub3+sub4+sub5
avg=Total/5
print("Average Marks=",avg)
if(avg>=90):
    print("Grade is O")
elif((avg>=80) and (avg<=89)):
    print("Grade is E")
elif((avg>=70) and (avg<=79)):
    print("Grade is A")
else:
    print("Grade is B")

