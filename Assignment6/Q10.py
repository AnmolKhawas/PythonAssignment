#Calculate the a list for the function xn=n^2+1.
#Sample: [2,4,3,8,12]   output:[5,17,10,65,145]

def sequence_list(list1):
    list2=[]
    for i in range(0,len(list1)):
        y=list1[i]**2+1
        list2.append(y)
    return list2

n=int(input("Enter the value of n:"))
list1=[]
print("Enter {} elements:".format(n))
for i in range(0,n):
    ele=int(input(''))
    list1.append(ele)
print(sequence_list(list1))
