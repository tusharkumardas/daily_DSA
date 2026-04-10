#find the max consecutive bit
def MaxBit(arr):
    n=len(arr)
    count=1
    max_count=1
    for i in range(1,n):
        if arr[i-1]==arr[i]:
            count+=1
        else:
            count=1
        if count>max_count:
            max_count=count
    return max_count
arr=[0,1,0,1,0,1,1,1,1]
print(MaxBit(arr))
