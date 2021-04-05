#Function which take input a string and return a string and return a string made of the first 2 and last 2 characters from a given string.
#If the string length is less than 2, return instead of the empty string.

str1=input("Enter string:")
count=0
for i in str1:
    count=count+1
    newstr=str1[0:2]+str1[count-2:count]
print("New String:"+newstr)
