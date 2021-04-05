#Function that takes a string as parameter and returns a string with every successive repetitive character replaced with *.

def replace(str):
    new_str=""
    for i in str:
        if i in new_str:
            new_str+='*'
        else:
            new_str+=i
    print(new_str)

str=input("Enter string:")
if __name__=="__main__":
    replace(str)
