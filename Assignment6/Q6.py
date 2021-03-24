def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s=input("Enter string: ")
print("original string: ",end=" ")
print(s)
print("Reversed string: ",end=" ")
print(reverse(s))
