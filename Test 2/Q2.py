#Bubble sort ascending.
arr=[53,22,33,12,56,67,32]
n=len(arr)
for i in range(n-1):
    for j in range(i+1):
        if arr[j]>arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
print("Sorted array is:")
for i in range(n):
    print(arr[i])
