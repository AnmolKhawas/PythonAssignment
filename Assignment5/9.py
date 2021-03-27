#Concatenation
L1=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input())
    L1.append(ele)
print("L1=",L1)

L2=[]
x=int(input("Enter number of elements: "))
for i in range(0,x):
    ele=int(input())
    L2.append(ele)
print("L2=",L2)

L3=[]

for i in L1:
    for j in L2:
        L3.append((i,j))
print(L3)

# or
# l1=[1,2]
# l2=[4,5]
# l3=[]
# for i in l1:
#     for j in l2:
#         l3.append((i,j))
# print(l3)        
