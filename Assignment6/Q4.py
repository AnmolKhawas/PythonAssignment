#python function which take two string as input and return a single string from two given strings,separated by a space
#and swap the first two characters of each string.

def fun(str1,str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    new_str = new_str1 + ' ' + new_str2
    print(new_str)

str1=input("Enter first string:")
str2=input("Enter second string:")

if __name__=="__main__":
    fun(str1,str2)
