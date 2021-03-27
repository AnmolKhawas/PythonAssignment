#expression that changes the first item in a tuple.(4,5,6) should become (1,5,6) in the process.
T=(4,5,6)
print(T)
temp=list(T)
temp[0]=1
T=tuple(temp)
print(T)
