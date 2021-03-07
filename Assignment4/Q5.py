#Palindrome
num=int(input("Enter an integer:"))
x=num
y=0
while(num>0):
    r=num%10
    y=(y*10)+r
    num=num//10
if(x==y):
    print("Palindrome number.")
else:
    print("Not a Palindrome number.")
