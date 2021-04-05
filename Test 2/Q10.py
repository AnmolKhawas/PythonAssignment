#Concatenate two lists in the following order.

l1=[1,2]
l2=[4,5]
l3=[]
for i in l1:
    for j in l2:
        l3.append((i,j))
print(l3)
