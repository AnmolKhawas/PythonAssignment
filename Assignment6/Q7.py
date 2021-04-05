#Recursive function to calculate length of a string.

def length(str):
    if str=='':
        return 0
    else:
        return 1 + length(str[1:])

str=input("Enter string: ")
print(length(str))
