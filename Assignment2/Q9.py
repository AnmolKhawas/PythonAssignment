unit=int(input("Enter the consumed unit:"))
if(unit<=300):
    r=unit*7
    print("Your total bill is:",r)
elif(unit>300 and unit<=800):
    r=(300*7)+((unit-300)*9)
    print("Your total bill is:",r)
elif(unit>800 and unit<=1500):
    r=(300*7)+(500*9)+((unit-800)*12)
    print("Your total bill is:",r)
elif(unit>1500):
    r=(300*7)+(500*9)+(700*12)+((unit-1500)*15)
    print("Your total bill is:",r)
