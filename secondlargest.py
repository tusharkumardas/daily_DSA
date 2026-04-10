arr=[99,97,96]
n=len(arr)
t=0
m=arr[0]
for i in range(n):
    if arr[i]>m:
        t=m
        m=arr[i]
print(t)
        
